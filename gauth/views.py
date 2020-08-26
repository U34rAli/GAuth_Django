from django.shortcuts import render
# Create your views here.
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import HttpResponse

CLIENT_ID = '333262129832-bq0fbu4e1112tv4r2jbno4n415sg5kgv.apps.googleusercontent.com'

def gauth_index(request):
    return render(request, 'gauth/index.html')

def gauth_authenticate(request, idtoken):
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(idtoken, requests.Request(), CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        print("-------------------------\n\n"+userid + "\n\n-----------------------------\n\n")
    except ValueError:
        # Invalid token
        print(ValueError)
    return HttpResponse("Welcome " + userid)