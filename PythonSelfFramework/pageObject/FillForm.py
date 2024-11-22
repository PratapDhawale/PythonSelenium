import pytest
from selenium.webdriver.common.by import By


class FillForm:

    def __init__(self, driver):
        self.driver = driver

    # name = "Pratap Uttam Dhawale"
    # email_id = "prtp5190@gmail.com"
    # pass_word = "Pratap@123"
    # DOB = "05-01-1990"

    full_name = (By.CSS_SELECTOR, "[name='name']")
    # name_text = (By.CSS_SELECTOR, "div form div:nth-child(1) input")
    email = (By.CSS_SELECTOR, "[name='email']")
    password = (By.CSS_SELECTOR, "[type='password']")
    checkbox = (By.CSS_SELECTOR, "[type='checkbox']")
    pre_gender = (By.CSS_SELECTOR, "div [class='form-group'] select")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    after_gender = (By.CSS_SELECTOR, "div [class='form-group'] select")
    radioButton = (By.CSS_SELECTOR, "#inlineRadio1")
    date = (By.CSS_SELECTOR, "[name='bday']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CSS_SELECTOR, ".alert-success")
    Two_Way = (By.CSS_SELECTOR, ".ng-pristine")
    add_text = (By.CSS_SELECTOR, "input[class='ng-valid ng-touched ng-dirty']")
    clear_text =(By.XPATH, "//*[@class='ng-valid ng-touched ng-dirty']")

    def getFullName(self, FullName):
        # self.driver.find_element(FillForm.full_name).send_keys(FillForm.name)
        enter_name = self.driver.find_element(*FillForm.full_name)
        enter_name.send_keys(FullName)

    def getFullNameText(self):
        enter_text = self.driver.find_element(*FillForm.full_name)
        # return enter_text.text
        return enter_text.get_attribute("value")

    def getEmail(self, email_address):
        enter_email = self.driver.find_element(*FillForm.email)
        enter_email.send_keys(email_address)

    def getEmailText(self):
        email_text = self.driver.find_element(*FillForm.email)
        return email_text.get_attribute("value")

    def getPassword(self, Password):
        enter_password = self.driver.find_element(*FillForm.password)
        enter_password.send_keys(Password)

    def getPasswordText(self):
        pass_text = self.driver.find_element(*FillForm.password)
        return pass_text.get_attribute("value")

    def getCheckBox(self):
        checkbox_element = self.driver.find_element(*FillForm.checkbox)
        checkbox_element.click()

    def getPreSelectGender(self):
        pre_gen = self.driver.find_element(*FillForm.pre_gender)
        return pre_gen.text

    def getGender(self):
        return self.driver.find_element(*FillForm.gender)

    def getAfterSelectGender(self):
        after_gen = self.driver.find_element(*FillForm.after_gender)
        return after_gen.text

    def getRadioButton(self):
        click_radiobutton = self.driver.find_element(*FillForm.radioButton)
        click_radiobutton.click()

    def getDateOfBirth(self, DOB):
        enter_DOB = self.driver.find_element(*FillForm.date)
        enter_DOB.send_keys(DOB)

    def getSubmit(self):
        submit_click = self.driver.find_element(*FillForm.submit)
        submit_click.click()

    def getMessage(self):
        verify_message = self.driver.find_element(*FillForm.message)
        return verify_message.text

    def getClearTwoWay(self):
        clear_text = self.driver.find_element(*FillForm.Two_Way)
        clear_text.clear()
        return clear_text

    def getTwoWayText(self, FullName):
        enter_text = self.driver.find_element(*FillForm.Two_Way)
        enter_text.send_keys(FullName)

    def getSecondClear(self):
        clear_matter = self.driver.find_element(*FillForm.clear_text)
        clear_matter.clear()
        return clear_matter


