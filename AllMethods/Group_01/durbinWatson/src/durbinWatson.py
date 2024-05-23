def durbinWatson(data):
    if not data:  # check if data is empty
        raise ValueError("Input data should not be empty")

    run = 0
    run_sq = data[0] ** 2

    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]
        run += diff ** 2
        run_sq += data[i] ** 2

    return run / run_sq
