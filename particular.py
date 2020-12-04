def getN(s: str):
    n = int(input(s))
    if n % 2 == 0 and n > 0:
        return n
    else:
        return getN(s)


def permutations(numbers: list, pos: int = 0):
    if pos == len(numbers):
        return verifylist(numbers)
    j = pos
    do = True
    while j < len(numbers) and do:
        numbers[j], numbers[pos] = numbers[pos], numbers[j]
        permutations(numbers, pos + 1)
        numbers[j], numbers[pos] = numbers[pos], numbers[j]
        j += 1
        if pos == 0 and numbers[j] != 1:
            do = False


def verifylist(Numbers: list, c: int = 0):
    l = len(Numbers)
    allprime = True  # Optimus prime :D... Just kidding.
    if c == l - 1:
        allprime = primepair(Numbers[c], Numbers[0])
    else:
        allprime = primepair(Numbers[c], Numbers[c + 1])
    if allprime and c < l - 1:
        return verifylist(Numbers, c + 1)
    else:
        if allprime:
            print(*Numbers)  # Putting a * before a list call, makes it print without [] and replaces ',' with blank spaces
        return allprime


def isprime(number: int, c: int = 2):
    if number <= 1:
        return False  # Exception in 1 or minus, 1 isnt a prime number
    elif number == 2:  # Exception in 2
        return True
    elif number - 1 == c and number % c != 0:  # Is the last and isnt a factor of the number
        return True
    elif number % c == 0:  # Isnt a prime number because there is a factor between 2 ... n-1
        return False
    else:
        return isprime(number, c + 1)  # Continue loop


def primepair(a: int, b: int):
    r = a + b
    return isprime(r)


n = getN("Inserte un numero entero positivo y par")
comb = [i for i in range(1, n + 1)]
permutations(comb)