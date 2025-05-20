## printing in the requirement order
import pytest
class Test_order:
    @pytest.mark.run(order=33)
    def test_method_C(self):
        print('Iam Method_C')
    @pytest.mark.run(order=4)
    def test_method_D(self):
        print('Iam Method_D')
    @pytest.mark.run(order=5)
    def test_method_E(self):
        print('Iam Method_E')
    @pytest.mark.run(order=1)
    def test_method_A(self):
        print('Iam Method_A')
    @pytest.mark.run(order=6)
    def test_method_F(self):
        print('Iam Method_F')
    @pytest.mark.run(order=2)
    def test_method_B(self):
        print('Iam Method_B')
