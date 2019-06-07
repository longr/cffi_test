#import os
import cffi
ffi = cffi.FFI()

#with open(os.path.join(os.path.dirname(__file__), "point.h")) as f:
#with open(os.path.join(os.path.dirname(__file__), "../src/point.h")) as f:
with open("src/point.h") as f:
    ffi.cdef(f.read())
    
ffi.set_source("point._point",
               # Since we are calling a fully built library directly no custom source
               # is necessary. We need to include the .h files, though, because behind
               # th scenes cffi generates a .c file which contains a Python-friendly
               # wrapper around each of the functions.
               '#include "point.h"',
               # The important thing is to include the pre-built lib in the list of
               # libraries we are linking against:
               #libraries=['point'],
               #library_dirs=[os.path.dirname(__file__),'',],
               #extra_objects=['/home/longr/Public/PyCFFI/my_cffi/_point.o'],
               #include_dirs=['/home/longr/Public/PyCFFI/my_cffi','.','./build'],
               include_dirs=['src/'],
               sources=['src/point.c'])
               #extra_compile_args=['--std=c99'])

ffi.compile(verbose=False)
