"""
kmd: Kernel-Mode Decomposition for 1-D signals.
"""

from .core import (                   # ? add everything the examples need
    make_omega_mesh,
    semimanual_maxpool_peel2,
    manual_maxpool_peel2,
    waveform_from_coeffs,             # ?whatever else you decide is ?public?
)

__all__: list[str] = [
    "make_omega_mesh",
    "semimanual_maxpool_peel2",
    "manual_maxpool_peel2",
    "waveform_from_coeffs",
]

# optional backward-compatibility shim
import sys as _sys
_sys.modules["KMD_lib"] = _sys.modules[__name__]
