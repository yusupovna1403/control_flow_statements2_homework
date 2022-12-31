def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b and b > c or c > b and c > a:
        answer = b
    elif b > c and c > a  or a > c and c > b:
        answer = c
    else: 
        answer = a
    return answer
print(main(1,2,4))
print(main(-1,0,-8))
print(main(5,2,9))