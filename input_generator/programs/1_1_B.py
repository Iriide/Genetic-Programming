import sys
import random

input_data = sys.argv[1]

output_data = [random.randint(0, 1000) for _ in range(random.randint(1, 100))]

position = random.randint(0, len(output_data) - 1)
output_data[position] = 789

print(output_data)
