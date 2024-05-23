def pooledMean(data1, data2):
    if len(data1) == 0 or len(data2) == 0:
        raise ValueError("Data sets must not be empty")

    mean1 = sum(data1) / len(data1)
    mean2 = sum(data2) / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
