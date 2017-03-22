class DatasetWithThisNameAlreadyExists(Exception):
    pass

class DatasetWithThisNameDoesNotExist(Exception):
    pass

class GroupDoesNotExist(Exception):
    pass

def __insert_data(MATRIX, matrix, what):
    array = eval('matrix.' + what)
    MATRIX.create_dataset(what, data = array,
                                shape = array.shape,
                                dtype = array.dtype)

def __get_group_in(HDF5ROOT, group):
    if group is None:
        return HDF5ROOT
    if group not in HDF5ROOT:
        GROUP = HDF5ROOT.create_group(group)
    else:
        GROUP = HDF5ROOT[group]
    return GROUP

def __get_group_out(HDF5ROOT, group):
    if group is None:
        return HDF5ROOT
    if group not in HDF5ROOT:
        raise GroupDoesNotExist
    else:
        GROUP = HDF5ROOT[group]
    return GROUP

def __get_matrix_in(GROUP, name):
    if name in GROUP:
        raise DatasetWithThisNameAlreadyExists
    else:
        return GROUP.create_group(name)

def __get_matrix_out(GROUP, name):
    if name in GROUP:
        return GROUP[name]
    else:
        raise DatasetWithThisNameDoesNotExist

def sparse_matrix_to_hdf5(matrix,
                          name,
                          hdf5root,
                          matrix_type,
                          representation,
                          attrs = {}
                          group = None,
                          mode = 'a'):
    '''
    Store a sparse matrix as hdf5.
    '''
    with h5py.File(hdf5root, mode) as HDF5ROOT:
        GROUP = __get_group_in(HDF5ROOT, group)
        MATRIX = __get_matrix_in(GROUP, name)
        MATRIX.attrs['format'] = matrix_type
        MATRIX.attrs['num_rows'] = matrix.shape[0]
        MATRIX.attrs['num_cols'] = matrix.shape[1]
        for attr in attrs:
            MATRIX.attrs[attr] = attrs[attr]
        for array_name in representation:
        __insert_data(MATRIX, matrix, 'indptr')

def sparse_matrix_from_hdf5(name,
                            hdf5root,
                            matrix_type,
                            representation,
                            group = None,
                            mode = 'a'):
    '''
    Get a sparse matrix from a HDF5 dataset.
    '''
    with h5py.File(hdf5root, mode) as HDF5ROOT:
        GROUP = __get_group_out(HDF5ROOT, group)
        MATRIX = __get_matrix_out(GROUP, name)
        if MATRIX.attrs['format'] != matrix_type:
            print("WARNING: Interpreting non-%s matrix format as %s.", matrix_type, matrix_type)
        shape = ( MATRIX.attrs['num_rows'], MATRIX.attrs['num_cols'] )
        sparse_matrix_init = tuple( [ MATRIX[array_name] for array_name in representation ] )
        ctor = 'scipy.sparse.' + matrix_type + '_matrix'
        return eval(ctor)(sparse_matrix_init, shape)
