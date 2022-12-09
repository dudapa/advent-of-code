from functools import reduce


FILE_PATH = './input_day1.txt'

def input_handler(data_path:str) -> list:
    # Read input data from file 
    with open(data_path, 'r', encoding='utf-8') as f:
        input_data = f.read()
    return input_data.split('\n')

def get_elve_calories(data:list) -> list:
    elve_calories = []
    temp_sum = 0
    for entry in data:
        if entry == '':
            elve_calories.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(entry)
    return elve_calories

def find_max_calory(data:list) -> int:
    # Get elve's calory list
    elve_calories = get_elve_calories(data)
    return max(elve_calories)

def top_three_calories(data:list):
    elve_top3_calories = sorted(get_elve_calories(data), reverse=True)[0:3]
    return reduce(lambda a, b: a+b, elve_top3_calories)

if __name__ == '__main__':
    data_list = input_handler(FILE_PATH)
    result_top = find_max_calory(data_list)
    result_top3 = top_three_calories(data_list)
