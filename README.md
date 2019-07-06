# Continuous Integration With Python: An Introduction

Welcome to Python Continuos Integration on Windows Machine

## Essential Python Extensions for VSCode

![Python Extensions in VSCode](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/python-extensions-in-vscode.PNG)

## 📗 Step 1. Environment Setup

👉 **Step 1. Install Python at your local box**

`https://www.python.org/`

![install python step-1](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/install-python-step-1.PNG)

👉 **Step 2.Confirm Python is installed**

![Confirm Python is installed](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/confirm-python-installed.PNG)

## 📗 Step 2. Installing Virtual Environment on Windows

👉 **Step 1. Install VirtualEnv**

```sh
pip install virtualenv
```

![Install VirtualEnv](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/install-virtualenv.PNG)

## 📗 Step 3. Creating Virtual Environment for Your Project

👉 **Step 1. Create Virtual Environment on Windows**

Run Below Script

```sh
# In your Command Prompt navigate to your project:

cd your_project

#Within your project run below script:
virtualenv env
```

![Creating Virtual Environment for Your Project](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/creating-project-venv.PNG)

You will notice your project will get env folder

![env in folder structure](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/env-folder-after-creating-virtual-env.PNG)

👉 Step 2. **Activate Virtual Environment on Windows**

Identify `activate.bat` file and run it.

![Find Activate.bat File](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/activate-bat-file-in-project.PNG)

`env\Scripts\activate.bat`

![activate bat file](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/activating-env-locally.PNG)

## 📗 Step 4. Preparing for Unit Tests

💡 For Test Driven Development we need Tests.
Also in order to secure our code from other devlopers such that they dont break the functionality we need to run test for entire project everytime we check-in code in to source repository.

👉 **Step 1. Install Unit Testing & Test Coverage Python Modules**
Run Below Script to install `flake8` , `pytest`, and `pytest-cov`.

```sh
pip install flake8 pytest pytest-cov
```

![Install Unit Testing & Test Coverage Python Modules](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/installing-unit-test-pckgs.PNG)

👉 **Step 2. Store external Dependencies in a Requirement.txt file**

```sh
pip freeze > requirements.txt
```

![Requirements file freeze](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/freeze%20requirements.PNG)

![Requirements file](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/requirements%20-file.PNG)

## 📗 Step 5. Writing Unit Test

👉 **Step 1. Creating Failing Test First**

Crate Test for Calculator

`src\test_calculator.py`

```py
"""
Unit Tests for the Calculator
"""

class TestCalculator:
    def test_i_can_add_numbers(self):
        assert 4 == calculator.add(2, 2)

    def test_i_can_subtract_numbers(self):
        assert 3 == calculator.subtract(5, 2)

```

Run below script to run test

`pytest -v`

![RunningFailingTEst](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/running-failing-test.PNG)

👉 **Step 2. Pass the Failing Test by Writing Production Code Required to Just Pass the Test**

`src\calculator.py`

```py
"""
Calculator Module
"""


def add(first_num, second_num):
    return first_num + second_num


def subtract(first_num, second_num):
    return first_num - second_num

```

`src\test_calculator.py`

```py
"""
Unit Tests for the Calculator
"""

import calculator


class TestCalculator:
    def test_i_can_add_numbers(self):
        assert 4 == calculator.add(2, 2)

    def test_i_can_subtract_numbers(self):
        assert 3 == calculator.subtract(5, 2)

```

👉 **Step 3. Run Test Again**

Run below script to run test

`pytest -v`

![passing test](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/passing-test.PNG)

**Folder Structure of the code base**

![Code Base Folder Src](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/folder-structure.PNG)

**Run Below Script to See the code coverage**

```sh
pytest -v --cov
```

![code coverage](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/code-coverage.PNG)

## 📗 Step 6. Connect to CircleCI

👉 **Step 1. Create the .circleci folder inside your repository**
👉 **Step 2. Create config.yml file with below content**

```yml
# Python CircleCI 2.0 configuration file
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:3.7

    working_directory: ~/repo

    steps:
      # Step 1: obtain repo from GitHub
      - checkout
      # Step 2: create virtual env and install dependencies
      - run:
          name: install dependencies
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      # Step 3: run linter and tests
      - run:
          name: run tests
          command: |
            . venv/bin/activate
            flake8 --exclude=venv* --statistics
            pytest -v --cov=calculator
```

![circle ci folder structure](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/circle-ci-folder-structure.PNG)

![circle ci website build success](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/build-success-incircleci.PNG)

## 📗 Step 7. Make Changes

👉 **Step 1. Add Multiply Test**
`src\test_calculator.py`

```py
    def test_i_can_multipy_numbers(self):
        assert 20 == calculator.multiply(4, 5)
```

![multiply failing test locally](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/failing-multiply-test.PNG)

Try Check-in your code and you will see error on circle ci website

![multiply failing test build machine](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/circle-ci-multiplication-failed.PNG)

👉 **Step 2. Fix Multiply Test**

`src\calculator.py`

```py
def multiply(first_num, second_num):
    return first_num * second_num

```

![multiply passing test locally](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/test-passing-multiply-locally.PNG)

![multiply passing test on circle-ci](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/multiply-test-passing-oncircleci.PNG)

## 📗 Step 8. Running Test in Watch ( Continuos Testing)

Run Below script to install `pytest-watch`

```sh
pip install pytest-watch
```

![pytest in watch](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/running-test-in-watchmode.PNG)

![Running Test in Watch](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/test-running-while-code-changing.PNG)

![Running Test in Watch mode and passing](https://github.com/rupeshtiwari/python-ci-example/blob/master/docs/test-running-while-code-changing-pass.PNG)

## 📗 Step 9. Updating Requirements.txt File

👉 **Step 1. Delete old Requirements.txt File**

👉 **Step 2. Create New Requirements.txt File**

Run Script

```sh
pip freeze > requirements.txt
```

![New Requirements File]()

💡 How to install packages using pip according to the requirements.txt file from a local directory.

**Run Below Script**

```sh
pip install -r requirements.txt
```
