import re

enabled = True
result = 0

def filter_text(text):
    # Regular expression pattern to match mul(int, int), do(), and don't()
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'

    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    return matches


with open('../input.txt', 'r') as file:
    text = file.read()

text = filter_text(text)

for match in text:
    if match == 'do()':
        enabled = True
    elif match == 'don\'t()':
        enabled = False
    elif enabled:
        nums = match[4:-1].split(',')
        result += int(nums[0]) * int(nums[1])
    else:
        pass

print(result)

