# Selenium4 X Pytest X Allure
Selenium4 in combination with Pytest test framework, and allure retorting example.


## Setup for Windows

### Install Allure 
1. Download Java 8+ : https://www.oracle.com/java/technologies/downloads/
2. Set `JAVA_HOME` environment variable, point it to the java root folder.
3. Download and unpack latest allure release: https://github.com/allure-framework/allure2/releases
   4. Or using Scoop: https://allurereport.org/docs/gettingstarted-installation/#install-via-scoop-for-windows
5. Into `PATH` - add path to the allure.bat file. Ex: `*\allure\allure-2.24.1\bin`


## TODO
2. Find how to reuse same browser session (Now each test starts own webdriver)
2. Find how to not start the browser at all (for API tests for example)
   3. Probably need to get rid off a pytest-selenium plugin.
3. 