result = []
def multiples(ending):
    n = 1
    done = True
    while done:
        if n % 3 == 0 or n % 5 == 0:
            ending.append(n)
        n += 1
        if  n == 1000:
            done = False
    return(ending)

multiples(result)
print(result)
