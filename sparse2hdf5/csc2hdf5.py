import h5py 
import scipy.sparse 

from . __common__ import sparse_matrix_to_hdf5, sparse_matrix_from_hdf5

__csc_repr__ = ['data', 'indices', 'indptr']

def csc_matrix_to_hdf5(matrix,
                       name,
                       hdf5root,
                       attrs = {}
                       group = None,
                       mode = 'a') 
    '''
    Store a sparse matrix in csc format as a HDF5 dataset.
    '''
    sparse_matrix_to_hdf5(matrix,
                          name,
                          hdf5root,
                          group,
                          mode,
                          matrix_type = 'csc',
                          representation = __csc_repr__)

def csc_matrix_from_hdf5(name,
                         hdf5root,
                         group = None,
                         mode = 'a'):
    '''
    Get a sparse matrix in csr format from a HDF5 dataset.
    '''
    return sparse_matrix_from_hdf5(name,
                                   hdf5root,
                                   group,
                                   mode,
                                   matrix_type = 'csc',
                                   representation = __csc_repr__)
