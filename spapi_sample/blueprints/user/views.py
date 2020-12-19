from flask import (
    Blueprint,
    redirect,
    request,
    url_for,
    render_template,
    current_app,
    jsonify,
    session
    )

import requests

user = Blueprint('user', __name__, template_folder='templates')



@user.route('/viewvar')
def view_var():
    print('CLIENT ID: ', current_app.config.get('GOOGLE_CLIENT_ID'))
    print('CLIENT SECRET: ', current_app.config.get('GOOGLE_CLIENT_SECRET'))
    print('GOOGLE AUTH URI: ', current_app.config.get('GOOGLE_AUTH_URI'))

@user.route('/')
def index():
    return ('Hello from the cookie cutter flask app! Please <a href="/login">Login</a>')

@user.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('user/login.html')


@user.route('/Gauthorize', methods=['GET', 'POST'])
def authorize_google():

    client_id = current_app.config.get('GOOGLE_CLIENT_ID')
    authorize_url = current_app.config.get('GOOGLE_AUTH_URI')
    callback_uri = current_app.config.get('GOOGLE_REDIRECT_URI')
    scope = current_app.config.get('GOOGLE_API_SCOPE')
    
    ## 1. Prepare the authorization URL, which will ping the callback URL with the authorization code.
    authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope='+scope

    print ("AUTH REDIRECT URL IS:  " + authorization_redirect_url)
    return redirect(authorization_redirect_url)


@user.route('/Gcallback')
def callback_google():
    ## 2. Get the authorization code
    authorization_code = request.args.get("code")
    print("CODE: ", authorization_code)

    client_id = current_app.config.get('GOOGLE_CLIENT_ID')
    client_secret = current_app.config.get('GOOGLE_CLIENT_SECRET')
    callback_uri = current_app.config.get('GOOGLE_REDIRECT_URI')
    token_url = current_app.config.get('GOOGLE_TOKEN_URI')
    user_info_url = current_app.config.get('GOOGLE_USER_INFO')
    ## 4. Prepare the token URL, pass the authorization code and request for the access_token
    data = {'grant_type': 'authorization_code', 
            'code': authorization_code, 
            'redirect_uri': current_app.config.get('GOOGLE_REDIRECT_URI')}

    print ("requesting access token")

    ## 5. Post the request for the access_token.
    access_token_response = requests.post(current_app.config.get('GOOGLE_TOKEN_URI'), data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

    ''' EXAMPLE HEADERS OF access_token_response
    {'Pragma': 'no-cache', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Date': 'Sun, 13 Dec 2020 13:42:09 GMT', 'Expires': 'Mon, 01 Jan 1990 00:00:00 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Vary': 'Origin, X-Origin, Referer', 'Content-Encoding': 'gzip', 'Server': 'scaffolding on HTTPServer2', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'X-Content-Type-Options': 'nosniff', 'Alt-Svc': 'h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Transfer-Encoding': 'chunked'}
    '''
    print ("Access TOken response HEADERS ", access_token_response.headers)
    
    ''' EXAMPLE BODY OF access_token_response
        {
          "access_token": "ya29.a0AfH6SMCvf7_eFHlwQyLdAjDNv2IQUC2cZxNAgHUf1jMHg37lSojM8A2hAprWC_MQo53N7GnSDov6uKvWOsA3Qcm-2ShISUXJHgIjE7B1NTK_wBxrbdAimXs3CF2QrRh7UXAfE",
          "expires_in": 3598,
          "scope": "openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email",
          "token_type": "Bearer",
          "id_token": "eyJhbGciOiJSzA1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMjY4Mjk0ODg44B5dY8JIpqmUwpCLlpe9MuaKSzXx0kA3nsUDDZtETrQ6zJX4W3Hq78mNF4UeHtEwqcYGqVXxvXuKVe9517gD9Bpx5ad7ds_ITftKxgQbkejKi_v0Jrv53ycXuZO6rLTY0Rn7yOsSJNxQChO5R4y12aCrS-GPTECy7giZy5egZGS093or1du3v1Po5oNg3XyBw"
        }
    '''
    print ('body: ' + access_token_response.text)

    ## 6. Use the response from the previous POST request to access the json returned by Google and load the access_token.
    tokens = access_token_response.json()
    access_token = tokens['access_token']
    print ("access token: " + access_token)

    ## 7. Use the access_token to get the user's email and other details (name, etc.)
    api_call_headers = {'Authorization': 'Bearer ' + access_token}
    api_call_response = requests.get(current_app.config.get('GOOGLE_USER_INFO'), headers=api_call_headers, verify=False)


    ''' sample json of user_info
    {'id': 'xxx', 'email': 'mmitalee@gmail.com', 'verified_email': True, 'name': 'Mitalee Mulpuru', 'given_name': 'Mitalee', 'family_name': 'Mulpuru', 'picture': 'https://lh3.googleusercontent.com/xxxxc', 'locale': 'en'}
    '''
    user_info = api_call_response.json()

    print (user_info)
    session['user_info'] = user_info
    print('G Is:', session['user_info'])
    ## 8. Encrypt the access_token and refresh_token 
    ## 9.Store the access_token, refresh_token and email in the database.

    return redirect(url_for('user.home'))
    # return render_template('user/welcome.html', user_info=user_info)


@user.route('/home')
def home():
    print('user info: ', session['user_info'])
    return render_template('user/welcome.html', user_info=session['user_info'])
    



