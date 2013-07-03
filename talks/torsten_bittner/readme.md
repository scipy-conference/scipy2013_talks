
Title : Analyzing IBM Watson experiments with IPython Notebook
=====================

Authors : 
----------


- Torsten Bittner, IBM


Track : 
-------

General

Abstract : 
----------

IBM's Emerging Technologies team was tasked with migrating the IBM Watson system that won the Jeopardy!-like game to a domain-independent codebase. This task started as a software engineering exercise and later became an information engineering exercise as we worked to optimize the system's question-answering ability for new domains. In this new paradigm the team would observe and measure a system behavior, such as its accuracy in generating candidate answers to a particular type of question, and then hypothesize what (software) change to the system would improve the behavior and how it would impact the original measurement. The team would then implement the change, re-run the system against a test dataset, analyze the gigabyte-sized test results to evaluate the difference in system behavior. By conducting many series of these experimental iterations, the team was able to significantly improve IBM Watson's question-answering performance.

Our initial attempts at information engineering used Java and the D3 JavaScript library to extract, analyze and visualize metrics of the system's behavior. Wiki pages were used to document the many experiments and their configurations. However, this arrangement proved overly cumbersome for handling the large numbers of experiments we ran, and our need to share experimental details, visualizations and results with other teams. Furthermore, we also needed to enable a broader skill set of people -- beyond expert Java programmers -- to conduct analyses, create visualizations, and share findings.

This talk describes how we used the IPython notebook environment and the rich set of Python data science libraries (e.g. Pandas, NumPy/SciPy) to perform reproducible science, which resulted in improvements to IBM Watson's accuracy.
