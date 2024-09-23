pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('jenkins:latest').inside {
                        sh 'başardın"'
                    }
                }
            }
        }
        stage('dockerhuba push') {
            steps {
                script {
                    sh 'docker tag jenkins:latest emreyesilkaya/jenkins:latest'
                    sh 'docker push emreyesilkaya/jenkins:latest'
                    }
                }
            }
        }
    }
}