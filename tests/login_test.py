

def test_positive_login(app):
    valid_user = app.config.TEST_USER
    email = valid_user['Login']
    password = valid_user['Password']
    app.session.login(email, password)
    profile_email = app.session.get_email_in_user_profile()
    assert email == profile_email

def test_wrong_password(app):
    valid_user = app.config.TEST_USER
    email = valid_user['Login']
    password = '111'
    app.session.login(email, password)
    app.wd.implicitly_wait(5)
    warning_text = app.session.get_warning_text()
    assert warning_text=="The email or password you entered is incorrect.\nPlease try again."
