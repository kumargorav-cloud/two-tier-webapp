pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                sh 'git clone https://github.com/kumargorav-cloud/two-tier-webapp.git .'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t two-tier-webapp -f docker/Dockerfile .'
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }

    }

}
