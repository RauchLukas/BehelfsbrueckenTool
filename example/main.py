import sys, os
sys.path.append('D:/Projekte/Untersuchung_des_Behelfsbrueckenbausatzes/Python/BehelfsbrueckenTool')
from Kernel.model import Model

# print('Process ID: ', os.getpid())
# print(' ')


testmodel = Model('testmodel')

testmodel.add_node(id=1,x=0,y=0)
testmodel.add_node(id=2,x=1,y=0)
testmodel.add_node(id=3,x=3,y=0)
testmodel.add_node(id=4,x=6,y=0)

testmodel.add_material(id=1, density=2,youngs_modulus=3,fmk=4,ft0k=5,ft90k=6,fc0k=7,fc90k=8)

testmodel.add_crosssection(id=1, area=0.5, Iz=0.1)


material = testmodel.get_material(id=2)
node = testmodel.get_node(id=1)







# print(testmodel.nodes)

# testmodel.add_node(key=3)

# print(testmodel.nodes)



print('done!')