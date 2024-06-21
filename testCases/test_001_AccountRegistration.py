import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen #for logging


class Test_001_AccountReg:
    # baseURL="https://demo.opencart.com/"
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()  #return logger object

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching apllication")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on MyAccount -->register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Providing customers details for registration")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        #self.regpage.setEmail("sba2334303249@gmail.com")
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        self.driver.close()
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Account registration is passed...")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("Account registration is failed...")
            self.driver.close()
            assert False

        self.logger.info("*** test_001_AccountRegistration finished ***")