Entry 2
=======

.. image:: entry2.png

Authors
-------
 - Jake Vanderplas
 - Zeljko Ivezic
 - Andrew Connolly

This figure is based on the data presented in Figure 1 of Cowan &
Ivezic (2008). A similar figure appears in the book "Statistics, Data
Mining, and Machine Learning in Astronomy", by Ivezic, Connolly,
Vanderplas, and Gray (2013).

Running this code requires astroML, a lightweight python package which
can be quickly installed using `pip install astroML`.  See
`<http://astroML.github.com>`_ for more information.  AstroML will
automatically download and cache the required dataset to
`$HOME/astroML_data`.

Figure Caption
--------------
The three panels of this figure show a hierarchical clustering of a subset
of galaxies from the Sloan Digital Sky Survey (SDSS).  This region is known
as the "SDSS Great Wall", and contains an extended cluster of several thousand
galaxies approximately 300Mpc (about 1 billion light years) from earth.  The
top panel shows the positions of over 8,000 galaxies projected to a 2D plane
with Earth at the point (0, 0).  The middle panel shows a dendrogram
representation of a Euclidean Minimum Spanning Tree (MST) over the galaxy
locations.  By eliminating edges of a MST which are greater than a given
length, we can measure the amount of clustering at that scale: this is one
version of a class of models known as Hierarchical Clustering.  The bottom
panel shows the results of this clustering approach for an edge cutoff of
3.5Mpc, along with a Gaussian Mixture Model fit to the distribution within
each cluster.

Products
--------

- :download:`PDF <great_wall_MST.pdf>`

Source
------

.. literalinclude:: entry2.py

- :download:`Python source <entry2.py>`
