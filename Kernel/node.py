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
    x : flaot 	
        Actual X coordiante
    y : flaot 
        Actual Y Coordiante

    #TODO for now not used:
    reference_x : float 
        Reference X coordinate.
    reference_y : float
        Reference Y coordiante.
    u : flaot 
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

    def get_actual_location(self):
        """
        Locaation of the node in the actiual configuration.

        Returns
        -------
        location: ndarray
            Numpy array containing the reference coordinates X and Y.
        """
        x = self.x
        y = self.y

        return np.array([x,y], dtype=float)

    
