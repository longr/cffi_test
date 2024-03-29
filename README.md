# CFFI - Python and C example.

This will mature into something better, but for now it is notes and scriblings as I fumble through running C code in python using cffi.  Links tho pages that have been used to achieve this are listed at the bottom.  Main source of knowledge has been Dimitri Merejkowsky's lets build chuck norris, and the code for this (point) comes from Jim Anderson's contribution on dbader.org



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

Needed to install packages.  Also calls files to build our c library.

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
#### py_modules

This is not needed at this level.. Just used for.        #py_modules=['point'], ?? What does this do?
      # explanation here  https://github.com/pypa/packaging.python.org/issues/397


### build_point.py

Should read CFFI docs at https://cffi.readthedocs.org/en/latest/ to explain this file.

create an instance of FFI() (name it that same as we did in the ```cffi_modules``` line of ```setup.py```

```
ffi = cffi.FFI()
```

Then we use ```cdef``` to declare the functions, variables, and so on that we have defined in out c code and want to access from our C extenion.  # https://cffi.readthedocs.org/en/latest/cdef.html#ffi-cdef-declaring-types-and-functions.  These are usually the things in your .h file(s)

Could do this manually as:

```
ffi.cdef(
	"""
	/* Simple structure for ctypes example */
	typedef struct {
	    int x;
	    int y;
	    } Point;

	void show_point(Point point);
	void move_point(Point point);
	void move_point_by_ref(Point *point);
	Point get_default_point(void);
	Point get_point(int x, int y);
	""")
```

If we want all accessible, or don't mind, then we could do:

```
with open("src/point.h") as f:
    ffi.cdef(f.read())
```

which instructs python to read in our point.h and send the contents to ```ffc.cdef```.  This fits better with DRY (Do not Repeat Yourself).

Next we need to tell ```ffi``` about our source files (the .c and associated files.)

```
# set_source is where you specify all the include statements necessary
# for your code to work and also where you specify additional code you
# want compiled up with your extension, e.g. custom C code you've written
#
# set_source takes mostly the same arguments as distutils' Extension, see:
# https://cffi.readthedocs.org/en/latest/cdef.html#ffi-set-source-preparing-out-of-line-modules
# https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension     
ffi.set_source("point._point",
               '#include "point.h"',
               include_dirs=['src/'],
               sources=['src/point.c'],
               extra_compile_args=['--std=c99'])
```

First argument is ***** which is usually the name of the directory containing the python module, followed by a dot, followed by an underscore, and then the name of the c library. ******EXPLAIN******

**** REASON FOR .h?? *********
The next are more obvious, any directories we need to include for it to be able to compile, we put in a list and pass to ```include_dirs```.  Same with source files.

Finally we need to run the compile method on our ```ffi``` object so that is will compile our c library.

```
ffi.compile(verbose=False)
```



### calling the library from python

Next we need to call out module from python. We need a python file that can import this compiled library.  The first thing we need to do in this file is import the our compiled library.

```
import _<library_name>
```

in the case of this example, that is:

```
import _point
```

Then we can access the methods and functions by doing:

```
<imported_module>.lib.<method/function/variable>
```

which again for our case is:

```
_point.lib.get_point(x, y)
```

### Layout
Layout is perhaps optional, but a module layout with module_name, and src is cleaner.

Basic tree is:


```
.---point
|   |--- build_point.py
|   |--- __init__.py
|   \--- point.py
|--- README.md
|--- setup.py
\--- src
     |--- point.c
     \--- point.h
```

NEED TO CHECK THIS.  PEP420 specifys namespace, new layout may be needed.


### Manifest

Need a `MANIFEST.in` and need to specify inclussion of `.h` files.  Need to check the reasoning behind this.


##
Links:
- https://python-packaging.readthedocs.io/en/latest/minimal.html
- https://inventwithpython.com/blog/2019/06/05/pythonic-ways-to-use-dictionaries/
- https://dbader.org/blog/python-cffi
- https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/contributing.html
- https://github.com/jiffyclub/cext23#cffi
- https://dzone.com/articles/executable-package-pip-install
- https://packaging.python.org/tutorials/installing-packages/
- https://realpython.com/python-modules-packages/
- https://dmerej.info/blog/post/chuck-norris-part-5-python-cffi/



###Questions
- PG 11, namespace and layout. Check how numpy handles this.
- Check if usig slashes due to windows.
- Data files, use pkg_resoucres
- Tr y and figure out how matplotlib or numpy does its C code.