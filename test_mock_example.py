import responses
from mock_example import get_user, HttpNotFound, User, APIUnreachableException
import unittest

MOCK_USER = {
    'results': [
        {
            'gender': 'female',
            'name': {
                'title': 'mrs',
                'first': 'mona',
                'last': 'rafrafi'
            },

            'email': 'mona.rafrafi@example.com',
            'login': {
                'username': 'greenladybug656'
            },
        }
]
}


class GetUserTestCase(unittest.TestCase):

    @responses.activate
    def test_get_user_mock_server(self):
        responses.add(responses.GET, 'https://randomuser.me/api', json=MOCK_USER)
        user = get_user()
        self.assertIsInstance(user, User)
        self.assertEqual(user.firstname,'mona')
        self.assertEqual(user.lastname, 'rafrafi')
        self.assertEqual(user.gender, 'female')
        self.assertEqual(user.email, 'mona.rafrafi@example.com')
        self.assertEqual(user.username, 'greenladybug656')


    @responses.activate
    def test_get_user_not_found(self):
        responses.add(responses.GET, 'https://randomuser.me/api', status=404)
        with self.assertRaises(HttpNotFound):
            user = get_user()

    @responses.activate
    def test_get_user_server_is_unreachable(self):
        # By default, with responses, we have a connexion error by default
        with self.assertRaises(APIUnreachableException):
            user = get_user()






