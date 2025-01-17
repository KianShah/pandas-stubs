from typing import (
    Any,
    Dict,
    Hashable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

import numpy as np
from pandas.core.computation.pytables import PyTablesExpr
from pandas.core.frame import DataFrame
from pandas.core.generic import NDFrame
from pandas.core.indexes.base import Index
from pandas.core.indexes.multi import MultiIndex
from pandas.core.series import Series

from pandas._typing import (
    ArrayLike,
    FilePathOrBuffer,
)

from pandas.core.dtypes.generic import ABCExtensionArray

# from tables import Col, File, Node
# pytables may not be installed so create them as dummy classes
class Col: ...
class Node: ...

Term = PyTablesExpr

class PossibleDataLossError(Exception): ...
class ClosedFileError(Exception): ...
class IncompatibilityWarning(Warning): ...

incompatibility_doc: str

class AttributeConflictWarning(Warning): ...

attribute_conflict_doc: str

class DuplicateWarning(Warning): ...

duplicate_doc: str
performance_doc: str
dropna_doc: str
format_doc: str

def to_hdf(
    path_or_buf: FilePathOrBuffer,
    key: str,
    value: NDFrame,
    mode: str = ...,
    complevel: Optional[int] = ...,
    complib: Optional[str] = ...,
    append: bool = ...,
    format: Optional[str] = ...,
    index: bool = ...,
    min_itemsize: Optional[Union[int, Dict[str, int]]] = ...,
    nan_rep=...,
    dropna: Optional[bool] = ...,
    data_columns: Optional[List[str]] = ...,
    errors: str = ...,
    encoding: str = ...,
): ...
def read_hdf(
    path_or_buf: FilePathOrBuffer,
    key=...,
    mode: str = ...,
    errors: str = ...,
    where: Optional[List[Any]] = ...,
    start: Optional[int] = ...,
    stop: Optional[int] = ...,
    columns: Optional[List[str]] = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    **kwargs,
): ...

class HDFStore:
    def __init__(
        self,
        path,
        mode: str = ...,
        complevel: Optional[int] = ...,
        complib=...,
        fletcher32: bool = ...,
        **kwargs,
    ) -> None: ...
    def __fspath__(self): ...
    @property
    def root(self): ...
    @property
    def filename(self): ...
    def __getitem__(self, key: str): ...
    def __setitem__(self, key: str, value): ...
    def __delitem__(self, key: str): ...
    def __getattr__(self, name: str): ...
    def __contains__(self, key: str) -> bool: ...
    def __len__(self) -> int: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def keys(self) -> List[str]: ...
    def __iter__(self): ...
    def items(self) -> None: ...
    iteritems = ...
    def open(self, mode: str = ..., **kwargs): ...
    def close(self) -> None: ...
    @property
    def is_open(self) -> bool: ...
    def flush(self, fsync: bool = ...): ...
    def get(self, key: str): ...
    def select(
        self,
        key: str,
        where=...,
        start=...,
        stop=...,
        columns=...,
        iterator=...,
        chunksize=...,
        auto_close: bool = ...,
    ): ...
    def select_as_coordinates(
        self, key: str, where=..., start: Optional[int] = ..., stop: Optional[int] = ...
    ): ...
    def select_column(
        self,
        key: str,
        column: str,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...
    def select_as_multiple(
        self,
        keys,
        where=...,
        selector=...,
        columns=...,
        start=...,
        stop=...,
        iterator=...,
        chunksize=...,
        auto_close: bool = ...,
    ): ...
    def put(
        self,
        key: str,
        value: NDFrame,
        format=...,
        index=...,
        append=...,
        complib=...,
        complevel: Optional[int] = ...,
        min_itemsize: Optional[Union[int, Dict[str, int]]] = ...,
        nan_rep=...,
        data_columns: Optional[List[str]] = ...,
        encoding=...,
        errors: str = ...,
    ): ...
    def remove(self, key: str, where=..., start=..., stop=...): ...
    def append(
        self,
        key: str,
        value: NDFrame,
        format=...,
        axes=...,
        index=...,
        append=...,
        complib=...,
        complevel: Optional[int] = ...,
        columns=...,
        min_itemsize: Optional[Union[int, Dict[str, int]]] = ...,
        nan_rep=...,
        chunksize=...,
        expectedrows=...,
        dropna: Optional[bool] = ...,
        data_columns: Optional[List[str]] = ...,
        encoding=...,
        errors: str = ...,
    ): ...
    def append_to_multiple(
        self, d: Dict, value, selector, data_columns=..., axes=..., dropna=..., **kwargs
    ): ...
    def create_table_index(
        self,
        key: str,
        columns=...,
        optlevel: Optional[int] = ...,
        kind: Optional[str] = ...,
    ): ...
    def groups(self): ...
    def walk(self, where: str = ...) -> None: ...
    def get_node(self, key: str) -> Optional[Node]: ...
    def get_storer(self, key: str) -> Union[GenericFixed, Table]: ...
    def copy(
        self,
        file,
        mode=...,
        propindexes: bool = ...,
        keys=...,
        complib=...,
        complevel: Optional[int] = ...,
        fletcher32: bool = ...,
        overwrite=...,
    ): ...
    def info(self) -> str: ...

class TableIterator:
    chunksize: Optional[int]
    store: HDFStore
    s: Union[GenericFixed, Table]
    func = ...
    where = ...
    nrows = ...
    start = ...
    stop = ...
    coordinates = ...
    auto_close = ...
    def __init__(
        self,
        store: HDFStore,
        s: Union[GenericFixed, Table],
        func,
        where,
        nrows,
        start=...,
        stop=...,
        iterator: bool = ...,
        chunksize: Optional[int] = ...,
        auto_close: bool = ...,
    ) -> None: ...
    def __iter__(self): ...
    def close(self) -> None: ...
    def get_result(self, coordinates: bool = ...): ...

class IndexCol:
    is_an_indexable: bool = ...
    is_data_indexable: bool = ...
    name: str
    cname: str
    values = ...
    kind = ...
    typ = ...
    axis = ...
    pos = ...
    freq = ...
    tz = ...
    index_name = ...
    ordered = ...
    table = ...
    meta = ...
    metadata = ...
    def __init__(
        self,
        name: str,
        values=...,
        kind=...,
        typ=...,
        cname: Optional[str] = ...,
        axis=...,
        pos=...,
        freq=...,
        tz=...,
        index_name=...,
        ordered=...,
        table=...,
        meta=...,
        metadata=...,
    ) -> None: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def kind_attr(self) -> str: ...
    def set_pos(self, pos: int): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def is_indexed(self) -> bool: ...
    def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str): ...
    def take_data(self): ...
    @property
    def attrs(self): ...
    @property
    def description(self): ...
    @property
    def col(self): ...
    @property
    def cvalues(self): ...
    def __iter__(self): ...
    def maybe_set_size(self, min_itemsize=...) -> None: ...
    def validate_names(self) -> None: ...
    def validate_and_set(self, handler: AppendableTable, append: bool): ...
    def validate_col(self, itemsize=...): ...
    def validate_attr(self, append: bool): ...
    def update_info(self, info) -> None: ...
    def set_info(self, info) -> None: ...
    def set_attr(self) -> None: ...
    def validate_metadata(self, handler: AppendableTable): ...
    def write_metadata(self, handler: AppendableTable): ...

class GenericIndexCol(IndexCol):
    @property
    def is_indexed(self) -> bool: ...
    def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str): ...
    def set_attr(self) -> None: ...

