import os
from setuptools import find_packages, setup

import numpy as np
from Cython.Build import cythonize
from Cython.Distutils import build_ext


include_path = [
    np.get_include()
]

ext_modules = cythonize("pyembree/*.pyx", language_level=3, include_path=include_path)

for ext in ext_modules:
    ext.include_dirs = include_path
    ext.libraries = [
        "pyembree/embree2/lib/embree",
        "pyembree/embree2/lib/tbb",
        "pyembree/embree2/lib/tbbmalloc",
    ]

setup(
    name="pyembree",
    version="0.1.6",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={"pyembree": ["*.cpp", "*.dll"]},
)

