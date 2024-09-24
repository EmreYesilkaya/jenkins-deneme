pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "3"
    }
    stages {
        stage('Docker build') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        stage('Remove existing container') {
            steps {
                script {
                    sh '''
                    docker ps -a | grep jenkins-test && docker rm -f jenkins-test || true
                    '''
                }
            }
        }
        stage ('Docker run') {
            steps {
                script {
                    // Docker imajını çalıştırıyoruz
                    sh 'docker run -d --name jenkins-test ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        stage('Docker Hub Login') {
            steps {
                script {
                    // Docker Hub lgiriş
                    withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                    }
                }
            }
        }
        stage('Docker Hub Push') {
            steps {
                script {
                    // Docker imajını Docker Hub'a push ediyoruz
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        stage('Kubernetes Deploy') {
            steps {
                script {
                    // Kubernetes ile yeni bir deployment oluşturuyoruz
                        sh '''
                            kubectl apply -f - <<EOF
                            apiVersion: apps/v1
                            kind: Deployment
                            metadata:
                              name: jenkins-deployment
                            spec:
                              replicas: 1
                              selector:
                                matchLabels:
                                  app: jenkins
                              template:
                                metadata:
                                  labels:
                                    app: jenkins
                                spec:
                                  containers:
                                  - name: jenkins-container
                                    image: ${DOCKER_IMAGE}:${DOCKER_TAG}
                                    ports:
                                    - containerPort: 8080
                            EOF
                        '''
                    }
                }
            }
    
    }
}