from pages.Login_Page import Login
from utilities.property_reader import ReadConfig
from utilities.logger import Loggen


class Test_001_Login:

    URL = ReadConfig.get_data("Application_Info", "URL")
    user_name = ReadConfig.get_data("Application_Info", "user_name")
    password = ReadConfig.get_data("Application_Info", "password")
    logger = Loggen.loggen()

    def test_login_title_validation(self, set_up):
        print('Get Log Method in TestCase : ', self.logger)
        self.logger.info("**********Test_001_Login***********")
        self.logger.info("**********Verify Login Title***********")
        self.driver = set_up
        self.driver.get(self.URL)
        actual_title = self.driver.title
        self.logger.info(f"Title is : {actual_title}")
        if actual_title == "UiBank":
            assert True
            self.logger.info("User Reaches to the Login Page")
        else:
            self.driver.save_screenshot(r"../screenshots/"+"test_login_title_validation.png")
            self.logger.error("User Not Reaches to the Login Page")
            assert False
        self.driver.quit()

    def test_login(self, set_up):
        self.logger.info("**********Validate User Login***********")
        self.driver = set_up
        self.driver.get(self.URL)
        self.lp = Login(self.driver)
        self.lp.type_user_name(self.user_name)
        self.lp.type_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title
        # self.driver.close()
        if actual_title == "UiBank":
            assert True
            self.logger.info("User Reaches to the Home Page")
            self.lp.click_logout()
            self.driver.quit()
        else:
            self.driver.save_screenshot(r"../screenshots/"+"test_login.png")
            self.driver.quit()
            self.logger.error("User Not Reaches to the Home Page")
            assert False



