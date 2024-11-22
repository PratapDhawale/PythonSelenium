# import io
import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

import os

os.environ['PYTHONIOENCODING'] = 'utf-8'

# import codecs
# sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestSecond(BaseClass):

    def test_e2ePageObject(self):
        # sys.stdout.reconfigure(encoding='utf-8')
        log = self.getlogger()
        homepage = HomePage(self.driver)
        # 1st Method
        # homepage.shopItems().click()
        # checkoutPage = CheckoutPage(self.driver)
        # 2nd Method
        checkoutPage = homepage.shopItems()
        log.info("Getting all the cart titles")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(f"Product title is: {cardText}")
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        #  1st method
        # checkoutPage = CheckoutPage(self.driver)
        # 2nd Method
        checkoutPage.getCartDetails().click()

        ExpectedProductName = "Blackberry"
        Actual_ProductName = checkoutPage.getVerifyProductName().text
        assert Actual_ProductName == ExpectedProductName
        log.info(f"Actual product name is: {Actual_ProductName}")

        ExpectedProductType = "Sim cart"
        Actual_ProductType = checkoutPage.getVerifyProductType().text
        assert Actual_ProductType == ExpectedProductType
        log.info(f"Actual product type is: {Actual_ProductType}")

        ExpectedProductStatus = "In Stock"
        Actual_ProductStatus = checkoutPage.getVerifyProductStatus().text
        assert Actual_ProductStatus == ExpectedProductStatus
        log.info(f"Actual product status is: {Actual_ProductStatus}")

        ExpectedProductQuantity = "1"
        Actual_ProductQuantity = checkoutPage.getVerifyProductQuantity().get_attribute("value")
        assert ExpectedProductQuantity == Actual_ProductQuantity
        log.info(f"Actual product quantity is: {Actual_ProductQuantity}")

        ExpectedProductPrice = "₹. 50000"
        Actual_ProductPrice = checkoutPage.getVerifyProductPrice().text
        assert ExpectedProductPrice == Actual_ProductPrice
        log.info(f"Actual product price is: {Actual_ProductPrice.encode('ascii', 'ignore').decode('ascii')}")

        ExpectedProductTotal = "₹. 50000"
        Actual_ProductTotal = checkoutPage.getVerifyTotalPrice().text
        assert ExpectedProductTotal == Actual_ProductTotal
        log.info(f"Actual product total is: {Actual_ProductTotal.encode('ascii', 'ignore').decode('ascii')}")

        ExpectedRemoveButton = "Remove"
        Actual_RemoveButton = checkoutPage.getVerifyRemoveButton().text
        assert ExpectedRemoveButton == Actual_RemoveButton
        log.info(f"Actual Remove button text is: {Actual_RemoveButton}")

        Expected_BottomOptions = [' ', ' ', ' ', 'Continue Shopping', 'Checkout']
        Actual_BottomOptions = []
        bottom_options = checkoutPage.getOptionsShown()
        for options in bottom_options:
            Actual_BottomOptions.append(options.text)
        assert Expected_BottomOptions == Actual_BottomOptions
        log.info(f"Actual bottom options are : {Actual_BottomOptions}")

        # 1st Method
        # checkoutPage.getCheckoutButton().click()
        # 2nd Method
        confirmPage = checkoutPage.getCheckoutButton()
        # 1st Method
        # confirmPage = ConfirmPage(self.driver)
        # 2nd Method
        log.info("Entering country name Ind")
        confirmPage.getAutosuggest().send_keys("Ind")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((confirmPage.getSuggestionPickup())))
        # self.test_e2ePageObject()
        countries = self.waitForAllConfirmPageElements(confirmPage.getSuggestionPickup())
        for country in countries:
            if country.text == "India":
                country.click()
                break

        checkBox = self.waitForConfirmPage(confirmPage.getCheckboxClick())
        checkBox.click()

        confirmPage.getPurchase().click()

        Expected_Message = "Success"
        Actual_Message = confirmPage.getVerifyMessage().text
        log.info(f"Actual final message is: " + Actual_Message)
        assert Expected_Message in Actual_Message


