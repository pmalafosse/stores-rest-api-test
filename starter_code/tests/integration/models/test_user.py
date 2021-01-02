from tests.base_test import BaseTest
from models.user import UserModel


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel("test", '1234')

            self.assertIsNone(UserModel.find_by_username('test'),
                              "Found a user with name {}, but expected not to.".format(user.username))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'))
            self.assertIsNotNone(UserModel.find_by_id(1))
