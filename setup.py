from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([
        "src/poke.pyx",
        "src/battle.pyx",
        "src/team.pyx"
    ])
)