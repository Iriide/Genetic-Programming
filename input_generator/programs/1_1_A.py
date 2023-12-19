import sys
import random

input_data = sys.argv[1]

output_data = [random.randint(0, 10) for _ in range(random.randint(1, 100))]

# Umieszcza liczbę 1 na losowej pozycji w liście
position = random.randint(0, len(output_data) - 1)
output_data[position] = 1

print(output_data)
