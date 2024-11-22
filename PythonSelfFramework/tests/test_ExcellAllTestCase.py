import pytest
from selenium.webdriver.support.ui import Select
from utilities.BaseClass import BaseClass
from pageObject.FillForm import FillForm
from TestData.ExcelUtils import getTestData  # Utility function

# Path to the Excel file
EXCEL_FILE_PATH = "F:\\Data Analyst\\Python Basic\\Automation_Testing\\ExcelFiles\\Data.xlsx"


class TestExcelAllTestCases(BaseClass):

    @pytest.mark.parametrize("test_case_data", getTestData(EXCEL_FILE_PATH))
    def test_formSubmission(self, test_case_data):
        log = self.getlogger()
        filling_form = FillForm(self.driver)

        # Access the test data dynamically
        filling_form.getFullName(test_case_data["FullName"])
        log.info(f"The Full name is: {test_case_data['FullName']}")

        filling_form.getEmail(test_case_data["email_address"])
        log.info(f"The Email address is: {test_case_data['email_address']}")

        filling_form.getPassword(test_case_data["Password"])
        log.info(f"The Password is: {test_case_data['Password']}")

        filling_form.getCheckBox()

        dropdown = filling_form.getGender()
        Select(dropdown).select_by_index(0)

        filling_form.getRadioButton()
        filling_form.getDateOfBirth(test_case_data["DOB"])
        log.info(f"The Date of Birth is: {test_case_data['DOB']}")

        filling_form.getSubmit()

        # Assertion for success message
        Expected_message = "Success"
        Actual_Message = filling_form.getMessage()
        assert Expected_message in Actual_Message
        log.info(f"The Actual message is: {Actual_Message}")

        filling_form.getClearTwoWay()
        filling_form.getTwoWayText(test_case_data["FullName"])
        filling_form.getSecondClear()

        self.driver.refresh()
        log.info("Test case executed successfully!")
