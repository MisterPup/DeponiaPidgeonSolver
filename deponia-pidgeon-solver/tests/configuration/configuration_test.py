import unittest
import configuration.configuration as configuration
import configuration.node as node


class ConfigurationTest(unittest.TestCase):

    def test__given_unknown_central_node__when_rotation__then_exception(self):
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

        central_node = node.Node(6, 1)  # unknown node

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test__given_non_central_node__when_rotation__then_exception(self):
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

        central_node = node.Node(1, 2, is_center=False, is_active=False)

        conf = configuration.Configuration(node_list)
        with self.assertRaises(ValueError):
            conf.get_rotated_configuration(central_node)

    def test__given_central_non_active_node__when_rotation__then_exception(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=True),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=False),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = node.Node(1, 1, is_center=True, is_active=False)

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

        central_node = node.Node(0, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_west_rotation_and_south_active__then_rotate(self):
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

        central_node = node.Node(0, 1, is_center=True, is_active=True)

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

        central_node = node.Node(0, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=False) in rotated_conf.nodes))  # south

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

        central_node = node.Node(0, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_west_rotation_and_south_north_active_and_east_not_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=True),  # top line
                 node.Node(1, 2, is_center=False, is_active=False),  # top line
                 node.Node(2, 2, is_center=False, is_active=True),  # top line

                 node.Node(0, 1, is_center=True, is_active=True),  # middle line
                 node.Node(1, 1, is_center=True, is_active=False),  # middle line
                 node.Node(2, 1, is_center=True, is_active=False),  # middle line

                 node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                 node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                 node.Node(2, 0, is_center=False, is_active=False),  # bottom line

                 node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = node.Node(0, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(0, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
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

        central_node = node.Node(1, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

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

        central_node = node.Node(1, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(1, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(1, 0, is_center=True, is_active=False) in rotated_conf.nodes))  # south
        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # west

    def test__given_middle_rotation_and_north_east_active__then_rotate(self):
        node_list = (
            [node.Node(0, 2, is_center=False, is_active=False),
             node.Node(1, 2, is_center=False, is_active=True),
             node.Node(2, 2, is_center=False, is_active=True),

             node.Node(0, 1, is_center=True, is_active=False),
             node.Node(1, 1, is_center=True, is_active=True),
             node.Node(2, 1, is_center=True, is_active=True),

             node.Node(0, 0, is_center=False, is_active=True),
             node.Node(1, 0, is_center=True, is_active=False),
             node.Node(2, 0, is_center=False, is_active=False),

             node.Node(1, -1, is_center=False, is_active=True)])

        central_node = node.Node(1, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(1, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(1, 0, is_center=True, is_active=True) in rotated_conf.nodes))  # south
        self.assertEqual(True, (node.Node(0, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # west

    def test__given_middle_rotation_with_bottom_node_and_south_west_active_then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=True),  # top line
                     node.Node(1, 2, is_center=False, is_active=True),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=False),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=False),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=False)]  # ultra bottom line

        central_node = node.Node(1, 0, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(1, 0, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(2, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # east
        self.assertEqual(True, (node.Node(1, -1, is_center=False, is_active=True) in rotated_conf.nodes))  # south
        self.assertEqual(True, (node.Node(0, 0, is_center=False, is_active=False) in rotated_conf.nodes))  # west

    def test__given_east_rotation_and_north_not_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=True),  # top line
                     node.Node(1, 2, is_center=False, is_active=True),  # top line
                     node.Node(2, 2, is_center=False, is_active=False),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=False),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=False),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = (node.Node(2, 1, is_center=True, is_active=True))

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(2, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # west
        self.assertEqual(True, (node.Node(2, 0, is_center=False, is_active=False) in rotated_conf.nodes))  # south

    def test__given_east_rotation_and_north_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=True),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=False),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=False),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = (node.Node(2, 1, is_center=True, is_active=True))

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(2, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # west
        self.assertEqual(True, (node.Node(2, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_east_rotation_and_north_west_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=True),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=False),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = (node.Node(2, 1, is_center=True, is_active=True))

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(2, 2, is_center=False, is_active=False) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # west
        self.assertEqual(True, (node.Node(2, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_east_rotation_and_north_west_south_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=False),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=True),  # middle line
                     node.Node(1, 1, is_center=True, is_active=True),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=True),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=False),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = (node.Node(2, 1, is_center=True, is_active=True))

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(2, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # west
        self.assertEqual(True, (node.Node(2, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south

    def test__given_east_rotation_and_north_south_active_and_west_not_active__then_rotate(self):
        node_list = [node.Node(0, 2, is_center=False, is_active=True),  # top line
                     node.Node(1, 2, is_center=False, is_active=False),  # top line
                     node.Node(2, 2, is_center=False, is_active=True),  # top line

                     node.Node(0, 1, is_center=True, is_active=False),  # middle line
                     node.Node(1, 1, is_center=True, is_active=False),  # middle line
                     node.Node(2, 1, is_center=True, is_active=True),  # middle line

                     node.Node(0, 0, is_center=False, is_active=False),  # bottom line
                     node.Node(1, 0, is_center=True, is_active=True),  # bottom line
                     node.Node(2, 0, is_center=False, is_active=True),  # bottom line

                     node.Node(1, -1, is_center=False, is_active=True)]  # ultra bottom line

        central_node = node.Node(2, 1, is_center=True, is_active=True)

        conf = configuration.Configuration(node_list)
        rotated_conf = conf.get_rotated_configuration(central_node)

        self.assertEqual(True, (node.Node(2, 1, is_center=True, is_active=True) in rotated_conf.nodes))  # center
        self.assertEqual(True, (node.Node(2, 2, is_center=False, is_active=True) in rotated_conf.nodes))  # north
        self.assertEqual(True, (node.Node(1, 1, is_center=True, is_active=False) in rotated_conf.nodes))  # west
        self.assertEqual(True, (node.Node(2, 0, is_center=False, is_active=True) in rotated_conf.nodes))  # south