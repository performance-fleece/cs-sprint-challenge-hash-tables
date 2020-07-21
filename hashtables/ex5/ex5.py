# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    directory = dict()
    result = []

    for i in files:
        path = i
        path_split = i.split("/")
        filename = path_split[-1]

        if filename in directory:
            old_record = directory[filename]
            old_record.append(path)
        else:
            directory[filename] = [i]

    for q in queries:
        if q in directory:
            result.extend(directory[q])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
