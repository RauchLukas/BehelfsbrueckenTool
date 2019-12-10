"""This module contains the Model class.

Authors: Lukas Rauch
"""

import numpy as np
import numpy.linalg as la
import operator 
from .node import Node
from .element import Element
from .material import Material
from .crosssection import Crosssection
from .load import Load
from .eurocode import Eurocode
from .substructure import Substructure
from .graphic import Graphic

#FIXIT import module node

class Model(object):
    """A Model contains all the objects that build the element model.
        Nodes, elements, loads, conditions..

        Attributes
        ----------
        name : str
            Name of the model
        nodes : dict
            Dictionary that stores node_id : node object
        elements : dict
            Dictionary that stores element_id : element object
        material : dict
            Dictionary that stores material_id : material object 
        #TODO add Crosssections
    """

    def __init__(self, name):

        self.name = name

        self._nodes = dict()
        # self._node_keys = list()

        self._elements = dict()
        # self._element_keys = list()

        self._materials = dict()
        # self._material_keys = list()

        self._crosssections = dict()
        # self._crosssection_keys = list()

        self._substructures = dict()
        
        self.dirichlet_condtion = dict()

        self.neumann_condition = dict()

        self._loadclasses = dict()

        self.ec = Eurocode()
        pass


# === get model information
    @property
    def node(self):
        """Get a list of all nodes in the model.

        Returns
        -------
        nodes : list
            List of all nodes in the model.
        """
        return self._nodes.values()

    def get_node(self, id):
        """Get a node by its ID.

        Parameters
        ----------
        id : int or str
            ID of the node.

        Returns
        -------
        node : list
            Node with the given ID.
        """

        if id not in self._nodes:
            raise RuntimeError('The model dose not contains a node with id: {}' .format(id))
        return self._nodes[id]

    @property
    def elements(self):
        """Get a list of all elements in the model.

        Returns
        -------
        elements : list
            List of all elements in the model.
        """
        return self._elements.values()

    def get_element(self, id):
        """Get an element by its ID.

        Parameters
        ----------
        id : int or str
            ID of the element.

        Returns
        -------
        element : list
            Element with the given ID.
        """
        if id not in self._elements:
            raise RuntimeError('The model does not contain a element with id: {}' .format(id))

        return self._elements[id]

    def get_material(self, id):     	
        """Get an material by its ID.

        Parameters
        ----------
        id : int or str
            ID of the material.

        Returns
        -------
        material : list
            material with the given ID.
        """
        if id not in self._materials:
            raise RuntimeError('The model does not contain a material with id: {}' .format(id))

        return self._materials[id]

    def get_crosssection(self, id):     	
        """Get the cross section by its ID.

        Parameters
        ----------
        id : int or str
            ID of the material.

        Returns
        -------
        cross section : list
            Cross section with the given ID.
        """

        if id not in self._crosssections:
            raise RuntimeError('The model does not contain a material with id: {}' .format(id))

        return self._crosssections[id]

    def get_loadclass(self, id):     	
        """Get the loadclass by its ID.

        Parameters
        ----------
        id : int or str
            ID of the loadclass.

        Returns
        -------
        loadclass : list
            loadclass with the given ID.
        """

        if id not in self._loadclasses:
            raise RuntimeError('The model does not contain a material with id: {}' .format(id))

        return self._loadclasses[id]

