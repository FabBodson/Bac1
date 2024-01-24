
def apply_merge_sort(collection):
    """
    This function applies the merge sort algorithm to the collection (list) in argument. The original list will not be modified.
    :param collection: list, a collection of any sortable items.
    :return: list, the sorted collection.
    """
    if len(collection) == 0:
        return []

    if len(collection) == 1:
        return [collection[0]]

    middle_index = len(collection) // 2
    left = apply_merge_sort(collection[:middle_index])
    right = apply_merge_sort(collection[middle_index:])

    return __merge(left, right)


def __merge(left, right):
    """
    This function merges two lists into a new (third) one. The resulting list will be sorted using the merge sort algorithm.
    :param left: list, a collection of any sortable items.
    :param right: list, a collection of any sortable items.
    :return: list, the sorted collection resulting from the merge of left and right.
    """
    result = []
    left_index, right_index = 0, 0

    # While both lists have elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            element = left[left_index]
            left_index += 1
        else:
            element = right[right_index]
            right_index += 1
        result.append(element)

    # If left has remaining elements
    if left_index < len(left):
        result.extend(left[left_index:])

    # If right has remaining elements
    if right_index < len(right):
        result.extend(right[right_index:])

    return result
