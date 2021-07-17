from pages.Login_Page import Login
from utilities.property_reader import ReadConfig
from utilities.logger import Loggen
from utilities.excel_utility import Excel


class Test_002_Login_MultiData:

    URL = ReadConfig.get_data("Application_Info", "URL")
    logger = Loggen.loggen()
    path = "../test_data/TC002.xlsx"
    sheet_name = "Sheet1"
    excel = Excel()

    def test_login(self, set_up):
        self.logger.info("********** Test_002_Login with multiple data ***********")
        self.logger.info("**********Validate User Login***********")
        self.driver = set_up
        self.driver.get(self.URL)
        self.lp = Login(self.driver)
        total_row = self.excel.get_total_row(self.path,self.sheet_name)
        for row in range(2,total_row+1):
            user_name = self.excel.get_value(self.path,self.sheet_name,row,1)
            password = self.excel.get_value(self.path,self.sheet_name,row,2)
            self.lp.type_user_name(user_name)
            self.lp.type_password(password)
            self.lp.click_login()
            actual_title = self.driver.title
            # self.driver.close()
            if actual_title == "UiBank":
                assert True
                self.logger.info("User Reaches to the Home Page")
                self.lp.click_logout()

            else:
                self.driver.save_screenshot(r"../screenshots/" + "test_login.png")
                # self.driver.quit()
                self.logger.error("User Not Reaches to the Home Page")
                assert False

        self.driver.quit()
