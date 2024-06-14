import pytest

@pytest.mark.usefixtures("login")
class TestLogin:
    def test_login_success(self, login):
        assert "https://qatest.uat.cloudbankin.com/#/" == self.driver.current_url
