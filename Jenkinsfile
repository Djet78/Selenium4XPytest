pipeline {
    agent any

    stages {
        stage('Create virtualenv') {
            steps {
                echo "${PATH}%"

                withPythonEnv('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312') {
                    bat "git submodule update --init --recursive"
                    bat "pip install -r submodules/type_validator/requirements.txt"
                    bat "pip install -r submodules/wd_actions/requirements.txt"
                    bat "pip install -r requirements.txt"
                    bat "pip freeze"
                }
            }
        }

        stage('Execute tests') {
            steps {
                withPythonEnv('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312') {
                    catchError(buildResult: 'SUCCESS', message: 'Tests failed') {
                        bat "pytest -m \"${Scope}\" --driver ${Driver} --env ${AutomationEnv}"
                    }
                }
            }
        }

        stage('Build report') {
            steps {
                withPythonEnv('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312') {
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                }
            }
        }
    }

}
