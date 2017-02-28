"""
    docsting
"""
from node import Node

class Add(Node):
    """
    another subclass of Node, actually can perform a calculation (addition).
    """
    def __init__(self, *inputs):
        Node.__init__(self, list(inputs))

    def forward(self):
        """
        Set the value of this node (`self.value`) to the sum of it's inbound_nodes.
        """
        self.value = sum(n.value for n in self.inbound_nodes)


class Mul(Node):
    """
    subclass of Node to do multiplication
    """
    def __init__(self, *inputs):
        Node.__init__(self, list(inputs))

    def forward(self):
        self.value = reduce(lambda x, y: x*y, map(lambda node: node.value, self.inbound_nodes))


class Linear(Node):
    def __init__(self, inputs, weights, bias):
        Node.__init__(self, [inputs, weights, bias])

        # NOTE: The weights and bias properties here are not
        # numbers, but rather references to other nodes.
        # The weight and bias values are stored within the
        # respective nodes.

    def forward(self):
        """
        Set self.value to the value of the linear function output.
        """
        inputs = self.inbound_nodes[0].value
        weights = self.inbound_nodes[1].value
        self.value = bias = self.inbound_nodes[2].value

        for x, w in zip(inputs, weights):
            self.value += x * w


class LinearMatrix(Node):
    def __init__(self, X, W, b):
        # Notice the ordering of the input nodes passed to the
        # Node constructor.
        Node.__init__(self, [X, W, b])

    def forward(self):
        """
        Set the value of this node to the linear transform output.

        Your code goes here!
        """