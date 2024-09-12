import pytest
import rand
from hw2_debugging import merge_sort


def test_sorted_array():
    """Test that a sorted array remains sorted"""
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorted_arr = merge_sort(input_arr)
    assert sorted_arr == input_arr, f"Expected {input_arr}, got {sorted_arr}"


def test_reverse_sorted_array():
    """Test that a reverse-sorted array gets properly sorted"""
    input_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_arr = sorted(input_arr)
    sorted_arr = merge_sort(input_arr)
    assert sorted_arr == expected_arr, f"Expected {expected_arr}, got {sorted_arr}"


def test_array_with_duplicates():
    """Test that an array with duplicates gets properly sorted"""
    input_arr = [4, 1, 3, 2, 4, 3, 2, 1, 5]
    expected_arr = sorted(input_arr)
    sorted_arr = merge_sort(input_arr)
    assert sorted_arr == expected_arr, f"Expected {expected_arr}, got {sorted_arr}"


def test_single_element_array():
    """Test that a single-element array returns the same"""
    input_arr = [42]
    sorted_arr = merge_sort(input_arr)
    assert sorted_arr == input_arr, f"Expected {input_arr}, got {sorted_arr}"


def test_empty_array():
    """Test that an empty array returns an empty array"""
    input_arr = []
    sorted_arr = merge_sort(input_arr)
    assert sorted_arr == input_arr, f"Expected {input_arr}, got {sorted_arr}"


def test_all_elements_same():
    """Test that an array where all elements are the same returns the same"""
    input_arr = [7, 7, 7, 7, 7]
    sorted_arr = merge_sort(input_arr)
    assert sorted_arr == input_arr, f"Expected {input_arr}, got {sorted_arr}"


def test_large_random_array():
    """Test a large randomly generated array"""
    input_arr = rand.random_array([None] * 1000)  # Random array of 1000 elements
    sorted_arr = merge_sort(input_arr)
    expected_arr = sorted(input_arr)
    assert sorted_arr == expected_arr, f"Expected {expected_arr}, got {sorted_arr}"


def test_random_array_small():
    """Test a small randomly generated array"""
    input_arr = rand.random_array([None] * 10)  # Random array of 10 elements
    sorted_arr = merge_sort(input_arr)
    expected_arr = sorted(input_arr)
    assert sorted_arr == expected_arr, f"Expected {expected_arr}, got {sorted_arr}"


def test_random_array_with_negatives():
    """Test an array containing both negative and positive numbers"""
    input_arr = [-5, 3, 0, -2, 8, -1]
    sorted_arr = merge_sort(input_arr)
    expected_arr = sorted(input_arr)
    assert sorted_arr == expected_arr, f"Expected {expected_arr}, got {sorted_arr}"


def test_random_large_array_duplicates():
    """Test a large array with duplicate values"""
    input_arr = rand.random_array([None] * 1000) + rand.random_array([None] * 1000)
    sorted_arr = merge_sort(input_arr)
    expected_arr = sorted(input_arr)
    assert sorted_arr == expected_arr, f"Expected {expected_arr}, got {sorted_arr}"