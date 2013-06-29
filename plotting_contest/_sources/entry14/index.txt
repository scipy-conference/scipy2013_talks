Entry 14
========

.. image:: entry14.png

Authors
-------

- Ludwig Schwardt

Description
-----------

My submission illustrates Bayesian inference in action. Suppose you
have a known non-linear function `y = f(x)` relating two random
variables `x` and `y`. The variable `y` has been measured but you really
want to know the variable `x`.

For every value of `x` you can write down the distribution of `y` -
this is the likelihood function `p(y|x)`. To simplify things we are
assuming a Gaussian likelihood with a mean and variance that depends
on `x`. This is illustrated in the left panel of the plot with a blue
line highlighting the conditional mean `E[y|x]`.

We now build up the joint distribution `p(x, y)` as the product of
`p(y|x)` and the prior distribution `p(x)` on the unknown variable
`x`. We take as `p(x) = 1` to indicate that we are quite ignorant
about `x`'s value before we observe `y`. This is how it should be if
`y` is a high-quality measurement of `x`. The joint pdf is shown in
the middle panel as a contour plot with logarithmically spaced contour
levels, together with the two conditional means that come into play
(more on that soon!). The likelihood function is obtained as vertical
slices through the joint pdf, as the left panel shows.

Now you want to go in the opposite direction: for a fixed value of `y`
you want to determine the distribution of `x`, called the posterior
`p(x|y)`. This is related to the joint pdf by Bayes' theorem, one
version of which states that `p(x|y) = p(x, y) / p(y)`. The data
distribution `p(y)` is merely a scaling factor in this example that
does not affect the mean, variance or shape of the posterior pdf and
can therefore be mostly ignored. The posterior pdf is obtained by
literally slicing the joint pdf (which happens to be equal to the
likelihood) in the opposite (horizontal) direction, as illustrated in
the final right panel of the plot. The posterior mean `E[x|y]` is
indicated by a red line in the middle and right panels. The resulting
distributions are *not* Gaussian and the posterior mean `E[x|y]` is
not the same as the likelihood mean `E[y|x]` (although both cases are
close matches!).

An important reason to use Bayesian inference is that it produces not
only an good estimate of `x` via the posterior mean `E[x|y]` but also
an estimate of the uncertainty of this estimate via the posterior
variance `var[x|y]`. This variance depends both on the likelihood
variance and the slope of the non-linear function in the region of the
measured `y` value. As can be seen in the right panel, the posterior
distribution quickly becomes very broad for large values of `y`
because both the likelihood variance increases and the non-linear
function slope decreases with increasing `x`.

[As an aside, the posterior mean and variance were estimated from the
peak region of the posterior pdf via Laplace approximation - but
that's another story...]

This specific data set arose in my studies of the effects of
quantisation on the measurement of power in a digital
radiometer. Given the quantised output of the radiometer it is
possible to get an improved estimate of the true input power as well
as its uncertainty. An earlier version of these plots appeared in my
talk entitled "Bayesian Quantisation Correction" at the CALIM workshop
(`<http://calim2012.ska.ac.za/>`_) in December 2012 (linked here
(`<http://calim2012.ska.ac.za/calim2012_schwardt.pdf?attredirects=0>`_)).

Best regards,

Ludwig Schwardt

Products
--------

- :download:`PDF <bayes_in_action.pdf>`

Source
------

.. literalinclude:: bayes_in_action.py

- :download:`Python source <bayes_in_action.py>`
