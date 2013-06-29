
Title : Matrix Expressions and BLAS/LAPACK 
==========================================

Authors : 
----------


- Matthew Rocklin, University of Chicago 


Track :  
-------

General

Abstract : 
----------

Numeric linear algebra is both important and ubiquitous. The BLAS/LAPACK libraries include high performance implementations of dense linear algebra algorithms in a variety of mathematical situations. They are underused because

*   The interface is challenging to scientific users
*   The number of routines is huge, pressuring users to select general routines rather than finding the one that best fits their situation.

I demonstrate a small DSL for Matrix Algebra embedded in the SymPy project. I use logic programming to infer attributes about larger matrix expressions. I describe the BLAS and LAPACK libraries programmatically and use strategic programming to automatically build directed acyclic graphs of BLAS/LAPACK operations to compute complex expressions. From these I generate readable Fortran code. I then use f2py to bring this back into Python. The result is a clean mathematical interface that efficiently generates mathematically informed numeric code.

Philosophically I'll plug the following ideas

1. **Multiple clean intermediate representations** - Aside from a runnable Python function this project also generates perfectly readable Fortran90 code and a directed acyclic graph.
2. **Declarative programming** - All of the math in this project is defined separately from the algorithms, increasing opportunities for independent development. I'll probably talk about separating what code from how code.
3. I may evangelize a bit about small, modular and generally applicable projects.
