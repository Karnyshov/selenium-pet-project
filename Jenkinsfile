pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pwd && ls -al'
                sh 'python -m venv test-env'
                sh '. test-env/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pytest test'
            }
        }
    }
}