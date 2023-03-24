import os
import unittest
from app import db, models
import md5
addTest = models.Users(username="testname", password="Password")

def logIn(user,password):
    for users in models.Users.query.all():
        if users.username == user\
            and users.password == password:
            return True
    return False

class TestCase(unittest.TestCase):
    def setUp(self):
        db.session.add(addTest)
    def tearDown(self):
        db.session.delete(addTest)
    def test_successful_login(self):
        assert logIn("testname", "Password") == True
    def test_wrong_username(self):
        assert logIn("fakename", "Password") == False
    def test_wrong_password(self):
        assert logIn("testname", "Password123") == False

if __name__ == '__main__':
    unittest.main()
