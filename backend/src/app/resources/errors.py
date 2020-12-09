class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UpdatingDealError(Exception):
    pass

class DealNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class HubSpotError(Exception):
    pass

class InvalidHeader(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UpdatingDealError": {
         "message": "Updating Deal added by other is forbidden",
         "status": 403
     },
     "DealNotExistsError": {
         "message": "Deal with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "HubSpotError": {
         "message": "HubSpot API error",
         "status": 500
     },
     "InvalidHeader": {
         "message": "Invalid Header",
         "status": 400
     }
}