# write tests for bfs
import pytest 
from search import Graph
import networkx as nx

"""I received help from Isaiah Hazelwood, Biophysics PhD Student"""
def test_graph():
    """load the graph before testing."""
    return graph("data/tiny_network.adjlist") #instance of graph, instance is an object belonging to the Graph class

def test_graph_2():
    return graph("data/citation_network.adjlist")


def test_bfs_traversal(test_graph):
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    #check if BFS traverses the entire graph 

    #breadth first search to traverse this network
    G_tiny = graph.Graph("./data/tiny_network.adjlist")
    #this runs bfs from "lani wu" and collects the traversal order
    lani_wu_traverse = G_tiny.bfs("Lani Wu", end=None)
    #there are a total of 30 nodes, here I check if this holds true
    assert len(lani_wu_traverse) == 30
    #now verify the BFS order to ensure the first few visited nodes mare the immediate neighbors
    #extract the first 5 nodes from 'lani_wu_traverse', then define list of expected nodes,
    #for each node in the expected list check if the node is in the first 5 nodes of lani_wu_traverse
    #if node is missing, raise an assertion error
    
    first_five_nodes = lani_wu_traverse[:5]
    #define expected nodes
    expected_nodes = ["Lani Wu", "32042149", "32036252", "31806696", "30727954"]
    #check if all expected nodes are in the first 5
    for node in expected_nodes:
        assert node in first_five_nodes, f"Node {node} is missing from first 5 nodes"

    #test on a nonexistent node and expected behavior is a raised error
    with pytest.raises(KeyError):
        toni_capra_traverse = G_tiny.bfs("Toni Capra", end=None)
    
    #test bfs on an empty graph
    G_empty = graph.Graph("./data/empty_network.adjlist")
    assert len(list(G_empty.graph.nodes)) == 0
    assert len(list(G_empty.graph.edges)) == 0

    with pytest.raises(KeyError):
        #raises key error
        nonexistent_traverse = G_empty.bfs("Nonexistent Node", end=None)
    
    #one edge case would be bfs with same start and end, should traverse without infinite loop
    def test_bfs_same_start_and_end():
        G_cyclic = graph.Graph("./data/cyclic_tiny_network.adjlist")
        cycle_traverse = G_cyclic.bfs("1", end=None) #star bfs from node 1

        expected_order = ["1", "2", "3", "4", "5", "6"]

        assert cycle_traverse == expected_order 

    def test_bfs_unconnected_nodes():
        G_self = graph.Graph("./data/unconnected_nodes.adjlist")
        self_traverse = G_self("1", end=None)

        expected_result = ["1"]

        assert self_traverse == expected_result


    pass

def test_bfs(test_graph_2):
    #test if BFS correctly finds the shortest path between nodes
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    #load the citation network graph 
    G_citation = graph.Graph("./data/citation_network.adjlist")

    #traverse from one node to another, verify the shortest path is found

    G_Michael_Keiser = G_citation.bfs("Michael Keiser", end = "Marina Sirota")
    assert G_Tony_Joe in list(nx.all_shortest_paths(G_citation.graph, source="Tony Capra", target="Joseph DeRisi"))

    #test BFS on an empty graph 
    G_empty = graph.Graph("./data/empty_citation.adjlist")
    with pytest.raises(KeyError):
        nonexistent_traverse = G_empty.bfs("Nonexistent Node", end="Nonexistent Node 2")

    #test BFS on a disconnected graph
    G_disconnected = graph.Graph("./data/unconnected_nodes.adjilist")
    with pytest.raises(KeyError):
        disconnected_traverse = G_disconnected("Disconnected Traverse", source="1", target="None")
    
    #test BFS in a cyclic graph
    G_cycle = graph.Graph("./data/cycle_network.adjlist")
    search_1_3 = G_cycle.bfs("1", end="3")
    assert search_1_3 == ["1", "2", "3"]

    #test bfs when start == end 
    G_self = graph.Graph("./data/unconnected_nodes.adjlist")
    search_1_1 = G_self.bfs("1", end="1")
    assert search_1_1 == ["1"]
    



    







    pass
