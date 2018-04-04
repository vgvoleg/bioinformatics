def read_input_data():
    with open('input.txt', encoding='utf-8') as input_file:
        strings = [line.strip() for line in input_file.readlines()]
    k = strings.pop(0)
    return k, strings

def write_output_data(result):
    with open('output.txt', 'w') as output_file:
        output_file.write(result)

def graph_de_bruijn(strings):
    kmers = set()
    result = []
    for string in strings:
        kmers.add(string[1:])
        kmers.add(string[:-1])
    graph = {}
    for kmer in kmers:
        graph[kmer] = []
    for string in strings:
        graph[str(string[:-1])].append(str(string[1:]))
    return graph

def euler_path(graph):
    frm, to = add_extra_edge_to_graph(graph)
    cycle = []
    while not empty(graph):
        start = frm if len(cycle) == 0 \
            else max(cycle, key=lambda k: len(graph[k]))
        new_cycle = find_cycle(graph, start)
        cycle = new_cycle if len(cycle) == 0 else append_cycle(cycle, new_cycle)
    cycle.pop(0)
    return cycle


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
