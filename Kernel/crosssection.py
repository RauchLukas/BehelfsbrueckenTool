"""
This modul only contains the Crosssection class

Author: Lukas Rauch
"""

class Crosssection(object):
    """
    Geomrtical data of a local cross section.

    Attributes 
    ---------
    id : int or str
        Unique matrial ID.
    area : float
        Area of the cross section.
    Iz : flaot
        Moment of inertia, rotation around the Z-axis

    """

    def __init__(self, id, hight, width):
        """
        creating a new local element crosssection.
        """
        self.id = id
        self.hight = hight 
        self.width = width 

        self.Iy = width * hight**3 / 12
        self.Iz = hight * width**3 / 12

        self.Wy = width * hight**2 / 6
        self.Wz = hight * width**2 / 6

        self.area = hight * width
