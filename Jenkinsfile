pipeline {
    agent any // Jenkins ana sunucusunda çalıştır

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Docker Build ve Push') {
            steps {
                script {
                    // Docker Hub'a giriş yap
                    withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                    
                    // Docker imajını build et ve push et
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                script {
                    // Kubernetes'e deploy et
                    withKubeConfig([credentialsId: 'my-kubeconfig']) {
                        sh "kubectl set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh "kubectl rollout status deployment/your-deployment-name"
                    }
                }
            }
        }
    }

    post {
        always {
            sh "docker logout"
        }
    }
}