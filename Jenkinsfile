pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('build') {
            steps {
                sh '''apt-get install -y wget

                    # Set up the Chrome PPA
                    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
                    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

                    # Update the package list and install chrome
                    apt-get update -y
                    apt-get install -y google-chrome-stable
                    google-chrome --version'''
                sh 'python --version'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pwd && ls -al'
                sh 'python -m venv test-env'
                sh '. test-env/bin/activate && pip install -r requirements.txt && pytest test'
            }
        }
    }
}