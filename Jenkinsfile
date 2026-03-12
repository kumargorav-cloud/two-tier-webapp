pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/<username>/two-tier-webapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t two-tier-webapp .'
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }

    }

}
