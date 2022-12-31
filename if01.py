def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b and a > c:
        answer = a
    elif b > c and b > a:
        answer = b
    elif c > a and c > b:
        answer = c
    return answer
print(main(1,2,4))
print(main(-1,0,-8))
print(main(5,3,2))
 

    