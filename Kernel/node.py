"""
This modul only contains the Node class.

Author: Lukas Rauch
"""
import numpy as np

class Node(object):
    """
    Two dimensional Node providing Dofs and unique position in 2D space

    Attributes
    ---------
    id : int or str
        Unique ID.
    x : float 	
        Actual X coordinate
    y : float 
        Actual Y coordinate

    #TODO for now not used:
    reference_x : float 
        Reference X coordinate.
    reference_y : float
        Reference Y coordinate.
    u : float 
        Displacement in x direction
    v : float
        Displacement in y direction
    """

    def __init__(self, id, x, y):
        """
        Create a nwe node.
        """
        self.id = id
        self.x = x
        self.y = y
        self.reference_x = x
        self.reference_y = y
        self.elementlist = []
        self.support_y = None

    def get_actual_location(self):
        """
        Location of the node in the actual configuration.

        Returns
        -------
        location: ndarray
            Numpy array containing the reference coordinates X and Y.
        """
        x = self.x
        y = self.y

        return np.array([x,y], dtype=float)
    
    def update_element_list(self, element_id):
        """
        Saves the elements connected to the present node in a list.
        """
        self.elementlist.append(element_id)
        pass


    

