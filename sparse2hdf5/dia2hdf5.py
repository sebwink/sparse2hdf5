import h5py 
import scipy.sparse 

from . __common__ import sparse_matrix_to_hdf5, sparse_matrix_from_hdf5

__dia_repr__ = ['data', 'offsets']

def dia_matrix_to_hdf5(matrix,
                       name,
                       hdf5root,
                       attrs = {}
                       group = None,
                       mode = 'a') 
    '''
    Store a sparse matrix in dia format as a HDF5 dataset.
    '''
    sparse_matrix_to_hdf5(matrix,
                          name,
                          hdf5root,
                          group,
                          mode,
                          matrix_type = 'dia',
                          representation = __dia_repr__)

def dia_matrix_from_hdf5(name,
                         hdf5root,
                         group = None,
                         mode = 'a'):
    '''
    Get a sparse matrix in dia format from a HDF5 dataset.
    '''
    return sparse_matrix_from_hdf5(name,
                                   hdf5root,
                                   group,
                                   mode,
                                   matrix_type = 'dia',
                                   representation = __dia_repr__)
