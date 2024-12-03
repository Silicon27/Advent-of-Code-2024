import re

with open('../input', 'r') as file:
    text = file.read()

pattern = r'mul\((\d+),(\d+)\)'

# Find all matching sequences
matches = re.findall(pattern, text)

result = 0
# Print the results
for match in matches:
    result += int(match[0]) * int(match[1])

print(result)