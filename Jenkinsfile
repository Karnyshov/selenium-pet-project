pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pwd && ls -al'
                sh 'python3 -m venv test-env'
                sh 'source test-env/bin/activate'
                sh 'pip3 install -r requirements.txt --user'
                sh 'pytest test'
            }
        }
    }
}