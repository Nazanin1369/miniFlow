from node import Node

class Add(Node):
    """
    another subclass of Node, actually can perform a calculation (addition).
    """
    def __init__(self, x, y):
        Node.__init__(self, [x, y])

    def forward(self):
        """
        You'll be writing code here in the next quiz!
        """
