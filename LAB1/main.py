# ++++++++++++
# Zadanie 1
# ++++++++++++


def n_surname_dot(n: str, surname: str):
    return n + ". " + surname

# ++++++++++++
# Zadanie 2
# ++++++++++++


def name_surname_dot(name: str, surname: str):
    return name[0].upper() + ". " + surname[0].upper() + surname[1:len(surname)].lower()

# ++++++++++++
# Zadanie 3
# ++++++++++++


def birth_year(yy1: int, yy2: int, age: int):
    return yy1 * 100 + yy2 - age

# ++++++++++++
# Zadanie 4
# ++++++++++++


def name_surname_dot2(name: str, surname: str, fun):
    return fun(name, surname)

# ++++++++++++
# Zadanie 5
# ++++++++++++


def div(x: int, y: int):
    if (x > 0) and (y > 0) and (y != 0):
        return x / y
    else:
        return "The input did not meet the requirements."

# ++++++++++++
# Zadanie 6
# ++++++++++++


result = 0
while result < 100:
    result += int(input(f"Aktualny wynik: {result}. Podaj liczbę: "))

# ++++++++++++
# Zadanie 7
# ++++++++++++


def list_to_tuple(alist):
    return tuple(alist)

# ++++++++++++
# Zadanie 8
# ++++++++++++


list_a = []
length = int(input("Number of elements: "))
for i in range(length):
    list_a.append(input(f"Element {i}: "))
list_a = tuple(list_a)
print(list_a)


# ++++++++++++
# Zadanie 9
# ++++++++++++


def weekday(num: int):
    dni = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    try:
        return dni[num-1]
    except IndexError:
        return "Podaj liczbe z zakresu 1 - 7"


# ++++++++++++
# Zadanie 10
# ++++++++++++

def palindrome(astr):
    for n in range(len(astr)//2):
        if astr[n].lower() != astr[-1 - n].lower():
            return False
    else:
        return True

# ++++++++++++
# Test
# ++++++++++++


print(n_surname_dot("J", "Kowalski"))
print(name_surname_dot("jAN", "kOWALski"))
print(birth_year(20, 22, 31))
print(name_surname_dot2("aNNA", "NoWAK", name_surname_dot))
print(div(3, 7))
print(div(2, 0))
print(div(-3, 6))
print(list_to_tuple([3, 5, 7, "Gosia", 3 + 2j]))
print(weekday(3))
print(weekday(47))
print(palindrome("Arrgrra"))
