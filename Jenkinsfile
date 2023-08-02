pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'cd /tmp'
                sh 'rm -rf pet'
                sh 'mkdir pet'
                sh 'cd pet'
                sh 'python3 -m venv test-env'
                sh '. test-env/bin/activate'
                sh 'pip3 install -r requirements.txt --user'
                sh 'pytest test'
            }
        }
    }
}