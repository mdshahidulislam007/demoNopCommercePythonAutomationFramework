class LoginPage:
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    button_login_tagName = "button"
    button_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.txtbox_username_id).clear()
        self.driver.find_element_by_id(self.txtbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txtbox_password_id).clear()
        self.driver.find_element_by_id(self.txtbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_tag_name(self.button_login_tagName).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()
