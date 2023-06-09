# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Fixture_Two.ipynb.

# %% auto 0
__all__ = []

# %% ../nbs/Fixture_Two.ipynb 1
from typing import *

from fastcore.basics import patch

from .fixture import Car

# %% ../nbs/Fixture_Two.ipynb 2
@patch
def patched_method_from_a_different_file(self:Car, s: str) -> str: 
    """I am a patched method from a different file
    
    Args:
        s: string
        
    Returns:
        A string
    """
    return f"Hello, {s}."
