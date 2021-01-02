from tests.unit.unit_base_test import UnitBaseTest

from models.store import StoreModel


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test_store')

        self.assertEqual(store.name, 'test_store',
                         "The name of the store after creation does not equal the constructor argument.")

    def test_store_json(self):
        store = StoreModel('test_store')
        expected = {
            'name': 'test_store',
            'items': []
        }

        self.assertEqual(
            store.json(),
            expected,
            "The JSON export of the store is incorrect. Received {}, expected {}.".format(store.json(), expected))
