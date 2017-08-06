
input = list("abcdefg")

mid = int(len(input)/2)
left = 0
right = len(input)-1

while left < right:
    input[left], input[right] = input[right], input[left]
    left += 1
    right -= 1

print(input)