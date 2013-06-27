Writing Reproducible Papers with Dexy
-------------------------------------
<br />
<http://dexy.it>
<a href="http://twitter.com/dexyit">@dexyit</a>
<br />
Ana Nelson
<a href="http://twitter.com/ananelson">@ananelson</a>
ana@ananelson.com
<http://github.com/ananelson/talks>


Reproducibility
---------------

- I want to redo the exact steps I did this morning on this machine, so I can update my article [with different data or code].
- I want to understand how someone else got to the results in their published paper.
- I want to make use of someone else's code and data so I can extend their work.


Ingredients
-----------

- Operating System/Software
- Data
- Source Code
- Workflow


Reproducibility
---------------

* *Capture* - capture of the steps carried out in an experiment
* *Representation* - creation of an executable specification of the experiment (e.g. workflow)
* *Portability* - ability for an experiment to be re-executed in an environment different from the one originally used
* *Document Linkage* - linkage between experiments and documents, creation of executable documents
* *Verification and Exploration* - ability to reproduce the original results and to vary original parameters/data
* *Archival* - archival of experiment and data (e.g. repository)
* *Longevity* - ability to maintain an experiment's consistency and reproducibility a long-term basis


Capturing & Tangling
--------------------

- Use virtual machine images (for example) to automatically capture full environments including software and data?
- Have self-contained documents with data, analysis and code?


Dexy's Approach
---------------

Dexy runs other tools
- in the order you specify,
- acting on the input data you specify,
- and helps you get all this content into static (but refreshable) documents.


Example
-------

[&rarr; A tiny example to make this more intuitive.](/example)


Dexy's Approach
---------------

Dexy runs other tools
- in the order you specify,
- acting on the input data you specify,
- and helps you get all this content into static (but refreshable) documents.


What Tools?
-----------

- Any automatable tools (interpreters/compilers, syntax highlighters, code analyzers, graphing/statistics tools)...
- ... which have a command line interface or other API.
- <http://dexy.it/filters>


What Input Data?
----------------

- Scripts, data files, document templates.
- Dexy works on file system directories (hopefully under version control).


What Documents?
---------------

- There is no native dexy document format. You can write documents using any text-based (or otherwise parseable/automatable) format.
- You can use a templating system (such as jinja) to insert references to locations in other files into your documents.
- Dexy will run any tool you want to convert your text plus the dynamically inserted content into other formats (e.g. run pdflatex on .tex, or run docutils on .rst, or run pandoc on .md) 


<img src="logo.png" width="400px;" />

* document-oriented 'make'
* project automation
* code is code, prose is prose, data is data
* many-to-many relationships of prose to code/data
* document live code
* Open Source (MIT)
* Written in Python


Software Documentation
----------------------

You can also use Dexy to document your:

* command line tool
* library
* web app


Get Started
-----------

http://www.dexy.it/guide/getting-started.html
info@dexy.it
