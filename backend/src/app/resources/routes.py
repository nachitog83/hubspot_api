from .auth import SignupApi, LoginApi, EditUser, GetCurrentUser
from .oauth import AuthorizeClient, Callback
from .deals import GetUpdateDeals, ShowDeals

def initialize_routes(api):
    api.add_resource(AuthorizeClient, '/api/oauth/authorize', endpoint="api.oauth.authorize")
    api.add_resource(Callback, '/api/oauth/callback',  endpoint="api.oauth.callback")

    api.add_resource(SignupApi, '/api/auth/signup',  endpoint="api.auth.signup")
    api.add_resource(LoginApi, '/api/auth/login',  endpoint="api.auth.login")
    api.add_resource(EditUser, '/api/auth/edituser',  endpoint="api.auth.edituser")
    api.add_resource(GetCurrentUser, '/api/auth/getcurrentuser',  endpoint="api.auth.getcurrentuser")


    api.add_resource(GetUpdateDeals, '/api/deals/update',  endpoint="api.deals.update")
    api.add_resource(ShowDeals, '/api/deals/show',  endpoint="api.deals.show")
