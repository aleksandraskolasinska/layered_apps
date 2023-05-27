from core.interfaces.login_service import LoginService

class LoginServiceImpl(LoginService):
    def authenticate(self, username, password):


login_service = LoginServiceImpl()
