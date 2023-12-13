/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Run Internal Tests') {
            steps {
                echo 'Test SCM change'
                bat '''
                pytest -m "internal"
                pip install -r submodules\type_validator\requirements.txt
                            -r submodules\wd_actions\requirements.txt
                            -r requirements.txt

                pip freeze
                '''
            }
        }
    }
}