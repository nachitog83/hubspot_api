from flask import request, jsonify, make_response
from flask.globals import current_app
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.database.models import User
from app.database.schemas import user_schema
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from .errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError, errors

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            current_app.logger.info(body)
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return jsonify(id=str(id))
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class EditUser(Resource):
    @jwt_required
    def post(self):
        try:
            id = get_jwt_identity()
            body = request.get_json()
            body['date_modified'] = datetime.datetime.utcnow
            User.objects.get(id=id).update(**body)
            return user_schema.dump(User.objects.get(id=id)), 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            access_token = create_access_token(identity=str(user.id), expires_delta=datetime.timedelta(days=1))
            refresh_token = create_refresh_token(identity=str(user.id), expires_delta=datetime.timedelta(days=7))
            
            return jsonify(access_token=str(access_token), refresh_token=str(refresh_token))
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError


class RefreshToken(Resource):
    @jwt_required
    def post(self):
        # Create the new access token
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=str(access_token))

class GetCurrentUser(Resource):
    def get(self):
        return jsonify(username=str(get_jwt_identity()))