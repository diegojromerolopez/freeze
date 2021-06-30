import typing
from typing import Any, Callable, Union, Optional, TYPE_CHECKING, TypeVar

from frozendict import frozendict


if TYPE_CHECKING:  # pragma: no cover
    from gelidum.frozen import FrozenBase  # noqa

try:
    _SpecialForm = getattr(typing, "_SpecialForm")

    @_SpecialForm
    def Final(self, parameters):  # noqa
        return typing.Final[parameters]

except AttributeError:  # pragma: no cover
    Final = typing.Final

_FrozenBase = "FrozenBase"

T = TypeVar('T')

FrozenType = Optional[
    Union[
        bool, int, float, bytes, complex, str,
        bytes, frozendict, tuple, frozenset,
        _FrozenBase, T
    ]
]

OnUpdateFuncType = Callable[[_FrozenBase, str, ...], None]


OnFreezeFuncType = Callable[[Any], Any]
