Title 1 : An efficient workflow for reproducible science
========================================================

Authors :
----------

- Trevor Bekolay, University of Waterloo

Track :
-------

Reproducible science

Abstract :
----------

Every scientist should be able to regenerate the figures in a
paper. However, all too often the correct version of a script goes
missing, or the original raw data is filtered by hand and the
filtering process undocumented, or the student who has the data or
code has switched labs.

In this talk, I will describe a workflow for a complete end-to-end
analysis pipeline, going from raw data to analysis to plotting, using
existing tools to make each step of the pipeline reproducible,
documented, and efficient, while requiring few sacrifices in terms of
a scientist's time and effort.

I will discuss a way to organize code in order to make analyzing and
plotting large data sets efficient, parallelizable, and
cacheable. Once completed, source code can be uploaded to a hosting
service like Github or Bitbucket, and data can be uploaded to a data
store like Amazon S3 or figshare. The end result is that readers can
completely regenerate the figures in your paper at no or nearly no
cost to you.

Slides :
--------

<http://bekolay.org/scipy2013-workflow> (press S to see notes)

Slides source :
---------------

[tbekolay/scipy2013-workflow](https://github.com/tbekolay/scipy2013-workflow)

Title 2 : A comprehensive look at representing physical quantities in Python
============================================================================

Authors :
----------

- Trevor Bekolay, University of Waterloo

Track :
-------

General

Abstract :
----------

Code that properly tracks the units associated with physical
quantities is self-documenting and far more robust to unit conversion
errors. Unit conversion errors are common in any program that deal
with physical quantities, and have been responsible for several
expensive and dangerous software errors, like the Mars Climate Orbiter
crash. Support for tracking units is lacking in commonly used packages
like NumPy and SciPy. As a result, a whole host of packages have been
created to fill this gap, with varying implementations. Some build on
top of the commonly used scientific packages, adding to their data
structures the ability to track units. Others packages track units
separately, and store a mapping between units and the data structures
containing magnitudes.

I will discuss why tracking physical quantities is an essential
function for any programming language heavily used in science. I will
then compare and contrast all of the packages that currently exist for
tracking quantities in terms of their functionality, syntax,
underlying implementation, and performance. Finally, I will present a
possible unification of the existing packages that enables the
majority of use cases, and I will discuss where that unified
implementation fits into the current scientific Python environment.

Slides :
--------

<http://bekolay.org/scipy2013-quantities> (press S to see notes)

Slides source :
---------------

[tbekolay/scipy2013-quantities](https://github.com/tbekolay/scipy2013-quantities)