class DataCol(IndexCol):
    is_an_indexable: bool = ...
    is_data_indexable: bool = ...
    dtype = ...
    data = ...
    def __init__(
        self,
        name: str,
        values=...,
        kind=...,
        typ=...,
        cname=...,
        pos=...,
        tz=...,
        ordered=...,
        table=...,
        meta=...,
        metadata=...,
        dtype=...,
        data=...,
    ) -> None: ...
    @property
    def dtype_attr(self) -> str: ...
    @property
    def meta_attr(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    kind = ...
    def set_data(self, data: Union[np.ndarray, ABCExtensionArray]): ...
    def take_data(self): ...
    @classmethod
    def get_atom_string(cls, shape, itemsize): ...
    @classmethod
    def get_atom_coltype(cls, kind: str) -> Type[Col]: ...
    @classmethod
    def get_atom_data(cls, shape, kind: str) -> Col: ...
    @classmethod
    def get_atom_datetime64(cls, shape): ...
    @classmethod
    def get_atom_timedelta64(cls, shape): ...
    @property
    def shape(self): ...
    @property
    def cvalues(self): ...
    def validate_attr(self, append) -> None: ...
    def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str): ...
    def set_attr(self) -> None: ...

class DataIndexableCol(DataCol):
    is_data_indexable: bool = ...
    def validate_names(self) -> None: ...
    @classmethod
    def get_atom_string(cls, shape, itemsize): ...
    @classmethod
    def get_atom_data(cls, shape, kind: str) -> Col: ...
    @classmethod
    def get_atom_datetime64(cls, shape): ...
    @classmethod
    def get_atom_timedelta64(cls, shape): ...

