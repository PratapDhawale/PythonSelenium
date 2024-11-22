from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_path = "F:/Data Analyst/Python Basic/Automation_Testing/ExcelFiles/download.xlsx"
# fruit_name = ["Mango", "Apple", "Papaya", "Banana", "Kivi", "Orange"]
fruit_name = []
prices = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.CSS_SELECTOR, '#downloadButton').click()

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 10)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(EC.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)

price_column = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
print("Price Column ID:", price_column)

fruit_elements = driver.find_elements(By.XPATH, "//div[contains(@id, 'cell-2-')]")  # Adjust XPath based on your page structure
for fruit_element in fruit_elements:
    fruit_name.append(fruit_element.text)

print(f"Fruits found: {fruit_name}")

for fruit in fruit_name:
    wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//div[text()='{fruit}']")))
    fruit_element = driver.find_element(By.XPATH, f"//div[text()='{fruit}']")
    # fruit_name.append(fruit_element.text)
    if fruit_element.text != "":
        price_xpath = f"//div[text()='{fruit}']/parent::div/parent::div/div[@id='cell-{price_column}-undefined']"
        price_element = fruit_element.find_element(By.XPATH, price_xpath)
        prices.append((fruit, price_element.text))

for fruit, price in prices:
    print(f"Price of {fruit}: {price}")