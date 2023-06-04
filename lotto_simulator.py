import random


# ta funkcja pobiera od użytkownika 6 liczb z inputu, sprawdza ich poprawność,
# obecność w zakresie i to czy się nie powtarzają
def get_guessed_numbers():
    """
    This function returns a sorted list of numbers from input, typed in by the user
    :param: int
    :return: list
    """
    guessed_numbers = []
    while len(guessed_numbers) != 6:
        try:
            input_number = int(input("Type a number in range 1 to 49: "))
            if input_number not in guessed_numbers and 49 >= input_number >= 1:
                guessed_numbers.append(input_number)
            elif input_number in guessed_numbers:
                print("Type in different number!")
        except ValueError:
            print("It's not a number!")
            input_number = int(input("Type a number in range 1 to 49: "))
            if input_number not in guessed_numbers and 49 >= input_number >= 1:
                guessed_numbers.append(input_number)
            elif input_number in guessed_numbers:
                print("Type in different number!")
    return sorted(guessed_numbers)


picked_numbers = get_guessed_numbers()

print(f"Your picks are: {picked_numbers}")

# losuję 6 liczb w zakresie od 1 do 49 włącznie i dodaję je na listę random_numbers
random_numbers = []
while len(random_numbers) != 6:
    random_number = random.randint(1, 49)
    if random_number not in random_numbers:
        random_numbers.append(random_number)
    else:
        pass

print(f"Drawn numbers are: {random_numbers}")


# funkcja opisująca wynik - dla każdej trafionej liczby wartość parametru numbers_correct zwiększa się o jeden.
# Powyżej 3 -> gracz zostanie poinformowany o tym, że wygrał.
def result():
    """
    This function returns a value of numbers repeating from draw and guess
    :param: int
    :return: int
    """
    for number in picked_numbers:
        numbers_correct = 0
        if number in random_numbers:
            numbers_correct += 1
        return numbers_correct


print(f"You guessed {result()} numbers right")

if result() > 3:
    print("You won!")

if __name__ == '__main__':
    result()
