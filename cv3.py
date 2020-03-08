def convert_to_int(input_str: str):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if wrong_format(input_str, values):
        return -9999
    result = 0
    add_last = True
    lower_previous = False
    tmp = 0
    for i in range(len(input_str) - 1):
        if lower_previous:
            if values[input_str[i + 1]] >= values[input_str[i -1]]:
                return -9999
            lower_previous = False
            continue
        if values[input_str[i]] < values[input_str[i + 1]]:
            if i > 0 and values[input_str[i - 1]] <= values[input_str[i + 1]]:
                return -9999
            result += values[input_str[i + 1]] - values[input_str[i]]
            lower_previous = True
            if i + 2 == len(input_str):
                add_last = False
        else:
            result += values[input_str[i]]
    if add_last:
        result += values[input_str[-1]]
    return  result

def wrong_format(input_str: str, values: dict):
    if not isinstance(input_str, str) or len(input_str) == 0:
        return True
    for i in input_str:
        if i not in values.keys():
            return True
    for i in [i * 4 for i in values.keys()]:
        if i in input_str:
            return True