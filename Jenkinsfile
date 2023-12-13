/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Install test dependencies') {
            steps {
                echo 'Test SCM change'
                bat '''
                pip install -r submodules/type_validator/requirements.txt
                pip install -r submodules/wd_actions/requirements.txt
                pip install -r requirements.txt

                pip freeze
                '''
            }
        }
    }
}