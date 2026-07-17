"""
Generic object registry.

The registry stores objects under a unique Identifier.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Generic
from typing import TypeVar

from .identifier import Identifier
from .exceptions import ValidationError

T = TypeVar("T")


class Registry(Generic[T]):
    """
    Generic registry.

    Objects are stored under a unique Identifier.
    """

    def __init__(self) -> None:

        self._objects: dict[Identifier, T] = {}

    def __len__(self) -> int:

        return len(self._objects)

    def __contains__(self, identifier: Identifier) -> bool:

        return identifier in self._objects

    def __iter__(self) -> Iterator[T]:

        return iter(self._objects.values())

    def identifiers(self) -> Iterator[Identifier]:

        return iter(self._objects.keys())

    def add(
        self,
        identifier: Identifier,
        obj: T,
    ) -> None:

        if identifier in self._objects:
            raise ValidationError(
                f"Duplicate identifier '{identifier}'."
            )

        self._objects[identifier] = obj

    def get(
        self,
        identifier: Identifier,
    ) -> T:

        try:
            return self._objects[identifier]

        except KeyError as exc:
            raise ValidationError(
                f"Unknown identifier '{identifier}'."
            ) from exc

    def remove(
        self,
        identifier: Identifier,
    ) -> None:

        try:
            del self._objects[identifier]

        except KeyError as exc:
            raise ValidationError(
                f"Unknown identifier '{identifier}'."
            ) from exc

    def clear(self) -> None:

        self._objects.clear()

    def values(self):

        return self._objects.values()

    def items(self):

        return self._objects.items()

    def to_dict(self):

        return {
            str(identifier): obj
            for identifier, obj in self._objects.items()
        }
