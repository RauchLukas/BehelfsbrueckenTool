"""
This modul only contains graphic class to visualice the input and output data.

Author: Lukas Rauch
"""

import numpy as np
import matplotlib.pyplot as plt



class Graphic(object):
    """
    Class including all necessary functions for visualization of the model.
    """

    def __init__(self, model, system=True, load=True, forces=True, results=True):
        """
        Initialize the visualization process.
        """
        
        fig = plt.figure("System") 
        ax = fig.add_subplot(1,1,1)
        self.plot_nodes(model)
        self.plot_elements(model)
        self.plot_support_forces(model)
        self.plot_moment_force(model)

        plt.show()
        pass
    
    def plot_nodes(self, model): 
        """
        Function to visualize all model nodes.
        """
        for id in model._nodes:
            plt.plot(model._nodes[id].x, model._nodes[id].y, marker='o', color='black')

    def plot_elements(self, model):
        """
        Function to visualize all model elements.
        """
        for id in model._elements:
            plt.plot([model._elements[id].node_a.x, model._elements[id].node_b.x],
                     [model._elements[id].node_a.y, model._elements[id].node_b.y], color='black', marker='_')
    
    def plot_support_forces(self, model):
        """
        Function to visualize all model support forces.
        """
        for id in model._nodes:
            x_head = model._nodes[id].x
            x_base = model._nodes[id].x
            y_head = model._nodes[id].y
            y_base = model._nodes[id].y-0.01

            plt.arrow(x_base, y_base, 0, 0.01, length_includes_head=True,
                head_width=0.3, head_length=0.007, color='green')
            plt.text(x_base, y_base-0.005, '{}' .format(model._nodes[id].support_y))
            # plt.annotate('test', xy=(model._nodes[id].x, model._nodes[id].y), 
            #     xytext=(0, model._nodes[id].y-0.01), arrowprops={'arrowstyle': '->'})  
            # 

    def plot_moment_force(self, model):
        for id in model._elements:
            x1 = model._elements[id].node_a.x
            y1=model._elements[id].node_a.y
            x2=0.5*(model._elements[id].node_b.x-model._elements[id].node_a.x)+model._elements[id].node_a.x
            y2=0.001
            x3=model._elements[id].node_b.x
            y3=model._elements[id].node_b.y

            self.calc_parabola_vertex(x1=x1,y1=y1,x2=x2,y2=y2,x3=x3,y3=y3)
            pass

    def calc_parabola_vertex(self, x1, y1, x2, y2, x3, y3):
        """
        TODO Fix text
        """
        denom  = (x1-x2) * (x1-x3) * (x2-x3)
        A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
        B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
        C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom

        x_pos=np.linspace(x1,x3,20)
        y_pos=[]

        for x in range(len(x_pos)):
            x_val=x_pos[x]
            y=(A*(x_val**2))+(B*x_val)+C
            y_pos.append(-y)

        plt.plot(x_pos, y_pos, linestyle='-', color='black') # parabola line


