
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
restarting (from a checkpoint image).  Applications of DMTCP are demonstrated
for: (i) Python-based graphics using VNC; (ii) a Fast/Slow technique
to use multiple hosts or cores to check one Cython computation in parallel;
and (iii) a reversible debugger, FReD[2], with a novel reverse-expression
watchpoint feature for locating the cause of a bug.

[1] http://dmtcp.sourceforge.net

[2] https://github.com/fred-dbg/fred
