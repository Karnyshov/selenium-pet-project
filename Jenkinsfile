pipeline {
    agent { docker { image 'python:3.9-slim-bullseye' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'sudo -H pip install -r requirements.txt --user'
                sh 'pytest test'
            }
        }
    }
}