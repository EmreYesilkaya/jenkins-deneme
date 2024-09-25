pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        // Ortam değişkenlerini kontrol et
        stage('Environment Check') {
            steps {
                sh 'printenv'
            }
        }

        // Docker Image Build
        stage('Docker Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        // Docker Hub Login
        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials-id', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                }
            }
        }

        // Docker Image Push
        stage('Docker Push') {
            steps {
                sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }

        // Kubernetes Deploy (Doğrudan Jenkins Pod'da)
        stage('Kubernetes Deploy') {
            steps {
                script {
                    def deployCmd = "kubectl set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                    
                    // Kubectl komutunu doğrudan Jenkins pod'unda çalıştır
                    sh deployCmd
                }
            }
        }
    }

    post {
        always {
            // Docker'dan çıkış yap
            sh 'docker logout'
        }
    }
}