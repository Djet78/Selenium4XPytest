/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Install test dependencies') {
            steps {
                echo 'Test SCM change'

                bat '''
                pip3 install -r submodules/type_validator/requirements.txt
                pip3 install -r submodules/wd_actions/requirements.txt
                pip3 install -r requirements.txt

                pip3 freeze
                '''
            }
        }
    }
}