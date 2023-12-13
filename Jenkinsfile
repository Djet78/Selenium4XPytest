/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Run Internal Tests') {
            steps {
                echo 'Test SCM change'
                bat '''
                pytest -m "internal"
                pip install -r submodules\type_validator\requirements.txt submodules\wd_actions\requirements.txt requirements.txt

                pip freeze
                '''
            }
        }
    }
}