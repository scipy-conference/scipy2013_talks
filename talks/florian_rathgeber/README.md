PyOP2: a Framework for Performance-Portable Unstructured Mesh-based Simulations and its Application to Finite-Element Computations
==================================================================================================================================

Authors :
---------

* **Florian Rathgeber, Department of Computing, Imperial College London**
* Graham Markall, OpenGamma
* Lawrence Mitchell, EPCC, University of Edinburgh
* Nicolas Loriant, Department of Computing, Imperial College London
* David Ham, Department of Computing, Grantham Institute for Climate Change, Imperial College London
* Gheorghe-teodor Bercea, Department of Computing, Imperial College London
* Fabio Luporini, Department of Computing, Imperial College London
* Paul Kelly, Department of Computing, Imperial College London

Track :
-------

General, [Wednesday June 26, 10:15 - 10:35, Room 204][1]

Abstract :
----------

We present PyOP2, a high-level domain-specific language embedded in Python for
mesh-based simulation codes. Through a simple interface, numerical kernels are
efficiently scheduled and executed over unstructured meshes in parallel.
Without any code changes required, an application can run on a range of
hardware platforms, while implementation details of the parallel execution are
abstracted from the programmer. Performance portability is achieved by
generating optimized low-level OpenMP, MPI, CUDA or OpenCL code for multi-core
CPUs or GPUs at runtime and just-in-time compiling the generated code.

PyOP2 is suitable as an intermediate representation for scientific
computations, which we demonstrate with a finite-element tool chain using the
domain-specific Unified Form Language UFL and the form compiler FFC from the
FEniCS project. Finite-element methods are widely used to approximately solve
partial differential equations on unstructured domains. The local assembly
operation executes the same kernel for every entity of the mesh and is
therefore a natural fit for the PyOP2 computation model. We show how these
kernels are generated automatically from the weak form of an equation given in
UFL. Global assembly and linear solves are passed through to platform-specific
linear algebra backends integrated into PyOP2 through a modular interface.
Using this tool chain, scientists can drive finite-element computations from
an input notation very close to the mathematical model and transparently
benefit from performance-portable parallel execution on their hardware
architecture of choice without requiring specialist knowledge in numerical
analysis or parallel programming.

Contact :
--------

Florian Rathgeber, [@frathgeber](https://twitter.com/frathgeber)

Slides :
--------

* [View slides online][2]
* [Slides repository][3]

Resources :
-----------

* PyOP2 <https://github.com/OP2/PyOP2>
* FFC <https://bitbucket.org/mapdes/ffc>
* Fluidity <https://code.launchpad.net/~fluidity-core/fluidity/firedrake>
* Benchmarks <https://github.com/OP2/PyOP2_benchmarks>

[1]: http://conference.scipy.org/scipy2013/presentation_detail.php?id=213
[2]: http://kynan.github.io/SciPy2013
[3]: http://github.com/kynan/SciPy2013
