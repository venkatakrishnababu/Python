import pytest
class Test_order:
    @pytest.mark.sixth
    def test_method_A(self):
        print('Iam Method_A')
    @pytest.mark.fifth
    def test_method_B(self):
        print('Iam Method_B')
    @pytest.mark.fourth
    def test_method_C(self):
        print('Iam Method_C')
    @pytest.mark.thrid
    def test_method_D(self):
        print('Iam Method_D')
    @pytest.mark.second
    def test_method_E(self):
        print('Iam Method_E')
    @pytest.mark.first
    def test_method_F(self):
        print('Iam Method_F')
