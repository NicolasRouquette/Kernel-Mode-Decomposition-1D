#!/usr/bin/env python3

import numpy as np
import kmd as KMD_lib
from pathlib import Path

# Resolve the base directory of the script
SCRIPT_DIR = Path(__file__).resolve().parent

s1=SCRIPT_DIR / 'data/python3_3635424_1748634244746.scheduler.csv'

scheduler_data: np.ndarray = np.loadtxt(fname=s1, delimiter=',', skiprows=1)
assert scheduler_data.ndim == 2
print(scheduler_data)

result = KMD_lib.semimanual_maxpool_peel2(signal=scheduler_data)
print(result)
