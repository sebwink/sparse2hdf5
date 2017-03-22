import h5py 
import scipy.sparse 

from . __common__ import ( GroupDoesNotExist,
                           DatasetWithThisNameAlreadyExists,
                           DatasetWithThisNameDoesNotExist,
                           __insert_data,
                           __get_group_in,
                           __get_group_out,
                           __get_matrix_in,
                           __get_matrix_out  )

def csr_matrix_to_hdf5(matrix,
                       name,
                       hdf5root,
                       group = None,
                       mode = 'a'):
    '''
    Store a sparse matrix in csr format as a HDF5 dataset.
    '''
    with h5py.File(hdf5root, mode) as HDF5ROOT:
        GROUP = __get_group_in(HDF5ROOT, group)
        MATRIX = __get_matrix_in(GROUP, name)
        MATRIX.attrs['num_rows'] = matrix.shape[0]
        MATRIX.attrs['num_cols'] = matrix.shape[1]
        __insert_data(MATRIX, matrix, 'data')
        __insert_data(MATRIX, matrix, 'indices')
        __insert_data(MATRIX, matrix, 'indptr')


def csr_matrix_from_hdf5(name,
                         hdf5root,
                         group = None,
                         mode = 'a'):
    '''
    Get a sparse matrix in csr format from a HDF5 dataset.
    '''
    with h5py.File(hdf5root, mode) as HDF5ROOT:
        GROUP = __get_group_out(HDF5ROOT, group)
        MATRIX = __get_matrix_out(GROUP, name)
        shape = ( MATRIX.attrs['num_rows'], MATRIX.attrs['num_cols'] )
        csr_init = ( MATRIX['data'], MATRIX['indices'], MATRIX['indptr'] )
        return scipy.sparse.csr_matrix(csr_init, shape)
