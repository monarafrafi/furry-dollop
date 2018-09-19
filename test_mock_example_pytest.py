import pytest

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


class TestGetUserInternal:

    @responses.activate
    def test_get_user_mock_server(self):
        responses.add(responses.GET, 'https://randomuser.me/api', json=MOCK_USER)
        user = mock_example.get_user()
        assert isinstance(user, mock_example.User)
        assert user.firstname == 'mona'
        assert user.lastname == 'rafrafi'
        assert user.gender == 'female'
        assert user.email == 'mona.rafrafi@example.com'
        assert user.username == 'greenladybug656'

    @responses.activate
    def test_get_user_not_found(self):
        responses.add(responses.GET, 'https://randomuser.me/api', status=404)
        with pytest.raises(mock_example.HttpNotFound):
            mock_example.get_user()

    @responses.activate
    def test_get_user_server_is_unreachable(self):
        # By default, with responses, we have a connexion error by default
        with pytest.raises(mock_example.APIUnreachableException):
            mock_example.get_user()


class TestGetUser:

    def test(self, mocker):
        # from mock_example import get_user, User
        mocker.patch('mock_example.get_user', return_value=mock_example.User.create_from_api(MOCK_USER))
        user = mock_example.get_user()
        assert user.firstname == 'mona'

