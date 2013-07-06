
Title : Data Wrangling with the SheafSystem™
=====================

Authors : 
----------


- Butler, David M., Limit Point Systems, Inc.


Abstract : 
----------

The computational chores associated with data interoperation in scientific computing workflows are often referred to as "data wrangling". Tools for data wrangling have not received the same degree of attention or the level of technical sophistication that the central processes in the workflows have received and the dearth of easy to use, high-level data wrangling tools constitutes a major limitation to both programmer and user productivity. 
A similar data wrangling problem exists in business computing work flows, but in that context it has been successfully addressed using the conceptual framework and rich tool ecosystem provided by the relational data model. Unfortunately, the relational data model has proven unable to provide the same benefits within the scientific computing domain. Succinctly put, the table-oriented conceptual structure and operations of the relational model are a poor fit to both the way we store and the way we use mesh-based data.
The sheaf data model, developed by Limit Point Systems, Inc. in collaboration with the U.S. national labs and with Shell Oil, was created specifically to provide the same benefits to scientific computing that the relational model provides to business computing.
In this poster we describe the architecture and functionality of the SheafSystem™, which implements the sheaf data model as a collection of C++ libraries with Python bindings.  We describe the API for the general sheaf data model, the API for the fiber bundle data model, implemented on top of the sheaf API, and how these layered abstractions support construction of generalized, mesh and property independent tools for data wrangling. We conclude with a summary of current status and plans for further development, including the forthcoming open source release of the SheafSystem™.
