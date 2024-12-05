with open("../input.txt", "r") as file:
    left, right = zip(*(map(int, line.split()) for line in file.read().splitlines()))

ans = 0
for i in left:
    ans += i * right.count(i)

print(ans)

