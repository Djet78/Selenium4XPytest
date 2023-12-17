# Selenium4 X Pytest X Allure
Selenium4 in combination with Pytest test framework, and allure retorting example.

#### Used python main packages:
1. pytest
2. selenium
3. allure
4. requrests
5. poetry

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
2. In the project root dir - run `poetry install`
3. Activate created env: `.\.venv\Scripts\activate` 

---



## TODO
6. Add API tests (3). 
   9. Add some default connector classes for SqlDB
6. Add linter
   7. Add type checker? https://www.infoworld.com/article/3575079/4-python-type-checkers-to-keep-your-code-clean.html
8. Add pytest-cov to type_checker submodule (package should be already there)
