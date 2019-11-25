#from .submoduleb.submoduleb import do_b
#__all__ = ["subpackageb", "submodule_C", "submoduleD"]
#from .submoduleD import do_D
#from .submodule_C import do_C
#from . import *
#import .submodule_b.submodule_b.py
#from .submodule_A import submodule_A as A
#from .submoduleb.submodelb import submoduleb as b
#__path__ = __import__('pkgutil').extend_path(__path__, __name__)
#__version__ = "0.9"
#from mypackage.subpackageb.b import do_b

import mypackage.subpackageb
import mypackage.submoduleD
import mypackage.submodule_C
import mypackage.subpackage_A

#from mypackage.subpackageb.b import do_b as do_b_function
