from collections import defaultdict
from heapq import heappop, heappush

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def read_file():
    f = open("day16.txt", "r")
    return ''.join([ [hex_to_bin[z] for z in v.strip()] for v in f][0])

input = read_file()



def parse_literal(input):
    start = input[:1]
    value = input[1:5]
    if start == '0':
        return value, 5
    else:
        req_val, req_lit_len = parse_literal(input[5:])
        return value + req_val, req_lit_len + 5

v_sum = 0


operator_map = {
    0: lambda a, b: a + b,
    1: lambda a, b: a * b,
    2: lambda a, b: min(a, b),
    3: lambda a, b: max(a, b),
    5: lambda a, b: 1 if a > b else 0,
    6: lambda a, b: 1 if a < b else 0,
    7: lambda a, b: 1 if a == b else 0,
}


def parse(string):
    packet_version = int(string[:3], 2)
    packed_type_id = int(string[3:6], 2)
    packet_length = 6

    res = 0
    if packed_type_id == 4:
        literal_string, literal_length = parse_literal(string[6:])
        packet_length += literal_length
        literal = int(literal_string, 2)
        res = literal
    else:
        length_type_id = string[6:7]
        packet_length += 1

        operator_results = []

        if length_type_id == '0':
            operator_length = int(string[7:22], 2)
            packet_length += 15
            aim = packet_length + operator_length

            while packet_length != aim:
                p_length, operator_res = parse(string[packet_length:])
                packet_length += p_length
                operator_results.append(operator_res)
        else:
            num_sub_packets = int(string[7:18], 2)
            packet_length += 11

            for _ in range(num_sub_packets):
                p_length, operator_res = parse(string[packet_length:])
                packet_length += p_length
                operator_results.append(operator_res)

        operator = operator_map[packed_type_id]
        curr_res = operator_results[0]
        for i in range(1, len(operator_results)):
            curr_res = operator(curr_res, operator_results[i])
        res = curr_res

    print("packet", packet_length, string, string[packet_length:])
    return packet_length, res


print(parse(input))