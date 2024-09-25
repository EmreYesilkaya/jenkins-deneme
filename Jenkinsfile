pipeline {
    agent none

    environment {
        DOCKER_IMAGE = "emreyesilkaya/time-checker" 
        DOCKER_TAG = "${BUILD_NUMBER}" 
    }

    stages {
        stage('Docker Build ve Push') {
            agent { label 'master' }
            steps {
                script {
                    // Docker Hub'a giriş yap
                    withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                    // Docker imajını oluştur ve Docker Hub'a yükle
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

        stage('Kubernetes Deploy') {
            agent { label 'master' }
            steps {
                script {
                    // Kubernetes pod'u deploy et
                    sh """
                    kubectl run time-checker --image=${DOCKER_IMAGE}:${DOCKER_TAG} --restart=Never --command -- python time_script.py
                    """
                }
            }
        }
    }

    post {
        always {
            node('master') {
                sh "docker logout"
            }
        }
    }
}