def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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
    ans = 1
    if d2 > max:
        max = d2
        ans = 2
    if d3 > max:
        max = d3
        ans = 3
    if d4 > max:
        max = d4
        ans = 4
    if d5 > max:
        max =  d5
        ans = 5
    return ans
print(main(23546))
print(main(76514))
