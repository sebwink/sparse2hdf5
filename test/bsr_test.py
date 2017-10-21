import os
import unittest

import numpy as np
from scipy.sparse import bsr_matrix

import sparse2hdf5

class BSRTest(unittest.TestCase):
    def setUp(self):
        self.S = bsr_matrix( np.array([ [0,1,0],[0,0,1],[1,1,0] ]) )
        self.path2hdf5File = 'output/BSRTest.hdf5'
    def test_bsr_to_hdf5(self):
        sparse2hdf5.bsr_matrix_to_hdf5(self.S,
                                       self.path2hdf5File)
        self.assertTrue( os.path.isfile(self.path2hdf5File) )
        T = sparse2hdf5.bsr_matrix_from_hdf5(self.path2hdf5File)
        self.assertTrue( (self.S.toarray() == T.toarray()).all() )
    def tearDown(self):
        os.remove(self.path2hdf5File)

if __name__ == '__main__':
    unittest.main(verbosity=2)

