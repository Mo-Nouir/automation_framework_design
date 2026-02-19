from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TransferPage(BasePage):

    amount_input = (By.ID, "amount")
    from_account_dropdown = (By.ID, "from_account")
    to_account_dropdown = (By.ID, "to_account")
    submit_btn = (By.ID, "submit_transfer")
    success_msg = (By.CSS_SELECTOR, ".alert-success")

    def transfer_money(self, from_acc, to_acc, amount):
        self.select_dropdown(self.from_account_dropdown, from_acc)
        self.select_dropdown(self.to_account_dropdown, to_acc)
        self.send_keys(self.amount_input, amount)
        self.click(self.submit_btn)

    def is_transfer_successful(self):
        return self.is_visible(self.success_msg)