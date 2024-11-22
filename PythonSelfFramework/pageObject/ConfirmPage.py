from selenium.webdriver.common.by import By


class ConfirmPage:

    autoSuggest = (By.CSS_SELECTOR, "#country")
    suggestionsPick = (By.CSS_SELECTOR, ".suggestions li")
    checkboxClick = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchaseButton = (By.CSS_SELECTOR, ".btn-success")
    successMessage = (By.CSS_SELECTOR, "div [class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def getAutosuggest(self):
        return self.driver.find_element(*ConfirmPage.autoSuggest)

    def getSuggestionPickup(self):
        # Return the locator tuple directly
        return ConfirmPage.suggestionsPick

    def getCheckboxClick(self):
        return ConfirmPage.checkboxClick

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getVerifyMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
