pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management:v1 .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images | grep employee-management'
            }
        }

    }
}
