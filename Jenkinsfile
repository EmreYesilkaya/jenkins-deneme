pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-python-app:latest .'  
                sh 'echo "Build başarılı"'
            }
        }
        
        stage('Run') {
            steps {
                sh 'docker run --rm my-python-app:latest'
                sh 'echo "Docker container çalıştırıldı"'
            }
        }
    }
}