pipeline {
    agent none

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins" 
        DOCKER_TAG = "${BUILD_NUMBER}" 
        KUBE_NAMESPACE = "default"  // Kubernetes namespace'i burada belirtin
        DEPLOYMENT_NAME = "my-app-deployment"  // Deployment ismini burada belirtin
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

        // Kubernetes Deploy aşaması
        stage('Kubernetes Deploy') {
            agent { label 'master' }  // Bu işlemi de master node üzerinde çalıştır.
            steps {
                script {
                    // Kubernetes'de yeni image ile pod'u deploy et
                    sh """
                    kubectl set image deployment/${DEPLOYMENT_NAME} my-app=${DOCKER_IMAGE}:${DOCKER_TAG} -n ${KUBE_NAMESPACE}
                    kubectl rollout status deployment/${DEPLOYMENT_NAME} -n ${KUBE_NAMESPACE}
                    """
                }
            }
        }

        // Pod çıktısını gösterme aşaması
        stage('Show Pod Logs') {
            agent { label 'master' }  // Bu işlemi de master node üzerinde çalıştır.
            steps {
                script {
                    // Pod adını almak için podları listeleyip loglarını gösterecek komut
                    sh """
                    POD_NAME=\$(kubectl get pods -n ${KUBE_NAMESPACE} -l app=my-app -o jsonpath='{.items[0].metadata.name}')
                    echo "Pod adı: \$POD_NAME"
                    kubectl logs \$POD_NAME -n ${KUBE_NAMESPACE}
                    """
                }
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