# # import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pytest
from selenium.webdriver.support.ui import Select
from TestData.HomePageData import HomePageData
from pageObject.FillForm import FillForm
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self, request):
        return request.param

    def test_formSubmission(self, getData):
        log = self.getlogger()
        filling_form = FillForm(self.driver)
        filling_form.getFullName(getData["FullName"])
        log.info(f"The Full name is: {getData['FullName']}")
        # print("Enter name is : ", filling_form.getFullNameText())
        filling_form.getEmail(getData["email_address"])
        # print("Enter email is : ", filling_form.getEmailText())
        log.info(f"The Full name is: {getData['email_address']}")
        filling_form.getPassword(getData["Password"])
        # print("Enter password is : ", filling_form.getPasswordText())
        log.info(f"The Full name is: {getData['Password']}")
        filling_form.getCheckBox()

        dropdown = filling_form.getGender()
        Select(dropdown).select_by_index(0)

        filling_form.getRadioButton()
        filling_form.getDateOfBirth(getData["DOB"])
        filling_form.getSubmit()

        Expected_message = "Success"
        Actual_Message = filling_form.getMessage()
        assert Expected_message in Actual_Message
        # print("Actual message prin on display is : ", Actual_Message)
        log.info(f"The Actual message is: "+Actual_Message)
        filling_form.getClearTwoWay()

        filling_form.getTwoWayText(getData["FullName"])
        filling_form.getSecondClear()
        self.driver.refresh()
        # print("Testing completed without any bug. Hurrey!!!!!!!")
        log.info("Testing completed without any bug. Hurrey!!!!!!!")
