pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
        KUBECONFIG = credentials('my-kubeconfig') // Kubeconfig credential
    }
    
    stages {
        stage('Environment Check') {
            steps {
                sh 'printenv'
            }
        }

        // Kubectl'in kurulu olduğunu kontrol et
        stage('Check Kubectl Installation') {
            steps {
                script {
                    def kubectlCheck = sh(script: 'which kubectl', returnStatus: true)
                    if (kubectlCheck != 0) {
                        error "kubectl not found, exiting."
                    } else {
                        echo "kubectl is installed."
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials-id', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                script {
                    def deployCmd = "kubectl --kubeconfig=${KUBECONFIG} set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                    sh deployCmd
                }
            }
        }
    }

    post {
        always {
            // Docker'dan logout yap
            sh 'docker logout'
        }
    }
}