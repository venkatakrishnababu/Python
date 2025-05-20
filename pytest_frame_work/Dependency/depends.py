import pytest
class Test_depend:
    @pytest.mark.dependency()
    def test_open_App(self):
        print('Iam Open App')
        assert True
    @pytest.mark.dependency(depends=["Test_depend::test_open_App"])
    def test_login(self):
        print('Iam login')
        assert False
    @pytest.mark.dependency(depends=["Test_depend::test_open_App","Test_depend::test_login"])
    def test_search(self):
        print('Iam Searching')
        assert True
    @pytest.mark.dependency(depends=["Test_depend::test_open_App", "Test_depend::test_login"])
    def test_adv_search(self):
        print('iam adv_search')
        assert True

    @pytest.mark.dependency(depends=["Test_depend::test_login"])
    def test_logout(self):
        print('iam logout')
        assert True
