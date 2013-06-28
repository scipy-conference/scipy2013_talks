Entry 19
========

.. image:: entry19.png

Authors
-------

- Elaine Angelino
- Diana Cai

Description
-----------

We are attaching a visualization we did of the "ingredient phase
space" for flour-based baked goods.  With Prof. Michael Brenner, we
downloaded thousands of recipes from allrecipes.com for cookies,
cakes, brownies, etc. and looked at the top 5 ingredients: flour (F),
sugar (S), liquid (L), eggs (E) and fat (T).  We normalized their
volumes to obtain ratios, making this a 4-dimensional space that we
visualized by projecting onto the faces of a tetrahedron.  Each vertex
of the tetrahedron corresponds to one of 4 ingredients (F, S, L, E).
In our diagram, individual points correspond to recipes.  Each
semantic category (cookies, cakes, etc.) is given a separate color,
and we also draw a convex hull for each category around a majority of
recipes that are closest to the average recipe in that category.

We used Python to do all of the downloading and parsing and to plot
each face of the tetrahedron.  The last step of putting the faces
together was done by hand.

We have had a lot of fun with this project -- we printed out large
tetrahedra on poster paper that we cut out and folded up and shared
through many presentations.

We used this code to draw the convex hulls (not our code):
`<http://code.activestate.com/recipes/66527-finding-the-convex-hull-of-a-set-of-2d-points/>`_

There is a little bit about it here:
`<http://www.eecs.harvard.edu/~elaine/sousvide/stories/bakery.html>`_

And it was in the Boston Globe:
`<http://www.bostonglobe.com/ideas/2011/12/11/food-pyramid-made-cookies/Ev66x0eHjUIcBSEAl1EIYI/story.html>`_

The Boston Globe infoviz team made this graphic based on our Python version:
`<http://cache.boston.com/ideas/graphics/buildatetrahedron.pdf>`_

Elaine and Michael also talked about
`<http://alumni.harvard.edu/events/science-and-history-cookies-and-brownies>`_

Thanks for the opportunity to share this with the SciPy community!

Products
--------

- :download:`PDF <tetrahedron.pdf>`

- Individual elements that make up the tetrahedron:

  - :download:`Some egg, liquid, flour <some_egg_liquid_flour.pdf>`

  - :download:`Some liquid, egg, sugar <some_liquid_egg_sugar.pdf>`

  - :download:`Some sugar, flour, egg <some_sugar_flour_egg.pdf>`

  - :download:`Some sugar, flour, liquid <some_sugar_flour_liquid.pdf>`

Source
------

The code to draw the scatter plots for the faces of the tetrahedra is
in the attached plot2d.py (see the simplex() function)

.. literalinclude:: plot2d.py

- :download:`Python source <plot2d.py>`

- :download:`TSV data <original.tsv>`
