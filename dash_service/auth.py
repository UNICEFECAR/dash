from .extensions import db

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/logout')
def logout():
    return 'Logout'