import numpy as np
from node import Node

class Sigmoid(Node):
    """
    constructor
    """
    def __init__(self, node):
        Node.__init__(self, [node])

    def _sigmoid(self, x):
        """
        calculates the Sigmoid function
        """
        return 1. / (1. + np.exp(-x))

    def forward(self):
        """
        This method is separate from `forward` because it
        will be used with `backward` as well.

        `x`: A numpy array-like object.
        """
        self.value = self._sigmoid(self.inbound_nodes[0].value)
