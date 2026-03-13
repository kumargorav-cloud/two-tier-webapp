pipeline {

    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                sh 'rm -rf *'
            }
        }

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

        stage('Verify Docker Image') {
            steps {
                sh 'docker images'
            }
        }

    }

}
