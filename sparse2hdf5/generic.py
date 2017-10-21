import h5py
import scipy.sparse

class DatasetWithThisNameAlreadyExists(Exception):
    pass

class DatasetWithThisNameDoesNotExist(Exception):
    pass

class GroupDoesNotExist(Exception):
    pass

def get_group_in(hdf5root, path=None):
    '''
    Get HDF5 group from HDF5 root by path. Returns root
    if the path is None. If the group does not exist, it
    will be created. Meant for creating a group when
    writing a matrix initially.

    Args:

        hdf5root (h5py.Group): HDF5 root group
        path (str): path of group to fetch

    Returns

        h5py.Group
    '''
    if path is None:
        return hdf5root
    if path not in hdf5root:
        group = hdf5root.create_group(path)
    else:
        group = hdf5root[path]
    return group

def get_group_out(hdf5root, path=None):
    '''
    Get HDF5 group from HDF5 root by path. Returns the root
    if path is None. If the group does not exist an error
    is raised. Meant for retrieving the group which contains
    the matrix as a subgroup when reading the matrix.

    Args:

        hdf5root (h5py.Group): HDF5 root group
        path (str): path of group to fetch

    Returns:

        h5py.Group
    '''
    if path is None:
        return hdf5root
    if path not in hdf5root:
        raise GroupDoesNotExist
    roup = hdf5root[path]
    return group

def get_matrix_in(group, name=None):
    '''
    Get the group representing the matrix by its name
    from an HDF5 group. If it does not exist it will
    be created. If it already exists an error is raised.
    Meant for initializing the matrix group.

    Args:

        group (h5yp.Group): HDF5 group
        name (str): name of subgroup containing the matrix
                    Default: 'matrix'

    Returns:

        h5py.Group
    '''
    if name is None:
        name = 'matrix'
    if name in group:
        raise DatasetWithThisNameAlreadyExists
    else:
        return group.create_group(name)

def get_matrix_out(group, name=None):
    '''
    Get the group representing the matrix by name. Raises an error
    if a dataset of that name does not exist. Meant for 
    retrieving the matrix.

    Args:

        group (h5py.Group): HDF5 group
        name (str): name of subgroup containing the matrix
                    Default: 'matrix'

    Returns:

        h5py.Group
    '''
    if name is None:
        name = 'matrix'
    if name in group:
        return group[name]
    else:
        raise DatasetWithThisNameDoesNotExist

def sparse_matrix_to_hdf5(matrix,
                          matrix_type,
                          representation,
                          path,
                          group,
                          name,
                          attrs,
                          mode,
                          file_kwargs={},
                          create_dataset_kwargs={}):
    '''
    Store a sparse matrix as hdf5.

    Args:

        matrix (scipy.sparse.spmatrix): the matrix to write
        matrix_type (str): its type (i.e. 'csc', 'csr', etc.)
        representation (list): array names of matrix representation
        path (str): path to HDF5 file
        attrs (dict): additional attributes to attach to the matrix
        group (str): path to HDF5 group to store the matrix in
        name (str): name of the HDF5 group to represent the matrix
        mode (str): mode of h5py.File
        file_kwargs (dict): additional keyword arguments passed to h5py.File
        create_dataset_kwargs (dict): additional keyword arguments to pass
                                      to h5py.Group.create_dataset calls
    '''
    def insert_data(dataset, matrix, what, **kwargs):
        array = eval('matrix.'+what)
        dataset.create_dataset(what,
                               data=array,
                               shape=array.shape,
                               dtype=array.dtype,
                               **kwargs)

    with h5py.File(path, mode, **file_kwargs) as hdf5root:
        group = get_group_in(hdf5root, group)
        mtrxgrp = get_matrix_in(group, name)
        mtrxgrp.attrs['format'] = matrix_type
        mtrxgrp.attrs['num_rows'] = matrix.shape[0]
        mtrxgrp.attrs['num_cols'] = matrix.shape[1]
        for attr in attrs:
            mtrxgrp.attrs[attr] = attrs[attr]
        for array_name in representation:
            insert_data(mtrxgrp,
                        matrix,
                        array_name,
                        **create_dataset_kwargs)

def mtrxgrp2scipy(mtrxgrp, matrix_type, representation):
    if matrix_type is None:
        matrix_type = mtrxgrp.attrs['format']
    elif matrix_type is not None and mtrxgrp.attrs['format'] != matrix_type:
        print("WARNING: Interpreting non-%s matrix format as %s.", matrix_type, matrix_type)
    shape = ( mtrxgrp.attrs['num_rows'], mtrxgrp.attrs['num_cols'] )
    sparse_matrix_init = tuple( [ mtrxgrp[array_name] for array_name in representation ] )
    spmat = eval('scipy.sparse.'+matrix_type+'_matrix')
    return spmat(sparse_matrix_init, shape)

def sparse_matrix_from_hdf5(matrix_type,
                            representation,
                            path,
                            group,
                            name,
                            mode):
    '''
    Get a sparse matrix from a HDF5 dataset.

    Args:

        matrix_type (str): its type (i.e. 'csc', 'csr', etc.)
        representation (list): array names of matrix representation
        path (str): path to HDF5 file
        group (str): path to HDF5 group the matrix is located in
        name (str): name of the HDF5 group representing the matrix
        mode (str): mode of h5py.File
    '''

    with h5py.File(path, mode) as root:
        group = get_group_out(root, group)
        mtrxgrp = get_matrix_out(group, name)
        return mtrxgrp2scipy(mtrxgrp, matrix_type, representation)
