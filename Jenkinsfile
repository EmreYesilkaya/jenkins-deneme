pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t jenkins:latest .'
                sh 'echo "Build başarılı"'
            }
        }
    }
    
 }