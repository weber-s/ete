import unittest 

from ete_dev import *

class Test_R_bindings(unittest.TestCase):
    """ This is experimental """
    def test_ape(self):
        """ Link to R-ape package """
        return # Don't test anything from now
        try:
            import rpy2.robjects as robjects
        except ImportError:
            print "\nNo rpy2 support. Skipping.\n"
            return

        # R
        t1 = Tree(nw_simple1)
        t2 = Tree(nw_simple2)


        R = robjects.r
        R.library("ape")
        CONS =  R["consensus"]([asRphylo(t1), \
                                    asRphylo(t1), \
                                    asRphylo(t1), \
                                    asRphylo(t1), \
                                    asRphylo(t2)])
        t = asETE(CONS)

