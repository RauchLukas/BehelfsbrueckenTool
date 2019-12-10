import sys, os
sys.path.append('D:/_UniBw/BehelfsbrueckenTool')
from Kernel.model import Model

# print('Process ID: ', os.getpid())
# print(' ')

# Neues Modell erzeugen
model = Model('model')

# Hinzufügen neuer Knoten
model.add_node(id=1,x=0,y=0)
model.add_node(id=2,x=1,y=0)
model.add_node(id=3,x=3,y=0)
model.add_node(id=4,x=6,y=0)

# Erstellung neuer Materialien
model.add_material(id=1,materialtype='wood', density=2,youngs_modulus=3,fmk=24, fvk=4,ft0k=5,ft90k=6,fc0k=7,fc90k=8)
model.add_material(id=2,materialtype='steal', density=2,youngs_modulus=3,fmk=24, fvk=2, ft0k=5,ft90k=6,fc0k=7,fc90k=8)

# Erstellung eines neuen Querschnittes
model.add_crosssection(id=1, hight=1, width=1)

# Testabfrage
material = model.get_material(id=1)
node = model.get_node(id=1)
crosssection=model.get_crosssection(id=1)

# Erstellung der ÜBerbauelemente
model.add_element(id='A', node_a=1, node_b=2, crosssection=1, material=1)
model.add_element(id='B', node_a=2, node_b=3, crosssection=1, material=2)
model.add_element(id='C', node_a=3, node_b=4, crosssection=1, material=1)

# Erzeugung der Unterbauten
model.add_substructure([1,2,3,4])

# Erzeugung eines Lastfalles nach MLC
model.add_loadclass(id=1, loadtype='mlc_wheeled', loadclass=40)

# loadclassvalue = model._loadclasses[1].get_loadclass_value(12)

em_mcl, eq_mcl = model.calc_forces(element_id='B', load_id=1, lm1=True)

# Berechnung des Überbaus
results = model.design_crosssection('B', load_id=1)

# Spannungsnachweis eines einzelnen Elements
ausnutzung_eines = model.solve_element(element_id='B', load_id=1)

# Spannungsnachweis aller Elemente
ausnutzung_alle = model.solve(1)


model.update_substructure(id=1, hight=1)


model.print_graphic()

print('done!')