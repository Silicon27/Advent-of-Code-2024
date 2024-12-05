with open("../input.txt", "r") as file:
    left, right = zip(*(map(int, line.split()) for line in file.read().splitlines()))

left, right = sorted(left), sorted(right)

ans = 0
for i in range(len(left)):
    if left[i] > right[i]:
        ans += left[i] - right[i]
    else:
        ans += right[i] - left[i]

print(ans)

