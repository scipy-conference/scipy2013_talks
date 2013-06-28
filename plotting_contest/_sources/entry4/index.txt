Entry 4
=======

.. image:: entry4.png

Authors
-------

- Rodrigo Nemmen

A Universal Scaling for the Energetics of Relativistic Jets from Black Hole Systems
-----------------------------------------------------------------------------------

Type of plot: 2d scatter plot with linear regressions, uses Numpy and
Matplotlib.

Scientific result
`````````````````

The plot demonstrates that the relativistic outflows produced by
supermassive black holes in the centers of active galaxies (displayed
as BL Lacs and FSRQs in the plot) and stellar mass black holes in
gamma-ray bursts (GRBs in the plot) follow the same universal scaling
for their energetics. Hence, the result showed in this plot implies
that the efficiency of energy dissipation in jets produced in black
hole systems is similar over 10 orders of magnitude in jet power.

Description of the plot
```````````````````````

Relation between the collimation-corrected gamma-ray luminosity `L =
fb*Liso` and the kinetic power Pjet for AGNs and GRBs. The shaded
regions display the 2sigma confidence band of the fits. The blazar and
GRB best-fit models (dashed and dotted lines, respectively) follow
correlations that are consistent, within the uncertainties, with the
best-fit model obtained from the joint data set (solid line). The
best-fit parameters obtained from the combined data set are `A = 0.98
± 0.02` and `B = 1.6 ± 0.9`, where `logPjet = AlogL + B`. The scatter
about the best-fit is 0.64 dex. The yellow data points correspond to
XRF 020903 and GRB 090423, which we do not take into account in the
statistics.

References
``````````

Nemmen, R., et al. Science, 2012, 338, 1445 (cf. Figure 3).
`<http://www.sciencemag.org/content/338/6113/1445>`_

The Science article above can be retrieved for free at the address
`<http://goo.gl/lnQEm>`_ (click the Science cover image in the web
page) or at `<http://arxiv.org/abs/1212.3343>`_ (arXiv article
repository).

Instructions
````````````

Unpack the attached zip file into some directory and execute the
script plot.py. The data files *.npz must be in the same directory as
the script.

Sincerely,

Rodrigo Nemmen


Products
--------

- :download:`PDF <plot.pdf>`

Source
------

.. literalinclude:: plot.py

- :download:`Python source <plot.py>`

- :download:`source.zip <source.zip>`
