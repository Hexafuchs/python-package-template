#   ---------------------------------------------------------------------------------
#   Copyright (c) Hexafuchs. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a Sample Python file."""


from __future__ import annotations

from .types import Id

__all__ = ["get_id", "hello_world", "hello_goodbye", "good_night"]


def get_id() -> Id:
    return "SomeId"


def hello_world(i: int = 0) -> str:
    """Doc String."""
    print("hello world")
    return f"string-{i}"


def good_night() -> str:
    """Doc String."""
    print("good night")
    return "string"


def hello_goodbye():
    hello_world(1)
    good_night()
