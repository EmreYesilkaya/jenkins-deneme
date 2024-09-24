pipeline {
    agent any
    stages {
        stage('run docker') {
            steps {
                script {
                    def img = 'httpd:2.4-alpine'
                    docker.image(img).run('-d -p 8080:80')
                }
            }
        }
    }
}