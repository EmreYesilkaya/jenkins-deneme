pipeline {
    agent { 
        docker {
        image 'docker:latest'
        args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
}

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