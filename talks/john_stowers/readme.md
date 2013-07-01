
Title : Managing Complex Experiments, Automation, and Analysis using Robot Operating System
=====================

Authors : 
----------


- John Stowers, TU Wien

- Andrew Straw, The Research Institute of Molecular Pathology (IMP)


Track : 
-------

Reproducible Science

Abstract : 
----------

The Robot Operating System (ROS), and its Python bindings, are well known and used
in the engineering and robotics communities for the many high level tools and algorithms
they provide. Less appreciated are the lower levels of the ROS stack; libraries for
inter-process-communication, parameter and configuration management, and distributed
process launching and control.

In the Straw laboratory we use ROS to automate the operation of, and experiments
using, virtual reality systems for fixed and freely flying Drosophila. This includes
real-time 10-camera tracking (100Hz), 5 projector panoramic virtual reality (120Hz),
and real-time visual stimulus generation and control (80Hz). Operation of this system
requires the launching of over 30 processes on 4 computers, and the associated
configuration of each in a known state. In addition, the progress of the experiment
must be monitored over its entire 12 hour duration.

In this talk we will describe how ROS makes this complex system manageable and
reproducible by implicitly recording the state of the system at all times, and by
automating the pre-configuration and launching of the multiple processes which
control the experiment. I will also describe how we tag all experimental data
with unique identifiers to facilitate live monitoring, post-experiment analysis,
and long time archival in case later forensics are required.

This talk will show that ROS is a very powerful tool and should not only be
considered for engineering and robotics applications; but by any scientist for
robustly and reproducibly managing complex scientific experiments.

