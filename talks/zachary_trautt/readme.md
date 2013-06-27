
Title : Using IPython Notebook with IPython Cluster for Reproducibility and Portability of Atomistic Simulations
=====================

Authors : 
----------


- Zachary Trautt, Materials Measurement Science Division, National Institute of Standards and Technology, Gaithersburg, MD 20899 USA

- Lawrence Friedman, Materials Measurement Science Division, National Institute of Standards and Technology, Gaithersburg, MD 20899 USA

- Chandler Becker, Materials Science and Engineering Division, National Institute of Standards and Technology, Gaithersburg, MD 20899 USA


Track : 
-------

Reproducible Science

Abstract : 
----------

The information presented in a typical journal article is rarely sufficient to reproduce all atomistic simulations reported within. A typical study requires the distribution of parallel preprocessing, production, and post processing tasks. This is typically accomplished with scripting and a queuing system and is not typically captured in a publication or supporting information. A traditional workflow tool can capture this. However, a traditional workflow tool has a steep learning curve and many are not capable of distributing parallel tasks. We present the use of IPython Notebook and IPython Cluster as a tool for reproducible and portable atomistic simulations. IPython Notebook is used to define and annotate functions that implement simulation tasks. IPython Cluster is used to execute and distribute tasks, including external parallel tasks. This combination is an improvement for a number of reasons. First, the IPython notebook documents all steps of all simulations and can easily be included as supplementary information with a journal submission. Second, the IPython Cluster executes computational tasks with minimal effort (a single map command) and therefore does not distract from the science. Third, the IPython Cluster abstracts computational resources, such that organization-specific computational details (cluster name, batch submission details, etc.) are not defined in the notebook. Therefore, if a third party attempts to reproduce simulation results, the notebook can be used without modification if all dependencies are met. Furthermore, the initial researcher may observe a reduction of their time effort because of the efficiency gains in using a single map command over traditional scripting for the distribution of tasks.
