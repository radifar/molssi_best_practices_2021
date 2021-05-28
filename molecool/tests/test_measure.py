"""
Tests for the measure module.
"""

from molecool.measure import calculate_angle
import molecool
import numpy as np

def test_calculate_distance():
    """Test that calculate_distance calculates what we expect"""

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():
    """Test that calculate_angle calculates what we expect"""

    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, True)

    assert expected_angle == calculated_angle
