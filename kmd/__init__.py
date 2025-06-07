"""Toplevel package for Kernel Mode Decomposition 1D (KMD1F).

This module re-exports every public symbol from :pymod:`kmd.core` so
that users can do::

    from kmd import make_omega_mesh, semimanual_maxpool_peel2, ...

or continue to run the legacy examples unchanged::

    import KMD_lib  # still works

Maintainers are encouraged to curate ``__all__`` inside :pymod:`kmd.core`.
If it is absent, we fall back to every attribute that does *not* start
with an underscore.
"""

from __future__ import annotations

import sys as _sys
from types import ModuleType as _ModuleType

from . import core as _core  # single import source of truth

# ---------------------------------------------------------------------------
# Public surface
# ---------------------------------------------------------------------------

if hasattr(_core, "__all__"):
    __all__: list[str] = list(_core.__all__)  # respect author intent
else:
    # Export every non?private attribute that doesn?t look like a dunder.
    __all__ = [name for name in dir(_core) if not name.startswith("_")]

# Inject the collected names into *this* module?s globals so they can be
# imported directly from ``kmd``.
_globals = globals()
for _name in __all__:
    _globals[_name] = getattr(_core, _name)

del _globals  # tidy?up namespace

# ---------------------------------------------------------------------------
# Backward compatibility shim ? legacy code used ``import KMD_lib``
# ---------------------------------------------------------------------------

_sys.modules["KMD_lib"] = _sys.modules[__name__]

# ---------------------------------------------------------------------------
# Housekeeping ? do not leak helper names
# ---------------------------------------------------------------------------

del _core, _ModuleType, _sys
