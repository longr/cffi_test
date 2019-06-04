from setuptools import setup, find_packages

setup(name='point',
      version='0.1',
      description='dbader point',
      py_modules=['point'],
      setup_requires=['cffi'],
      cffi_modules=['build_point.py:ffi'],
      install_requires=['cffi'],
)
