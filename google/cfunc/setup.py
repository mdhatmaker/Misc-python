from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3

# python setup.py build_ext --inplace

examples_extension = Extension(
    name="pyfunction",
    sources=["pyfunction.pyx"],
    libraries=["function"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)
setup(
    name="pyfunction",
    ext_modules=cythonize([examples_extension])
)
