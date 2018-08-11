import itertools
import configuration
import copy


class ConfigurationFactory(object):

    def get_configurations(self, all_nodes, num_actives):
        config_list = []
        nodes_combinations = list(itertools.combinations(all_nodes, num_actives))

        for combination in nodes_combinations:
            configuration_nodes = []
            for node in all_nodes:
                new_node = copy.deepcopy(node)
                if new_node in list(combination):
                    new_node.is_active = True
                configuration_nodes.append(new_node)
            c = configuration.Configuration(configuration_nodes)
            # print(c.get_signature())
            # print(c)
            # print("*****")
            config_list.append(c)
        return config_list
