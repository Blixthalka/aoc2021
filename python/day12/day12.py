from collections import defaultdict

def read_file():
    f = open("day12.txt", "r")
    return [ line.strip().split("-") for line in f]

graph = {}
input = read_file()

for entry in input:
    if entry[0] in graph.keys():
        graph[entry[0]].append(entry[1])
    else:
        graph[entry[0]] = [entry[1]]

    if entry[1] in graph.keys():
        graph[entry[1]].append(entry[0])
    else:
        graph[entry[1]] = [entry[0]]

def is_small(node):
    return node.lower() == node


result = []

def contains_len(node, path):
    return len(list(filter(lambda x: x == node, path)))

def contains_double_small(path):
    dict = defaultdict(int)
    for key in list(filter(is_small, path)):
        dict[key] += 1
    for v in dict.values():
        if v > 1:
            return True
    return False

def walk(node, path):
    path_c = path.copy()
    print('I am at "' + str(node) + '" I can go to ' + str(graph[node]))
    path_c.append(node)

    if node == 'end':
        result.append(path)
        return

    for edge in graph[node]:
        #print(str(edge) + ' ' + str(contains_len(edge, path_c.copy())))
        if edge == 'start':
            continue

        if is_small(edge) and ((edge in path_c) and contains_double_small(path_c)):
            continue
        #print(str(edge) + ' ' + str(path_c))

        walk(edge, path_c)

    return

print(graph)
walk("start", [])

#print(result)
print(len(result))

