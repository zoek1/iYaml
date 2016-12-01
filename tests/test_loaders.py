import unittest
import iyaml.loaders as l


class TestRawResources(unittest.TestCase):
    def test_if_one_directory_is_a_valid_yaml_file(self):
        self.assertFalse(l.isyamlfile('.'))

    def test_if_non_existing_file_is_a_valid_yaml_file(self):
        self.assertFalse(l.isyamlfile("random.yml"))

    def test_if_one_yaml_file_resource_is_a_valid_yaml_file(self):
        self.assertTrue(l.isyamlfile('examples/basic.yml'))



class TestFileCollector(unittest.TestCase):
    def test_if_directory_no_collect_yaml_files(self):
        self.assertEqual(l.collect_resources('test'), {})

        self.assertEqual(l.collect_resources('/tmp'), {})


    def test_if_directory_collect_yaml_files(self):
        self.assertEqual(len(l.collect_resources('examples').keys()), 1)
        self.assertEqual(len(l.collect_resources('examples').values()), 1)


class TestKeyBuilder(unittest.TestCase):
    @unittest.skip("Need flat_hases, normalize_keys and get_all_kv implementation")
    def test_if_given_a_path_build_correct_keys(self):
        self.assertEqual(l.build_keys('examples'), {'basic.msg': "Hola mundo"})


class TestBinder(unittest.TestCase):
    @unittest.skip("requires storage and key builder")
    def test_if_key_and_storage_share_same_value():
        pass

if __name__ == '__main__':
    unittest.main()
