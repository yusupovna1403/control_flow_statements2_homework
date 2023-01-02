def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    d1 = n % 10
    n//=10
    d2 = n % 10
    n//=10
    d3 = n % 10
    n//=10
    d4 = n % 10
    n//=10
    d5 = n % 10
    max = d1
    if d2 > max:
        max = d2
    if d3 > max:
        max = d3
    if d4 > max:
        max = d4
    if d5 > max:
        max =  d5
    return max
print(main(23546))
print(main(76514))
