pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script
                    sh 'docker build -t jenkins:latest .'
                }
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

