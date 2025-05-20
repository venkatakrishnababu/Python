import pytest
class Test_group:
    @pytest.mark.Reg
    @pytest.mark.sanity
    def test_login_fb(self):
        print('Iam fb login')
    @pytest.mark.sanity
    def test_login_Insta(self):
        print('Iam insta login')
    @pytest.mark.sanity
    def test_login_twit(self):
        print('Iam twiteer login')
    @pytest.mark.sanity
    @pytest.mark.Reg
    def test_singup_fb(self):
        print('Iam fb singup')
    @pytest.mark.Reg
    def test_singup_Insta(self):
        print('Iam insta singup')
    @pytest.mark.Reg
    def test_singup_twit(self):
        print('Iam twiteer singup')
