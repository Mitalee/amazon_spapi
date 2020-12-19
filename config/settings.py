import os

SERVER_NAME = None

# required for session variables
SECRET_KEY = 'insecurekeyfordev'

SPAPI_APP_ID=os.getenv('SPAPI_APP_ID')
SPAPI_CLIENT_ID=os.getenv('SPAPI_CLIENT_ID')
SPAPI_CLIENT_SECRET=os.getenv('SPAPI_CLIENT_SECRET')


SPAPI_REDIRECT_URI = 'https://c89f0ea6c0d7.ngrok.io/AMZSPAPIcallback'
SPAPI_AUTH_URI = 'https://sellercentral.amazon.in/apps/authorize/consent'
SPAPI_TOKEN_URI = 'https://api.amazon.com/auth/o2/token'
