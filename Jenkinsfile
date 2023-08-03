pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pwd && ls -al'
                sh 'python -m venv test-env'
                sh '. test-env/bin/activate && pip install -r requirements.txt && pytest test'
            }
        }
    }
}