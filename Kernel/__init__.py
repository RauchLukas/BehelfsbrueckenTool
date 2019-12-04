import sys

print("""
--------------------------------------------------------------------------------

                 ______  ______
                /      |       |
               /   _/  /   _/  /
              /    ___/    ___/
             /      |       |     
            /   _/  /   _/  /
           /_______/_______/ BemessungsTool
    
Authors:    Lukas Rauch
Copyright:  © 2019 Uni Bw Massivbau
Version:    1.0 Beta

This is a beta tool! All results without warranty.
--------------------------------------------------------------------------------
""")

if sys.version_info < (3, 5):
    raise RuntimeError("The BB Tool requires at least Python 3.5!")

from .model import Model
# from .node import Node
# from .element import Element
# from .material import Material
# from .crosssection import Crosssection
# from .eurocode import Eurocode


def test():
    import unittest
    suite = unittest.TestLoader().discover('.', pattern='test*')
    unittest.TextTestRunner(verbosity=2).run(suite)

