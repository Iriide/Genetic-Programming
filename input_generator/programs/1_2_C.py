import sys

input_data = sys.argv[1]
input_data = input_data.replace('[', "")
input_data = input_data.replace(']', "")
input_data = input_data.split(',')

input_data = [int(x) for x in input_data]

output_data = input_data[0] + input_data[1]

print(output_data)