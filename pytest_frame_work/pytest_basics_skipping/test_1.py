import pytest
class TestClass:
    @pytest.fixture()
    def setup(self):
        print('Launching browser using driver.....')
        print('Open application by getting url.....')
        yield
        print('closing browser')
    def test_login(self,setup):
        print('This is Login test')
    def test_search(self,setup):
        print("This is search test")
    def test_dropdown(self,setup):
        print('This is dropdown test')
    def test_logout(self):
        print('this is Logout test')

