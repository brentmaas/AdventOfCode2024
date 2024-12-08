operators = ["+", "*", "||"]

def test(value, nums):
    for i in range(len(operators) ** (len(nums) - 1)):
        test_operators = []
        for _ in range(len(nums) - 1):
            test_operators.append(operators[i%len(operators)])
            i //= len(operators)
        result = nums[0]
        for i in range(len(test_operators)):
            if test_operators[i] == "+":
                result += nums[i+1]
            elif test_operators[i] == "*":
                result *= nums[i+1]
            elif test_operators[i] == "||":
                result = int(str(result) + str(nums[i+1]))
        if result == value:
            return True
    return False

total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        split = line.split()
        value = int(split[0][:-1])
        nums = [int(i) for i in split[1:]]
        if test(value, nums):
            total += value
print(total)