#!/usr/bin/env python3

import numpy as np
import kmd as KMD_lib
from pathlib import Path
from matplotlib import pyplot as plt

# Resolve the base directory of the script
SCRIPT_DIR = Path(__file__).resolve().parent

s1=SCRIPT_DIR / 'data/02/05/node_777087_1749792543132.cycles.csv'

scheduler_data: np.ndarray = np.genfromtxt(fname=s1, delimiter=',', skip_header=1)
assert scheduler_data.ndim == 2
print(scheduler_data)

assert scheduler_data.shape[1] == 417

# Extract the signal column (assume column 1 is time, column 2 is value)
scheduling_iteration_1_0 = scheduler_data[:, 3]
scheduling_iteration_1_1 = scheduler_data[:, 4]
scheduling_iteration_2_1 = scheduler_data[:, 5]

wave_p=0
t_mesh=np.zeros(1)
ref_fin=False

alphas = [0.05, 0.1, 0.3, 1.0, 3.0]
thrs = [0.001, 0.005, 0.01, 0.05]
thr_ens = [0.01, 0.05, 0.1, 0.2]

best_params = None
max_modes = 0

# for alpha in alphas:
#     for thr in thrs:
#         for thr_en in thr_ens:
#             try:
#                 Comp_data_full, wp = KMD_lib.semimanual_maxpool_peel2(
#                     signal=scheduling_iteration_2_1, wave_p=wave_p, alpha=alpha, t_mesh=t_mesh,
#                     thr=thr, thr_en=thr_en, ref_fin=ref_fin
#                 )
#                 num_modes = Comp_data_full.shape[0]
#                 print(f"alpha={alpha}, thr={thr}, thr_en={thr_en} => modes: {num_modes}")
#                 if num_modes > max_modes:
#                     max_modes = num_modes
#                     best_params = (alpha, thr, thr_en)
#             except Exception as e:
#                 print(f"alpha={alpha}, thr={thr}, thr_en={thr_en} => error: {e}")

Comp_data_full, wp = KMD_lib.semimanual_maxpool_peel2(
                    signal=scheduling_iteration_2_1, alpha=2.0
                )
num_modes = Comp_data_full.shape[0]
max_modes = num_modes

# print(f"{scheduling_iteration_1_0=}")
# print(f"{scheduling_iteration_1_1=}")
# print(f"{scheduling_iteration_2_1=}")

# print(f"Best params: {best_params} with {max_modes} modes")

if max_modes == 0:
    print("No modes found.")
    exit(1)

num_modes = Comp_data_full.shape[0]
print(f"Number of modes found: {num_modes}")
for i in range(num_modes):
    j = i
    if i == 0:
        j = 0
    if i == 1:
        j = 1
    amp   = Comp_data_full[i, :, 0]
    phase = Comp_data_full[i, :, 1]
    plt.plot(amp * KMD_lib.wave(wp, phase), label=f"mode {i}")
    plt.plot(scheduling_iteration_2_1)
    plt.legend()
    plt.show()

