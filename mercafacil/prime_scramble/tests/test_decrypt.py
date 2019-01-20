from mercafacil.prime_scramble.decrypt import decrypt, decrypt_sequence


def test_decrypt_a_string(encrypted_string, decrypted_string):
    result = decrypt(encrypted_string)
    assert result == decrypted_string


def test_decrypt_a_sequence(encrypted_string, decrypted_string):
    decrypted_sequence = decrypt_sequence(encrypted_string)

    for index, item in enumerate(decrypted_sequence):
        assert item == decrypted_string[index]
