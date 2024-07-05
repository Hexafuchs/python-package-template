#   ---------------------------------------------------------------------------------
#   Copyright (c) Hexafuchs. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""
This is a configuration file for pytest containing customizations and fixtures.

In VSCode, Code Coverage is recorded in config.xml. Delete this file to reset reporting.
"""

from __future__ import annotations

import pytest
from _pytest.nodes import Item


def pytest_collection_modifyitems(items: list[Item]):
    for item in items:
        if "spark" in item.nodeid:
            item.add_marker(pytest.mark.spark)
        if "_int_" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        else:
            item.add_marker(pytest.mark.unit)


@pytest.fixture
def unit_test_mocks(monkeypatch: None):
    """Include Mocks here to execute all commands offline and fast."""
    pass
