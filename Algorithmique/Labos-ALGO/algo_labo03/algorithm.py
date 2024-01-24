def apply_merge_sort(collection):
    """
    This function applies the merge sort algorithm to the collection (list) in argument. The original list will not be modified.
    :param collection: list, a collection of any sortable items.
    :return: list, the sorted collection.
    """
    collection_copy = collection.copy()
    length = len(collection_copy)
    if length < 2:
        return collection_copy

    middle = length//2
    left = collection_copy[:middle]
    right = collection_copy[middle:]
    left = apply_merge_sort(left)
    right = apply_merge_sort(right)

    return __merge(left, right)


def __merge(left, right):
    """
    This function merges two lists into a new (third) one. The resulting list will be sorted using the merge sort algorithm.
    :param left: list, a collection of any sortable items.
    :param right: list, a collection of any sortable items.
    :return: list, the sorted collection resulting from the merge of left and right.
    """
    left_len = len(left)
    right_len = len(right)
    collection = []
    i, j = 0, 0

    while (i < left_len) and (j < right_len):
        if left[i] <= right[j]:
            collection.append(left[i])
            i += 1
        else:
            collection.append(right[j])
            j += 1

    while i < left_len:
        collection.append(left[i])
        i += 1
    while j < right_len:
        collection.append(right[j])
        j += 1

    return collection
