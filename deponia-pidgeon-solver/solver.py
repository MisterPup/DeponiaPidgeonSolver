import configuration.configuration_factory as configuration_factory
import configuration.node as node

if __name__ == "__main__":
    node_list = [node.Node(0, 2), node.Node(1, 2), node.Node(2, 2),
                 node.Node(0, 1, is_center=True), node.Node(1, 1, is_center=True), node.Node(1, 2, is_center=True),
                 node.Node(0, 0), node.Node(1, 0, is_center=True), node.Node(2, 0),
                 node.Node(1, -1)]

    num_active_nodes = 6

    configurations = configuration_factory.ConfigurationFactory().get_configurations(node_list, num_active_nodes)
