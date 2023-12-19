import sys
import numpy as np

input_data = sys.argv[1]
input_data = input_data.replace('[', "")
input_data = input_data.replace(']', "")
input_data = input_data.split(',')

input_data = [int(x) for x in input_data]

if input_data[0] > input_data[1]:
    output_data = input_data[0]
else:
    output_data = input_data[1]

print(output_data)