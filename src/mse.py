from node import Node
import numpy as np

class MSE(Node):
    """
    MSE operator
    """
    def __init__(self, y, a):
        Node.__init__(self, [y, a])

    def forward(self):
        """
        Calculates the mean squared error.
        """
        y = self.inbound_nodes[0].value.reshape(-1, 1)
        a = self.inbound_nodes[1].value.reshape(-1, 1)
        m = self.inbound_nodes[1].value.shape[0]

        diff = y - a
        self.value = np.mean(diff**2)
