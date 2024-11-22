import inspect
import logging
import sys

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log', encoding='utf-8')  # Set encoding
        # fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        fileHandler.setFormatter(formatter)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleFormatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        consoleHandler.setFormatter(consoleFormatter)

        logger.addHandler(fileHandler)
        logger.addHandler(consoleHandler)
        logger.setLevel(logging.INFO)
        return logger

    def waitForConfirmPage(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def waitForAllConfirmPageElements(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located(locator))
        return element

    def waitForVisibility(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
