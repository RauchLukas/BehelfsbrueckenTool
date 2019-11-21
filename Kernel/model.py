"""This module contains the Model class.

Authors: Lukas Rauch
"""

import numpy as np
import numpy.linalg as la
from .node import Node
from .material import Material
from .crosssection import Crosssection



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
        self._node_keys = list()

        self._elements = dict()
        self._element_keys = list()

        self._materials = dict()
        self._material_keys = list()

        self._crosssections = dict()
        self._crosssection_keys = list()

        self.dirichlet_condtion = dict()

        self.neumann_condition = dict()

        self.loadclass = str


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
            Y Coordiante
        
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
        Add a two dimensionla bridge element to the model.

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

        #TODO ADD ELEMENT




    def add_material(self,id, 
            density=0, youngs_modulus=0, fmk=0, ft0k=0, ft90k=0, fc0k=0, fc90k=0):
        """Add a new material to the model.

        Parameters 
        ---------
        id : int or str
            Unique matrial ID.
        density : float
            Material densitiy to calculate the material weight.
        youngs_modulus : float
            Material young's modulus.
        fmk : float
            Avarage bending stiffness - charactraristic.
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

        self._materials[id] = Material(id, 
            density=0, youngs_modulus=0, fmk=0, ft0k=0, ft90k=0, fc0k=0, fc90k=0)

        
    def add_crosssection(self, id, area, Iz):
        """
        Add a new local element cross section to the model

        Parameters
        ----------
        id : int or str
            Unique matrial ID.
        area : float
            Area of the cross section.
        Iz : flaot
            Moment of inertia, rotation around the Z-axis
        """
        
        if id in self._crosssections:
            raise RuntimeError('The model already contains a cross section with id: {}' .format(id))

        self._crosssections[id] = Crosssection(id, area, Iz)








