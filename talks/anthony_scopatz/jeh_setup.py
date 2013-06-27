import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'jehsrc'), np.get_include()]

ext_modules = [
    Extension("jedgar.hoover", ['jehsrc/hoover.cpp', "jedgar/hoover.pyx", ],
    	include_dirs=incdirs, language="c++")
    ]

setup(  
  name = 'jedgar',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['jedgar']
)
