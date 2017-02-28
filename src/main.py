# pylint: disable=invalid-name
"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""
from operator import Add, Mul, Linear
from utils import topological_sort, forward_pass
from inputNode import Input

x, y, z = Input(), Input(), Input()
l, m, n = Input(), Input(), Input()

f1 = Add(x, y, z)
f2 = Mul(x, y, z)

feed_dict1 = {x: 4, y: 5, z: 10}
feed_dict2 = {l: 4, m: 5, n: 10}

sorted_nodes1 = topological_sort(feed_dict1)
output1 = forward_pass(f1, sorted_nodes1)

sorted_nodes2 = topological_sort(feed_dict2)
output2 = forward_pass(f2, sorted_nodes2)

# NOTE: because topological_sort set the values for the `Input` nodes we could also access
# the value for x with x.value (same goes for y).
print ("{} + {} = {} (according to miniflow - add)".format(feed_dict1[x], feed_dict1[y], output1))
print ("{} + {} = {} (according to miniflow - mul)".format(feed_dict2[x], feed_dict2[y], output2))


inputs, weights, bias = Input(), Input(), Input()

f = Linear(inputs, weights, bias)

feed_dict = {
    inputs: [6, 14, 3],
    weights: [0.5, 0.25, 1.4],
    bias: 2
}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

print(output)
