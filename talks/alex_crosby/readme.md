
Title : LarvaMap - A python powered larval transport modeling system
=====================

Authors : 
----------

- Alexander Crosby, RPS ASA, South Kingstown, RI (alex.crosby@rpsgroup.com)
- Kyle Wilcox, RPS ASA, South Kingstown, RI

Track : 
-------

GIS-Geospatial Data Analysis

Talk Slides:
------------
http://slid.es/alexandercrosby/larvamap

Abstract : 
----------

LarvaMap is an open-access larval transport modeling tool. The idea behind LarvaMap is to make it easy for researchers everywhere to use sophisticated larval transport models to explore and test hypotheses about the early life of marine organisms.

LarvaMap integrates four components: an ocean circulation model, a larval behavior library, a python Lagrangian particle model, and a web-system for running the transport models.

An open-source particle transport model was written in python to support LarvaMap. The model utilizes a parallel multi-process architecture. Remote data are cached to a local file in small chunks when a process requires data, and the local data are shared between all of the active processes as the model runs. The caching approach improves performance and reduces the load on data servers by limiting the frequency and total number of web requests as well as the size of the data being moved over the internet.

Model outputs include particle trajectories in common formats (i.e. netCDF-CF and ESRI Shapefile), a web accessible geojson representation of the particle centroid trajectory, and a stochastic GeoTIFF representation of the probabilities associated with a collection of modeling runs. The common interoperable data formats allow a variety of tools to be used for in-depth analysis of the model results.

_____


Title : SCI-WMS: A Python Based Web Map Service For Met-Ocean Data Accessible Over OpenDAP Or As NetCDF
=====================

Authors : 
----------

- Alexander Crosby, RPS ASA, South Kingstown, RI (alex.crosby@rpsgroup.com)

Track : 
-------

GIS-Geospatial Data Analysis

Talk Slides:
------------
http://slid.es/alexandercrosby/sci-wms

Abstract : 
----------

SCI-WMS is a Python based web map service (WMS) designed as a web service for visualization of local or remote data such that they can be overlaid in georeferenced mapping environments like web maps or geographic information systems (GIS). The service follows the Open Geospatial Consortium (OGC) WMS specifications and is focused on the visualization of gridded data and unstructured meshes commonly stored in NetCDF files or available from distributed servers over the OpenDAP protocol. WMS servers are commonly used to visualize large archives of numerically modeled and observed data, and SCI-WMS is currently used in several U.S. Integrated Ocean Observing System (IOOS) projects around the country including the IOOS Super-regional Modeling Testbed and regional data portals. SCI-WMS was originally developed to fill a need for standards based visualization and data access tools to examine differences between unstructured mesh ocean models like FVCOM and ADCIRC, and the available visualization styles attempt to preserve as much of the complex topology as possible in the unstructured meshes. Support for regularly gridded datasets expanded the applicability of SCI-WMS for use with more commonly available ocean and meteorological model output as well as satellite derived observations.
