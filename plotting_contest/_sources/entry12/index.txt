Entry 12
========

.. image:: entry12.png

Authors
-------

- Arulalan.T

About the data
--------------

1) Madden-Julian Oscillation Phase 2 Dimensional Diagram

     The nc file :download:`mjo_npcs.nc <mjo_npcs.nc>` contains MJO
     Normalized PC1 & PC2 for the years from 1979-1-1 to 2005-12-31. I
     Just plotted for the first year alone.  User can test/draw the
     phase diagrams with different years dataset.  This mjo pc1, pc2
     is produced by myself using my python/uvcdat code.

     Plot Properties Reference:
     `<http://climate.snu.ac.kr/mjo_diagnostics/index.htm>`_


2) Monsoon Intraseasonal Oscillation Phase 2 Dimensional Diagram

    The nc file :download:`miso_phases.nc <miso_phases.nc>` is a fake
    data produced by myself to plot the Monsoon Intraseasonal
    Oscillation Phase.

    Plot Properties Reference: "An Indian monsoon intraseasonal
    oscillations (MISO) index for real time monitoring and forecast
    verification", E. Suhas • J. M. Neena • B. N. Goswami, Clim Dyn,
    DOI 10.1007/s00382-012-1462-5

About the code
--------------

There is no module/method/function in python/cdat to plot these kind
of (8) phase diagrams (As for as I know). So I just written this
python function phase2d to plot it.

`phase2d` function needs it dependencies modules which are all written
by myself namely `timeutils` and `trig`.

In `timeutils` I have written more than 20 methods (about 3000 lines)
to make time utilities. But here I have included only 2 methods which
is needed to the phase2d function. Soon we will release the full
timeutils module to the public!

Code, Data & Plots License: GPL V3

Reproducing plots
-----------------

To plot and save it as ps files, you may need to run the
:download:`plot_phase_diagrams.py <plot_phase_diagrams.py>`.

Dependencies
````````````

* To run these python scripts you must need CDAT5.2 [#f1]_ / UVCDAT
  1.2.0 [#f2]_

* grace software must be installed in your operating system. I didnt
  use VCS, instead of that I used xmgrace package to do line plot.  If
  you are using ubuntu system, then::

    $ apt-get install grace

* Developed & Tested In Ubuntu 12.04 LTS OS and UVCDAT 1.2.0

.. [#f1] http://www2-pcmdi.llnl.gov/cdat
.. [#f2] http://uv-cdat.llnl.gov/

Products
--------

- :download:`miso_phase2d_monsoon.pdf <miso_phase2d_monsoon.pdf>`

- :download:`mjo_phase2d_summer.pdf <mjo_phase2d_summer.pdf>`

- :download:`mjo_phase2d_summer_red.pdf <mjo_phase2d_summer_red.pdf>`

- :download:`mjo_phase2d_winter.pdf <mjo_phase2d_winter.pdf>`

- :download:`mjo_phase2d_winter_red.pdf <mjo_phase2d_winter_red.pdf>`

- :download:`phase2d_red.pdf <phase2d_red.pdf>`

Source
------

.. literalinclude:: phase2d.py

- :download:`Python source phase2d.py <phase2d.py>`

.. literalinclude:: plot_phase_diagrams.py

- :download:`Python source plot_phase_diagrams.py <plot_phase_diagrams.py>`

.. literalinclude:: trig.py

- :download:`Python source trig.py <trig.py>`

.. literalinclude:: timeutils.py

- :download:`Python source timeutils.py <timeutils.py>`

- :download:`Data 1 miso_phases.nc <miso_phases.nc>`

- :download:`Data 2 mjo_npcs.nc <mjo_npcs.nc>`
