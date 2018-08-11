
class GraphGenerator(object):
    def __init__(self, configurations):
        self.configurations = configurations

    def generate(self):
        edges = []

        for config in self.configurations:
            rotated_configuration_tuples = config.get_rotated_configurations()
            for rotated_conf, central_node in rotated_configuration_tuples:
                edges.append(((config.get_signature(), rotated_conf.get_signature(), 1), central_node))

        return edges
