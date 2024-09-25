pipeline {
    agent any  // Bu pipeline herhangi bir uygun ajan üzerinde çalışacaktır.

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins" // Docker imajının ismi
        DOCKER_TAG = "${BUILD_NUMBER}" // Her build için otomatik artan versiyon numarası
        KUBE_NAMESPACE = "jenkins" // Kubernetes namespace'i
        DEPLOYMENT_NAME = "my-app-deployment" // Deployment ismi
    }

    stages {
        // Docker imajını oluşturma ve Docker Hub'a yükleme aşaması
        stage('Docker Build ve Push') {
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

        // Kubernetes'e deploy etme aşaması
        stage('Kubernetes Deploy') {
            steps {
                script {
                    // Kubernetes'de imajı güncelle ve deploy et
                    sh """
                    kubectl set image deployment/${DEPLOYMENT_NAME} my-app=${DOCKER_IMAGE}:${DOCKER_TAG} -n ${KUBE_NAMESPACE}
                    kubectl rollout status deployment/${DEPLOYMENT_NAME} -n ${KUBE_NAMESPACE}
                    """
                }
            }
        }
    }

    // Pipeline her zaman çalıştıktan sonra yapılacak işlemler
    post {
        always {
            // Docker Hub'dan çıkış yap
            sh "docker logout"
        }
    }
}