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
