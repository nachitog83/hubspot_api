from .services import access_is_valid, save_tokens, get_redirect_uri, token_refresh
from .errors import HubSpotError
from app.database.schemas import token_schema
from flask import request, current_app, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from hubspot import HubSpot
from hubspot.utils.oauth import get_auth_url
import os

class AuthorizeClient(Resource):
    @jwt_required
    def get(self):
        tokens, valid = access_is_valid()
        if tokens:
            if valid:
                inst = token_schema.dump(tokens)
                return jsonify(msg='Access token is valid', data=inst['expires_at'])
            
            token_refresh(tokens)
            return jsonify(msg='Token refreshed', data=tokens['refresh_token'])

        auth_url = get_auth_url(
            scopes=("contacts",),
            client_id=os.environ.get("HUBSPOT_CLIENT_ID"),
            redirect_uri=get_redirect_uri(),
        )

        return jsonify(msg='Callback auth', data=auth_url)


class Callback(Resource):
    def get(self):
        try:
            tokens_response = HubSpot().auth.oauth.default_api.create_token(
                grant_type="authorization_code",
                code=request.args.get("code"),
                redirect_uri=get_redirect_uri(),
                client_id=os.environ.get("HUBSPOT_CLIENT_ID"),
                client_secret=os.environ.get("HUBSPOT_CLIENT_SECRET"),
            )
            tokens = save_tokens(tokens_response)
            return token_schema.dump(tokens), 200
        except:
            raise HubSpotError
