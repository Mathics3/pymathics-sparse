# -*- coding: utf-8 -*-
"""
PyMathics SparseArray test module.


A PyMathics module is a Python module which can be loaded into Mathics using the
``LoadModule[]`` method.

In particular, to load this after installing this module as a Python module run inside
Mathics:
   ::

      In[1]:= LoadModule["pymathics.sparsearray"]
      Out[1]= pymathics.sparsearray
   ::

Once loaded, we can use it to define and operate over SparseArray expressions:
   ::
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
   ::
 
"""

from pymathics.hello.version import __version__
from pymathics.hello.__main__ import SparseArray, Dimensions  # noqa

__all__ = ("__version__", "SparseArray", "Dimensions", "pymathics_version_data")

# To be recognized as an external mathics module, the following variable
# is required:
#
pymathics_version_data = {
    "author": "The Mathics Team",
    "version": __version__,
    "requires": [],
}
