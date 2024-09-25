pipeline {
    agent any 

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins" 
        DOCKER_TAG = "${BUILD_NUMBER}" 
        credentialsId = 'df4ec335-a92d-46a8-ae3a-5c7b852481bc'
    }

    stages {
        stage('Docker Build ve Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

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
                          terminationGracePeriodSeconds: 180  # 3 dakika sonra otomatik kapanma
                    """
                }
            }
            steps {
                container('my-app') {
                    // Pod 3 dakika çalışacak ve her 10 saniyede bir saati gösterecek
                    sh 'echo "Uygulama çalışmaya başladı. Her 10 saniyede bir saati gösterecek..."'
                    sh 'sleep 180'  // 3 dakika boyunca çalışmasını simüle et
                }
            }
        }
    }

    post {
        always {
            // Docker Hub'dan çıkış yap
            sh "docker logout"
        }
    }
}