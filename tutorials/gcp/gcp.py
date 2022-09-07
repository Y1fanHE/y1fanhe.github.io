import numpy as np
from igraph import Graph, plot


def violation_point(x, A):
    I = x[:,None]==x
    return np.sum(I*A)//2


def random_graph(n_node, n_edge):
    A = np.zeros((n_node, n_node), dtype=int)
    while np.sum(A)//2 < n_edge:
        i, j = np.random.randint(n_node, size=2)
        if (i-j)%3!=0 and A[i][j]==0:
            A[i][j] = A[j][i] = 1
    return A


def is_connected(A):
    D = np.diag(np.sum(A, axis=1))
    w,_ = np.linalg.eig(D-A)
    return sorted(w)[1] > 0


def random_connected_graph(n_node, n_edge):
    is_A_connected = False
    while not is_A_connected:
        A = random_graph(n_node, n_edge)
        is_A_connected = is_connected(A)
    return A


def plot_graph(A, x=None, target=None, colors = ["red", "green", "blue"], bbox=(300, 300)):
    g = Graph.Adjacency(A, mode="undirected")
    g.vs["color"] = "gray"
    if isinstance(x, np.ndarray):
        color = [colors[i] for i in x]
        g.vs["color"] = color
    plot(g, layout=g.layout("kk"), target=target, bbox=bbox)
