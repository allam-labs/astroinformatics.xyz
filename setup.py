from os.path import join, dirname, realpath
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name='spinup',
    py_modules=['spinup'],
    version=__version__,
    install_requires=[
        'ipython',
        'joblib',
        'matplotlib==3.1.1',
        'mpi4py',
        'numpy',
        'pandas',
        'pytest',
        'scipy',
        'seaborn==0.8.1',
        'tensorflow>=1.8.0,<2.0',
        'tqdm'
    ],
    description="All things Astroinformatics.",
    author="Joshua Achiam",
)
