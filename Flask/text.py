def count_common_elements(list1, list2):
    """Count the number of common elements between two lists."""
    # Convert lists to sets to remove duplicates and for efficient lookup
    set1, set2 = set(list1), set(list2)
    # Count how many elements from set1 are also in set2
    return sum(elem in set2 for elem in set1)

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
print(count_common_elements(list1,list2))