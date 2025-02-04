"""
Tests for Twittersa

Jesse Mu
"""

import twittersa
import unittest
import pickle  # Standard pickle for unicode support


DATA_SOURCES = [
    'lib/noslang.pickle'
    'lib/stopwords.pickle'
]


class TwittersaTestCase(unittest.TestCase):
    def setUp(self):
        twittersa.app.config['TESTING'] = True
        self.app = twittersa.app.test_client()

    def tearDown(self):
        pass

    def test_twitter_api(self):
        """Test to make sure the API is getting tweets"""
        tweets = twittersa.api.search(q='hello')
        assert tweets and len(tweets)

    def test_invalid_search_query(self):
        """Test for invalid search queries"""
        rv = self.app.get('/search?q=')
        assert 'Invalid search query' in rv.data
        rv = self.app.get('/search?nonsense=nonsense')
        assert 'Invalid search query' in rv.data

    def test_invalid_user_id(self):
        """Test for invalid user ids"""
        rv = self.app.get('/user?username=')
        assert 'Invalid username' in rv.data
        rv = self.app.get('/user?nonsense=nonsense')
        assert 'Invalid username' in rv.data

    def test_data_sources(self):
        """Test to make sure data sources exist and can be loaded"""
        for filename in DATA_SOURCES:
            with open(filename, 'r') as f:
                data = pickle.load(f)
                assert data

if __name__ == '__main__':
    unittest.main()
