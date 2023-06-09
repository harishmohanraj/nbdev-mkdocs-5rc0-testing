# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Fixture.ipynb.

# %% auto 0
__all__ = ['Car']

# %% ../nbs/Fixture.ipynb 1
from typing import *
from tempfile import TemporaryDirectory

from nbdev.doclinks import NbdevLookup
from fastcore.basics import patch

from nbdev_mkdocs.mkdocs import prepare

from .core import foo

# %% ../nbs/Fixture.ipynb 2
class Car:
    """A class representing a car.

    Attributes:
        make: The make of the car.
        model: The model of the car.
        year: The year the car was made.
        color: The color of the car.
    """
    SOME_ATTRIBUTE = "Some class attribute"

    def __init__(self, make: str, model: str, year: int, color: str):
        """Initialize a new car.

        Args:
            make: The make of the car.
            model: The model of the car.
            year: The year the car was made.
            color: The color of the car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
        
    def __len__(self):
        """len function"""
        return 5

    def start(self):
        """Start the car."""
        self.is_running = True

    def stop(self):
        """Stop the car."""
        self.is_running = False

    def drive(
        self,
        distance: float,
        speed: Optional[float] = None,
        passengers: Optional[int] = None,
    ) -> float:
        """Drive the car a certain distance at an optional speed with an optional number of passengers and
        return the distance driven.

        Args:
            distance: The distance to drive in kilometers.
            speed: The speed to drive at in kilometers per hour. Defaults to None.
            passengers: The number of passengers in the car. Defaults to None.

        Returns:
            The distance driven in kilometers.
        """
        if not self.is_running:
            raise ValueError("Cannot drive a stopped car.")

        if speed:
            print(f"Driving at {speed} km/h.")

        if passengers:
            print(f"Driving with {passengers} passengers.")

        return distance
    
    def random_method(self, nb_lookup: NbdevLookup, d:TemporaryDirectory, p: foo): 
        """random_method

        Args:
            nb_lookup: nb_lookup
            d: TemporaryDirectory
            p: prepare
        """
        return f"random_method."
    
    def patched_method_in_same_file(self, s: str) -> foo:
        raise NotImplementedError()
        
    def patched_method_from_a_different_file(self, s: str) -> str:
        raise NotImplementedError()

    @staticmethod
    def i_am_a_static_method(name: str) -> str:
        """I am a static method
        
        Args:
            name: Name to say hello
            
        Returns:
            A string
            
        Example:

            ```python

            from  nbdev_mkdocs.docstring import run_examples_from_docstring

            def f():
                ```python
                Example:
                    print("Hello {fill in name}!")
                    print("Goodbye {fill in other_name}!")
                ```
                pass


            run_examples_from_docstring(f, name="John", other_name="Jane")
            ```
        """
        if not isinstance(name, str):
            raise ValueError("I will accept only string")
        return f"Hello, {name}"
    
    @classmethod
    def i_am_a_class_method(cls):
        """I am a class method
        
        I return "Nothing"
        """
        return f"Nothing"

# %% ../nbs/Fixture.ipynb 4
@patch
def patched_method_in_same_file(self:Car, s: str) -> prepare: 
    """I am a patched method in the same file
    
    Args:
        s: string
    
    Returns:
        prepare
    """
    return prepare