class GenericDataIndexableCol(DataIndexableCol): ...

class Fixed:
    pandas_kind: str
    format_type: str = ...
    obj_type: Type[Union[DataFrame, Series]]
    ndim: int
    encoding: str
    parent: HDFStore
    group: Node
    errors: str
    is_table: bool = ...
    def __init__(
        self, parent: HDFStore, group: Node, encoding: str = ..., errors: str = ...
    ) -> None: ...
    @property
    def is_old_version(self) -> bool: ...
    @property
    def version(self) -> Tuple[int, int, int]: ...
    @property
    def pandas_type(self): ...
    def set_object_info(self) -> None: ...
    def copy(self): ...
    @property
    def shape(self): ...
    @property
    def pathname(self): ...
    @property
    def attrs(self): ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    @property
    def storable(self): ...
    @property
    def is_exists(self) -> bool: ...
    @property
    def nrows(self): ...
    def validate(self, other): ...
    def validate_version(self, where=...): ...
    def infer_axes(self): ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...
    def delete(
        self, where=..., start: Optional[int] = ..., stop: Optional[int] = ...
    ): ...

class GenericFixed(Fixed):
    attributes: List[str] = ...
    def validate_read(self, columns, where) -> None: ...
    @property
    def is_exists(self) -> bool: ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    def write(self, obj, **kwargs) -> None: ...
    def read_array(
        self, key: str, start: Optional[int] = ..., stop: Optional[int] = ...
    ): ...
    def read_index(
        self, key: str, start: Optional[int] = ..., stop: Optional[int] = ...
    ) -> Index: ...
    def write_index(self, key: str, index: Index): ...
    def write_multi_index(self, key: str, index: MultiIndex): ...
    def read_multi_index(
        self, key: str, start: Optional[int] = ..., stop: Optional[int] = ...
    ) -> MultiIndex: ...
    def read_index_node(
        self, node: Node, start: Optional[int] = ..., stop: Optional[int] = ...
    ) -> Index: ...
    def write_array_empty(self, key: str, value: ArrayLike): ...
    def write_array(self, key: str, value: ArrayLike, items: Optional[Index] = ...): ...

class SeriesFixed(GenericFixed):
    pandas_kind: str = ...
    name: Optional[Hashable]
    @property
    def shape(self): ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...
    def write(self, obj, **kwargs) -> None: ...

class BlockManagerFixed(GenericFixed):
    nblocks: int
    @property
    def shape(self): ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...
    def write(self, obj, **kwargs) -> None: ...

class FrameFixed(BlockManagerFixed):
    pandas_kind: str = ...

