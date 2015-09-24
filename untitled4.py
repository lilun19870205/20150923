# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:54:51 2015

@author: lilun
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:40:55 2015

@author: lilun
"""

import numpy as np
import cPickle as pickle

x=1.0
f=open('x.txt','w')
f.write("%18.16f" % x)
f.close()

pickle.dump(x,open('x.p','wb'))