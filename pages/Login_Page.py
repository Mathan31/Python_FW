

class Login:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_sign_in_xpath = "//button[text()='Sign In']"
    link_sign_out_xpath = "//a[text()='Logout']"
    link_register_xpath = "//*[text()='Register For Account']"

    def __init__(self, driver):
        self.driver = driver

    def type_user_name(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def type_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_sign_in_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.link_sign_out_xpath).click()

    def click_register_link(self):
        self.driver.find_element_by_xpath(self.link_register_xpath).click()

