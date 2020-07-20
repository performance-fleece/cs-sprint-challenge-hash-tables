# from hashtables.ex4.hashtable import HashTable, HashTableEntry, Bucket
from hashtable import HashTable, HashTableEntry, LinkedList


results = []


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    new_capacity = len(a)
    num_table = HashTable(new_capacity)
    print(num_table.capacity)

    for item in a:
        opposite = -item
        # print(item)
        num_table.put(str(item), 0)
        if num_table.get(str(opposite)) is not None:
            results.append(abs(item))
    print(results)
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
