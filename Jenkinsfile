pipeline {
    agent any // Herhangi bir ajan kullanılabilir.

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins" // Docker imajının ismi
        DOCKER_TAG = "${BUILD_NUMBER}" // Her build için otomatik artan versiyon numarası
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
            agent {
                kubernetes {
                    yaml """
                        apiVersion: v1
                        kind: Pod
                        metadata:
                          labels:
                            app: my-app
                        spec:
                          containers:
                          - name: my-app
                            image: ${DOCKER_IMAGE}:${DOCKER_TAG}
                            ports:
                            - containerPort: 80
                    """
                }
            }
            steps {
                // Uygulamanın çalıştığını simüle etme ve deploy mesajı yazdırma
                container('my-app') {
                    sh 'echo "Uygulama başarıyla deploy edildi ve çalışıyor!"'
                    sh 'sleep 30' // Uygulamanın simülasyonu için
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