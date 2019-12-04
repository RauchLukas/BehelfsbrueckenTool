"""
This modul only contains the Eurocode class.

Author: Lukas Rauch
"""

class Eurocode(object):
    """
        Class for predefining and storing data concerning the EUROCODE norm. 
    """

    def __init__(self):
        """
        #TODO fix __init__ if needed
        """
        # Load
        self.Gg = 1.35      # Eigengewicht 
        self.Gq = 1.50      # Verkehrslasten 

        # Wood
        self.Gm_w = 1.30    # Holz und Holzwerkstoffe
        self.Gm_ws = 1.30   # Stahl in Verbindungen

        # steel 
        self.Gm_s0 = 1.00   # Stahl Querschnittnachweis
        self.Gm_s1 = 1.10   # Stabilität
        self.Gm_s2 = 1.25   # Verbindungsmittel

        # concrete
        self.Gm_c = 1.50    # Beton
        self.Gm_cs = 1.15   # Betonstahl

        
    
