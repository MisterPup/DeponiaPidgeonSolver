import unittest
import model.configuration as configuration
import model.node as node


class ConfigurationTest(unittest.TestCase):

    def test__given_unknown_central_node__when_rotation__then_exception(self):
        node_list = self.get_nodes()
        central_node = node.Node(6, 1)  # unknown node

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test__given_non_central_node__when_rotation__then_exception(self):
        node_list = self.get_nodes()
        central_node = node_list[1]

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test__given_central_non_active_node__when_rotation__then_exception(self):
        node_list = self.get_nodes()
        central_node = node_list[4]

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test__given_west_rotation_and_south_not_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[3]

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_west_rotation_and_south_active_and_east_not_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=False),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[3]

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=False) in rotated_conf.nodes))  # south

    def test__given_west_rotation_and_south_east_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[3]  # rotate central node of left column

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=False) in rotated_conf.nodes))  #south

    def test__given_west_rotation_and_south_east_north_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=True),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=False)]  # ultra bottom line
        central_node = node_list[3]  # rotate central node of left column

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_middle_rotation_and_south_active_then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=True),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=False),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=False),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[4]  # rotate central node of left column

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)
        print(rotated_conf)
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(1, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(1, 0, is_center=True, is_active=False) in rotated_conf.nodes))  # south
        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # west

    def test__given_middle_rotation_and_south_west_active_then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=False),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[4]  # rotate central node of left column

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)
        print(rotated_conf)
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(1, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(1, 0, is_center=True, is_active=False) in rotated_conf.nodes))  # south
        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # west

    def get_nodes(self):
        return [node.Node(0, 2, is_center=False, is_active=False),  # top line
                node.Node(1, 2, is_center=False, is_active=False),  # top line
                node.Node(2, 2, is_center=False, is_active=False),  # top line

                node.Node(0, 1, is_center=True, is_active=True),  # middle line
                node.Node(1, 1, is_center=True, is_active=False),  # middle line
                node.Node(2, 1, is_center=True, is_active=True),  # middle line

                node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
