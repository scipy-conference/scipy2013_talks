Title : Using Python to Study Rotational Velocities of Hot Stars
================================================================

Authors :
----------

- Gustavo Bragança, Observatório Nacional

- Simone Daflon, Observatório Nacional

- Katia Cunha, Observatório Nacional, NOAO, University of Arizona

- Thomas Bensby, Lund Observatory

- M. Sally Oey, University of Michigan

- Gregory Walth, Steward Observatory


Abstract :
----------

Poster is availabe [here](http://dx.doi.org/10.6084/m9.figshare.722949).

Our research is focused in characterizing the stellar properties of hot stars
in the Galactic plane. Recently, we have been working with a sample of nearby
hot stars with the intent to study the sample projected rotational velocity
distribution. With this purpose, we have sub-selected our sample using the
stars birthplace as criteria. Our conclusions were that the rotational
velocity distributions seems to be different between subsamples, but the
reasons for these are still dubious.

The observed spectra were reducted using IRAF, that "is the Image Reduction
and Analysis Facility, a general purpose software system for the reduction and
analysis of astronomical data." It is not written in python, but there is a
package called pyRAF that allows controls on IRAF tasks. With this python
package, we were able to speed up the process of spectra reduction by putting
several IRAF tasks in one script.

Throughout our research, we checked if the stars subsamples from different
birthplaces belonged for the same population. Thus, we had extensively used
the Kolmogorov-Smirnov hypothesis test, and this is coded inside the 'stats'
package of Scipy.

Also, we choose the Matplotlib package as our plotting tool.

Nowadays, we have been using python and Scipy to write a suite that will allow
to obtain stellar parameters by spectral synthesis on a semi-automatic way. We
are still working on the methodology, checking its robustness and also
verifying if the models that generate the synthetic electromagnetic spectra of
star are consistent with observational data. For these tests we are using
python and its availabe libraries.

Original work can be found on [ArXiv](http://arxiv.org/abs/1208.1674)

