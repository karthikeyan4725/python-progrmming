def find_number_indices(numbers, target):
    positive_indices = []
    negative_indices = []
    count = 0

    for i, num in enumerate(numbers):
        if num == target:
            count += 1
            positive_indices.append(i+1)
            negative_indices.append(-len(numbers)+i+1)

    return count, positive_indices, negative_indices


numbers = input("Enter the list of numbers (comma-separated): ").split(",")
numbers = [int(num) for num in numbers]


target = int(input("Enter the element to be found: "))


count, positive_indices, negative_indices = find_number_indices(numbers, target)


print(f"Element {target} occurs {count} times in the list.")


print("Positive Index:", end=" ")
print(*positive_indices, sep=", ")


print("Negative Index:", end=" ")
print(*negative_indices, sep=", ")
