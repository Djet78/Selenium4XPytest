[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

# Selenium4 X Pytest X Allure
Selenium4 in combination with Pytest test framework, and allure retorting example.

#### Used python main packages:
1. `pytest` - Test runner
2. `selenium` - Web UI interactions driver
3. `allure` - reporting
   1. `allure-pytest` - integration with pytest
4. `requrests` - API interactions 
5. `poetry` - Dependencies management
6. `ruff` - Linter and formatting tool

---

## Setup for Windows

### 1. Install Allure 
1. Download Java 21 : https://www.oracle.com/java/technologies/downloads/
2. Set `JAVA_HOME` environment variable, point it to the java root folder.
3. Download and unpack latest allure release: https://github.com/allure-framework/allure2/releases
   1. Or using Scoop: https://allurereport.org/docs/gettingstarted-installation/#install-via-scoop-for-windows
4. Into `PATH` - add path to the allure.bat file. Ex: `*\allure\allure-2.24.1\bin`


### 2. Install Poetry
1. Install pipx via pip - https://github.com/pypa/pipx?tab=readme-ov-file
2. Install poetry via pipx - https://python-poetry.org/docs/#installing-with-pipx 
3. Add poetry executable into `PATH`. Ex: `c:\users\test\.local\bin`


### 3. Jenkins configuration for local win11 agent:
1. Download Java 21 : https://www.oracle.com/java/technologies/downloads/
2. Set `JAVA_HOME` environment variable, point it to the java root folder.
3. Complete Win installation of Jenkins: https://www.jenkins.io/doc/book/installing/windows/ 
4. Install required non default plugins:
   1. Allure - https://plugins.jenkins.io/allure-jenkins-plugin/

5. Configure the Allure plugin: https://allurereport.org/docs/integrations-jenkins/ - 
6. Configure Jenkins pipeline:
   1. Fetch git from here: https://github.com/Djet78/Selenium4XPytest
   2. And use Jenkinsfile script form repo


### 4. Configure local project: 
1. Clone the repo
2. Run `git submodules --init --recursive`
3. Run `pre-commit install`
4. Run `pre-commit install-hooks`
5. In the project root dir - run `poetry install`
6. Activate created env: `.\.venv\Scripts\activate` 



---



## TODO
1. Add some default connector classes for SqlDB
2. Add test execution into CI for type_validator package 
3. Add requests class, to handle timeouts, requests sending, file upload and so on. 

