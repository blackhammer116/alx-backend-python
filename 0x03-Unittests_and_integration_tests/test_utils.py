#!/usr/bin/env python3
"""
Essential testing and annotation modules
that will be used in this module
"""
from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(TestCase):
    """
    A class that tests the function access_nested_map
    from utils module
    Args:
        TestCase: a base class inherited from unittest
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result) -> Any:
        """
        A method that tests access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
