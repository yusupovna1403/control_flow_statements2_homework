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
    
    if d2 > d1:
        return d2
    elif d3 > d1:
        return d3
    elif d4 > d1:
        return d4
    elif d5 > d1:
        return d5
    else:
        return d1
print(main(23546))
