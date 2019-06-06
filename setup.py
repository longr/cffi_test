from setuptools import setup, find_packages

setup(name='point',
      version='0.1',
      #packages=find_packages(),
      description='dbader point',
      #py_modules=['point'], ?? What does this do?
      setup_requires=['cffi'],
      cffi_modules=['point/build_point.py:ffi'],
      install_requires=['cffi'],
)
