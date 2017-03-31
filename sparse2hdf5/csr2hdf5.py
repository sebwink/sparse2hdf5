import h5py 
import scipy.sparse 

from . generic import sparse_matrix_to_hdf5, sparse_matrix_from_hdf5

__csr_repr__ = ['data', 'indices', 'indptr']

def csr_matrix_to_hdf5(matrix,
                       name,
                       hdf5root,
                       attrs = {},
                       group = None,
                       mode = 'a'): 
    '''
    Store a sparse matrix in csr format as a HDF5 dataset.
    '''
    sparse_matrix_to_hdf5(matrix,
                          name,
                          hdf5root,
                          attrs,
                          group,
                          mode,
                          matrix_type = 'csr',
                          representation = __csr_repr__)

def csr_matrix_from_hdf5(name,  
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
                                   matrix_type = 'csr',
                                   representation = __csr_repr__)
