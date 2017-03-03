from node import Node

class Linear(Node):
    """
    """
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
