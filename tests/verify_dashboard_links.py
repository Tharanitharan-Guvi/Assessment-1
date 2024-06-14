import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("login")
class TestNavigationLinks:
    def test_all_links_working(self):
        for i in range(2,20):
            item = self.driver.find_element(By.XPATH, f'//*[@id="mifos-reskin-side-nav"]/div/ul/li[{i}]/a')
            href = item.get_attribute('href')
            self.driver.get(href)
            assert self.driver.current_url == href, f"Link {href} is not working"