class Node(object):
    """
    This module represent a node in neaural network

    Attributes:
        inbound_nodes (array)
        outbound_nodes (array)
        value ()
    """
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this Node passes values
        self.outbound_nodes = []
        # A calculated Value
        self.value = None
        # For each inbound Node here, add this Node as an outbound Node to _that_ Node.
        for node in self.inbound_nodes:
            node.outbound_nodes.append(self)


    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_nodes` and
        store the result in self.value.
        """
        raise NotImplementedError

