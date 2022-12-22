import unittest
from unittest.mock import patch

from login_app import login

class TestLogin(unittest.TestCase):

##############################################################################
# USERNAME VALIDATION TESTS
##############################################################################
    
    def test_username_valid(self):
        self.assertTrue(
                login.is_valid_username(username="Bob", usernames=['Roger']))

    def test_username_invalid_exact_match(self):
        self.assertFalse(
                login.is_valid_username(username="Roger", usernames=['Roger']))

    def test_username_invalid_case_mismatch(self):
        self.assertFalse(
                login.is_valid_username(username="roger", usernames=['Roger']))

    def test_username_invalid_null(self):
        with self.assertRaises(ValueError):
            login.is_valid_username(username="", usernames=['Roger'])


##############################################################################
# PASSWORD VALIDATION TESTS
##############################################################################
    
    def test_password_valid(self):
        self.assertTrue(login.is_valid_password(password="v@l1dP@ssw0rd"))

    def test_password_invalid_too_short(self):
        # Password must be at least 8 character
        with self.assertRaises(ValueError):
            login.is_valid_password(password="Abcd!23")

    def test_password_invalid_null(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="")

    def test_password_invalid_no_number(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="Abcdefg!")

    def test_password_invalid_no_letter(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="1234567!")

    def test_password_invalid_no_special_character(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="Abcd1234")

    def test_password_invalid_no_upper(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="abcd123!")

    def test_password_invalid_no_lower(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="ABCD123!")

    def test_password_invalid_equals_to_username(self):
        with self.assertRaises(ValueError):
            login.is_valid_password(password="ABCD123!")


##############################################################################
# PROMPT TESTS
##############################################################################
    
    def test_username_prompt_valid(self):
        with patch('builtins.input', return_value='jim'):
            self.assertEqual(login.username_prompt(), 'jim')

    def test_password_prompt_valid(self):
        with patch('builtins.input', return_value='jim'):
            self.assertEqual(login.username_prompt(), 'jim')

    def test_login_greeting(self):
        self.assertEqual(login.login_greeting(), 
                "Hello, welcome to Tomorrow. Please log in...")

if __name__=='__main__':
    unittest.main()
