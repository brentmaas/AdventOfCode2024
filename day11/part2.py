stones = {}
with open("Input.txt", "r") as f:
    for stone in [int(i) for i in f.readline().rstrip().split()]:
        if stone in stones:
            stones[stone] += 1
        else:
            stones[stone] = 1
cache = {0: [1]}
for _ in range(75):
    new_stones = {}
    for stone in stones:
        if stone in cache:
            for new_stone in cache[stone]:
                if new_stone in new_stones:
                    new_stones[new_stone] += stones[stone]
                else:
                    new_stones[new_stone] = stones[stone]
        elif len(str_stone := str(stone)) % 2 == 0:
            left = int(str_stone[:len(str_stone)//2])
            right = int(str_stone[len(str_stone)//2:])
            if left in new_stones:
                new_stones[left] += stones[stone]
            else:
                new_stones[left] = stones[stone]
            if right in new_stones:
                new_stones[right] += stones[stone]
            else:
                new_stones[right] = stones[stone]
            cache[stone] = [left, right]
        else:
            cache[stone] = [2024 * stone]
            if cache[stone][0] in new_stones:
                new_stones[cache[stone][0]] += stones[stone]
            else:
                new_stones[cache[stone][0]] = stones[stone]
    stones = new_stones
print(sum(stones.values()))