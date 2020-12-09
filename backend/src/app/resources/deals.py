from .services import access_is_valid
from app.database.models import Deal
from app.database.schemas import deal_schema
from .services import access_is_valid, token_refresh
from flask import current_app, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from .errors import DealNotExistsError, InvalidHeader
import os, requests

class GetUpdateDeals(Resource):
    @jwt_required
    def get(self):
        tokens, valid = access_is_valid()
        if tokens:
            if not valid:
                tokens = token_refresh(tokens)
            
            url = "https://api.hubapi.com/crm/v3/objects/deals"
            querystring = {
                    "limit": "100",
                    "properties": "dealid, dealname, dealstage, closedate, amount, dealtype",
                    "paginateAssociations": "false",
                    "archived": "false"
                    }

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {tokens['access_token']}"
                }
            try:
                response = requests.get(url, headers=headers, params=querystring)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
            except InvalidHeader as err:
                raise SystemExit(err)

            response = response.json().get('results')
            deals = deal_schema.load(response)
            for deal in deals:
                Deal(dealid=deal['dealid']).update(**deal, upsert=True)
            return jsonify(success='deals updated')

class ShowDeals(Resource):
    @jwt_required
    def get(self):
        dealobj = Deal.objects
        if dealobj:
            return deal_schema.dump(dealobj), 200
        else:
            raise DealNotExistsError
