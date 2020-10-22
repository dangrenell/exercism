def slices(series, length):
    if length < 1:
        raise ValueError("Length must be at least 1.")
    if length > len(series):
        raise ValueError("Length cannot be greater than series length.")
    if len(series) == 0:
        raise ValueError("Series cannot be empty.")

    result = []
    for i in range(len(series) - length + 1):
        result.append(str(series[i:i+length]))

    return result
