# Selenium4 X Pytest X Allure
Selenium4 in combination with Pytest test framework, and allure retorting example.


## Setup for Windows

### Install Allure 
1. Download Java 8+ : https://www.oracle.com/java/technologies/downloads/
2. Set `JAVA_HOME` environment variable, point it to the java root folder.
3. Download and unpack latest allure release: https://github.com/allure-framework/allure2/releases
   4. Or using Scoop: https://allurereport.org/docs/gettingstarted-installation/#install-via-scoop-for-windows
5. Into `PATH` - add path to the allure.bat file. Ex: `*\allure\allure-2.24.1\bin`

### Used python main packages:
1. pytest
2. selenium
3. allure
4. requrests

### Jenkins configuration for local win11 agent:
1. Complete Win installation of Jenkins: https://www.jenkins.io/doc/book/installing/windows/ 
1. Install required non default plugins:
   2. Pyenv Pipeline - https://plugins.jenkins.io/pyenv-pipeline/
   3. Allure - https://plugins.jenkins.io/allure-jenkins-plugin/

2. Configure the Allure plugin: https://allurereport.org/docs/integrations-jenkins/ - 
3. Add following env. variables for Jenkins: 
   4. `PythonPath` - Path to a python exe, ie: `C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312` 
4. Configure Jenkins pipeline:
   5. Fetch git from here: https://github.com/Djet78/Selenium4XPytest
6. 




## TODO
6. Add API tests (3). 
   7. """Update `def selenium(request):` fixture to create driver only for UI tests.""" - instead was added marks for tests. So if test no need selenium - it won't be used.
   9. Add some default connector classes for SqlDB
4. Add user factory (at least some template).
5. Add different `pytest.ini` file for different envs. 
5. Add urls_mapper for different envs.
6. Add linter
   7. Add type checker? https://www.infoworld.com/article/3575079/4-python-type-checkers-to-keep-your-code-clean.html
8. 
