pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'mkdir -p allure_results'
                sh 'echo "Installing all needed dependencies..."'
                sh 'pwd && ls -al'
                //sh 'apt-add-repository ppa:qameta/allure'
                //sh 'apt-get update'
                //sh 'apt-get install allure'
                sh 'python -m venv test-env'
                sh '. test-env/bin/activate && pip install -r requirements.txt && chmod 777 ./chromedriver && pytest test'
            }
        }
        stage('Reports') {
            steps {
                allure([
      	            includeProperties: false,
      	            jdk: '',
      	            properties: [],
      	            reportBuildPolicy: 'ALWAYS',
      	            results: [[path: 'allure_results']]
    	            ])
  	            }
            }
        }
    }