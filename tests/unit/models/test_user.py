from tests.unit.unit_base_test import UnitBaseTest
from models.user import UserModel

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel("jose", "1234")

        self.assertEqual(user.username, 'jose')
        self.assertEqual(user.password, '1234')