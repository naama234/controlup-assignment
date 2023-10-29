import pytest
from selenium import webdriver
from LoginPage import LoginPage
from TransactionPage import TransactionPage

SITE_URL = "https://demo.applitools.com/"
USERNAME = "testuser"
PASSWORD = "password123"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_transactions_count(browser):
    browser.get(SITE_URL)
    browser.implicitly_wait(10)
    login_page = LoginPage(browser)

    login_page.login(USERNAME, PASSWORD)

    transaction_page = TransactionPage(browser)

    num_succeeded = transaction_page.count_successful_transactions()

    expected_num_succeeded = 0
    assert num_succeeded == expected_num_succeeded, f"Expected {expected_num_succeeded} succeeded transactions, but " \
                                                    f"found {num_succeeded}"
