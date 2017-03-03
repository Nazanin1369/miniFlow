from functools import reduce
from node import Node


class Mul(Node):
    """
    subclass of Node to do multiplication
    """
    def __init__(self, *inputs):
        Node.__init__(self, list(inputs))

    def forward(self):
        self.value = reduce(lambda x, y: x*y, map(lambda node: node.value, self.inbound_nodes))

