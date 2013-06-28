Entry 13
========

.. image:: entry13.png

Authors
-------

- Tim Cera

Description
-----------

The plot is of the orbits of Jupiter and its moons, but unusual in
that it is from a sun centered frame of reference.  Each color of the orbit
represents 1 week.

There are two Python scripts, the first is called
:download:`01_get_ephemeris_telnet.py <01_get_ephemeris_telnet.py>`
which will get the planet and moon ephemeris data from the Jet
Propulsion Lab Horizons server and save them in text files in the
subdirectory `ephemeris_helio`.  The script
:download:`02_create_plots.py <02_create_plots.py>` can then be run.
`02_create_plots.py` develops hundreds of plots, I am only submitting
for the competition `solar_system_plot_page_021.eps`.

Reproducing plots
-----------------

Run `01_get_ephemeris_telnet.py` to create the required data sets that
will be stored in a subdirectory named `ephemeris_helio`.

Run `02_create_plots.py` to create EPS plots in `figs_eps`, and PNG
plots in `figs_png`.  It creates hundreds of plots.

The plot that I am submitting for the competition is
'figs_eps/solar_system_plot_page_021.eps'.

Kindest regards,
Tim Cera

Products
--------

- :download:`PDF <solar_system_plot_page_021.pdf>`

Source
------

.. literalinclude:: 01_get_ephemeris_telnet.py

- :download:`Python source 01_get_ephemeris_telnet.py <01_get_ephemeris_telnet.py>`

.. literalinclude:: 02_create_plots.py

- :download:`Python source 02_create_plots.py <02_create_plots.py>`

.. literalinclude:: orbit_plot_utils.py

- :download:`Python source orbit_plot_utils.py <orbit_plot_utils.py>`

.. literalinclude:: variables.py

- :download:`Python source variables.py <variables.py>`
