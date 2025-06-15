#!/usr/bin/env python3

import numpy as np
import kmd as KMD_lib
from pathlib import Path
from matplotlib import pyplot as plt

# Resolve the base directory of the script
SCRIPT_DIR = Path(__file__).resolve().parent

s1=SCRIPT_DIR / 'data/python3_3635424_1748634244746.scheduler.csv'

scheduler_data: np.ndarray = np.loadtxt(fname=s1, delimiter=',', skiprows=1)
assert scheduler_data.ndim == 2
print(scheduler_data)

# Extract the signal column (assume column 1 is time, column 2 is value)
signal = scheduler_data[:, 1]
print(f"Signal length: {len(signal)}")

wave_p=0
t_mesh=np.zeros(1)
ref_fin=False

alphas = [0.05, 0.1, 0.3, 1.0, 3.0]
thrs = [0.001, 0.005, 0.01, 0.05]
thr_ens = [0.01, 0.05, 0.1, 0.2]

best_params = None
max_modes = 0

for alpha in alphas:
    for thr in thrs:
        for thr_en in thr_ens:
            try:
                Comp_data_full, wp = KMD_lib.semimanual_maxpool_peel2(
                    signal=signal, wave_p=wave_p, alpha=alpha, t_mesh=t_mesh,
                    thr=thr, thr_en=thr_en, ref_fin=ref_fin
                )
                num_modes = Comp_data_full.shape[0]
                print(f"alpha={alpha}, thr={thr}, thr_en={thr_en} => modes: {num_modes}")
                if num_modes > max_modes:
                    max_modes = num_modes
                    best_params = (alpha, thr, thr_en)
            except Exception as e:
                print(f"alpha={alpha}, thr={thr}, thr_en={thr_en} => error: {e}")

print(f"Best params: {best_params} with {max_modes} modes")

num_modes = Comp_data_full.shape[0]
if num_modes == 0:
    print("No modes found.")
    exit(1)
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
    plt.plot(signal)
    plt.legend()
    plt.show()

