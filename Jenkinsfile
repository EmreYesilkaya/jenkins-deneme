pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
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
                sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }

        stage('Trigger Kubernetes Job') {
            steps {
                script {
                    sh 'kubectl apply -f kubectl-job.yaml'
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}