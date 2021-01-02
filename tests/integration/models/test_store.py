from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel("test")

        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test_store')

            self.assertIsNone(StoreModel.find_by_name('test_store'),
                              "Found an item with name {}, but expected not to.".format(store.name))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test_store'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test_store'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("test_store")
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.all(), [item])

    def test_store_json(self):
        with self.app_context():
            store = StoreModel("test_store")
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': "test_store",
                'items': [
                    {
                        'name': 'test',
                        'price': 19.99
                    }
                ]
            }
            self.assertDictEqual(store.json(), expected)