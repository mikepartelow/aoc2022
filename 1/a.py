import os
import heapq

def part_one(filename):
    max_calories = 0
    elf_calories = 0

    with open(os.path.abspath(filename)) as f:
        for line in f:
            item = line.strip()
            if item == "":
                max_calories = max(max_calories, elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(item)

    max_calories = max(max_calories, elf_calories)

    print(f"   max_calories: {max_calories}")
    return max_calories

def part_two(filename):
    calorie_heap = []
    elf_calories = 0

    with open(os.path.abspath(filename)) as f:
        for line in f:
            item = line.strip()
            if item == "":
                heapq.heappush(calorie_heap, -elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(item)

    heapq.heappush(calorie_heap, -elf_calories)
    max_calories = sum(-heapq.heappop(calorie_heap) for _ in range(3))

    print(f"   max_calories: {max_calories}")
    return max_calories


assert 24000 == part_one('example.txt')
assert 1 == part_one('test0.txt')
print()
print(f"-> part one answer: {part_one('input.txt')}")
print()

assert 45000 == part_two('example.txt')
assert 203 == part_two('test1.txt')
print()
print(f"-> part two answer: {part_two('input.txt')}")
print()
