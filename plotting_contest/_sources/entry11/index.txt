Entry 11
========

.. image:: entry11.png

Authors
-------

- Jack Parmer
- Alex Johnson

Description
-----------

A Cholesky decomposition is in some sense the square root of a
matrix. In this case it is applied to a covariance matrix as part of a
model to generate many random time series with the same statistical
properties as a measured set. The covariance of the original time
series (modeled here as a Gaussian with width 15% of the total
measurement time) is decomposed (and plotted for inspection), then it
is multiplied by white noise vectors to generate arbitrarily many
analogous time series. This particular decomposition was used in the
Monte Carlo simulation of proposed enhanced oil recovery projects for
economic risk/reward analysis. Every tenth trace is wider than the
others to highlight the evolution of the decomposition.

Products
--------

- :download:`PDF <plotly_cholesky.pdf>`

Source
------

.. literalinclude:: plot.py

- :download:`Python source <plot.py>`
