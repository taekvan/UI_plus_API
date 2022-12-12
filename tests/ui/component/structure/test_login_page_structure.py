import pytest

from logic.base_case import BaseCase


@pytest.mark.component_structure
class TestCase(BaseCase):

    def test_login_page_structure(self):
        page = self.page_factory.get_page('login')

        assert page.is_login_btn_visible()
        actual_username_placeholder = page.get_username_field_placeholder()
        assert actual_username_placeholder == 'Username', \
            f'The Username field has wrong placeholder: {actual_username_placeholder}'
        actual_password_placeholder = page.get_password_field_placeholder()
        assert actual_password_placeholder == 'Password', \
            f'The Password field has wrong placeholder: {actual_password_placeholder}'
        actual_login_btn_name = page.get_login_btn_name()
        assert actual_login_btn_name == 'Login', \
            f'The Login btn has wrong name: {actual_login_btn_name}'
