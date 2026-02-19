# Scalable Test Automation Framework Documentation

## Overview

This framework is designed to support Web, Mobile, and API automation
testing using:

-   **Behave (BDD)**
-   **Selenium (UI automation)**
-   **Requests (API testing)**
-   **Allure (Reporting)**
-   **GitHub Actions (CI/CD)**

------------------------------------------------------------------------

## Architecture

### Folder Structure

    automation-framework/
    │
    ├── features/
    │   ├── steps/
    │       ├── transfer_steps.py
    │   ├── transfer_money.feature
    │   ├── schedule_payment.feature
    │   ├── currency_conversion.feature
    │
    │
    ├── pages/
    │   ├── base_page.py
    │   ├── transfer_page.py
    │
    ├── config/
    │   ├── config.json
    │
    ├── runner.py
    ├── requirements.txt
    └── .github/workflows/manual-ci.yml

------------------------------------------------------------------------

## Configuration (`config/config.json`)

``` json
{
  "environment": "dev",
  "dev": {
    "base_url": "https://dev.bankapp.com"
  },
  "QA": {
    "base_url": "https://qa.bankapp.com"
  },
  "production": {
    "base_url": "https://bankapp.com"
  }
}
```

------------------------------------------------------------------------

## Sample Feature File (`features/transfer_money.feature`)

``` gherkin
Feature: Transfer money between accounts

  Scenario Outline: Successful transfer between accounts
    Given I am logged in as "<user>"
    When I transfer "<amount>" from "<from_account>" to "<to_account>"
    Then I should see a success message
```

------------------------------------------------------------------------

## Sample Step Definition (`steps/transfer_steps.py`)

``` python
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
```

------------------------------------------------------------------------

## Runner (`runner.py`)

``` python
import subprocess
import sys

mode = sys.argv[1] if len(sys.argv) > 1 else "sequential"

if mode == "parallel":
    subprocess.run([
        "behave-parallel",
        "features/transfer_money.feature",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", "reports"
    ])
else:
    subprocess.run([
        "behave",
        "features/transfer_money.feature",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", "reports"
    ])
```

### Run Sequential:

    python runner.py

### Run Parallel:

    python runner.py parallel

------------------------------------------------------------------------

## Requirements (`requirements.txt`)

    behave==1.2.7
    selenium==5.11.2
    requests==2.31.0
    allure-behave==2.9.43
    behave-parallel==0.1.3

------------------------------------------------------------------------

## CI/CD Pipeline (`.github/workflows/ci.yml`)

``` yaml
name: Manual CI/CD Test Runner

# Trigger manually
on:
  workflow_dispatch:

jobs:
  run-tests:
    runs-on: ubuntu-latest

    steps:
      # 1. Checkout the repository
      - name: Checkout code
        uses: actions/checkout@v3

      # 2. Setup Python
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      # 3. Install dependencies
      - name: Install dependencies
        run: pip install -r requirements.txt

      # 4. Run your runner.py
      - name: Run Tests
        run: python runner.py
```

------------------------------------------------------------------------

## Reporting

Allure results are generated inside:

    reports/

Generate HTML report locally:

    allure serve reports

------------------------------------------------------------------------

## Data-Driven Testing

Data-driven testing is implemented using Behave parameters directly inside feature files
```
Feature: Transfer money between accounts

  Scenario Outline: Successful transfer between accounts
    Given I am logged in as "<user>"
    When I transfer "<amount>" from "<from_account>" to "<to_account>"
    Then I should see a success message

    Examples:
      | user      | from_account | to_account | amount |
      | dev_user  | Savings      | Checking   | 100    |
      | dev_user  | Checking     | Savings    | 50     |
```

------------------------------------------------------------------------

## Key Capabilities

-   Multi-environment support (dev / QA / production)
-   Data-driven testing via Behave parameters
-   Parallel execution support
-   CI/CD integration with GitHub Actions
-   Detailed Allure reporting
-   Scalable structure for Web, and API testing

------------------------------------------------------------------------



