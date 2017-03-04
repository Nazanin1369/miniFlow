# pylint: disable=invalid-name
"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""
from add import Add
from mul import Mul
from linear import Linear
from linearMatrix import LinearMatrix
from sigmoid import Sigmoid
from mse import MSE
from utils import topological_sort, forward_pass, forward_pass_graph
from inputNode import Input
import numpy as np


def addProcessor():
    """
    Processor node for add operation
    """
    x, y, z = Input(), Input(), Input()
    f1 = Add(x, y, z)
    feed_dict1 = {x: 4, y: 5, z: 10}
    sorted_nodes1 = topological_sort(feed_dict1)
    output1 = forward_pass(f1, sorted_nodes1)

    print ("{} + {}  + {} = {} (according to miniflow - add)".format(feed_dict1[x], feed_dict1[y], feed_dict1[z], output1))


def mulProcessor():
    """
    Processor node for multiplication operation
    """
    l, m, n = Input(), Input(), Input()
    f2 = Mul(l, m, n)
    feed_dict2 = {l: 4, m: 5, n: 10}
    sorted_nodes2 = topological_sort(feed_dict2)
    output2 = forward_pass(f2, sorted_nodes2)

    print ("{} + {} + {} = {} (according to miniflow - mul)".format(feed_dict2[l], feed_dict2[m], feed_dict2[n], output2))



def linearProcessor():
    """
    Processor node for linear operation
    """
    inputs, weights, bias = Input(), Input(), Input()

    f = Linear(inputs, weights, bias)

    feed_dict = {
        inputs: [6, 14, 3],
        weights: [0.5, 0.25, 1.4],
        bias: 2
    }

    graph = topological_sort(feed_dict)
    output = forward_pass(f, graph)

    print(output , "(according to miniflow - linear)")



def linearMatrixProcessor():
    """
    Processor node for linear matrix operation
    """
    X, W, b = Input(), Input(), Input()

    f = LinearMatrix(X, W, b)

    X_ = np.array([[-1., -2.], [-1, -2]])
    W_ = np.array([[2., -3], [2., -3]])
    b_ = np.array([-3., -5])

    feed_dict = {X: X_, W: W_, b: b_}

    graph = topological_sort(feed_dict)
    output = forward_pass(f, graph)

    """
    Output should be:
    [[-9., 4.],
    [-9., 4.]]
    """
    print(output, "(according to miniflow - LinearMatrix)")



def linearSigmoidProcessor():
    """
    Processor node for linear and Sigmoid operation
    """
    X, W, b = Input(), Input(), Input()

    f = LinearMatrix(X, W, b)
    g = Sigmoid(f)

    X_ = np.array([[-1., -2.], [-1, -2]])
    W_ = np.array([[2., -3], [2., -3]])
    b_ = np.array([-3., -5])

    feed_dict = {X: X_, W: W_, b: b_}

    graph = topological_sort(feed_dict)
    output = forward_pass(g, graph)

    """
    Output should be:
    [[  1.23394576e-04   9.82013790e-01]
    [  1.23394576e-04   9.82013790e-01]]
    """
    print(output, "(according to miniflow - LinearSigmoid)")


def mseProcessor():
    y, a = Input(), Input()
    cost = MSE(y, a)

    y_ = np.array([1, 2, 3])
    a_ = np.array([4.5, 5, 10])

    feed_dict = {y: y_, a: a_}
    graph = topological_sort(feed_dict)
    # forward pass
    forward_pass_graph(graph)

    """
    Expected output

    23.4166666667
    """
    print(cost.value, "(according to miniflow - MSE)")



# Calling operator functions

addProcessor();
mulProcessor();
linearProcessor();
linearMatrixProcessor();
linearSigmoidProcessor();
