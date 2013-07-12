import numpy as np
from nose.tools import raises
from numpy.testing import assert_equal
from skimage.util.regular_grid import regular_grid


def test_regular_grid_2d_8():
    ar = np.zeros((20, 40))
    g = regular_grid(ar.shape, 8)
    assert_equal(g, [slice(5.0, None, 10.0), slice(5.0, None, 10.0)])
    ar[g] = 1
    assert_equal(ar.sum(), 8)


def test_regular_grid_2d_32():
    ar = np.zeros((20, 40))
    g = regular_grid(ar.shape, 32)
    assert_equal(g, [slice(2.0, None, 5.0), slice(2.0, None, 5.0)])
    ar[g] = 1
    assert_equal(ar.sum(), 32)


def test_regular_grid_3d_8():
    ar = np.zeros((3, 20, 40))
    g = regular_grid(ar.shape, 8)
    assert_equal(g, [slice(1.0, None, 3.0), slice(5.0, None, 10.0),
                     slice(5.0, None, 10.0)])
    ar[g] = 1
    assert_equal(ar.sum(), 8)


if __name__ == '__main__':
    np.testing.run_module_suite()
