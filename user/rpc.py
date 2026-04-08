from jsonrpc import jsonrpc_method
from .views import login_user

@jsonrpc_method('auth.login')
def login(request, username, password):
    return login_user(request, username, password)