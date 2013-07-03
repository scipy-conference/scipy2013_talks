Entry 10 (Second Place)
=======================

.. image:: entry10.png

Authors
-------

- Kristen Thyng

Description
-----------

This figure is from a paper for the European Wave and Tidal Energy
Conference (EWTEC) that I am working on with a co-author. The paper
describes a study we did together combining a simulation of an
idealized tidal channel with a symmetric headland in the middle and an
array of ten turbines near the headland. This combination of efforts
allows us to start to understand the effects of turbines on
increasingly realistic flows, both near the turbine array and farther
field, kilometers away down the channel.

The plot shows the difference in maximum turbulent kinetic energy
(TKE) between a simulation with no turbines and a simulation with an
array of turbines. Positive (red) values indicate areas in which the
initial case has larger maximum values and negative (grey) values
indicate areas in which the turbine array case has larger values. Line
plots to the left (bottom) of the main plot area show the along-
(across-) channel average of the plot values, with coloring indicating
position greater than (red) or less than (grey) zero.

There is a distinction in relative behavior in the cases in the near-
and far-field. Very near to the turbines and in their wake, the TKE is
stronger in the turbine case, which is expected given that several
terms have been added to the turbulence equations in order to model
the effect of the turbines. Further downstream, the initial, no
turbine case TKE is larger than the turbine case, probably due to the
dissipation due to the turbines in the regular array case. These
trends are reflected in the along- and across-channel averages shown
alongside the plot: the initial case tends to be larger except near
the turbines themselves.

Products
--------

- :download:`PDF <tkemax.pdf>`

Source

.. literalinclude:: run.py

- :download:`Python source (run.py) <run.py>`

.. literalinclude:: plot_gen.py

- :download:`Python source (plotgen.py) <plot_gen.py>`

- :download:`diff.npz <diff.npz>`
