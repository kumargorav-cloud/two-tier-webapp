pipeline {

    agent any

    environment {
        IMAGE_NAME = "kumargoravcloud/two-tier-webapp"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG -f docker/Dockerfile ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                credentialsId: 'dockerhub-credentials',
                usernameVariable: 'USERNAME',
                passwordVariable: 'PASSWORD')]) {

                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
            }
        }

        stage('Update Helm Chart') {
            steps {
                sh """
                sed -i 's/tag:.*/tag: $IMAGE_TAG/' helm/two-tier-webapp/values.yaml
                """
            }
        }

        stage('Push Changes to GitHub') {
            steps {
                sh """
                git config --global user.email "jenkins@devops.com"
                git config --global user.name "jenkins"
                git add helm/two-tier-webapp/values.yaml
                git commit -m "update image tag $IMAGE_TAG"
                git push origin HEAD:main
                """
            }
        }

    }

}
