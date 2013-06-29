
Title : lmonade: a platform for development and distribution of scientific software
=====================

Authors :
----------

- [Burcin Erocal](http://erocal.org/burcin), TU Kaiserslautern


Track :
-------

Reproducible Science

Abstract :
----------

Most results in experimental mathematics are accompanied by software
implementations which often push the boundaries of what can be computed in
terms of mathematical theory and efficiency. Since new algorithms are built
on existing ones, just as theorems are derived from existing results, it
would be natural to expect that the code produced for one project will be
useful later on, to both the same researcher and others.

While theorems blissfully stay intact over time, software deteriorates and
ages. Implementations need to be updated with respect to changes in
underlying libraries and hardware architectures. Even if up to date,
software developed for a specific application area often needs to be
adapted to new situations. Like proofs can be reused by taking some
components intact and modifying certain parts, software needs similar
adaptations to be reusable.

It is natural that researchers cannot commit any more time than absolutely
necessary for distributing and maintaining their software.  [The lmonade
project](http://www.lmona.de) aims to provide infrastructure and tools to
foster code sharing and openness in scientific software development by

* simplifying the tasks of distributing software with its dependencies,
* ensuring that it can be built on different platforms, and
* making sure the software is compatible across new releases of its
  dependencies.

This is achieved through

* a light-weight meta distribution which can be installed by a user without
  administrative rights. Building on the [Gentoo Linux
  distribution](http://www.gentoo.org) and the [Gentoo Prefix
  project](http://www.gentoo.org/proj/en/gentoo-alt/prefix/),
  [lmonade](http://www.lmona.de) creates a uniform environment for software
  development where latest versions of scientific libraries can be found
  easily.
* access to a continuous integration infrastructure to detect compatibility
  problems between new versions of packages automatically and warn authors.

By simplifying code sharing and distribution, especially when complex
dependencies are involved, this platform enables researchers to build on
existing tools without fear of losing users to baffling installation
instructions.

**Slides:** [pdf](http://erocal.org/burcin/talks/20130627-scipy2013-lmonade.pdf)
