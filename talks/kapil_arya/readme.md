
Title : DMTCP: Bringing Checkpoint-Restart to Python
=====================

Authors : 
----------


- Kapil Arya, Northeastern Universiry

- Gene Cooperman, Northeastern Universiry


Track : 
-------

General

Abstract : 
----------

DMTCP (Distributed MultiThreaded CheckPointing)[1] is a mature
checkpoint-restart package.  It operates in user-space without kernel
privilege, and adapts to application-specific requirements through plugins.
While DMTCP has been able to checkpoint Python and IPython "from  the
outside" for many years, a Python module has recently been created to
support DMTCP.  IPython support is included through a new DMTCP plugin.
A checkpoint can be requested interactively within a
Python session, or under the control of a specific Python program.
Further, the Python program can execute specific Python code prior
to checkpoint, upon resuming (within the original process), and upon
restarting (from a checkpoint image).

Classically, this is used to implement a saveWorkspace function
(including visualization and the distributed processes of IPython).
In addition, at least three novel uses of DMTCP for helping debug
Python are demonstrated.

1.  FReD[2] --- a Fast Reversible Debugger that works closely with
    the Python pdb debugger, as well as other Python debuggers.

2.  Reverse Expression Watchpoint --- A bug occurred in the past.
    It is associated with the point in time when a certain
    expression changed.  Bring the user back to a pdb session
    at the step before the bug occurred.

3.  Fast/Slow Computation[3] --- Cython provides both traditional
    interpreted functions and compiled C functions.  Interpreted
    functions are slow, but correct.  Compiled functions are fast,
    but users sometimes define them incorrectly, whereupon the
    compiled function silently returns a wrong answer.  The idea
    of fast/slow computation is to run the compiled version on
    one core, with checkpoints at frequent intervals, and to
    copy a checkpoint to another core.  The second core re-runs
    the computation over that interval, but in interpreted mode.

[1] http://dmtcp.sourceforge.net
[2] https://github.com/fred-dbg/fred
