import h5py
import scipy.sparse

from . generic import sparse_matrix_to_hdf5

__coo_repr__ = ['data', 'row', 'col']

def coo_matrix_to_hdf5(matrix,
                       name,
                       hdf5root,
                       attrs,
                       group = None,
                       mode = 'a'):
    '''

    '''
    sparse_matrix_to_hdf5(matrix,
                          name,
                          hdf5root,
                          group,
                          mode,
                          matrix_type = 'coo',
                          representation = __coo_repr__)

def coo_matrix_from_hdf5(name,
                         hdf5root,
                         group = None,
                         mode = 'a'):
    raise NotImplementedError
