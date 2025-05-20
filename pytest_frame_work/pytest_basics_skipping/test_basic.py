import pytest
## basic example

class TestBasic:
    def test_1(self):
        print('test1')
    def test_2(self):
        print('test_2')
### using fixtures and skipping concept

class Test_basic:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def test_m1(self):
        print('Iam 1st method')
        print(f"I'm from test_m1 My name is {self.name} and my age is {self.age}")
    def test_m2(self):
        print('Iam 2nd method')
        print(f"I'm from test_m2 My name is {self.name} and my age is {self.age}")
# obj=Test_basic('rahul',24)
# obj.test_m1()
# obj1=Test_basic('krishna',28)
# obj1.test_m2()
@pytest.fixture
def test_obj1():
    return Test_basic("rahul", 24)
@pytest.fixture
def test_obj2():
    return Test_basic("krishna", 28)
@pytest.mark.skip
def test_method1(test_obj1):
    test_obj1.test_m1()

def test_method2(test_obj2):
    test_obj2.test_m2()
