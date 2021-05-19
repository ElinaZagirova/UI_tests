import pytest
from configs import conf
from fixture.application import Application

fixture = None

# Launch Pytest and Application fixture
@pytest.fixture
def app(request, config):
    global fixture
    web_config = conf
    base_url = web_config.BASE_URL
    if fixture is None:
        fixture = Application(base_url=base_url, config=config)
    else:
        if not fixture.is_valid():
            fixture = Application(base_url= base_url, config=config)
    return fixture


@pytest.fixture(scope="session")
def config(request):
    return conf


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
