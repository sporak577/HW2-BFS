# write tests for bfs
import pytest 
from search import Graph

def test_graph():
    """load the graph before testing."""
    return Graph("data/tiny_network.adjlist") #instance of graph, instance is an object belonging to the Graph class

def test_graph_2():
    return Graph("data/citation_network.adjlist")

def test_bfs_traversal(test_graph):
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    #picking a start node
    start_node = '31806696'
    bfs_result = test_graph.bfs(start_node)
    expected_nodes = {"31806696" , "Luke Gilbert"}
    assert set(expected_nodes).issubset(set(bfs_result))
    

    pass

def test_bfs(test_graph_2):
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
