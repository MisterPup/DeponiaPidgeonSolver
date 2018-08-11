import copy
import node as node_mod


class Configuration(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.nodes_map = {}
        for node in self.nodes:
            self.nodes_map[str(node.x) + str(node.y)] = node

    def get_signature(self):
        return ''.join(["{}{}".format(node.x, node.y) for node in self.nodes if node.is_active])

    def __repr__(self):
        return str(self.nodes)

    def get_rotated_configurations(self):
        configurations = []
        central_nodes = [x for x in self.nodes if x.is_center and x.is_active]
        for central_node in central_nodes:
            configurations.append((self.get_rotated_configuration(central_node), central_node))
        return configurations

    def get_rotated_configuration(self, central_node):
        if central_node not in self.nodes:
            raise ValueError('Unknown node')
        else:
            found_node = self.nodes[self.nodes.index(central_node)]
            if not found_node.is_center:
                raise ValueError('Not a central node')
            elif not found_node.is_active:
                raise ValueError('Central node not active')

        new_configuration_nodes = []

        for node in self.nodes:
            deepcopy = copy.deepcopy(node)
            new_configuration_nodes.append(deepcopy)

        new_conf = Configuration(new_configuration_nodes)

        if self.west_exist(central_node) and self.east_exist(central_node):
            self.middle_rotation(central_node, new_conf)
        elif not self.west_exist(central_node) and self.east_exist(central_node):
            self.west_rotation(central_node, new_conf)
        elif self.west_exist(central_node) and not self.east_exist(central_node):
            self.east_rotation(central_node, new_conf)
        else:
            raise Exception('Invalid Configuration')

        return new_conf

    def west_exist(self, central_node):
        west_x = central_node.x - 1
        west_y = central_node.y
        return self.get_node_by_coordinate(west_x, west_y) != node_mod.InvalidNode()

    def east_exist(self, central_node):
        east_x = central_node.x + 1
        east_y = central_node.y
        return self.get_node_by_coordinate(east_x, east_y) != node_mod.InvalidNode()

    def get_node_by_coordinate(self, x, y):
        return self.nodes_map.get(str(x) + str(y), node_mod.InvalidNode())

    def middle_rotation(self, central_node, new_conf):
        north_x = central_node.x
        north_y = central_node.y + 1

        south_x = central_node.x
        south_y = central_node.y - 1

        east_x = central_node.x + 1
        east_y = central_node.y

        west_x = central_node.x - 1
        west_y = central_node.y

        new_conf.get_node_by_coordinate(south_x, south_y).is_active = (
            self.get_node_by_coordinate(east_x, east_y).is_active)

        new_conf.get_node_by_coordinate(east_x, east_y).is_active = (
            self.get_node_by_coordinate(north_x, north_y).is_active)

        new_conf.get_node_by_coordinate(north_x, north_y).is_active = (
            self.get_node_by_coordinate(west_x, west_y).is_active)

        new_conf.get_node_by_coordinate(west_x, west_y).is_active = (
            self.get_node_by_coordinate(south_x, south_y).is_active)

    def west_rotation(self, central_node, new_conf):
        north_x = central_node.x
        north_y = central_node.y + 1

        south_x = central_node.x
        south_y = central_node.y - 1

        east_x = central_node.x + 1
        east_y = central_node.y

        is_one_rotation = (not self.get_node_by_coordinate(south_x, south_y).is_active
                           or (self.get_node_by_coordinate(south_x, south_y).is_active
                               and not self.get_node_by_coordinate(east_x, east_y).is_active))

        is_double_rotation = (self.get_node_by_coordinate(south_x, south_y).is_active
                              and self.get_node_by_coordinate(east_x, east_y).is_active
                              and not self.get_node_by_coordinate(north_x, north_y).is_active)

        if is_one_rotation:
            # substitute nodes of new_conf with nodes from original conf to avoid overwriting original values
            new_conf.get_node_by_coordinate(south_x, south_y).is_active = (
                self.get_node_by_coordinate(east_x, east_y).is_active)

            new_conf.get_node_by_coordinate(east_x, east_y).is_active = (
                self.get_node_by_coordinate(north_x, north_y).is_active)

            new_conf.get_node_by_coordinate(north_x, north_y).is_active = (
                self.get_node_by_coordinate(south_x, south_y).is_active)
        elif is_double_rotation:
            new_conf.get_node_by_coordinate(south_x, south_y).is_active = False
            new_conf.get_node_by_coordinate(east_x, east_y).is_active = True
            new_conf.get_node_by_coordinate(north_x, north_y).is_active = True

    def east_rotation(self, central_node, new_conf):
        north_x = central_node.x
        north_y = central_node.y + 1

        south_x = central_node.x
        south_y = central_node.y - 1

        west_x = central_node.x - 1
        west_y = central_node.y

        is_one_rotation = (not self.get_node_by_coordinate(north_x, north_y).is_active
                           or (self.get_node_by_coordinate(north_x, north_y).is_active
                               and not self.get_node_by_coordinate(west_x, west_y).is_active))

        is_double_rotation = (self.get_node_by_coordinate(north_x, north_y).is_active
                              and self.get_node_by_coordinate(west_x, west_y).is_active
                              and not self.get_node_by_coordinate(south_x, south_y).is_active)

        if is_one_rotation:
            # substitute nodes of new_conf with nodes from original conf to avoid overwriting original values
            new_conf.get_node_by_coordinate(south_x, south_y).is_active = (
                self.get_node_by_coordinate(north_x, north_y).is_active)

            new_conf.get_node_by_coordinate(west_x, west_y).is_active = (
                self.get_node_by_coordinate(south_x, south_y).is_active)

            new_conf.get_node_by_coordinate(north_x, north_y).is_active = (
                self.get_node_by_coordinate(west_x, west_y).is_active)
        elif is_double_rotation:
            new_conf.get_node_by_coordinate(north_x, north_y).is_active = False
            new_conf.get_node_by_coordinate(west_x, west_y).is_active = True
            new_conf.get_node_by_coordinate(south_x, south_y).is_active = True
