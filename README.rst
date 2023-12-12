SparseArray PyMathics module

This is a Python module for Mathics that provides some basic support for `SparseArray` expressions.

To install in development mode (run code from the source tree):

::

   $ make develop


After installing inside Mathics you can load this using the
``LoadModule[]`` function.

Then the function ```Hello[]`` is available::

      $ mathicsscript
      In[1]:= LoadModule["pymathics.sparsearray"]
      Out[1]= pymathics.sparsearray

      In[2]:= A = SparseArray[{{1,2}->1},{2,2}]
      Out[2]:= SparseArray[<1>, {2,2}]
      In[3]:= A // Normal
      Out[3]:= {{0, 1}, {0, 0}}
      In[3]:= A.Transpose[A]
      Out[3]:= SparseArray[<1>, {2,2}]
      In[4]:= A.Transpose[A]
      Out[4]:= SparseArray[<1>, {2,2}]
      In[5]:= %//Normal
      Out[5]:= {{1, 0}, {0, 0}}


You can test with ``py.test``::

     $ py.test test

or simply::

     $ make check
