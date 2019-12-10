"""
This modul only contains the substructure class of the model.

Author: Lukas Rauch
"""

class Substructure(object):
    """
    # TODO fix: what exactly does this class in the end.
    """

    def __init__(self, id, structuretype=None, load=None, material_id=None):
        """
        Defining all necessary variables of substructure elements. 
        """
        self.id = id
        self.structuretype = structuretype
        self.load = load
        self.marerial_id = material_id
        self.hight = None
        self.crosssection_id = None

        
