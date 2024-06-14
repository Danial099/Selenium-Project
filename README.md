360 Manager Automated Testing

This project contains automated tests for the admin functionality of user creation within the 360 Manager web portal. The tests are designed using Selenium for web automation, Python 3 for scripting, and Pytest for managing the tests. The primary goal is to validate the login and user creation functionalities, providing a scalable foundation for future test development.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Tests](#running-the-tests)
- [Test Details](#test-details)
- [Future Expansion](#future-expansion)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is part of a screening challenge to assess the ability to create scalable test components for the 360 Manager customer web portal. The provided tests focus on:
1. Logging in with admin credentials.
2. Retrieve username and password that are automatically generated for the new customer .
3. Fill out the form, entering values for all required fields, and save as the new customer 

## Project Structure
TestAutomationChallenge/
├── tests/
│   ├── __init__.py
│   └── test_user_creation.py
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── user_creation_page.py
├── conftest.py
├── requirements.txt
└── README.md

*Create and activate a virtual environment (optional but recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

1. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Tests

To run the tests, navigate to the project directory and use the following command:

```sh
pytest 
pytest tests/test_admin_login.py
pytest tests/test_customer_list.py
pytest tests/test_dashboard.py
pytest tests/test_login_new_user.py
pytest tests/test_user_creation.py

