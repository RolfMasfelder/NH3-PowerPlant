"""
Generic object registry.

The registry stores objects exposing an Identifier.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Generic
from typing import TypeVar

from .exceptions import NotFoundError
from .exceptions import ValidationError
from .identifiable import Identifiable
from .identifier import Identifier

T = TypeVar("T", bound=Identifiable)


class Registry(Generic[T]):
    """
    Generic registry for identifiable objects.

    Objects are stored under their Identifier.

    Notes
    -----
    The registry guarantees that every Identifier exists only once.
    """

    def __init__(self) -> None:
        """Create an empty registry."""
        self._objects: dict[Identifier, T] = {}

    def __len__(self) -> int:
        """Return the number of registered objects."""
        return len(self._objects)

    def __contains__(self, identifier: Identifier) -> bool:
        """Return True if *identifier* exists in the registry."""
        return identifier in self._objects

    def __iter__(self) -> Iterator[T]:
        """Iterate over all registered objects."""
        return iter(self._objects.values())

    def __getitem__(self, identifier: Identifier) -> T:
        """Return the object belonging to *identifier*."""
        return self.get(identifier)

    def add(self, obj: T) -> None:
        """
        Add an object to the registry.

        Parameters
        ----------
        obj
            Object implementing the Identifiable protocol.

        Raises
        ------
        ValidationError
            If the identifier already exists.
        """
        identifier = obj.identifier

        if identifier in self._objects:
            raise ValidationError(
                f"Duplicate identifier '{identifier}'."
            )

        self._objects[identifier] = obj

    def get(self, identifier: Identifier) -> T:
        """
        Return the object identified by *identifier*.

        Raises
        ------
        NotFoundError
            If the identifier is unknown.
        """
        try:
            return self._objects[identifier]

        except KeyError as exc:
            raise NotFoundError(
                f"Unknown identifier '{identifier}'."
            ) from exc

    def remove(self, identifier: Identifier) -> None:
        """
        Remove an object from the registry.

        Raises
        ------
        NotFoundError
            If the identifier is unknown.
        """
        try:
            del self._objects[identifier]

        except KeyError as exc:
            raise NotFoundError(
                f"Unknown identifier '{identifier}'."
            ) from exc

    def clear(self) -> None:
        """Remove all objects."""
        self._objects.clear()

    def identifiers(self) -> Iterator[Identifier]:
        """Iterate over all identifiers."""
        return iter(self._objects.keys())

    def values(self) -> Iterator[T]:
        """Iterate over all objects."""
        return iter(self._objects.values())

    def items(self) -> Iterator[tuple[Identifier, T]]:
        """Iterate over all (Identifier, object) pairs."""
        return iter(self._objects.items())

    def to_dict(self) -> dict[str, T]:
        """
        Return a dictionary using string representations
        of the identifiers as keys.
        """
        return {
            str(identifier): obj
            for identifier, obj in self._objects.items()
        }
