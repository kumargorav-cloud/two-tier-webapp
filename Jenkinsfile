pipeline {

    agent any

    stages {


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
