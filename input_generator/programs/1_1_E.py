import sys
import random

input_data = sys.argv[1]

output_data = [random.randint(0, 1000) for _ in range(random.randint(1, 100))]

output_data[0] = 789

print(output_data)
