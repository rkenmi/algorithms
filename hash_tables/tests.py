import unittest

from hash_tables.LRUCache import LRUCache, LRUCacheSlow, LRUCacheFast


class LRUCacheD(unittest.TestCase):
    def test_delete(self):
        for cls in (LRUCache, LRUCacheSlow, LRUCacheFast):
            d = cls(capacity=5)
            d.put('Rogers', 4.0)
            d.put('Bill', 3.2)
            self.assertEqual(True, d.delete('Bill'))
            self.assertEqual(False, d.delete('Bill'))

    def test_get_put(self):
        for cls in (LRUCache, LRUCacheSlow, LRUCacheFast):
            d = cls(capacity=5)
            d.put('Rogers', 4.0)
            d.put('Bill', 3.2)
            d.put('Tony', 1.8)
            d.put('Durant', 2.5)
            d.put('Kappa', 3.8)
            d.put('James', 3.0)
            d.put('John', 3.9)
            d.put('Gabe', 2.1)
            self.assertEqual(None, d.get('Rogers'))
            self.assertEqual(2.5, d.get('Durant'))
            self.assertEqual(2.1, d.get('Gabe'))

            if getattr(d, '_reset_counter', None):
                d._reset_counter()
                for v in d._d.values():
                    self.assertLess(v.index, 5)



if __name__ == '__main__':
    unittest.main()
