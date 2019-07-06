# python-ci-example

Welcome to Python Continuos Integration on Windows Machine

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

![Install Unit Testing & Test Coverage Python Modules]()

👉 **Step 2. Store external Dependencies in a Requirement.txt file**

```sh
pip freeze > requirements.txt
```

![Requirements file]()