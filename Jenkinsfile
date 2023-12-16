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
            parallel {
                stage('Test on Chrome') {
                    steps {
                        withPythonEnv('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312') {
                            catchError(buildResult: 'SUCCESS', message: 'Tests failed') {
                                bat "pytest -m \"ui\" --driver chrome --env ${AutomationEnv}"
                            }
                        }
                    }
                }

                stage('Test on FireFox') {
                    steps {
                        withPythonEnv('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312') {
                            catchError(buildResult: 'SUCCESS', message: 'Tests failed') {
                                bat "pytest -m \"ui\" --driver firefox --env ${AutomationEnv}"
                            }
                        }
                    }
                }

                stage('Test API') {
                    steps {
                        withPythonEnv('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python312') {
                            catchError(buildResult: 'SUCCESS', message: 'Tests failed') {
                                bat "pytest -m \"api" --env ${AutomationEnv}"
                            }
                        }
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
