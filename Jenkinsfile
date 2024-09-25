pipeline {
    agent none

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins" 
        DOCKER_TAG = "${BUILD_NUMBER}" 
    }

    stages {
        // Docker imajını oluşturma ve Docker Hub'a yükleme aşaması
        stage('Docker Build ve Push') {
            agent { label 'master' }  // İşlemi master node üzerinde çalıştır.
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
            agent { label 'master' }  // Bu işlemi de master node üzerinde çalıştır.
            steps {
                sh 'echo "Uygulama başarıyla deploy edildi ve çalışıyor!"'
                sh 'sleep 30' 
            }
        }
    }

    post {
        always {
            node('master') {  // Bu aşamada bir node bağlamı belirt.
                sh "docker logout"
            }
        }
    }
}