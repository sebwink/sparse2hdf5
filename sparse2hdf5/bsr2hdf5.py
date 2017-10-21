import h5py
import scipy.sparse

from sparse2hdf5.generic import sparse_matrix_to_hdf5, sparse_matrix_from_hdf5

__bsr_repr__ = ['data', 'indices', 'indptr']

def bsr_matrix_to_hdf5(matrix,
                       path,
                       name=None,
                       group=None,
                       attrs={},
                       mode='a',
                       file_kwargs={},
                       create_dataset_kwargs={}):
    '''
    Store a sparse matrix in bsr format as a HDF5 dataset.
    '''
    sparse_matrix_to_hdf5(matrix,
                          'bsr',
                          __bsr_repr__,
                          path,
                          group,
                          name,
                          attrs,
                          mode,
                          file_kwargs,
                          create_dataset_kwargs)

def bsr_matrix_from_hdf5(path,
                         name=None,
                         group=None,
                         mode='a'):
    '''
    Get a sparse matrix in bsr format from a HDF5 dataset.
    '''
    return sparse_matrix_from_hdf5('bsr',
                                   __bsr_repr__,
                                   path,
                                   group,
                                   name,
                                   mode)
