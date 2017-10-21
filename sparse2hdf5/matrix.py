import h5py

from sparse2hdf5.generic import (get_group_out,
                                 get_matrix_out,
                                 mtrxgrp2scipy)

_repr_ = {
           'csr' : ['data', 'indices', 'indptr'],
           'csc' : ['data', 'indices', 'indptr']
         }

class SparseMatrix(h5py.Group):
    def __init__(self, path, name=None, group=None, mode='a'):
        root = h5py.File(path, mode)
        group = get_group_out(root, group)
        super().__init__(get_matrix_out(group, name).id)

    @property
    def format(self):
        return self.attrs['format']

    @property
    def nrows(self):
        return self.attrs['num_rows']

    @property
    def ncols(self):
        return self.attrs['num_cols']

    @property
    def scipy(self):
        return mtrxgrp2scipy(self, self.format, _repr_[self.format])


class CsxMatrix(SparseMatrix):

    @property
    def data(self):
        return self['data']

    @property
    def indices(self):
        return self['indices']

    @property
    def indptr(self):
        return self['indptr']


class CscMatrix(CsxMatrix):
    pass


class CsrMatrix(CsxMatrix):
    pass
