from setuptools import setup, find_packages

setup(name='point',
      version='0.1',
      packages=find_packages(),
      description='python calling c code through cffi. supporedt by dbader point',
      setup_requires=['cffi'],
      cffi_modules=['point/build_point.py:ffi'],
      include_dirs=['src'],
      install_requires=['cffi'],
      author='Robin Long',
      author_email='r.l@l.com',
      url='github.com',
      keywords='python cffi example c-code',
      license='need one',
)
