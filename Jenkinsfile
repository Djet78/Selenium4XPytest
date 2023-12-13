/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('install test dependencies') {
            steps {
                echo 'Test SCM change'
                bat '''
                pytest -m "internal"
                pip install -r submodules\type_validator\requirements.txt
                pip install -r submodules\wd_actions\requirements.txt
                pip install -r requirements.txt

                pip freeze
                '''
            }
        }
    }
}