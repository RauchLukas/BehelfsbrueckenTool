"""
This modul only contains the Element class

Author: Lukas Rauch
"""
import math
import numpy as np
import numpy.linalg as la

class Element(object):
    """
    Description of a local element.

    Attributes 
    ---------
    id : int or str
        Unique element ID.
    node_a : int or str
        ID of the first element node.
    node_b : int or str
        ID of the second element node.
    material : int or str
        ID of the element material.
    crosssection : int or str
        ID of the element cross section.
    
    """

    def __init__(self, id, node_a, node_b, material, crosssection):
        """
        Initialize a defined element by its required attributes.

        #TODO: Fix text
         
        """

        self.id = id
        self.node_a = node_a
        self.node_b = node_b
        self.material = material
        self.crosssection = crosssection

        

        # internal storage
        self.forces = {
            'moment' : 0,
            'q_a' : 0,
            'q_e' : 0 
        }



        # self.length = float
        # self.weight_pm = self.material.density() * self.crosssection.get_area()
        # self.weight = self.weight_pm * self.length

        pass

    @property
    def dofs(self):
        """FIXME"""

        a_id = self.node_a.id
        b_id = self.node_b.id
    
        return [(a_id), (b_id)]
    
    def get_element_vector(self):
        """Returns the 2D element orientation"""
        actual_a = self.node_a.get_actual_location()
        actual_b = self.node_b.get_actual_location()

        return actual_b - actual_a
    
    def get_actual_length(self):
        """Returns the 2D Element vector length"""
        actual_a = self.node_a.get_actual_location()
        actual_b = self.node_b.get_actual_location()

        return la.norm(actual_b - actual_a)

    

