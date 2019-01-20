import pytest

from mercafacil.prime_scramble import main


def test_main_with_arguments(encrypted_string):
    main(encrypted_string)  # It simply should not throw an Exception...


def test_main_without_arguments():
    with pytest.raises(SystemExit) as ex:
        main()
    assert ex.value.code == 1


def test_main_with_empty_string():
    with pytest.raises(SystemExit) as ex:
        main('')
    assert ex.value.code == 1
