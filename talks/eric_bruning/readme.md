
Title : Streamed Clustering of Lightning Mapping Data in Python Using scikit-learn
=====================

Authors : 
----------

- Eric Bruning, Texas Tech University


Track : 
-------
Mini-Symposia, Day 1 - Wed., June 26th
GIS - Geospatial Data Analysis
Rm 102, 6:00 - 6:15 pm


Abstract : 
----------
Lightning mapping at radio frequencies (here with VHF Lightning Mapping Array data) is typically performed by a time-of-arrival source retrieval method. Thereafter, it is common to cluster the located sources into flash-level entities (often comprised of 10^2 - 10^3 sources) using space and time separation thresholds. A previously-used clustering algorithm was a one-off implementation in Fortran, and was designed without reference to the machine learning literature. This study replaces the previous algorithm, which had been wrapped into the Python-based lmatools workflow, with the general-purpose DBSCAN implementation in Python's sklearn package. The legacy code included substantial, file format-specific, I/O boilerplate. The new code clarifies the boundary between algorithm and I/O, and promotes clean integration with the rest of the lmatools infrastructure, aiding maintainability.

A chunked, streamed processing method was developed to account for continuous data rates that may exceed 10^5 four-coordinate (space and time) source vectors per minute. The chunking method exploits known physical limits to lightning flash duration, allowing the N^2 implementation of DBSCAN in sklearn to achieve real-time processing rates within available memory. The streaming technique is expected to be useful in future work as a flexible building block for end-to-end real-time and post-processing scripts and interactive analysis tools.

The algorithm is expected to find immediate use in our analysis of data from the NSF-sponsored Deep Convective Clouds and Chemistry campaign. The open nature of the underlying clustering libraries promotes code reuse by other research groups. Accounts of source-to-flash clustering in the literature are complemented by the availability of this open, objective reference implementation for clustering of lightning mapping datasets.