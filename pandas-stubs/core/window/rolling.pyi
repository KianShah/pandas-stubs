from typing import (
    Callable,
    Dict,
    Optional,
    Set,
    Tuple,
    Union,
)

import numpy as np
from pandas.core.base import (
    PandasObject,
    SelectionMixin,
    ShallowMixin,
)
from pandas.core.indexes.api import Index
from pandas.core.window.common import WindowGroupByMixin

from pandas._typing import (
    Axis,
    FrameOrSeriesUnion as FrameOrSeries,
    Scalar,
)

class _Window(PandasObject, ShallowMixin, SelectionMixin):
    exclusions: Set[str] = ...
    obj = ...
    on = ...
    closed = ...
    window = ...
    min_periods: int = ...
    center = ...
    win_type: str = ...
    win_freq = ...
    axis = ...
    def __init__(
        self,
        obj,
        window=...,
        min_periods: Optional[int] = ...,
        center: Optional[bool] = ...,
        win_type: Optional[str] = ...,
        axis: Axis = ...,
        on: Optional[Union[str, Index]] = ...,
        closed: Optional[str] = ...,
        **kwargs,
    ) -> None: ...
    @property
    def is_datetimelike(self) -> Optional[bool]: ...
    @property
    def is_freq_type(self) -> bool: ...
    def validate(self) -> None: ...
    def __getattr__(self, attr: str): ...
    def __iter__(self): ...
    def aggregate(
        self, func: Optional[Callable] = ..., *args, **kwargs
    ) -> Union[Scalar, FrameOrSeries]: ...
    agg = aggregate

class Window(_Window):
    def validate(self) -> None: ...
    def sum(self, *args, **kwargs): ...
    def mean(self, *args, **kwargs): ...
    def var(self, ddof: int = ..., *args, **kwargs): ...
    def std(self, ddof: int = ..., *args, **kwargs): ...

class _Rolling(_Window): ...

class _Rolling_and_Expanding(_Rolling):
    def count(self) -> FrameOrSeries: ...
    def apply(
        self,
        func,
        raw: bool = ...,
        engine: str = ...,
        engine_kwargs: Optional[Dict] = ...,
        args: Optional[Tuple] = ...,
        kwargs: Optional[Dict] = ...,
    ): ...
    def sum(self, *args, **kwargs) -> FrameOrSeries: ...
    def max(self, *args, **kwargs) -> FrameOrSeries: ...
    def min(self, *args, **kwargs) -> FrameOrSeries: ...
    def mean(self, *args, **kwargs) -> FrameOrSeries: ...
    def median(self, **kwargs) -> FrameOrSeries: ...
    def std(self, ddof: int = ..., *args, **kwargs) -> FrameOrSeries: ...
    def var(self, ddof: int = ..., *args, **kwargs) -> FrameOrSeries: ...
    def skew(self, **kwargs) -> FrameOrSeries: ...
    def kurt(self, **kwargs) -> FrameOrSeries: ...
    def quantile(
        self, quantile: float, interpolation: str = ..., **kwargs
    ) -> FrameOrSeries: ...
    def cov(
        self,
        other: Optional[Union[FrameOrSeries, np.ndarray]] = ...,
        pairwise: Optional[bool] = ...,
        ddof: int = ...,
        **kwargs,
    ) -> FrameOrSeries: ...
    def corr(
        self,
        other: Optional[Union[FrameOrSeries, np.ndarray]] = ...,
        pairwise: Optional[bool] = ...,
        **kwargs,
    ) -> FrameOrSeries: ...

class Rolling(_Rolling_and_Expanding):
    def is_datetimelike(self) -> bool: ...
    win_freq = ...
    window = ...
    win_type: str = ...
    min_periods: int = ...
    def validate(self) -> None: ...
    def count(self) -> FrameOrSeries: ...
    def apply(
        self,
        func,
        raw: bool = ...,
        engine: str = ...,
        engine_kwargs=...,
        args=...,
        kwargs=...,
    ): ...

class RollingGroupby(WindowGroupByMixin, Rolling): ...
