class Configuration(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def get_signature(self):
        return ''.join(["{}{}".format(node.x, node.y) for node in self.nodes if node.is_active])

    def __repr__(self):
        return str(self.nodes)

    # def get_rotated_configurations(self):
    #     central_nodes = [x for x in self.actives_nodes if x.is_center]

    def get_rotated_configuration(self, central_node):
        if central_node not in self.nodes:
            raise ValueError('Unknown node')
        else:
            found_node = self.nodes[self.nodes.index(central_node)]
            if not found_node.is_center:
                raise ValueError('Not a center node')
            elif not found_node.is_active:
                raise ValueError('Node not active')

        c_x = central_node.x
        c_y = central_node.y

        nord_x = central_node.x
        nord_y = central_node.y + 1

        sud_x = central_node.x
        sud_y = central_node.y - 1

        est_x = central_node.x + 1
        est_y = central_node.y

        ovest_x = central_node.x - 1
        ovest_y = central_node.y

        return Configuration(self.nodes)

