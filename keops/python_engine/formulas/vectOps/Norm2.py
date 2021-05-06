from keops.python_engine.formulas.maths import Sqrt
from keops.python_engine.formulas.basicMathOps import Scalprod

##########################
######    Norm2      #####
##########################

def Norm2(arg):
    return Sqrt(Scalprod(arg, arg))