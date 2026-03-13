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
                    passwordVariable: 'PASSWORD'
                )]) {
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
                withCredentials([usernamePassword(
                    credentialsId: 'github-credentials',
                    usernameVariable: 'GIT_USERNAME',
                    passwordVariable: 'GIT_PASSWORD'
                )]) {

                    sh '''
                    git config --global user.email "ci-bot@devops.local"
                    git config --global user.name "ci-bot"

                    git add helm/two-tier-webapp/values.yaml
                    git commit -m "update image tag $IMAGE_TAG"

                    git push https://$GIT_USERNAME:$GIT_PASSWORD@github.com/kumargorav-cloud/two-tier-webapp.git HEAD:main
                    '''
                }
            }
        }

    }
}
