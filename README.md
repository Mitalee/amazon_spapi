# Description

Without adding additional libraries, this simple user blueprint allows for spapi OAuth2 Login, to be added to existing Flask apps with minimal effort. It follows the app factory pattern which imports this blueprint, and seamlessly allows the **Login with Google->authorize->welcome** flow.

The only dependency is the requests module (apart from Flask, of course).

## 1. How to set up your SPAPI app and credentials:


## 2. Setting up the flask cookie cutter application
1. The main directory has to have an app. This is `spapi_sample`.  
2. Within this sample app, we will have the `app.py` file and `blueprints` folder that will house the blueprints and the main app creation function. We also create an `__init__.py` file in the `spapi_sample` directory and the `blueprints` directory, so that we can make this a module and start importing other folders.  
3. One level above the spapi_sample, we create the `config` folder, and a `settings.py` file inside it. Though strictly not required, this folder is nice to have so that we can have multiple settings (local, staging, production, etc). We also create an `__init__.py` so that we can import the settings from here.
4. Inside the blueprints folder is the first blueprint called `user` that has an `__init__.py` file and a `views.py` file that is imported into `app.py` and instantiated from there. It will also house the templates for login, logout etc.
5. Create the .env file in the main directory based on the sample `.env.sample`.

    ```

## 3. Running the app

```python
$ pip install -r requirements.txt
$ flask run
```
Navigate to the ngrok url (`https://34b3dfc6c2b3.ngrok.io`) or `localhost:5000` and check if the home page is rendered.
Debug will be set to True as the flask environment has been set to 'Development'. If this command is not run, the default flask environment is 'Production', and Debug will be set to 'False'.



## 4. Reference links

- https://console.developers.google.com/apis/credentials/consent
- https://console.developers.google.com/apis/credentials

- Oauth2 playground - https://developers.google.com/oauthplayground/?
- Scopes for Oauth2 - https://developers.google.com/identity/protocols/oauth2/scopes

- https://www.googleapis.com/auth/userinfo.email
- https://www.googleapis.com/auth/userinfo.profile

- https://www.toolsqa.com/postman/oauth-2-0-authorization-with-postman/
- https://oauthdebugger.com/

- https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code
- https://bitwiser.in/2015/09/09/add-google-login-in-flask.html
