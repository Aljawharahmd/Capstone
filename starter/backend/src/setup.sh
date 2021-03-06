export AUTH0_DOMAIN='<AUTH0_DOMAIN>'
export AUTH0_CLIENTID='<AUTH0_CLIENTID>'
export AUTH0_CALLBACK_URL='<AUTH0_CALLBACK_URL>'
export AUTH0_CLIENT_SECRET='<AUTH0_CLIENT_SECRET>'
export AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
export AUTH0_AUDIENCE='<AUTH0_AUDIENCE>'
export API_AUDIENCE='<API_AUDIENCE>'
export FLASK_APP=app.py
export FLASK_DEBUG=true
export DATABASE_URL='postgresql://postgres:13ad@localhost:5432/capstone'

flask run --reload