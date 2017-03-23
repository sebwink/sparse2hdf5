import h5py 
import scipy.sparse 

from . __common__ import sparse_matrix_to_hdf5, sparse_matrix_from_hdf5

__bsr_repr__ = ['data', 'indices', 'indptr']

def bsr_matrix_to_hdf5(matrix,
                       name,
                       hdf5root,
                       attrs = {}
                       group = None,
                       mode = 'a') 
    '''
    Store a sparse matrix in bsr format as a HDF5 dataset.
    '''
    sparse_matrix_to_hdf5(matrix,
                          name,
                          hdf5root,
                          group,
                          mode,
                          matrix_type = 'bsr',
                          representation = __bsr_repr__)

def bsr_matrix_from_hdf5(name,
                         hdf5root,
                         group = None,
                         mode = 'a'):
    '''
    Get a sparse matrix in bsr format from a HDF5 dataset.
    '''
    return sparse_matrix_from_hdf5(name,
                                   hdf5root,
                                   group,
                                   mode,
                                   matrix_type = 'bsr',
                                   representation = __bsr_repr__)
