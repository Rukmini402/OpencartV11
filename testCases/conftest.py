import os
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(self,browser):
    if browser=='edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.....")

    elif browser=='firefox':
        driver=webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser.....")

    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.....")
    return driver

def pytest_addoption(parser):
    parser.addoption("__browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("__browser")


##########pytest HTML Reports ###############
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='Orange HRM'
    config._metadata['Module Name']='CustRegistration'
    config._metadata['Tester']='Rukmini'

#It is hook for dalete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugin",None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"
