from selenium.webdriver.support.select import Select


class Registration:
    textbox_firstname_id = "firstName"
    drop_title_id = "title"
    textbox_middlename_id = "middleName"
    textbox_lastname_id = "lastName"
    drop_gender_id = "sex"
    textbox_username_id = "username"
    textbox_email_id = "email"
    textbox_password_id = "password"
    btn_register_xpath = "//button[text()='Register']"
    text_registration_xpath = "//h1[text()='Register']"
    text_welcome_xpath = "//h2[text()=' Welcome To The UiBank Family! ']"

    def __init__(self, driver):
        self.driver = driver

    def verify_registration_text(self):
        result = self.driver.find_element_by_xpath(self.text_registration_xpath).is_displayed()
        return result

    def verify_welcome_text(self):
        result = self.driver.find_element_by_xpath(self.text_welcome_xpath).is_displayed()
        return result

    def type_first_name(self, firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)

    def select_title(self, title):
        drop = self.driver.find_element_by_id(self.drop_title_id)
        oSelect = Select(drop)
        oSelect.select_by_visible_text(title)

    def type_middle_name(self, middlename):
        self.driver.find_element_by_id(self.textbox_middlename_id).clear()
        self.driver.find_element_by_id(self.textbox_middlename_id).send_keys(middlename)

    def type_last_name(self, lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def select_gender(self, gender):
        drop = self.driver.find_element_by_id(self.drop_gender_id)
        oSelect = Select(drop)
        oSelect.select_by_visible_text(gender)

    def type_user_name(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def type_email(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def type_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_register_button(self):
        self.driver.find_element_by_xpath(self.btn_register_xpath).click()

