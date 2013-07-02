
Title : Scikit-Fuzzy: A New Fuzzy Logic Toolkit for SciPy
=========================================================

Authors : 
---------

- Joshua D. Warner, MD/PhD Candidate, Mayo Graduate School

- Hal H. Ottesen, Adjunct Professor, Mayo Graduate School


Track : 
-------

General

Abstract : 
----------

Scikit-fuzzy is a robust set of foundational tools for problems involving fuzzy logic
and fuzzy systems. This area has been a challenge for the scientific Python community,
largely because the common first exposure to this topic is through the MATLAB® 
Fuzzy Logic Toolbox™. This talk officially introduces a general set of original fuzzy 
logic algorithms to the scientific Python community which predate the commercial
toolbox, were released under the 3-clause BSD license, and were translated to Python 
by an author who never used the MathWorks® Fuzzy Logic Toolbox™.

The current capabilities of scikit-fuzzy include:

* fuzzy membership function generation
* fuzzy set operations
* lambda-cuts
* fuzzy mathematics including
    * Fuzzy set operations using Zadeh's extension principle
    * Fuzzy implication given an IF THEN system of fuzzy rules, via two implications
        * Mamdani [min]
        * Larsen [product]
    * The vertex and DSW methods
    * Various defuzzification algorithms
    * Fuzzy c-means clustering
    * Fuzzy Inference Ruled by Else-action (FIRE) denoising of 1d or 2d signals.

The goals of scikit-fuzzy are to provide the community with a robust toolkit of
independently developed and implemented fuzzy logic algorithms, filling a void in the
capabilities of scientific and numerical Python, and to increase the attractiveness of
scientific Python as a valid alternative to closed-source options.

Scikit-fuzzy is structured similarly to scikit-learn and scikit-image, current source
code is available on GitHub, and pull requests are welcome.