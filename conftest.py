import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver") or getattr(item.instance, "driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot,name="screenshot_on_failure",attachment_type=allure.attachment_type.PNG)