class Table(Fixed):
    pandas_kind: str = ...
    format_type: str = ...
    table_type: str
    levels: int = ...
    is_table: bool = ...
    index_axes: List[IndexCol]
    non_index_axes: List[Tuple[int, Any]]
    values_axes: List[DataCol]
    data_columns: List
    metadata: List
    info: Dict
    nan_rep = ...
    def __init__(
        self,
        parent: HDFStore,
        group: Node,
        encoding=...,
        errors: str = ...,
        index_axes=...,
        non_index_axes=...,
        values_axes=...,
        data_columns=...,
        info=...,
        nan_rep=...,
    ) -> None: ...
    @property
    def table_type_short(self) -> str: ...
    def __getitem__(self, c: str): ...
    def validate(self, other) -> None: ...
    @property
    def is_multi_index(self) -> bool: ...
    def validate_multiindex(self, obj): ...
    @property
    def nrows_expected(self) -> int: ...
    @property
    def is_exists(self) -> bool: ...
    @property
    def storable(self): ...
    @property
    def table(self): ...
    @property
    def dtype(self): ...
    @property
    def description(self): ...
    @property
    def axes(self): ...
    @property
    def ncols(self) -> int: ...
    @property
    def is_transposed(self) -> bool: ...
    @property
    def data_orientation(self): ...
    def queryables(self) -> Dict[str, Any]: ...
    def index_cols(self): ...
    def values_cols(self) -> List[str]: ...
    def write_metadata(self, key: str, values: np.ndarray): ...
    def read_metadata(self, key: str): ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    def validate_version(self, where=...) -> None: ...
    def validate_min_itemsize(self, min_itemsize) -> None: ...
    def indexables(self): ...
    def create_index(self, columns=..., optlevel=..., kind: Optional[str] = ...): ...
    @classmethod
    def get_object(cls, obj, transposed: bool): ...
    def validate_data_columns(self, data_columns, min_itemsize, non_index_axes): ...
    def process_axes(self, obj, selection: Selection, columns=...): ...
    def create_description(
        self,
        complib,
        complevel: Optional[int],
        fletcher32: bool,
        expectedrows: Optional[int],
    ) -> Dict[str, Any]: ...
    def read_coordinates(
        self, where=..., start: Optional[int] = ..., stop: Optional[int] = ...
    ): ...
    def read_column(
        self,
        column: str,
        where=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...

class WORMTable(Table):
    table_type: str = ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...
    def write(self, **kwargs) -> None: ...

class AppendableTable(Table):
    table_type: str = ...
    def write(
        self,
        obj,
        axes=...,
        append: bool = ...,
        complib=...,
        complevel=...,
        fletcher32=...,
        min_itemsize=...,
        chunksize=...,
        expectedrows=...,
        dropna: bool = ...,
        nan_rep=...,
        data_columns=...,
    ) -> None: ...
    def write_data(self, chunksize: Optional[int], dropna: bool = ...): ...
    def write_data_chunk(
        self,
        rows: np.ndarray,
        indexes: List[np.ndarray],
        mask: Optional[np.ndarray],
        values: List[np.ndarray],
    ): ...
    def delete(
        self, where=..., start: Optional[int] = ..., stop: Optional[int] = ...
    ): ...

class AppendableFrameTable(AppendableTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    obj_type: Type[Union[DataFrame, Series]] = ...
    @property
    def is_transposed(self) -> bool: ...
    @classmethod
    def get_object(cls, obj, transposed: bool): ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...

class AppendableSeriesTable(AppendableFrameTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    @property
    def is_transposed(self) -> bool: ...
    @classmethod
    def get_object(cls, obj, transposed: bool): ...
    def write(self, obj, data_columns=..., **kwargs): ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ) -> Series: ...

class AppendableMultiSeriesTable(AppendableSeriesTable):
    pandas_kind: str = ...
    table_type: str = ...
    def write(self, obj, **kwargs): ...

class GenericTable(AppendableFrameTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    @property
    def pandas_type(self) -> str: ...
    @property
    def storable(self): ...
    nan_rep = ...
    def get_attrs(self) -> None: ...
    def indexables(self): ...

class AppendableMultiFrameTable(AppendableFrameTable):
    table_type: str = ...
    ndim: int = ...
    @property
    def table_type_short(self) -> str: ...
    def write(self, obj, data_columns=..., **kwargs): ...
    def read(
        self,
        where=...,
        columns=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ): ...

class Selection:
    table = ...
    where = ...
    start = ...
    stop = ...
    condition = ...
    filter = ...
    terms = ...
    coordinates = ...
    def __init__(
        self,
        table: Table,
        where=...,
        start: Optional[int] = ...,
        stop: Optional[int] = ...,
    ) -> None: ...
    def generate(self, where): ...
    def select(self): ...
    def select_coords(self): ...
