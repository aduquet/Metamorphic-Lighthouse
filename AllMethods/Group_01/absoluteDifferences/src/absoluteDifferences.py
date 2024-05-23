def absoluteDifferences(z):
    if not isinstance(z, list):
        raise TypeError("Input must be a list")

    return [abs(i) if isinstance(i, (int, float)) else None for i in z]
