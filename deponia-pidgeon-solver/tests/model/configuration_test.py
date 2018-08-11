import unittest
import model.configuration as configuration
import model.node as node


class ConfigurationTest(unittest.TestCase):

    def test_given_unknown_central_node_then_exception(self):
        node_list = self.get_nodes()
        central_node = node.Node(6, 1)  # unknown node

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test_given_non_central_node_then_exception(self):
        node_list = self.get_nodes()
        central_node = node_list[1]

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test_given_central_non_active_node_then_exception(self):
        node_list = self.get_nodes()
        central_node = node_list[4]

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test_given_west_central_node_and_south_not_active_then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 2, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[3]

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)
        print(rotated_conf)

        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=False) in rotated_conf.nodes))
        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=True) in rotated_conf.nodes))

    def test_given_west_central_node_and_south_active_and_east_not_active_then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=False),  # middle line
                     node.Node(1, 2, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
        central_node = node_list[3]

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)
        print(rotated_conf)

        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))
        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=False) in rotated_conf.nodes))

    def get_nodes(self):
        return [node.Node(0, 2, is_center=False, is_active=False),  # top line
                node.Node(1, 2, is_center=False, is_active=False),  # top line
                node.Node(2, 2, is_center=False, is_active=False),  # top line
                node.Node(0, 1, is_center=True, is_active=True),  # middle line
                node.Node(1, 1, is_center=True, is_active=False),  # middle line
                node.Node(1, 2, is_center=True, is_active=True),  # middle line
                node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                node.Node(2, 0, is_center=False, is_active=True),  # bottom line
                node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line
