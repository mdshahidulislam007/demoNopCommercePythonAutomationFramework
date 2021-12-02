import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
#from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getBaseURL()
    path = ".\\TestData\\LoginData.xlsx"
    #logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):

        #self.logger.info("****** test_login_ddt Started ******")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of row", self.rows - 1)
        status_list = []

        for row in range(2, self.rows):
            self.username = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', row, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.expected == 'Pass':
                    # self.logger.info('*** Passsed ***')
                    self.lp.clickLogout()
                    status_list.append('Pass')
                elif self.expected == 'Fail':
                    # self.logger.info('*** Failed ***')
                    self.lp.clickLogout()
                    status_list.append('Fail')
            elif actual_title != exp_title:
                if self.expected == 'Pass':
                    # self.logger.info('*** Failed ***')
                    status_list.append('Fail')
                elif self.expected == 'Fail':
                    # self.logger.info('*** Passsed ***')
                    status_list.append('Pass')
            print(status_list)

        if "Fail" not in status_list:
            print("DDT Login Test Passed")
            # self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            print("DDT Login Test Failed")
            # self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        print("Complete")
