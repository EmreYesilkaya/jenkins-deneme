pipeline {
    agent {
        kubernetes {
            yaml '''
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: kubectl-container
                image: bitnami/kubectl:latest
                command:
                - cat
                tty: true
            '''
        }
    }
    
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
        KUBECONFIG = credentials('my-kubeconfig') // Kubeconfig credential
    }
    
    stages {
        stage('Environment Check') {
            steps {
                sh 'printenv'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                sh 'kubectl --kubeconfig=${KUBECONFIG} set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}