import os
import unittest

import numpy as np
from scipy.sparse import csr_matrix

import scipy_sparse_hdf5

class CSRTest(unittest.TestCase):
    def setUp(self):
        self.S = csr_matrix( np.array([ [0,1,0],[0,0,1],[1,1,0] ]) )
        self.path2hdf5File = 'data/CSRTest.hdf5'
    def test_csr_to_hdf5(self):
        scipy_sparse_hdf5.csr_matrix_to_hdf5(self.S, 
                                             'CSRTEST',
                                             self.path2hdf5File)
        self.assertTrue( os.path.isfile(self.path2hdf5File) )
    
        T = scipy_sparse_hdf5.csr_matrix_from_hdf5('CSRTEST', self.path2hdf5File )
        self.assertTrue( self.S.toarray() == T.toarray() )
    def tearDown(self):
        os.remove(self.path2hdf5File)

if __name__ == '__main__':
    unittest.main(verbosity=2)

