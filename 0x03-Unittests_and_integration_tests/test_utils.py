#!/usr/bin/env python3
"""
Essential testing and annotation modules
that will be used in this module
"""
import requests
from parameterized import parameterized
from unittest import TestCase
from unittest import mock
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ({}, ("a"), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
        ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_result
            ) -> Any:
        """
        A test method that tests for exceptions
        """
        with self.assertRaises(KeyError) as er:
            access_nested_map(nested_map, path)
            self.assertEqual(str(er.exception), "Key not found")


class TestGetJson(TestCase):
    """
    A class to test the get_json function from utils module
    Args:
        TestCase: inherited from unittest
    """
    """@parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])"""
    @mock.patch('requests.get')
    def test_get_json(self, mock_get) -> Dict:
        """
        A method that will test the get_json function in utils
        module
        """
        test_cases = [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
                ]
        for test_url, test_payload in test_cases:
            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
            mock_get.reset_mock()


class TestMemoize(TestCase):
    """
    A class to test memoize decorator
    Args:
        TestCase: a test case inherited from unittest
    """
    def test_memoize(self):
        """
        A method to test memoize decorator
        """
        class TestClass:
            """
            A test class to test the methods return value
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with mock.patch.object(test_instance, 'a_method') as mock_a_method:
            mock_a_method.return_value = mock.Mock(return_value=42)
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            mock_a_method.assert_called_once()
            self.assertEqual(result1, result2)
