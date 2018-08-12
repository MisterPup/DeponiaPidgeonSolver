import configuration.configuration_factory as configuration_factory
import configuration.node as node
import configuration.configuration as configuration
import graph.graph_generator as graph_generator
import algorithm.dijkstra as dijkstra

if __name__ == "__main__":

    node_list = (
        [node.Node(0, 2, is_center=False),  # top line
         node.Node(1, 2, is_center=False),  # top line
         node.Node(2, 2, is_center=False),  # top line

         node.Node(0, 1, is_center=True),  # middle line
         node.Node(1, 1, is_center=True),  # middle line
         node.Node(2, 1, is_center=True),  # middle line

         node.Node(0, 0, is_center=False),  # bottom line
         node.Node(1, 0, is_center=True),  # bottom line
         node.Node(2, 0, is_center=False),  # bottom line

         node.Node(1, -1, is_center=False)])  # ultra bottom line

    num_active_nodes = 6

    # generate all possible configurations (combinations of 6 element active out of a total of 10)
    configurations = configuration_factory.ConfigurationFactory().get_configurations(node_list, num_active_nodes)
    # config_map = {}
    # for c in configurations:
    #     config_map[c.get_signature()] = c

    # calculate each possible rotations for each configuration
    # each configuration is a vertex of the graph
    # edges connect configurations to their rotations

    # the first part of the tuple is the edge that connects a configuration to its rotation
    # the second part of the tuple is the central node that triggers the rotation
    edge_tuples = graph_generator.GraphGenerator(configurations).generate()

    edges = []
    edges_map = {}
    for edge_tuple in edge_tuples:
        edge = edge_tuple[0]
        edges.append(edge)

        edge_start_config = edge[0]
        edge_end_config = edge[1]
        rotation_node = edge_tuple[1]
        key = "S" + str(edge_start_config) + "E" + str(edge_end_config)
        # commodity structure for retrieving the nodes that trigger the rotation that will lead to the solution
        edges_map[key] = rotation_node

    start_nodes = (
        [node.Node(0, 2, is_center=False, is_active=True),
         node.Node(1, 2, is_center=False, is_active=True),
         node.Node(2, 2, is_center=False, is_active=True),

         node.Node(0, 1, is_center=True, is_active=True),
         node.Node(1, 1, is_center=True, is_active=True),
         node.Node(2, 1, is_center=True, is_active=False),

         node.Node(0, 0, is_center=False, is_active=False),
         node.Node(1, 0, is_center=True, is_active=False),
         node.Node(2, 0, is_center=False, is_active=True),

         node.Node(1, -1, is_center=False, is_active=False)])
    start_configuration = configuration.Configuration(start_nodes)

    end_nodes = (
        [node.Node(0, 2, is_center=False, is_active=True),
         node.Node(1, 2, is_center=False, is_active=False),
         node.Node(2, 2, is_center=False, is_active=True),

         node.Node(0, 1, is_center=True, is_active=True),
         node.Node(1, 1, is_center=True, is_active=False),
         node.Node(2, 1, is_center=True, is_active=False),

         node.Node(0, 0, is_center=False, is_active=True),
         node.Node(1, 0, is_center=True, is_active=True),
         node.Node(2, 0, is_center=False, is_active=True),

         node.Node(1, -1, is_center=False, is_active=False)])
    end_configuration = configuration.Configuration(end_nodes)

    # starting from a graph of connected configurations, we use Dijkstra to get the shortest path between two of them
    d = dijkstra.Dijkstra()
    solution = d.solve(edges, start_configuration.get_signature(), end_configuration.get_signature())

    if solution == float("inf"):
        print("No solution!")
    else:
        # print(str(solution[0]))
        # print(str(solution[1]))
        # print(str(solution[2]))

        print("Rotations to apply")
        traversed_configs = solution[2]
        for i in range(0, len(traversed_configs) - 1):
            cur_config = traversed_configs[i]
            next_config = traversed_configs[i + 1]
            print(edges_map["S" + cur_config + "E" + next_config])