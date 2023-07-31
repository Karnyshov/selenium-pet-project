pipeline {
    agent { docker { image 'python:3.9-slim-bullseye' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip3 install virtualenv'
                sh 'virtualenv venv -p python3'
  -             sh 'source venv/bin/activate'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pip3 install -r requirements.txt --user'
                sh 'pytest test'
            }
        }
    }
}