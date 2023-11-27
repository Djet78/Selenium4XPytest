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

## TODO
1. Add browser version data to env. file `pytest_report_collectionfinish`
3. Check if Safari webdriver can run on Windows. 
4. 