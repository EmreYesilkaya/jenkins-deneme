pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
        KUBERNETES_MASTER = "138.201.189.196"  // Master node IP'si
    }
    stages {
        stage('Docker build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                }
            }
        }
        stage('Docker Hub Push') {
            steps {
                sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }
        stage('Kubernetes Deploy') {
            steps {
                script {
                    def deployCmd = "kubectl set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                    
                    // Eğer Jenkins Kubernetes içinde çalışıyorsa:
                    sh deployCmd
                    
                    // Eğer Jenkins Kubernetes dışında çalışıyorsa ve SSH kullanmanız gerekiyorsa:
                    //sh """
                    // sshpass -p 'Sgnm238..' ssh -o StrictHostKeyChecking=no master@${KUBERNETES_MASTER} '${deployCmd}'
                    //"""
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}