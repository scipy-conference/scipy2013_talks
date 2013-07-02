Title : Advances in delivery and access tools for coastal ocean model data
=================================

Authors : 
----------

Rich Signell, US Geological Survey, Woods Hole, MA (rsignell@usgs.gov)


Track : 
-------

Meteorology, Climatology, Atmospheric and Oceanic Science

Abstract : 
----------

Coastal ocean modelers are producers and consumers of vast and varied data, and spend significant effort on tasks that could be eliminated by better tools. In the last several years, standardization led by the US Integrated Ocean Observing System Program to use OPeNDAP for delivery of gridded data (e.g. model fields, remote sensing) and OGC Sensor Observation Services (SOS) for delivery of in situ data (e.g. time series sensors, profilers, ADCPs, drifters, gliders) has resulted in significant advancements, making it easier to deliver, find, access and analyze data. For distributing model results, the Unidata THREDDS Data Server and PyDAP deliver aggregated data via OPeNDAP and other web services with low impact on providers. For accessing data, NetCDF4-Python and PyDAP both allow efficient access to OPeNDAP data sources, but do not take advantage of common data models for structured and unstructured grids enabled by community-developed CF and UGRID conventions. This is starting to change with CF-data model based projects like the UK Met Office Iris project. Examples of accessing and visualizing both curvilinear and unstructured grid model output in Python will be presented, including both the IPython Notebook and ArcGIS 10.1.

