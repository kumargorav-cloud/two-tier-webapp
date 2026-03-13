pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t two-tier-webapp -f docker/Dockerfile .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images'
            }
        }

    }

}
