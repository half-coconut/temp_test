from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    """init version"""

    def setup_class(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://infstones.com/")
        self.driver.implicitly_wait(30)

    def setup_method(self):
        ...

    def teardown_class(self):
        self.driver.quit()

    def teardown_method(self):
        ...

    def test_indexPage(self):
        assert "TRY FOR FREE" in self.driver.find_element(By.CSS_SELECTOR,
                                                          "a:nth-child(1) > .Button_primary__mrG7O > span").text

        assert "Trusted By" in self.driver.find_element(By.XPATH,
                                                        '//*[@id="TrustedBy_trustedbyContainer__MyT2N"]/div[2]/span').text

        assert "What Our Clients Are Saying" in self.driver.find_element(By.XPATH,
                                                                         '//*[@id="Community_communityContainer__AAuUc"]/div/div[1]/div[1]').text

        assert "Join Our Community" in self.driver.find_element(By.XPATH,
                                                                '//*[@id="Community_communityContainer__AAuUc"]/div/div[2]/div[1]').text

        assert "Featured On" in self.driver.find_element(By.XPATH,
                                                         '//*[@id="feature_container"]/div[1]').text
