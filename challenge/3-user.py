#!/usr/bin/python3
"""
3-user.py module
"""
import hashlib


class User:
    """User class definition"""

    def __init__(self):
        """Initialize user"""
        self.__password = None

    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, pwd):
        """Password setter with MD5 hashing"""
        if not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """Validates if the provided password matches the stored hash"""
        if not isinstance(pwd, str) or self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == "__main__":
    # Test cases
    u = User()
    u.password = "Holberton"
    print(u.password)
    print(u.is_valid_password("Holberton"))
