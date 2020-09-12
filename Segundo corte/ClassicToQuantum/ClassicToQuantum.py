from ComplexVector import *

def sistemaProbabilistico(mat,vec,times):
    for i in range(times):
        vec = accion(mat,vec)
    return vec
