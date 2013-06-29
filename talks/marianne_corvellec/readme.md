Title : OS deduplication with SIDUS (single-instance distributing universal system)
=====================


Authors : 
----------

- Emmanuel Quémener, Centre Blaise Pascal (Lyon, France)

- Marianne Corvellec, Wajam Internet Technologies Inc. (Montréal, Canada)


Track : 
-------

Reproducible Science

Wed, June 26, 2013
3:30pm


Abstract : 
----------

Developing scientific programs to be run on multiple platforms takes caution.
Python is typically great as a glue language (COTS approach, for 'Component
Off the Shelf'). But massive integration requires a technical platform which
may be difficult to even deploy. It may be tempting to stick to the same
environment for both development and operation. But environments on HPC nodes
are very different from those on workstations. Even if Python comes with
'batteries included', it relies on external (C or Fortran) libraries,
especially via SciPy. So you want to be careful when running your Python codes
on a cluster, after developing it on your workstation. In the end, how do you
compare two scientific results from the same program run on two different
stations? In the variability, how do you tell the part due to the hardware
from the part due to the software? As a scientist, you typically port your
Python code from your workstation to cluster nodes. You want to have a uniform
software base, so that discrepancies between runs can be attributed to
hardware differences, or to the actual code, if edited. SIDUS (single-instance
distributing universal system) is your solution for extreme deduplication of
an operating system (OS). SIDUS offers scientists a framework for conducting
reproducible experiments. Two nodes booting on the same SIDUS base run the
exact same system. This way, actually relevant tests can be carried out. We
recently used Python to evaluate performance for a cluster-distributed file
system. Unexpectedly, early results showed lack of reproducibility over time
as well as over the different nodes. Using SIDUS, it was possible to discard
that discrepancies might come from the OS. We could identify that they were due
to C-states (CPU power-saving modes), which are responsible for large
fluctuations in global performance losses (up to 50%).


Slideshow viewable at http://slideviewer.herokuapp.com/urls/bitbucket.org/StatMarianne/sidus-slideshow/raw/675878a2c998d541a25d455f48f3d83df3b2e60e/sidus_scipy2013.ipynb#/

Talk repository available at https://bitbucket.org/StatMarianne/sidus-slideshow
