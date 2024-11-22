# import time
#
# import pytest
# from selenium.webdriver.common.by import By
#
# from utilities.BaseClass import BaseClass
#
#
# # @pytest.mark.usefixtures("setup")
# class TestOne(BaseClass):
#
#     def test_e2e(self):
#
#         self.driver.get("https://rahulshettyacademy.com/angularpractice/")
#         self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
#
#         ProductList = []
#         displayList = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
#         for dlist in displayList:
#             AllList = ProductList.append(dlist.text)
#         print("Product names are displayed on screen : ", ProductList)
#
#         products = self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
#         for product in products:
#             productNames = product.find_element(By.CSS_SELECTOR, "div h4 a").text
#             if productNames == "Blackberry":
#                 product.find_element(By.CSS_SELECTOR, "div button").click()
#
#         self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()
#         self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
