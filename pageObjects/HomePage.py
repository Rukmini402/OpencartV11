from selenium.webdriver.common.by import By

class HomePage():
    lnk_myaccount_xpath="//a[@title='My Account']"
    lnk_register_linktext="Register"
    lnk_login_linktext="Login"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccount(self):
        #self.driver.find_element(By.XPATH,self.link_logout_xpath).click()
        self.driver.find_element_by_xpath(self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element_by_link_text(self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element_by_link_text(self.lnk_login_linktext).click()

