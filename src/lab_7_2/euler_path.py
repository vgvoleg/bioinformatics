import utils

def empty(graph):
    for key in graph:
        if len(graph[key]) > 0:
            return False
    return True

def append_cycle(cycle, new_part):
    i = cycle.index(new_part[0])
    return cycle[:i] + new_part + cycle[i+1:]

def find_cycle(graph, start):
    cycle = []
    cycle.append(start)
    current = graph[start].pop()
    while current != start:
        cycle.append(current)
        current = graph[current].pop()
    cycle.append(current)
    return cycle

def add_extra_edge_to_graph(graph):
    from_to = {}
    for node_from in graph:
        if node_from not in from_to:
            from_to[node_from] = {"from": 0, "to": 0}
        for node_to in graph[node_from]:
            if node_to not in from_to:
                from_to[node_to] = {"from": 0, "to": 0}
            from_to[node_from]["from"] += 1
            from_to[node_to]["to"] += 1
    odd_from = ''
    odd_to = ''
    for node in from_to:
        if from_to[node]["from"] < from_to[node]["to"]:
            odd_from = node
        elif from_to[node]["from"] > from_to[node]["to"]:
            odd_to = node
    if odd_from not in graph:
        graph[odd_from] = []
    graph[odd_from].append(odd_to)
    return odd_from, odd_to

def euler_path(strings):
    graph = {}
    for string in strings:
        frm = string.split(' -> ')[0]
        to = string.split(' -> ')[1].split(',')
        graph[frm] = to
    frm, to = add_extra_edge_to_graph(graph)
    cycle = []
    while not empty(graph):
        start = frm if len(cycle) == 0 \
            else max(cycle, key=lambda k: len(graph[k]))
        new_cycle = find_cycle(graph, start)
        cycle = new_cycle if len(cycle) == 0 else append_cycle(cycle, new_cycle)
    cycle.pop(0)
    return cycle


if __name__ == '__main__':
    strings = utils.read_input_data()
    result = euler_path(strings)
    utils.write_output_data('->'.join(result))