Entry 1
=======

.. image:: entry1.png

Authors
-------
- Frédéric Vogt
- Luke Shingles

Please find attached to this email our entry to the 2013 Scipy John
Hunter Excellence in Plotting Contest.

We rely on the Mayavi plotting module to create an interactive 3D map
of the oxygen-rich ejecta in the young supernova remnant N132D. These
'chunks' of pure oxygen correspond to the outer layers of a star that
have been expelled into space as it exploded some 2500 years
ago. Their distribution in 3D space is key to understanding the
explosion mechanism of the parent stars and its asymmetries. This data
was originally used and published in Vogt&Dopita, Ap&SS (2011), 331,
521 (`<http://adsabs.harvard.edu/abs/2010arXiv1009.0964V>`_), and more
recently in Vogt&Shingles, Ap&SS (2013), submitted.

Our plot is both 'interactive' and 'augmented'. Relying on the
advances in PDF technology, we embed the interactive 3D map behind its
projection. When using Adobe Acrobat Reader, the viewer can load and
freely zoom, rotate and fly through the interactive model. In
addition, we rely on the latest advances in the area of augmented
reality to allow smartphone users to access an animation of the 3D map
directly on their device. The animation (and additional contact and
share options) can be accessed by snapping a picture of our plot with
a smartphone and the Layar app (freely available). A copy of the
interactive plot and of the movie is accessible online :
`<http://www.mso.anu.edu.au/~fvogt/dokuwiki/doku.php?id=Online_Material>`_

Understanding the 3D structure of the ejecta in this complex system
has been subject to much debate in the past. Being able to share with
the science community the exact 3D model, and giving them the
opportunity to directly interact and visualise it is key to a better
understanding of the mechanisms shaping young supernova remnants.

All plots are strictly produced with Python (see the attached code,
which was used to produce the projection, the interactive model and
the individual movie frames). To assemble our 3-layers final plot, we
rely on Latex and the movie15 package. We used ffmpeg to assemble the
movie frames into an animation, and used the PDF3D software to
transform the .vrml file produced from Mayavi into a .u3d file
compatible with Latex.

A pickled file containing the original data has not been included in
the submission because of its large size (~650Mb). If required, we
would be happy to make this file available online for the Contest
Organisers to access.

We are very much looking forward to the outcome of this exciting new
contest, and would welcome a confirmation that our entry has been
received.

With our best regards,
Frédéric Vogt and Luke Shingles

Products
--------

- :download:`PDF with interactive 3D visualization <Vogt+Shingles.pdf>`

- :download:`EPS version <Vogt+Shingles.eps>`

Source
------

.. literalinclude:: Vogt+Shingles.py

- :download:`Python source <Vogt+Shingles.py>`

- :download:`U3D file <Vogt+Shingles.u3d>`

- :download:`VRML .wrl file <Vogt+Shingles.wrl>`

- :download:`LaTeX source <Vogt+Shingles.tex>`
