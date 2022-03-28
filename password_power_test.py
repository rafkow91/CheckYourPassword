from password_power import StrongPassword

test_password1 = StrongPassword('1@Za-1@Za')    # all requirements met
test_password2 = StrongPassword('1qaZx@')       # too short
test_password3 = StrongPassword('!qazZsw@#')    # without number
test_password4 = StrongPassword('1qazZ123')     # without special char
test_password5 = StrongPassword('1qazxasd@')    # without upper letter
test_password6 = StrongPassword('1ASVXJKZXH&@')  # without lower letter


def test_has_acceplable_length():
    assert test_password1._has_acceptable_length() == True
    assert test_password2._has_acceptable_length() == False
    assert test_password3._has_acceptable_length() == True
    assert test_password4._has_acceptable_length() == True
    assert test_password5._has_acceptable_length() == True
    assert test_password6._has_acceptable_length() == True


def test_has_number():
    assert test_password1._has_number() == True
    assert test_password2._has_number() == True
    assert test_password3._has_number() == False
    assert test_password4._has_number() == True
    assert test_password5._has_number() == True
    assert test_password6._has_number() == True


def test_has_special_sign():
    assert test_password1._has_special_sign() == True
    assert test_password2._has_special_sign() == True
    assert test_password3._has_special_sign() == True
    assert test_password4._has_special_sign() == False
    assert test_password5._has_special_sign() == True
    assert test_password6._has_special_sign() == True


def test_has_lower_and_upper_letters():
    assert test_password1._has_lower_and_higher_letter() == True
    assert test_password2._has_lower_and_higher_letter() == True
    assert test_password3._has_lower_and_higher_letter() == True
    assert test_password4._has_lower_and_higher_letter() == True
    assert test_password5._has_lower_and_higher_letter() == False
    assert test_password6._has_lower_and_higher_letter() == False


def test_validate():
    assert test_password1.validate() == True
    assert test_password2.validate() == False
    assert test_password3.validate() == False
    assert test_password4.validate() == False
    assert test_password5.validate() == False
    assert test_password6.validate() == False


def test_check_strong():
    assert test_password1.check_strong() == 100
    assert test_password2.check_strong() == 75
    assert test_password3.check_strong() == 75
    assert test_password4.check_strong() == 75
    assert test_password5.check_strong() == 75
    assert test_password6.check_strong() == 75

    test_password7 = StrongPassword('asd')
    assert test_password7.check_strong() == 0

    test_password8 = StrongPassword('asd1')
    assert test_password8.check_strong() == 25
    
