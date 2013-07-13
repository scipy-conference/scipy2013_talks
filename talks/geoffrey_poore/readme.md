
Title : Reproducible Documents with PythonTeX
=============================================


Author : 
--------

- Geoffrey Poore, Union University


Track :
-------

Reproducible Science


Abstract : 
----------

Writing a scientific document can be slow and error-prone. When a figure 
or calculation needs to be modified, the code that created it must be 
located, edited, and re-executed. When data changes or analysis is 
tweaked, everything that depends on it must be updated. PythonTeX is a 
LaTeX package that addresses these issues by allowing Python code to be 
included within LaTeX documents. Python code may be entered adjacent to 
the figure or calculation it produces. Built-in utilities may be used to 
track dependencies. 

PythonTeX maximizes performance and efficiency. All code output is 
cached, so that documents can be compiled without executing code. Code 
is only re-executed when user-specified criteria are met, such as exit 
status or modified dependencies. In many cases, dependencies can be 
detected and tracked automatically. Slow code may be isolated in 
user-defined sessions, which automatically run in parallel. Errors and 
warnings are synchronized with the document so that they have meaningful 
line numbers. 

Since PythonTeX documents mix LaTeX and Python code, they are less 
portable than plain LaTeX documents. PythonTeX includes a conversion 
utility that creates a new copy of a document in which all Python code 
is replaced by its output. The result is suitable for journal submission 
or conversion to other formats such as HTML. 

While PythonTeX is primarily intended for Python, its design is largely 
language-independent. Users may easily add support for additional 
languages. 


Links :
-------

- https://github.com/gpoore/pythontex
