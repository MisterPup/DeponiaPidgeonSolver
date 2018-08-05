import itertools
import configuration


class ConfigurationFactory(object):

    def get_configurations(self, nodes, num_actives):
        config_list = []
        nodes_combinations = itertools.combinations(nodes, num_actives)

        for nodes_comb in list(nodes_combinations):
            print nodes_comb
            config_list.append(configuration.Configuration(nodes_comb))
        return config_list
