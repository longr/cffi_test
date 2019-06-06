# Test base.

## Build and install
Build using
```
python setup.py sdist
```

and then install by doing:

```
pip install . --user
```


## Running.

Run the code using following commands:

```
import Point
new_point = point.Point(2, 3)
new_point.show_point()
```


## How it works.

### Modules / package
Not entirly sure. __init__.py needed so that python knows it is a module. This needs to contain
```
from point import Point
```
otherwise to run the code you need:

```
from point.point import Point
a = Point(2, 3)
```
or
```
import point
point.point.Point()
```

### setup.py

```
from setuptools import setup#, find_packages

setup(name='point',
      version='0.1',
      #packages=find_packages(), #still builds, maynot be needed.
      description='dbader point',
      #py_modules=['point'], ?? What does this do?
      setup_requires=['cffi'],
      cffi_modules=['point/build_point.py:ffi'],
      install_requires=['cffi'],
)
```
name, version, and descrition are obvious.
- TODO: google diff between setup requires and install requires.
```cffi_modules``` is a list of modules for cffi to run for building the c code. Syntax is:
```
<path_to_module>/<build_file>:<name_of_FFI_object_instance)
```


### build_point.py

