class LoginService:
    @staticmethod
    def login(username, password):
        if username == 'admin' and password == 'password':
            return True
        else:
            return False
