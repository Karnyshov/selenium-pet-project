pipeline {
    agent { docker { image 'python:3.9-slim-bullseye' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'python3 -m venv test_env'
                sh 'source test_env/bin/activate'
                sh 'pip3 install -r requirements.txt --user'
                sh 'pytest test'
            }
        }
    }
}