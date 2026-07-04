pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Build') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Docker Version') {
            steps {
                sh 'docker --version'
            }
        }

    }
}
