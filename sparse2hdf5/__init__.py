'''


'''

import h5py
import scipy.sparse

from sparse2hdf5.csr2hdf5 import csr_matrix_to_hdf5, csr_matrix_from_hdf5
from sparse2hdf5.csc2hdf5 import csc_matrix_to_hdf5, csc_matrix_from_hdf5
from sparse2hdf5.dia2hdf5 import dia_matrix_to_hdf5, dia_matrix_from_hdf5
from sparse2hdf5.bsr2hdf5 import bsr_matrix_to_hdf5, bsr_matrix_from_hdf5
from sparse2hdf5.coo2hdf5 import coo_matrix_to_hdf5, coo_matrix_from_hdf5

__matrix_types__ = {
                     scipy.sparse.csr_matrix : 'csr',
                     scipy.sparse.csc_matrix : 'csc',
                     scipy.sparse.dia_matrix : 'dia',
                     scipy.sparse.bsr_matrix : 'bsr',
                     scipy.sparse.coo_matrix : 'coo'
                   }

def matrix_type(matrix):
    '''

    '''
    return __matrix_types__[type(matrix)]

def sparse2hdf5(matrix,
                path,
                name=None,
                group=None,
                attrs={},
                mode='a'):
    '''

    '''
    eval(matrix_type(matrix)+'_matrix_to_hdf5')(matrix,
                                                path,
                                                group,
                                                name,
                                                attrs,
                                                mode)


def hdf52sparse(path,
                name=None,
                group=None,
                mode='a'):
    '''

    '''
    return eval(matrix_type(matrix)+'_matrix_from_hdf5')(path,
                                                         name,
                                                         group,
                                                         mode)
