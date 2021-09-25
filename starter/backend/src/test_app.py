import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "capstone_test"
        # self.database_path = "postgres://{}/{13ad}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


        #####################
        #       Actor       #
        #####################


        # ---    Get     --- #

    def test_success_retrieve_actors(self):
        res = self.client().get('/actors',headers=casting_assistent)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_failure_retrieve_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Needs a Permission)


        # ---    Post     --- #

    def test_success_create_actors(self):
        post_data = {
            'name': 'John',
            'age': '46',
            'gender': 'Male'
        }

        res = self.client().post('/actors', json=post_data,headers=casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
  
    def test_failure_create_actors(self):
        post_data = {
            'name': 'John',
            'age': '46',
        }

        res = self.client().post('/actors', json=post_data,headers=casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Unprocessable')


        # ---    Patch     --- #

    def test_success_patch_actors(self):
        patch_actor = {
            'name': 'Mark'
        }
        res = self.client().patch('/actors/1',json=patch_actor,headers=casting_director)
        data = json.loads(respresonse.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_failure_patch_actors(self):
        res = self.client().patch('/actors/1',headers=casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)


        # ---    Delete     --- #

    def test_success_delete_actors(self):
        res = self.client().delete('/actors/1',headers=casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_failure_delete_actors(self):
        res = self.client().delete('/actors/1',headers=casting_assistent)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Needs a Permission')

        #####################
        #       Movie       #
        #####################

        # ---    Get     --- #
        
        def test_success_retrieve_movies(self):
        res = self.client().get('/movies',headers=casting_assistent)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_failure_retrieve_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Needs a Permission')

        # ---    Post     --- #
    def test_success_create_movies(self):
        post_data = {
            'title': 'Everybody',
            'genre': 'Action'
        }

        res = self.client().post('/movies', json=post_data,headers=executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
  
    def test_failure_create_movies(self):
        post_data = {
            'title': 'Everybody'
        }

        res = self.client().post('/movies', json=post_data,headers=executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Unprocessable')


        # ---    Patch     --- #

    def test_success_patch_movies(self):
        patch_movie = {
            "title": "Nobody"
        }
        res = self.client().patch('/movies/1',json=patch_movie,headers=casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_failure_patch_movies(self):
        res = self.client().patch('/movies/1',headers=casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)


        # ---    Patch     --- #

    def test_success_delete_movies(self):
        res = self.client().delete('/movies/1',headers=executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_failure_delete_movies(self):
        res = self.client().delete('/movies/1',headers=casting_assistent)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'Needs a Permission')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()