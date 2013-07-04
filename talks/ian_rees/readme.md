
Title : EMAN2 and EMEN2: Flexible Python-based platforms for electron microscopy
=====================

Authors : 
----------


- Ian Rees, Baylor College of Medicine

- Steven J. Ludtke, Baylor College of Medicine


Track : 
-------

Bioinformatics: Frameworks

Abstract : 
----------

Three-dimensional electron microscopy has developed into a powerful technique
for obtaining structural information that often cannot be obtained with other
methods. Progress in the field continually produces new experimental techniques
for sample preparation, imaging, image processing, reconstruction algorithms,
and structural analysis tools -- resulting in rich data sets with substantial
amounts of experimental variation. This constantly evolving landscape requires
flexible software platforms for developing new algorithms and for sharing data
with collaborators and the public. At the National Center for Macromolecular
Imaging, we have developed two open-source, Python-based tools: EMAN2 and EMEN2.

EMAN2 is a modular, extensible scientific image processing suite implemented in
Python and C++. This mixed approach allows speed-critical image processing
algorithms to be written in C++, as high resolution 3D reconstructions can
require tens of thousands of images and hundreds of thousands of CPU hours. The
core distribution includes over 200 image processing algorithms, and new
algorithms can easily be added and called from C++ or Python. Conversely,
application-level code and UIs are written in Python, which enhances developer
productivity and lowers the level of difficulty for scientists to write new
programs.

EMEN2 is an object-oriented scientific database and electronic lab notebook,
with a flexible schema based on user-created descriptions of experimental
protocols. These descriptions allow investigators to quickly add new types of
data to the system without requiring a database administrator. EMEN2 provides a
flexible security model for sharing data with collaborators and public. EMEN2
uses Berkeley DB for the storage backend, provides a web interface built using
Twisted and MakoTemplates, and allows API access via JSON-RPC. EMEN2 also
includes a desktop client, EMDash, for uploading raw data from instruments in
real time.

While both EMAN2 and EMEN2 have their roots in the electron microscopy
community, we hope they may be of interest to users in other domains.
