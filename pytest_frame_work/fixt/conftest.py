import pytest
@pytest.fixture()
def setup():
    print('Launching browser using driver.....')
    print('Open application by getting url.....')
    yield
    print('closing browser')