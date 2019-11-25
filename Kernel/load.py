"""
This modul only contains the load class

Author: Lukas Rauch
"""

class Load(object):
    """
    Load class data of military and civil use.

    Attributes 
    ---------
    id : int or str
        Unique loadclass ID.
    loadclass : str
        Loadclass of military or civil use. 
    wheeled : bool
        Loadclass type - necessary ony with military use
    tracked : bool
        Loadclass type - necessary ony with military use

    """

    def __init__(self, id, loadtyp, loadclass):
        """Create a new loadcondition"""

        self.id = id
        self.loadtyp = loadtyp
        self.loadclass = loadclass

       
    def get_loadclass_value(self, id, loadclass, weight_type='weight'):
        """
        Get loadclass value from database

        Attributes 
        ----------
        #TODO fixit id
        loadtyp : str
            MLC loadtyp by STANAG 2021 (mlc_wheeled / mlc_tracked)
        loadclass : int
            MLC loadclass number by STANGAG 2021 
        weight_type : str
            classification  of loadtyp (total weight = 'weight', weight of the axis = 'axis')
        """

        MLC_classes ={
        'mlc_wheeled': {
            4:      {'weight' : 4.09	, 'axis' : [0.91	,1.59	,1.59   ]},
            8:      {'weight' : 8.16	, 'axis' : [2.72	,2.72	,2.72   ]},
            12:     {'weight' : 13.61	, 'axis' : [2.72	,4.54	,4.54	,1.81   ]},
            16:     {'weight' : 16.79	, 'axis' : [2.72	,5.9	,5.9	,2.27   ]},
            20:     {'weight' : 21.77	, 'axis' : [3.63	,7.71	,7.71	,2.72   ]},
            24:     {'weight' : 25.4	, 'axis' : [4.54	,9.07	,9.07	,2.72	]},
            30:     {'weight' : 30.84	, 'axis' : [5.44	,9.98	,9.98	,5.44	]},
            40:     {'weight' : 42.63	, 'axis' : [6.35	,11.79	,11.79	,12.7	]},
            50:     {'weight' : 52.62	, 'axis' : [7.26	,13.61	,13.61	,18.14	]},
            60:     {'weight' : 63.5	, 'axis' : [7.26	,16.33	,16.33	,11.79	,11.79	]},
            70:     {'weight' : 73.02	, 'axis' : [9.52	,19.05	,19.05	,12.7	,12.7	]},
            80:     {'weight' : 83.45	, 'axis' : [10.89	,21.77	,21.77	,14.51	,14.51  ]},
            90:     {'weight' : 93.89	, 'axis' : [12.25	,24.49	,24.49	,16.33	,16.33	]},
            100:    {'weight' : 104.33	, 'axis' : [13.61	,27.22	,27.22	,18.14	,18.14	]},
            120:    {'weight' : 125.19	, 'axis' : [16.33	,32.66	,32.66	,21.77	,21.77	]},
            150:    {'weight' : 154.22	, 'axis' : [19.96	,38.1	,38.1	,29.03	,29.03	]}},
        'mlc_tracked': {
            4	:   {'weight' : 3.63},
            8	:   {'weight' : 7.26},
            12	:   {'weight' : 10.88},
            16	:   {'weight' : 14.51},
            20	:   {'weight' : 18.14},
            24	:   {'weight' : 21.77},
            30	:   {'weight' : 27.22},
            40	:   {'weight' : 36.29},
            50	:   {'weight' : 45.36},
            60	:   {'weight' : 54.43},
            70	:   {'weight' : 63.50},
            80	:   {'weight' : 72.58},
            90	:   {'weight' : 81.65},
            100	:   {'weight' : 90.72},
            120	:   {'weight' : 108.86},
            150	:   {'weight' : 136.08}}
        }

        return MLC_classes[self.loadtyp][loadclass][weight_type]









