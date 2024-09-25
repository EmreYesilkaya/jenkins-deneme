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
                    yaml '''
                        apiVersion: v1
                        kind: Pod
                        spec:
                          serviceAccountName: jenkins
                          containers:
                          - name: kubectl
                            image: bitnami/kubectl:latest
                            command:
                            - cat
                            tty: true
                          - name: docker
                            image: docker:latest
                            command:
                            - cat
                            tty: true
                            volumeMounts:
                            - name: docker-sock
                              mountPath: /var/run/docker.sock
                          volumes:
                          - name: docker-sock
                            hostPath:
                              path: /var/run/docker.sock
                    '''
                }
            }
            steps {
                container('kubectl') {
                    withKubeConfig([credentialsId: 'my-kubeconfig']) {
                        sh "kubectl set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh "kubectl rollout status deployment/your-deployment-name"
                    }
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