from app.database.models import HubspotData
from flask import request, current_app
import time, datetime, os
from hubspot import HubSpot
from mongoengine.errors import DoesNotExist
from .errors import HubSpotError

def save_tokens(tokens_response):
    tokens = {
        "access_token": tokens_response.access_token,
        "refresh_token": tokens_response.refresh_token,
        "expires_in": tokens_response.expires_in,
        "expires_at": time.time() + tokens_response.expires_in * 0.95,
    }
    tokens['expires_at'] = datetime.datetime.fromtimestamp(tokens['expires_at'])

    HubspotData(refresh_token=tokens['refresh_token']).update(**tokens, upsert=True)

    return tokens

def access_is_valid():
    try:
        key = HubspotData.objects.get()
        if key._data['expires_at'] > datetime.datetime.utcnow():
            return key._data, True
        else:
            return key._data, False
    except DoesNotExist:
        return None, None

def get_redirect_uri():
    url = request.url_root
    if '127.0.0.1' in url: url = url.replace('127.0.0.1', 'localhost')
    return url + "api/oauth/callback"

def token_refresh(tokens):
    try:
        tokens_response = HubSpot().auth.oauth.default_api.create_token(
                    grant_type="refresh_token",
                    redirect_uri=get_redirect_uri(),
                    refresh_token=tokens["refresh_token"],
                    client_id=os.environ.get("HUBSPOT_CLIENT_ID"),
                    client_secret=os.environ.get("HUBSPOT_CLIENT_SECRET"),
                )
        tokens = save_tokens(tokens_response)
        return tokens
    except:
        raise HubSpotError
