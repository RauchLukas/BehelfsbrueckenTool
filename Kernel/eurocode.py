"""
This modul only contains the Eurocode class.

Author: Lukas Rauch
"""

import numpy as np

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

        
    
