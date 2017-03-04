from node import Node
import numpy as np

class LinearMatrix(Node):
    """
        Z = XW + b
    """
    def __init__(self, X, W, b):
        # Notice the ordering of the inputs passed to the
        # Node constructor.
        Node.__init__(self, [X, W, b])

    def forward(self):
        X = self.inbound_nodes[0].value
        W = self.inbound_nodes[1].value
        b = self.inbound_nodes[2].value
        self.value = np.dot(X, W) + b
