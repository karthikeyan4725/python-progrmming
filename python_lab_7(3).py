def get_element_at_index(numbers, index):
        element = numbers[index]
        print("Element at index", index, "is", element)
numbers = input("enter a list (comma seperated):").split(",")
index = int(input("Enter the index: "))
get_element_at_index(numbers, index)
