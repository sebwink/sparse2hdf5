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
