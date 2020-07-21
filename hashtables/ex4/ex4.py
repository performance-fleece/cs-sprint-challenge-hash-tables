# from hashtables.ex4.hashtable import HashTable, HashTableEntry, Bucket


def has_negatives(a):
    """
    YOUR CODE HERE

    tried using hashtable, not efficient enough, fails on large arrays

    """

    results = []

    # Your code here
    # new_capacity = len(a)
    # num_table = HashTable(new_capacity)
    # print(num_table.capacity)

    # for item in a:
    #     opposite = -item
    #     # print(item)
    #     num_table.put(str(item), 0)
    #     if num_table.get(str(opposite)) is not None:
    #         results.append(abs(item))
    # print(results)
    # return results

    """
    Below uses list comprehension completes ~ 0.9s
    """
    # positive = dict()
    # negative = dict()

    # for i in a:
    #     if i > 0:
    #         positive[i] = 0
    #     if i < 0:
    #         negative[abs(i)] = 0

    # results = [key for key in positive if key in negative]

    """
    variation 2 test completes ~0.95s
    """
    data = dict.fromkeys(a, "")

    for i in a:
        opposite = -i
        if i > 0:
            if opposite in data:
                results.append(i)

    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
