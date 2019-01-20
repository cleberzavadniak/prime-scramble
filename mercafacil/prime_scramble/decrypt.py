from .constants import *  # NOQA
from .tables import prime_numbers


def decrypt_sequence(source):
    """
    Given a `source` sequence, returns a generator that
    yield decrypted values for each correspondent item in
    that sequence.
    """

    # "Listify" parameters **IS** an official recommendation
    # and, yes, it makes a lot of sense when you think about
    # it...
    source = tuple(source)

    normalized_higher_limit = HIGHER_LIMIT - LOWER_LIMIT

    for index, prime_number in enumerate(prime_numbers()):
        try:
            current_char = source[index]
        except IndexError:
            break

        value = ord(current_char)
        normalized_value = value - prime_number - LOWER_LIMIT
        normalized_result = normalized_value % (normalized_higher_limit + 1)

        denormalized_value = LOWER_LIMIT + normalized_result
        decrypted_char = chr(denormalized_value)

        yield decrypted_char


def decrypt(source):
    """
    Given a `source` sequence (most probably a str object),
    returns a str object in which each character is the
    correspondent decrypted value of that sequence.
    The `source` items must be valid parameters to the
    `ord` function (for example: str characters).
    """
    return ''.join(decrypt_sequence(source))
