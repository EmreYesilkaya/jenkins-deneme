pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "2"
    }
    stages {
        stage('Docker build') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        stage ('Docker run') {
            steps {
                script {
                    sh 'docker run -t ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        stage('Docker Hub Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credential-id', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                    }
                }
            }
        }
        stage('Docker Hub Push') {
            steps {
                script {
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        stage('Kubernetes Deploy') {
            steps {
                script {
                    // Secret file kullanarak kubeconfig'i kullanıyoruz
                    withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                        sh '''
                            export KUBECONFIG=${KUBECONFIG}
                            kubectl set image deployment/jenkins-deployment jenkins-container=${DOCKER_IMAGE}:${DOCKER_TAG} --record
                        '''
                    }
                }
            }
        }
    }
}