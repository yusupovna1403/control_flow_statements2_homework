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
        ans = d2
    if d3 > d1:
        ans = d3
    if d4 > d1:
        ans = d4
    if d5 > d1:
        ans =  d5
    else:
        ans = d1
    return ans
print(main(23546))
print(main(76514))
