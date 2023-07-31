pipeline {
    agent { docker { image 'python:3.9-slim-bullseye' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pip3 install virtualenv'
                sh 'virtualenv venv -p python3'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt --user'
            }
        }
    }
}