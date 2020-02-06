from __future__ import print_function
import datetime
import numpy as np
import os
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

import cntk as C
import cntk.tests.test_utils
cntk.tests.test_utils.set_device_from_pytest_env() # (only needed for our build system)
C.cntk_py.set_fixed_random_seed(1) # fix a random seed for CNTK components

#%matplotlib inline


