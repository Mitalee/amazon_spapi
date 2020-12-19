import os

SERVER_NAME = None

# required for session variables
SECRET_KEY = 'insecurekeyfordev'

SPAPI_APP_ID=os.getenv('SPAPI_APP_ID')
SPAPI_CLIENT_ID=os.getenv('SPAPI_CLIENT_ID')
SPAPI_CLIENT_SECRET=os.getenv('SPAPI_CLIENT_SECRET')


SPAPI_REDIRECT_URI = 'https://34b3dfc6c2b3.ngrok.io/Gcallback'
SPAPI_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
SPAPI_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
SPAPI_USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
SPAPI_API_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile+https://www.googleapis.com/auth/userinfo.email'
