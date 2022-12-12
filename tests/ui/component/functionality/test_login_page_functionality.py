import pytest
from logic.base_case import BaseCase


@pytest.mark.component_functionality
class TestCase(BaseCase):
    testdata_negative = [
        ('', '', 'Epic sadface: Username is required'),
        ('', 'fevvreber', 'Epic sadface: Username is required'),
        ('testuser', '', 'Epic sadface: Password is required'),
        ('testuser', 'testpassword', 'Epic sadface: Username and password do not match any user in this service'),

    ]

    @pytest.mark.testit_case_id(1000)
    @pytest.mark.testit_case_title("Login page login with incorrect creds")
    @pytest.mark.parametrize("login, pswd, expected_error", testdata_negative)
    def test_login_page_negative_functionality(self, login, pswd, expected_error):
        page = self.page_factory.get_page('login')
        page.login(login, pswd)
        actual_error = page.get_login_error_text()

        assert actual_error == expected_error, \
            f'Expected error text is {expected_error}, but actual is {actual_error}'

    testdata_positive = [
        ('standard_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
    ]

    @pytest.mark.testit_case_id(1001)
    @pytest.mark.testit_case_title("Login page login with correct creds")
    @pytest.mark.parametrize("login, pswd", testdata_positive)
    def test_login_page_positive_functionality(self, login, pswd):
        page = self.page_factory.get_page('login')
        page.login(login, pswd)

        assert page.get_page_title() == 'PRODUCTS', \
            f'Page Products should be opened'
