import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_cors import CORS
import json
from models import db_drop_and_create_all, setup_db, Movie, Actor
from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    db = SQLAlchemy(app)
    CORS(app)


        #####################
        #       Actor       #
        #####################

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.all()
            actors = [actor.format() for actor in actors]
            return jsonify({
                'success': True,
                'actors': actors
            }), 200

        except:
            abort(404)


    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(payload):

        body = request.get_json()

        if not ('name' in body ):
            abort(422)
        
        try:
            name = body.get('name')
            age = body.get('age')
            gendre = body.get('gendre')

            actor = Actor(name=name, age=age, gendre=gendre)

            actor.insert()

            actor = Actor.query.filter_by(name=name).first()
            return jsonify({
                'success': True,
                'actors': actor.format()
            }), 200
        except:
            abort(500)


    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(payload, id):

        actor = Actor.query.filter_by(id=id).first()
        
        if not actor:
            abort(404)

        try:
            body = request.get_json()

            name = body.get('name')
            age = body.get('age')
            gendre = body.get('gendre')

            if name:
                actor.name = name
            if age:
                actor.age = age
            if name:
                actor.gendre = gendre

            actor.update()  
                
            return jsonify({
                'success': True,
                'actors': [actor.format()]
            }), 200
        except:
            abort(422)

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload, id):
        
        actor = Actor.query.filter_by(id=id).first()

        if not actor:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                'success': True,
                'delete': id
            }), 200
        except:
            abort(422)


            #####################
            #       Movie       #
            #####################

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.all()
            movies = [movie.format() for movie in movies]
            return jsonify({
                'success': True,
                'movies': movies
            }), 200

        except:
            abort(404)


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):

        body = request.get_json()

        if not ('title' in body and 'genre' in body):
            abort(422)
        
        try:
            title = body.get('title')
            genre = body.get('genre')

            movie = Movie(title=title, genre=genre)

            movie.insert()

            movie = Movie.query.filter_by(title=title).first()
            return jsonify({
                'success': True,
                'actors': movie.format()
            }), 200
        except:
            abort(500)


    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(payload, id):

        movie = Movie.query.filter_by(id=id).first()
        
        if not movie:
            abort(404)

        try:
            body = request.get_json()
            
            title = body.get('title')
            genre = body.get('genre')

            if title:
                movie.title = title
            if genre:
                movie.genre = genre

            movie.update()  
                
            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200
        except:
            abort(422)

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload, id):
        
        movie = Movie.query.filter_by(id=id).first()

        if not movie:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                'success': True,
                'delete': id
            }), 200
        except:
            abort(422)


    # Error Handling
    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':400,
            'message':'Bad request'
        }), 400

    @app.errorhandler(404)
    def notfound(error):
        return jsonify({
            'success':False,
            'error':404,
            'message':'Resource not found'
        }), 404

    @app.errorhandler(405)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':405,
            'message':'Method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':422,
            'message':'Unprocessable entity'
        }), 422

    @app.errorhandler(500)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':500,
            'message':'Internal server error'
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code


    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
