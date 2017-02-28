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