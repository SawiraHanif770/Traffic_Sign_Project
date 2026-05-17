import unittest
import os

class TestProject(unittest.TestCase):

    def test_model_exists(self):
        self.assertTrue(os.path.exists("models/best_model.h5"))

    def test_data_folder_exists(self):
        self.assertTrue(os.path.exists("data"))

if __name__ == '__main__':
    unittest.main()