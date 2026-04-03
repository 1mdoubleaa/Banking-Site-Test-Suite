# Banking-Site-Test-Suite

Automated test suite for [Guru99 Bank](https://demo.guru99.com/V4/) — a demo banking web application. 

---

## Overview

The suite automates testing of the Guru99 Bank manager portal, covering input validation, form interactions, alerts, and CRUD operations across 9 banking features.

| Module | Test Class | Tests |
|---|---|---|
| New Customer | `NewCustomer` | 28 |
| Edit Customer | `EditCustomer` | 20 |
| Delete Customer | `DeleteCustomer` | 8 |
| New Account | `NewAccount` | 16 |
| Edit Account | `EditAccount` | 8 |
| Delete Account | `DeleteAccount` | 8 |
| Balance Enquiry | `BalanceEnquiry` | 7 |
| Mini Statement | `MiniStatement` | 8 |
| Customized Statement | `CustomizedStatement` | 17 |

---

## Tech Stack

- **Language:** Python 3
- **Test Framework:** `unittest`
- **Browser Automation:** Selenium WebDriver (Firefox)

---

## Project Structure

```
Banking-Site-Test-Suite/
├── docs/                              # Project report and peer feedback
├── tests/
│   ├── test_GuruBank_Group9.py        # Main test suite (120 tests)
│   └── test_testCases9_UPDATED.py     # Updated account tests (32 tests)
└── .vscode/settings.json             # VSCode unittest configuration
```

---

## Requirements

- Python 3.x
- Selenium: `pip install selenium`
- Firefox browser + [geckodriver](https://github.com/mozilla/geckodriver/releases) in your PATH

---

## Running the Tests

**Via VSCode:** Use the built-in Test Explorer — unittest discovery is pre-configured.

**Via terminal:**
```bash
python -m unittest discover -v -s tests -p "test_*.py"
```
