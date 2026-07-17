"""
Protocol for identifiable objects.
"""

from __future__ import annotations

from typing import Protocol

from .identifier import Identifier


class Identifiable(Protocol):
    """
    Protocol for objects exposing a unique identifier.
    """

    @property
    def identifier(self) -> Identifier:
        """
        Return the unique identifier of the object.
        """
        ...
