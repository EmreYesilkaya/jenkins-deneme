pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Docker Build ve Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
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
                    """
                }
            }
            steps {
                container('my-app') {
                    sh 'echo "Uygulama başarıyla deploy edildi ve çalışıyor!"'
                    sh 'sleep 30' // Uygulamanın çalıştığını simüle etmek için
                }
            }
        }
    }

    post {
        always {
            sh "docker logout"
        }
    }
}