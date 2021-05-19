import os

BASE_URL = os.environ.get('BASE_URL', 'https://test.com/')

LOGIN_URL = BASE_URL + 'login/'
TEST_USER = {
    'Login': 'test@gmail.com',
    'Password': 'testpass'

}
