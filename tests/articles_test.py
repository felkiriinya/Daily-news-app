import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Bloomberg','Peter Polle','The tech scene in Africa-Is it the next big thing?','A look at various tech hubs in Africa and the impact they have on the worlds economy','techie.com','techie.com/7643t94.jpg','2018-04-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_article.id,'Bloomberg')
        self.assertEqual(self.new_article.author,'Peter Polle')
        self.assertEqual(self.new_article.title,'The tech scene in Africa-Is it the next big thing?')
        self.assertEqual(self.new_article.description,'A look at various tech hubs in Africa and the impact they have on the worlds economy')
        self.assertEqual(self.new_article.url,'techie.com')
        self.assertEqual(self.new_article.image,'techie.com/7643t94.jpg')
        self.assertEqual(self.new_article.date,'2018-04-11T07:57:16Z')

# if __name__ == '__main__':
#     unittest.main()        