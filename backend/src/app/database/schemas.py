import flask
from flask.globals import current_app
import marshmallow as ma
from marshmallow import pre_load, fields, pprint

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "first_name", "last_name", "date_created", "date_modified")

user_schema = UserSchema()

class TokenSchema(ma.Schema):
    class Meta:
        #Fields to expose
        fields = ("access_token", "refresh_token", "expires_in", "expires_at")

token_schema = TokenSchema()

class DealSchema(ma.Schema):
    dealid = fields.Str()
    dealname = fields.Str()
    dealstage = fields.Str()
    closedate = fields.DateTime()
    amount = fields.Str()
    dealtype = fields.Str()
   
    @pre_load
    def flat(self, data, **kwargs):
        if type(data) == dict:
            for key, value in data['properties'].items():
                if key in ('dealname', 'dealstage', 'closedate', 'amount', 'dealtype'):
                    data[key] = value
            for a in ['properties', 'createdAt', 'updatedAt', 'archived']:
                data.pop(a, None)
            data['dealid'] = data.pop('id')
        return data

deal_schema = DealSchema(many=True)
