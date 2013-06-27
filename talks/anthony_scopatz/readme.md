Title : XDress - Type, But Verify
=================================

Authors : 
----------

- Anthony Scopatz, University of Wisconsin-Madison


Track : 
-------

General Track

Abstract : 
----------

XDress is an automatic wrapper generator for C/C++ written
in pure Python. Currently, xdress may generate Python bindings (via Cython) for
C++ classes & functions and in-memory wrappers for C++ standard library
containers (sets, vectors, maps). In the future, other tools and bindings
will be supported.

The main enabling feature of xdress is a dynamic type system that was designed
with the purpose of API generation in mind.  This type system provides a
canonical abstraction of various kinds of types: base types (int, str, float,
non-templated classes), refined types (even or odd ints, strings containing the
letter ‘a’), and dependent types (templates such arrays, maps, sets, vectors).
This canonical form is itself hashable, being comprised only of strings, ints,
and tuples.

On top of this type system, xdress provides a tool for auto-generating classes
which are views into template instantiations of C++ standard library maps and sets.
Additionally, this tool also creates custom numpy dtypes for any C++ type, class
or struct.  This allows the user to have numpy array views into C++ vectors.

Furthermore, xdress also has a tool which inspects a C++ code base and
automatically generates Cython wrappers for all user-specified classes and
functions.  This significantly eases the burden of supporting mixed language
projects.

The above code generators, however, are just the beginning.  The xdres
system is flexible and powerful enough to engender a suite of other tools which
take advantage of less obvious features.  For example, an automatic verification
& validation utility could take advantage of refinement type predicate functions
to interdict parameter constraints into the API right under the users nose!

This talk will focus on xdress's type system and its use cases.

http://xdress.org/
