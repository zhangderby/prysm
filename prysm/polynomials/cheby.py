"""Chebyshev polynomials."""

from .jacobi import jacobi, jacobi_sequence

from prysm.coordinates import optimize_xy_separable


def cheby1(n, x):
    """Chebyshev polynomial of the first kind of order n.

    Parameters
    ----------
    n : `int`
        order to evaluate
    x : `numpy.ndarray`
        point(s) at which to evaluate, orthogonal over [-1,1]

    """
    c = 1 / jacobi(n, -.5, -.5, 1)  # single div, many mul
    return jacobi(n, -.5, -.5, x) * c


def cheby1_sequence(ns, x):
    """Chebyshev polynomials of the first kind of orders ns.

    Faster than chevy1 in a loop.

    Parameters
    ----------
    ns : `int`
        orders to evaluate
    x : `numpy.ndarray`
        point(s) at which to evaluate, orthogonal over [-1,1]

    """
    ns = list(ns)
    cs = [1/jacobi(n, -.5, -.5, 1) for n in ns]
    seq = jacobi_sequence(ns, -.5, -.5, x)
    cntr = 0
    for elem in seq:
        yield elem * cs[cntr]
        cntr += 1


def cheby2(n, x):
    """Chebyshev polynomial of the second kind of order n.

    Parameters
    ----------
    n : `int`
        order to evaluate
    x : `numpy.ndarray`
        point(s) at which to evaluate, orthogonal over [-1,1]

    """
    c = (n+1) / jacobi(n, .5, .5, 1)  # single div, many mul
    return jacobi(n, .5, .5, x) * c


def cheby2_sequence(ns, x):
    """Chebyshev polynomials of the second kind of orders ns.

    Faster than chevy1 in a loop.

    Parameters
    ----------
    ns : `int`
        orders to evaluate
    x : `numpy.ndarray`
        point(s) at which to evaluate, orthogonal over [-1,1]

    """
    ns = list(ns)
    cs = [(n+1)/jacobi(n, .5, .5, 1) for n in ns]
    seq = jacobi_sequence(ns, .5, .5, x)
    cntr = 0
    for elem in seq:
        yield elem * cs[cntr]
        cntr += 1


def cheby1_2d_sequence(ns, ms, x, y):
    """Chebyshev polynomials of the first kind in both X and Y (as for a rectangular aperture).

    Parameters
    ----------
    ns : iterable of `int`
        orders n for the x axis, if None not computed and return only contains y
    ms : iterable of `int`
        orders m for the y axis, if None not computed and return only contains x
    x : `numpy.ndarray`
        x coordinates, 1D or 2D
    y : `numpy.ndarray`
        y coordinates, 1D or 2D

    Returns
    -------
    `list`, `list` [x, y] modes, with each of 'x' and 'y' in the return being
        a list of its own containing 1D modes

    """
    x, y = optimize_xy_separable(x, y)
    if ns is not None and ms is not None:
        xs = list(jacobi_sequence(ns, -.5, -.5, x))
        ys = list(jacobi_sequence(ms, -.5, -.5, y))
        return xs, ys
    if ns is not None:
        return list(jacobi_sequence(ns, -.5, -.5, x))
    if ms is not None:
        return list(jacobi_sequence(ms, -.5, -.5, y))


def cheby2_2d_sequence(ns, ms, x, y):
    """Chebyshev polynomials of the second kind in both X and Y (as for a rectangular aperture).

    Parameters
    ----------
    ns : iterable of `int`
        orders n for the x axis, if None not computed and return only contains y
    ms : iterable of `int`
        orders m for the y axis, if None not computed and return only contains x
    x : `numpy.ndarray`
        x coordinates, 1D or 2D
    y : `numpy.ndarray`
        y coordinates, 1D or 2D

    Returns
    -------
    `list`, `list` [x, y] modes, with each of 'x' and 'y' in the return being
        a list of its own containing 1D modes

    """
    x, y = optimize_xy_separable(x, y)
    if ns is not None and ms is not None:
        xs = list(jacobi_sequence(ns, .5, .5, x))
        ys = list(jacobi_sequence(ms, .5, .5, y))
        return xs, ys
    if ns is not None:
        return list(jacobi_sequence(ns, .5, .5, x))
    if ms is not None:
        return list(jacobi_sequence(ms, .5, .5, y))
