pipeline {
    agent any

    stages {
        stage('Create virtualenv') {
            steps {
                echo "${PATH}"
                bat "git submodule update --init --recursive"
                bat "poetry install"
                bat "poetry show --top-level -vv"
            }
        }

        stage('Execute tests') {
            steps {
                catchError(buildResult: 'SUCCESS', message: 'Tests failed') {
                    bat "poetry run pytest -m \"${Scope}\" --driver ${Driver} --env ${AutomationEnv}"
                }
            }
        }

        stage('Build report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
