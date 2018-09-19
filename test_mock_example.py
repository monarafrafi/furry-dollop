from mock_example import get_user, HttpNotFound, User, APIUnreachableException
import unittest


class GetUserTestCase(unittest.TestCase):

    def test_get_user_works(self):
        user = get_user()
        self.assertIsInstance(user, User)

    @unittest.skip('not implemented')
    def test_get_user_not_found(self):
        with self.assertRaises(HttpNotFound):
            user = get_user()

    @unittest.skip('not implemented')
    def test_get_user_server_is_unreachable(self):
        with self.assertRaises(APIUnreachableException):
            user = get_user()






