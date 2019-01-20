import pytest


@pytest.fixture
def first_5_prime_numbers():
    return [2, 3, 5, 7, 11]


@pytest.fixture
def encrypted_string():
    return 'cqil}##$E3.79>AuKEXMMXW_mt8{u'


@pytest.fixture
def decrypted_string():
    return 'anderson.slompo@mercafacil.me'
