import utils


if __name__ == '__main__':
    k, strings = utils.read_input_data()
    graph = utils.graph_de_bruijn(strings)
    cycle = utils.euler_path(graph)
    result = cycle.pop(0) + ''.join([s[-1] for s in cycle])
    utils.write_output_data(result)