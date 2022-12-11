from string import ascii_letters

FILE_PATH = './input_day3.txt'

def data_handler(data_path: str) -> list:
    with open(data_path, 'r', encoding='utf-8') as f:
        return f.read().split('\n')

# Functions part 1
def process_data(data: list) -> int:
    total = 0
    for rucksack in data:
        half1, half2 = rucksack[0:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2)::]
        for letter in half1:
            if letter in  half2:
                total += ascii_letters.index(letter) + 1
                break
    return total

# Functions part 2
# Function to group elves to particular gropus 
def group_data2(data:list) -> list:
    groups = []
    group = []
    counter = 0
    for elf in data:
        counter += 1
        group.append(elf)
        if counter == 3:
            groups.append(group)
            group = []
            counter = 0
    return groups

def process_data2(data:list) -> int:
    groups = group_data2(data)
    total = 0
    for group in groups:
        elf1, elf2, elf3 = group
        for letter in elf1:
            if letter in elf2 and letter in elf3:
                total += ascii_letters.index(letter) + 1
                break
    return total 
        

if __name__ == '__main__':
    data_list = data_handler(FILE_PATH)
    # Result of part 1
    result = process_data(data_list)
    # Result of part 2
    result2 = process_data2(data_list)
