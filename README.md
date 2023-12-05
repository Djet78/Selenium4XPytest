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
