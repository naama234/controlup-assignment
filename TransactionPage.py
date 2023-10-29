from selenium.webdriver.common.by import By

TRANSACTION_TABLE_XPATH = "//div[@class='table-responsive']//tbody//tr"
STATUS_ELEMENT_XPATH = ".//td[1]//span[2]"


class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.transaction_table = driver.find_elements(By.XPATH, TRANSACTION_TABLE_XPATH)

    def count_successful_transactions(self):
        succeeded_count = 0
        for row in self.transaction_table:
            status_element = row.find_elements(By.XPATH, STATUS_ELEMENT_XPATH)
            status_text = status_element[0].text
            if status_text == "Succeeded":
                succeeded_count += 1
        return succeeded_count
