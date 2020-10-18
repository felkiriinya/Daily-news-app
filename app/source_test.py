import unittest
from models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('Bloomberg','Bloomberg News','Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring','bloomberg.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'Bloomberg')
        self.assertEqual(self.new_source.name,'Bloomberg News')
        self.assertEqual(self.new_source.description,'Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring')
        self.assertEqual(self.new_source.url,'bloomberg.com')
        self.assertEqual(self.new_source.category,'general')
        self.assertEqual(self.new_source.country,'U.S.A')
        self.assertEqual(self.new_source.language,'en')

if __name__ == '__main__':
    unittest.main()