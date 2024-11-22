import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FSer
from selenium.webdriver.edge.service import Service as ESer

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser: chrome, firefox, or IE"
    )


# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("Plugins", None)  # Remove the Plugins field if not needed

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        ser_obj = Service(
            "F:/Data Analyst/Python Basic/Automation_Testing/Drivers/Chrome/chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)

    elif browser_name == "firefox":
        ser1_obj = FSer("F:/Data Analyst/Python Basic/Automation_Testing/Drivers/Firefox/geckodriver"
                        ".exe")
        driver = webdriver.Firefox(service=ser1_obj)

    elif browser_name == "IE":
        ie_ob = ESer("F:/Data Analyst/Python Basic/Automation_Testing/Drivers/Edge/msedgedriver.exe")
        driver = webdriver.Edge(service=ie_ob)

    else:
        raise ValueError(f"Unsupported browser : {browser_name}")

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    # driver.execute_script("window.localStorage.clear();")
    # driver.execute_script("window.sessionStorage.clear();")
    # driver.delete_all_cookies()
    driver.quit()


"""
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Hook to capture screenshot on test failure
    # Execute all other hooks to obtain the report
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        # driver = item.funcargs.get('driver')  # Get the WebDriver instance
        global driver
        if driver:

            # Create the screenshots directory if it doesn't exist
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save the screenshot
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            # Attach the screenshot to the report
            if "pytest_html" in item.config.pluginmanager.get_plugins():
                extra = getattr(report, "extra", [])
                html = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:300px;height:200px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
                report.extra = extra            """
"""
@pytest.fixture(scope="function")
def driver():
    # Fixture to initialize WebDriver.
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()   """
"""
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    # Extend the Pytest Plugin to make and ambed screenshot in html report, whenever test fails.
    # :param item:
        
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == 'setup':
            xfail = hasattr(report, 'wasxfail')

            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _cpature_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px" ' \
                           'onclick="window.open(this.src)" align="right"/><div>' % file_name
                    extra.append(pytest_html.extras.html(html))
                    report.extra = extra

def _cpature_screenshot(name):
    driver.get_screenshot_as_file(name)         """


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots and embed them in the HTML report for failed tests.
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only for failed tests
    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            # Create screenshots directory if it doesn't exist
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save the screenshot
            screenshot_path = os.path.join(screenshots_dir, f"{item.nodeid.replace('::', '_')}.png")
            driver.save_screenshot(screenshot_path)

            # Embed the screenshot in the HTML report
            pytest_html = item.config.pluginmanager.get_plugin("html")
            # print("Pytest HTML Plugin:", pytest_html)

            if pytest_html:
                extra = getattr(report, "extra", [])
                html = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:300px;height:200px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
                report.extra = extra
