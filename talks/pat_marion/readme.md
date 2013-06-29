
Title : Import without a filesystem: scientific Python built-in with static linking and frozen modules
======================================================================================================

Authors :
---------

- Pat Marion, Kitware, Inc.
- Aron Ahmadia
- Bradley M. Froehle, University of California, Berkeley

Track :
-------

General

Abstract :
----------

Scientific Python is growing in popularity among HPC and supercomputing communities, but suffers from a seemingly simple and fundamental problem: importing modules from a shared network filesystem at extreme scale will cripple the performance of a parallel Python program.

At SciPy '12, the presentation titled "Solving the import problem: Scalable Dynamic Loading Network File Systems" analyzed the issue and proposed several remedies, but concluded there was more work to be done. Now, this talk introduces a new technique that leverages the linker to embed C-extension modules, and uses Python freeze to embed pure python modules. The result is a program that imports the Python standard library and scientific Python modules such as NumPy without accessing the filesystem. It achieves near-instant, and always-constant, import time even at full machine scale on today's largest supercomputers. The same technique is also relevant to Python app developers on mobile and embedded systems where filesystem access and dynamic loading inflate app startup time.

This talk will discuss the concepts involved using a simple hello-world demonstration, and overview a real-world example where Python was used to compute at full machine scale on Argonne's Intrepid BlueGene/P supercomputer.
