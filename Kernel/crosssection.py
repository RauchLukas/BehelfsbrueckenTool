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

def __init__(self, id, area, Iz):
    """
    creating a new local element crosssection.
    """
    self.id = id
    self.area = area 
    self.Iz = Iz
