## CFFI API out-of-line implementation.
# Test as potential for speed up by not using sources=
# CFFI Docs, page 26.

import cffi
ffi = cffi.FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
with open("src/point.h") as f:
    ffi.cdef(f.read())


# set_source() gives the name of the python extension module to
# produce, and some C source code as a string. This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".

ffi.set_source("point._point",
               '#include "point.h"',
               # include_dirs is needed to let cffi find the .h files.
               # their examples do not need this. Investigate?
               include_dirs=['src/'],
               sources=['src/point.c'])
               #extra_compile_args=['--std=c99'])

ffi.compile(verbose=False)

