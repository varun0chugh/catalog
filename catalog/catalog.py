import json


def decode_value(base, value):
    return int(value, int(base))

def lagrange_interpolation_at_zero(points, k):
    def basis(j, points):
        x_j, _ = points[j]
        result = 1
        for m in range(k):
            if m != j:
                x_m, _ = points[m]
                result *= (-x_m) / (x_j - x_m)
        return result
   
    constant_term = 0
    for j in range(k):
        x_j, y_j = points[j]
        constant_term += y_j * basis(j, points)
    return round(constant_term)
def parse_input(json_data):
    n = json_data['keys']['n']
    k = json_data['keys']['k']
    points = []
 
    for key, value_data in json_data.items():
        if key != 'keys':
            x = int(key) 
            base = value_data['base']
            encoded_value = value_data['value']
            y = decode_value(base, encoded_value)
            points.append((x, y))
    return points, k
def find_secret_constant(json_input):
    points, k = parse_input(json_input)
    
    
    c = lagrange_interpolation_at_zero(points, k)
    return c


json_input_1 = {
    "keys": {
        "n": 4,
        "k": 3
    },
    "1": {
        "base": "10",
        "value": "4"
    },
    "2": {
        "base": "2",
        "value": "111"
    },
    "3": {
        "base": "10",
        "value": "12"
    },
    "6": {
        "base": "4",
        "value": "213"
    }
}

json_input_2 = {
    "keys": {
        "n": 9,
        "k": 6
    },
    "1": {
        "base": "10",
        "value": "28735619723837"
    },
    "2": {
        "base": "16",
        "value": "1A228867F0CA"
    },
    "3": {
        "base": "12",
        "value": "32811A4AA0B7B"
    },
    "4": {
        "base": "11",
        "value": "917978721331A"
    },
    "5": {
        "base": "16",
        "value": "1A22886782E1"
    },
    "6": {
        "base": "10",
        "value": "28735619654702"
    },
    "7": {
        "base": "14",
        "value": "71AB5070CC4B"
    },
    "8": {
        "base": "9",
        "value": "122662581541670"
    },
    "9": {
        "base": "8",
        "value": "642121030037605"
    }
}


result_1 = find_secret_constant(json_input_1)
result_2 = find_secret_constant(json_input_2)

print("Result for Test Case 1:", result_1)
print("Result for Test Case 2:", result_2)
