pipeline {
    agent any
    parameters {
        string(name: 'NUMPROCESS', defaultValue: '1', description: 'Number of processes')
        string(name: 'TESTS', defaultValue: '', description: 'Tests name')
    }
    environment {
        GIT_REPO = 'https://github.com/ola290919/API_sppi.git'
        ALLURE_RESULTS = 'allure-results'
        NUMPROCESS = "${params.NUMPROCESS}"
        TESTS = "${params.TESTS}"
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: "${env.GIT_REPO}"
            }
        }
        stage('Install dependencies for tests') {
            steps {
             withCredentials([file(credentialsId:'env_api',variable:'ENV_API')]){
              catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip3 install -r requirements.txt
                cp ${ENV_API} .env
                pytest --numprocesses ${NUMPROCESS} --alluredir ${ALLURE_RESULTS} ${TESTS}
                rm -f .env
                '''
              }
             }
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${env.ALLURE_RESULTS}"]]
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}