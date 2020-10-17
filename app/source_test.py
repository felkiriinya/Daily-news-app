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
        self.new_source = Source('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Newtork that is a leader in providing news worldwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

if __name__ == '__main__':
    unittest.main()