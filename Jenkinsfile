/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Run Internal Tests') {
            steps {
                echo 'Test SCM change'
                bat '''
                pytest -m "internal"
                '''
            }
        }
    }
}