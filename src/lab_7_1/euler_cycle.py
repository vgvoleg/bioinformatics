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
    # print(cycle)
    return cycle

def euler_cycle(strings):
    graph = {}
    for string in strings:
        frm = string.split(' -> ')[0]
        to = string.split(' -> ')[1].split(',')
        graph[frm] = to
    cycle = []
    while not empty(graph):
        start = max(graph, key=lambda k: len(graph[k])) if len(cycle) == 0 \
            else max(cycle, key=lambda k: len(graph[k]))
        new_cycle = find_cycle(graph, start)
        cycle = new_cycle if len(cycle) == 0 else append_cycle(cycle, new_cycle)
    return cycle

if __name__ == '__main__':
    strings = utils.read_input_data()
    result = euler_cycle(strings)
    utils.write_output_data('->'.join(result))