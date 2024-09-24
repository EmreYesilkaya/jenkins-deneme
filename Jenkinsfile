pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"  
        DOCKER_TAG = "2"  // tagı daha kolay koyabilmek için
    }
    stages {
        stage('Docker build') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        stage ('Docker run'){
            steps {
                script {
                    sh 'docker run -t ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        stage('Docker Hub Login') {
            steps {
                script {
                    // Docker Hub'da oturum açma
                    withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
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
    }
}