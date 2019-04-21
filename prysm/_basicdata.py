"""Basic class holding data, used to recycle code."""
import copy
from prysm import mathops as m


class BasicData:
    """Abstract base class holding some data properties."""
    _data_attr = 'data'

    def __init__(self, unit_x, unit_y, data):
        """Initialize a new BasicData instance.

        Parameters
        ----------
        unit_x : `numpy.ndarray`
            x unit axis
        unit_y : `numpy.ndarray`
            y unit axis
        data : `numpy.ndarray`
            data

        Returns
        -------
        BasicData
            the BasicData instance

        """
        self.unit_x = unit_x
        self.unit_y = unit_y
        setattr(self, self._data_attr, data)

    @property
    def shape(self):
        """Proxy to phase or data shape."""
        try:
            return getattr(self, self._data_attr).shape
        except AttributeError:
            return (0, 0)

    @property
    def size(self):
        """Proxy to phase or data size."""
        try:
            return getattr(self, self._data_attr).size
        except AttributeError:
            return 0

    @property
    def samples_x(self):
        """Number of samples in the x dimension."""
        return self.shape[1]

    @property
    def samples_y(self):
        """Number of samples in the y dimension."""
        return self.shape[0]

    @property
    def sample_spacing(self):
        """center-to-center sample spacing."""
        try:
            return self.unit_x[1] - self.unit_x[0]
        except TypeError:
            return m.nan

    @property
    def center_x(self):
        """Center "pixel" in x."""
        return self.samples_x // 2

    @property
    def center_y(self):
        """Center "pixel" in y."""
        return self.samples_y // 2

    @property
    def slice_x(self):
        """Retrieve a slice through the X axis of the phase.

        Returns
        -------
        self.unit : `numpy.ndarray`
            ordinate axis
        slice of self.phase or self.data : `numpy.ndarray`

        """
        return self.unit_x, getattr(self, self._data_attr)[self.center_y, :]

    @property
    def slice_y(self):
        """Retrieve a slice through the Y axis of the phase.

        Returns
        -------
        self.unit : `numpy.ndarray`
            ordinate axis
        slice of self.phase or self.data : `numpy.ndarray`

        """
        return self.unit_y, getattr(self, self._data_attr)[:, self.center_x]

    def copy(self):
        """Return a (deep) copy of this instance)."""
        return copy.deepcopy(self)
