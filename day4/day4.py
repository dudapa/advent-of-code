PATH_FILE = './input_day4.txt'

def input_hadler(input_path: str) -> list:
    with open(input_path, 'r', encoding='utf-8') as f:
        return list(map(lambda x: x.strip().split(','), f.readlines()))

# Fuctions part 1
def all_included(range1:tuple, range2:tuple) -> bool:
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

# Functions part 2
def any_included(range1:tuple, range2:tuple) -> bool:
    if range1[0] >= range2[0] and range1[0] <= range2[1]:
        return True
    if range2[1] >= range1[0] and range2[0] <= range1[1]:
        return True
    return False

# Function for both part 1 and part 2   
def check_assigments(pair: str, all:bool) -> bool:
    range1 = tuple(map(lambda x: int(x),pair[0].split('-')))
    range2 = tuple(map(lambda x: int(x), pair[1].split('-')))
    if all:
        return all_included(range1, range2)
    return any_included(range1, range2)

def process_data(data: list, all=True) -> int:
    return len(list(filter(lambda x: x==True, (map(lambda x: check_assigments(x, all), data)))))

if __name__ == '__main__':
    data_list = input_hadler(PATH_FILE)
    # Result part 1
    result = process_data(data_list)
    # Result part 2
    result2 = process_data(data_list, all=False)
    