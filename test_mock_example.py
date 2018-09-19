from unittest import mock
import unittest

import responses
# Attention, si on importe la fonction
import mock_example# import get_user, HttpNotFound, User, APIUnreachableException

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


class GetUserInternalTestCase(unittest.TestCase):

    @responses.activate
    def test_get_user_mock_server(self):
        responses.add(responses.GET, 'https://randomuser.me/api', json=MOCK_USER)
        user = mock_example.get_user()
        self.assertIsInstance(user, mock_example.User)
        self.assertEqual(user.firstname, 'mona')
        self.assertEqual(user.lastname, 'rafrafi')
        self.assertEqual(user.gender, 'female')
        self.assertEqual(user.email, 'mona.rafrafi@example.com')
        self.assertEqual(user.username, 'greenladybug656')

    @responses.activate
    def test_get_user_not_found(self):
        responses.add(responses.GET, 'https://randomuser.me/api', status=404)
        with self.assertRaises(mock_example.HttpNotFound):
            mock_example.get_user()

    @responses.activate
    def test_get_user_server_is_unreachable(self):
        # By default, with responses, we have a connexion error by default
        with self.assertRaises(mock_example.APIUnreachableException):
            mock_example.get_user()


class GetUserTestCase(unittest.TestCase):

    @mock.patch('mock_example.get_user')
    def test(self, my_mock_test_user):
        # from mock_example import get_user, User
        my_mock_test_user.return_value = mock_example.User.create_from_api(MOCK_USER)
        user = mock_example.get_user()
        self.assertEqual(user.firstname, 'mona')

