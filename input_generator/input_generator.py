import subprocess
from random import seed
import json
import random
import numpy as np

SAMPLES = 500
OUTPUT_FOLDER = "input/"
SEED = 1
PROGRAM_FILES = [['1_1_A', False, None, None, None],
                 ['1_1_B', False, None, None, None],
                 ['1_1_C', False, None, None, None],
                 ['1_1_D', False, None, None, None],
                 ['1_1_E', False, None, None, None],
                 ['1_1_F', False, None, None, None],
                 ['1_2_A', True, 0, 9, 2],
                 ['1_2_B', True, -9, 9, 2],
                 ['1_2_C', True, 0, 9999, 2],
                 ['1_2_D', True, 0, 9999, 2],
                 ['1_2_E', True, 0, 9, 2],
                 ['1_3_A', True, 0, 9, 2],
                 ['1_3_B', True, -9999, 9999, 2],
                 ['1_4_A', True, -99, 99, 10],
                 ['1_4_B', True, -99, 99, 100]]  # Add your program file names here

seed(SEED)


def generate_input(only_int=False, min_value=None, max_value=None, length=None):
    array = []
    if length is None:
        length = random.randint(1, 100)
    else:
        length = random.randint(length, length+100)

    if max_value is None:
        max_value = random.randint(-1000, 1000)
    if min_value is None:
        min_value = random.randint(-1000, 1000)

    max_val = np.max([max_value, min_value])
    min_val = np.min([max_value, min_value])

    if only_int:
        for i in range(length):
            array.append(random.randint(min_val, max_val))
        return array
    else:
        for i in range(length):
            array.append(random.uniform(min_val, max_val))

    return array


def execute_program(program_path, input_data):
    process = subprocess.Popen(['python', program_path, str(input_data)], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error executing {program_path}: {error.decode()}")
        return None

    return output.decode().strip()


def save_data_to_file(data, filename):
    with open(filename, 'a') as file:
        json.dump(data, file)
        file.write(',\n')


filename = 'genetic_program_data.json'

for program in PROGRAM_FILES:
    open(OUTPUT_FOLDER + program[0] + filename, "w").close()
    print(program[0])
    for _ in range(SAMPLES):
        input_data = generate_input(program[1], program[2], program[3], program[4])
        if program[0] == "1_4_B":
            input_data[0] = int(np.abs(input_data[0]))
        output_data = execute_program('programs/' + program[0] + ".py", input_data)

        if output_data is not None:
            data_pair = {'input': input_data, 'output': output_data}
            save_data_to_file(data_pair, OUTPUT_FOLDER + program[0] + filename)
