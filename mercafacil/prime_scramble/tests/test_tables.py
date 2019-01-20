from mercafacil.prime_scramble.tables import prime_numbers


def test_prime_numbers_table(first_5_prime_numbers):
    prime_numbers_sample = tuple(prime_numbers())[0:5]

    for index, item in enumerate(prime_numbers_sample):
        assert item == first_5_prime_numbers[index]
