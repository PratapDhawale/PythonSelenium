from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    cartDetails = (By.CSS_SELECTOR, ".btn-primary")

    productName = (By.CSS_SELECTOR, "div [class='media-body'] h4")
    productType = (By.CSS_SELECTOR, "div [class='media-body'] h5 a")
    productStatus = (By.CSS_SELECTOR, "div [class='media-body'] span strong")

    productQuantity = (By.CSS_SELECTOR, "td input:nth-child(1)")

    productPrice = (By.CSS_SELECTOR, "div td:nth-child(3) strong")
    productTotal = (By.CSS_SELECTOR, "div td:nth-child(4) strong")
    removeButton = (By.CSS_SELECTOR, "tbody tr:nth-child(1) button")
    finalAmount = (By.CSS_SELECTOR, "tbody tr:nth-child(2) strong")
    optionsShown = (By.CSS_SELECTOR, "div [class='row'] tr:nth-child(3) td")
    checkoutButton = (By.CSS_SELECTOR, "tbody tr:nth-child(3) td:nth-child(5) button")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCartDetails(self):
        return self.driver.find_element(*CheckoutPage.cartDetails)

    def getVerifyProductName(self):
        return self.driver.find_element(*CheckoutPage.productName)

    def getVerifyProductType(self):
        return self.driver.find_element(*CheckoutPage.productType)

    def getVerifyProductStatus(self):
        return self.driver.find_element(*CheckoutPage.productStatus)

    def getVerifyProductQuantity(self):
        return self.driver.find_element(*CheckoutPage.productQuantity)

    def getVerifyProductPrice(self):
        return self.driver.find_element(*CheckoutPage.productPrice)

    def getVerifyTotalPrice(self):
        return self.driver.find_element(*CheckoutPage.productTotal)

    def getVerifyRemoveButton(self):
        return self.driver.find_element(*CheckoutPage.removeButton)

    def getVerifyFinalAmount(self):
        return self.driver.find_element(*CheckoutPage.finalAmount)

    def getOptionsShown(self):
        return self.driver.find_elements(*CheckoutPage.optionsShown)

    def getCheckoutButton(self):
        # 1st Method
        #  return self.driver.find_element(*CheckoutPage.checkoutButton)
        # 2nd Method
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
