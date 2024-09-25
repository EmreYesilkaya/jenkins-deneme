pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
        KUBECONFIG = credentials('my-kubeconfig') // Kubeconfig credential
        MASTER_NODE_IP = "138.201.189.196" // Master node IP adresi
    }
    
    stages {
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
                withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
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

        // Kubernetes Deploy (SSH ile Master Node'da çalıştır)
        stage('Kubernetes Deploy') {
            steps {
                script {
                    def deployCmd = "kubectl --kubeconfig=${KUBECONFIG} set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                    
                    // SSH ile master node'da kubectl komutunu çalıştır
                    sh """
                    sshpass -p 'your-master-node-password' ssh -o StrictHostKeyChecking=no user@${MASTER_NODE_IP} '${deployCmd}'
                    """
                }
            }
        }
    }

    post {
        always {
            // Docker logout
            sh 'docker logout'
        }
    }
}