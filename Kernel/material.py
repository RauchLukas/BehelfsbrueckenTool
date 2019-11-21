"""
This modul only contains the Material class

Author: Lukas Rauch
"""

class Material(object):
    """
    Matreral data of a local cross section.

    Attributes 
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

    def __init__(self, id, 
        density=0, youngs_modulus=0, fmk=0, 
        ft0k=0, ft90k=0, fc0k=0, fc90k=0):
        """
        Create a new material.
        """
        self.id = id
        self.density = density
        self.youngs_modulus = youngs_modulus
        self.fmk = fmk
        self.ft0k = ft0k
        self.ft90k = ft90k
        self.fc0k = fc0k
        self.fc90k = fc90k
        