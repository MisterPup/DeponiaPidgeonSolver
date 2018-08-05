import model.configuration_factory as configuration_factory
import model.node as node

if __name__ == "__main__":
    node_list = [node.Node('A', 0, 2), node.Node('B', 1, 2), node.Node('C', 2, 2), node.Node('D', 0, 1),
                 node.Node('E', 1, 1), node.Node('F', 1, 2), node.Node('G', 0, 0), node.Node('H', 1, 0),
                 node.Node('I', 2, 0), node.Node('J', 1, -1)]

    num_active_nodes = 6

    configurations = configuration_factory.ConfigurationFactory().get_configurations(node_list, num_active_nodes)
