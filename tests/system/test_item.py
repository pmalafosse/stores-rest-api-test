from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel("test", "1234").save_to_db()
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = 'JWT ' + auth_token

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test')
                self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                header = {'Authorization': self.access_token}
                resp = client.get('/item/test', headers=header)
                self.assertEqual(resp.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                ItemModel("test", 19.99, 1).save_to_db()
                header = {'Authorization': self.access_token}
                resp = client.get('/item/test', headers=header)
                self.assertEqual(resp.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                ItemModel("test", 19.99, 1).save_to_db()
                resp = client.delete('/item/test')
                self.assertEqual(resp.status_code, 200)

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                resp = client.post('/item/test', data={'store_id': 1, 'price': 19.99})
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(ItemModel.find_by_name('test').name, 'test')

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                ItemModel("test", 19.99, 1).save_to_db()
                resp = client.post('/item/test', data=json.dumps({'store_id': 1, 'price': 19.99}))
                self.assertEqual(resp.status_code, 400)

    def test_put_item(self):
        pass

    def test_put_update_item(self):
        pass

    def test_item_list(self):
        pass