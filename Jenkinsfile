pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                  - name: docker
                    image: docker:dind
                    command:
                    - cat
                    tty: true
                    privileged: true
                    volumeMounts:
                    - name: dind-storage
                      mountPath: /var/lib/docker
                  - name: kubectl
                    image: bitnami/kubectl:latest
                    command:
                    - cat
                    tty: true
                  volumes:
                  - name: dind-storage
                    emptyDir: {}
            '''
        }
    }
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "3"
    }
    stages {
        stage('Docker build') {
            steps {
                container('docker') {
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        stage('Docker Hub Login') {
            steps {
                container('docker') {
                    withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                    }
                }
            }
        }
        stage('Docker Hub Push') {
            steps {
                container('docker') {
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                container('kubectl') {
                    withKubeConfig([credentialsId: 'kubernetes-config']) {
                        sh '''
                        cat <<EOF | kubectl apply -f -
                        apiVersion: apps/v1
                        kind: Deployment
                        metadata:
                          name: jenkins-test-deployment
                        spec:
                          replicas: 1
                          selector:
                            matchLabels:
                              app: jenkins-test
                          template:
                            metadata:
                              labels:
                                app: jenkins-test
                            spec:
                              containers:
                              - name: jenkins-test
                                image: ${DOCKER_IMAGE}:${DOCKER_TAG}
                                ports:
                                - containerPort: 8080
                        ---
                        apiVersion: v1
                        kind: Service
                        metadata:
                          name: jenkins-test-service
                        spec:
                          selector:
                            app: jenkins-test
                          ports:
                            - protocol: TCP
                              port: 80
                              targetPort: 8080
                          type: LoadBalancer
                        EOF
                        '''
                    }
                }
            }
        }
    }
}