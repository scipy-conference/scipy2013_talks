## Title: Using Python to drive the General NOAA Operational Modeling Environment.

## Authors:

Christopher H. Barker:          Chris.Barker@noaa.gov

Jasmine Sandhu:          Jasmine.Sandhu@noa.gov


NOAA Emergency Response Division
7600 Sand Point Way NE
Seattle WA 98115
(206) 526-6959

The General NOAA Operational Modeling Environment (GNOME) is a general purpose modeling tool originally designed for operational oil spill modeling. It was developed by NOAA's Emergency Response Division primarily to provide oil spill transport forecasts to the Federal On Scene Coordinator. In the years since its original development, the model has been extended to support other drifting objects, and has been used for modeling a wide variety cases, including: Marine Debris, larval transport, chemicals in water, etc. It played a key role in the Deepwater Horizon oil spill in 2010, and is being used to forecast the drift of debris from the Japanese Tsunami in 2011. In addition, the model is distributed freely to the general public, and is widely used in education and oil spill response planning.

The first version of the program has proven to be powerful, flexible, and easy to use. However, the program is written in C++, with the computational components and a desktop graphical interface code tightly integrated. As we move forward with development, we require a system that allows a new web-based user interface, easier extension of the model, easier scripting for automation, use of the core algorithms in other models, and easier testing. To achieve these goals, we are re-writing the model as a system of components, tied together with Python. Each component can be written in Python, or any language Python can call (primarily C++), and tested either individually or as part of the system with Python. We have written the new model driver in Python, and are wrapping the existing C++ components using Cython. In this paper, the model architecture is presented, with a discussion of the strengths and pitfalls of the approach.

