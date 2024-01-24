from typing import List


def has_duplicates_1(collection: List) -> bool :
    """
    O(n ** 2)
    """
    for i in range(0, len(collection)):
        for j in range(0, len(collection)):
            if i != j and collection[i] == collection[j]:
                return True
    return False

def has_duplicates_2(collection):
    """
    O(n log n)
    """
    sorted_collection = sorted(collection)
    for i in range(1, len(sorted_collection)):
        if sorted_collection[i] == sorted_collection[i-1]:
            return True
    return False

def has_duplicates_3(collection):
    """
    O(n)
    """
    return len(set(collection)) != len(collection)



