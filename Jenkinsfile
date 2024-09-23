pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script
                    sh 'docker build -t jenkins:latest .'
                }
            }
        stage('dockerhuba push') {
            steps {
                script {
                    //imagea çeken bölüm burası olcak
                    sh 'docker tag jenkins:latest emreyesilkaya/jenkins:latest'
                    sh 'docker push emreyesilkaya/jenkins:latest'
                }
            }
        }
    
    }
}

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Docker image build etme
                    sh 'docker build -t jenkins:latest .'
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    // Docker image tag'leme ve push etme
                    sh 'docker tag jenkins:latest yemreyesilkaya/jenkins:latest'
                    sh 'docker push yemreyesilkaya/jenkins:latest'
                }
            }
        }
    }
}