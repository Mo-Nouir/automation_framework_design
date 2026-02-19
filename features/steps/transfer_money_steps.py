from behave import given, when, then
from pages.transfer_page import TransferPage
from pages.login_page import LoginPage
from utils.config import Config
from selenium import webdriver

config = Config(env="dev")
driver = webdriver.Chrome()
login_page = LoginPage(driver)
transfer_page = TransferPage(driver)

@given('I am logged in as "{user}"')
def step_login(context, user):
    login_page.open(config.base_url)
    login_page.login(config.credentials["user"], config.credentials["pass"])

@when('I transfer "{amount}" from "{from_account}" to "{to_account}"')
def step_transfer(context, amount, from_account, to_account):
    transfer_page.transfer_money(from_account, to_account, amount)

@then('I should see a success message')
def step_verify_transfer(context):
    assert transfer_page.is_transfer_successful()
