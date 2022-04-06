def mdc(x, y):
    
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd

if __name__ == "__main__":
    x = int(input("x: "))
    y = int(input("y: "))
    print(f"{mdc(x, y)=}")
