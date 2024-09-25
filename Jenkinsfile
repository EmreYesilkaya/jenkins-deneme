pipeline {
    agent any 

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins" 
        DOCKER_TAG = "${BUILD_NUMBER}" 
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
                      - name: jnlp
                        image: jenkins/inbound-agent:4.10-3
                        args: ["\${computer.jnlpmac}", "\${computer.name}"]
                    """
                }
            }
            steps {
                container('my-app') {
                    sh 'echo "Uygulama başarıyla deploy edildi ve çalışıyor!"'
                    sh 'sleep 30' 
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