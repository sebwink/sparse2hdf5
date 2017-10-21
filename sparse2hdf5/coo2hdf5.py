import h5py
import scipy.sparse

from sparse2hdf5.generic import sparse_matrix_to_hdf5

__coo_repr__ = ['data', 'row', 'col']

def coo_matrix_to_hdf5(matrix,
                       path,
                       group=None,
                       name=None,
                       attrs={},
                       mode='a',
                       file_kwargs={},
                       create_dataset_kwargs={}):
    '''

    '''
    sparse_matrix_to_hdf5(matrix,
                          'coo',
                          __coo_repr__,
                          path,
                          group,
                          name,
                          attrs,
                          mode,
                          file_kwargs,
                          create_dataset_kwargs)

def coo_matrix_from_hdf5(path,
                         name=None,
                         group=None,
                         mode='a'):
    raise NotImplementedError
