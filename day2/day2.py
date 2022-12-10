PATH = './input_day2.txt'

# Rules for part 1
RULES = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
    }

# Rules for part 2
NEED_PLAY =  {
        'AX': 3,
        'AY': 4,
        'AZ': 8,
        'BX': 1,
        'BY': 5,
        'BZ': 9,
        'CX': 2,
        'CY': 6,
        'CZ': 7,
    }

def input_handler(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        return list(map(lambda x: ''.join(x.split(' ')),f.read().split('\n')))

# Functions to calculate part 1    
def point_handler(game: str, rules: dict) -> int:
    return rules[game] + rules[game[1]]
    
def total_result(data:list) -> int:
    return sum([point_handler(game, RULES) for game in data])

# Function to calculate part 2
def total_result2(data:list, rules:dict) -> int:
    return sum([rules[game] for game in data])
    
    
if __name__ == '__main__':
    input_data =  input_handler(PATH)
    result = total_result(input_data)
    result2 = total_result2(input_data, NEED_PLAY)