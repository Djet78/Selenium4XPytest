/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('Run Internal Tests') {
            steps {
                sh 'pytest -m "internal"'
            }
        }
    }
}