def prime_numbers():
    with open('assets/prime-numbers.txt') as file_object:
        for line in file_object:
            value = int(line)
            yield value