# === modeling
    def add_node(self, id, x, y):
        """Add a two dimensional node to the model.

        Parameters
        ----------
        id: int or str
            Unique ID of the node
        x : float
            X Coordinate
        y : float
            Y Coordinate
        
        Examples
        --------
        Add node with ID 'B':

        model.add_node(id'B', x=2, y=0)
        """

        if id in self._nodes:
            raise RuntimeError('The model already contains a node with id: {}' .format(id))

        self._nodes[id] = Node(id, x, y)

    def add_element(self, id, node_a, node_b, crosssection, material):
        """
        Add a two dimensional bridge element to the model.

        id : int or str
            Unique ID of the element
        node_a : int or str
            ID of the first node
        node_b : int or str
            ID of the second node
        cross section : dict
            crosssection data of the local bride element
        material :  dict
            Material data of the local cross section
        """

        if id in self._elements:
            raise RuntimeError('The model already contains an element with id {}'.format(id))

        if node_a not in self._nodes:
            raise RuntimeError('The model does not contain a node with id {}'.format(node_a))

        if node_b not in self._nodes:
            raise RuntimeError('The model does not contain a node with id {}'.format(node_b))

        self._elements[id] = Element(
            id, self._nodes[node_a], self._nodes[node_b], self._materials[material], self._crosssections[crosssection])

        self._nodes[node_a].update_element_list(element_id=id) 
        self._nodes[node_b].update_element_list(element_id=id) 

    def add_material(self,id, materialtype = 'wood',
            density=0, youngs_modulus=0, fmk=0, fvk=0, ft0k=0, ft90k=0, fc0k=0, fc90k=0):
        """Add a new material to the model.

        Parameters 
        ---------
        id : int or str
            Unique matrial ID.
        density : float
            Material density to calculate the material weight.
        youngs_modulus : float
            Material young's modulus.
        fmk : float
            Avarage bending stiffness - characteristic.
        ft0k : float
            Tension stiffness parallel to material fiber.
        ft90k : float
            Tension stiffness vertical to material fiber.
        fc0k : float
            Compression stiffness parallel to material fiber.
        fc90k : float
            Compression stiffness vertical to material fiber.
        """

        if id in self._materials:
            raise RuntimeError('The model already contains a material with id: {}' .format(id))

        self._materials[id] = Material(
            id, materialtype, density, youngs_modulus, fmk, fvk, ft0k, ft90k, fc0k, fc90k)
        
    def add_crosssection(self, id, hight, width):
        """
        Add a new local element cross section to the model

        Parameters
        ----------
        id : int or str
            Unique matrial ID.
        area : float
            Area of the cross section.
        Iz : float
            Moment of inertia, rotation around the Z-axis
        """
        
        if id in self._crosssections:
            raise RuntimeError('The model already contains a cross section with id: {}' .format(id))

        self._crosssections[id] = Crosssection(id, hight, width)


    def add_loadclass(self, id, loadtype, loadclass):
        """
        Add a new loadclass to the model environment.
        """

        if id in self._loadclasses:
            raise RuntimeError('The model already contains a loadclass with id: {}' .format(id))
        
        self._loadclasses[id] = Load(id, loadtype, loadclass)

