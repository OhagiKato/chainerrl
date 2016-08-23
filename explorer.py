from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future import standard_library
from future.utils import with_metaclass
standard_library.install_aliases()

from abc import ABCMeta
from abc import abstractmethod


class Explorer(with_metaclass(ABCMeta, object)):
    """Abstract explorer."""

    @abstractmethod
    def select_action(self, t, greedy_action_func):
        """
        Args:
          t: current time step
          greedy_action_func: function with no argument that returns an action
        """
        raise NotImplementedError()