# === solving

    def calc_forces(self, element_id, load_id, lm1=False):
        """
        Calculates the bending moment and the shearforces of the passed in element
        
        Parameters
        ----------

        id : str
            Unique ID of an existing element.
        """
        span = self._elements[element_id].get_actual_length()
        loadclass = self._loadclasses[load_id].loadclass

        mlc_unit_m = self._loadclasses[load_id].get_unit_moment_mlc(loadclass, span)
        mlc_q = self._loadclasses[load_id].get_shear_mlc(loadclass, span)
        unit_m_max = mlc_unit_m[np.argmax(mlc_unit_m)]
        q_max = mlc_q[np.argmax(mlc_q)]

        if lm1:
            lm1_unit_m = self._loadclasses[load_id].get_unit_moment_lm1(span)
            lm1_q = self._loadclasses[load_id].get_shear_lm1(span)

            unit_m_max = max(unit_m_max, lm1_unit_m)
            q_max = max(q_max, lm1_q)

        m_max = span * unit_m_max

        self._elements[element_id].forces['moment'] = m_max
        self._elements[element_id].forces['q_a'] = q_max
        self._elements[element_id].forces['q_e'] = q_max

        return  [m_max, q_max]

    def design_crosssection(self, element_id, load_id, lm1=False):
        """
        Tool for designing a given cross section by the passed in load.
        distinguishes by the material type
        """

        Gg = self.ec.Gg
        Gq = self.ec.Gq

        materialtype = self._elements[element_id].material.materialtype 
        material = self._elements[element_id].material
        crosssection = self._elements[element_id].crosssection
        
        Wy = crosssection.Wy
        mk_max , qk_max =  self.calc_forces(element_id, load_id, lm1=False)

        if materialtype == 'wood':
            kcr = self._materials[material.id].get_kcr()
            kmod = self._materials[material.id].get_kmod(nkl=1, kled='kurz')
            
            kh = (150/crosssection.hight*1000)**0.2  # TODO fix problem with variable units. kh has to be [mm] !
            if kh >= 1.3:
                kh = 1.3
            if kh <= 1.0:
                kh = 1.0

            fmk = material.fmk
            fvk = material.fvk

            Gm = self.ec.Gm_w
            fmd = fmk/Gm
            fvd = fvk/Gm

            nu_mk = mk_max/(1000*Wy*fmk)                                # fix Teislicherheitsbeiwerte
            nu_qk = 1.5*qk_max/(1000*kcr*crosssection.area*fvk)      # fix Teislicherheitsbeiwerte 
            
            nu_md = Gq*mk_max/(1000*Wy*fmd)                             # fix Teislicherheitsbeiwerte
            nu_qd = 1.5*Gq*qk_max/(1000*kcr*crosssection.area*fvd)     # fix Teislicherheitsbeiwerte 

        elif materialtype == 'steal':
            Gm = self.ec.Gm_s0

            fyk = material.fmk
            fyd = fyk/Gm
            av = 0.4*crosssection.area      # TODO fix correct crosssection area web - 0.4 is only approximation 

            nu_mk = mk_max/(1000*Wy*fyk)
            nu_qk = np.sqrt(3)*qk_max/(1000*av*fyk)

            nu_vmk =  nu_mk**2 + 3*nu_qk**2
            
            nu_md = Gq*mk_max/(1000*Wy*fyd)
            nu_qd = np.sqrt(3)*Gq*qk_max/(1000*av*fyd)    
            
            nu_vmd =  nu_md**2 + 3*nu_qd**2

        else:
            raise RuntimeError('Material with type "{}" is not part of the library. Solving the system is not possible!' .format(id))
        
        return {'nu_mk': nu_mk, 'nu_qk': nu_qk, 'nu_md': nu_md, 'nu_qd': nu_qd}

    def solve_element(self, element_id, load_id, lm1=False, design=True):
        """
        Function that solves a single element.
        """
        results = self.design_crosssection(element_id=element_id, load_id=load_id, lm1=lm1)

        nu_char = np.array([[results['nu_mk'], results['nu_qk']]], dtype=float)
        nu_desi = np.array([[results['nu_md'], results['nu_qd']]], dtype=float)
        
        nu_all = results.values()

        # if max(nu_all) >= 1.0:
        #     print('Nachweis nicht erbracht! Maximale Querschnittsausnutzung {:.2f}% ' .format(max(nu_all)*100))
        # else:
        #     print('Nachweis erbracht! Maximale Querschnittsausnutzung {:.2f}% ' .format(max(nu_all)*100))
        # pass

        if design:
            return nu_desi
        else:
            return nu_char

    def solve(self, load_id, design=True):
        """
        Function that solves all elements for one certain load case.
        """

        out = np.empty((0,2), float)
        for i, id in enumerate(self._elements.keys()):
            element = self._elements[id]
            temp = self.solve_element(element_id=id, load_id=load_id, design=design)

            out = np.append(out, temp, axis=0)

        self.calc_supportforce_auto()
        return out

    # == Substructure
    def add_substructure(self, id):
        """
        # TODO fix description
        """
        for i in id:  
            if i in self._substructures:
                raise RuntimeError('The model already contains an substructure with id {}'.format(i))

            self._substructures[i] = Substructure(i)

    def update_substructure(self, id, hight=None, structuretype=None, load=None, marerial_id=None): 
        """
        # TODO fix desccription
        """
        if id not in self._substructures:
            raise RuntimeError('The model dose not contains an substructure with id {}'.format(id))
        else:
            if hight is not self.update_substructure.__defaults__[0]:
                self._substructures[id].hight = hight
            if structuretype is not self.update_substructure.__defaults__[0]:
                self._substructures[id].structuretype = structuretype
            if load is not self.update_substructure.__defaults__[0]:
                self._substructures[id].load = load
            if marerial_id is not self.update_substructure.__defaults__[0]:
                self._substructures[id].marerial_id = marerial_id

            
    def add_substructure_auto(self, id, structuretype, load, material_id): 
        """
        Add a new substructure element to the model.
        """
        if id in self._substructures:
            raise RuntimeError('The model already contains an substructure with id {}'.format(id))

        self._substructures[id] = Substructure(
            id, structuretype, load, material_id)
        
    def calc_supportforce_auto(self):
        """
        Calculates though all substructure elements.
        """
        supportforce = 0

        for id in self._substructures:
            for i in self._nodes[id].elementlist:
                supportforce = supportforce + self._elements[i].forces['q_a']

            self._nodes[id].support_y = supportforce
            supportforce = 0



# == Visualization

    def print_graphic(self):
        """
        Visualize the system.
        """
        Graphic(self)

        

