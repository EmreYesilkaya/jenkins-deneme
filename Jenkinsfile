pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('jenkins:latest').inside {
                        sh 'echo "başardın"'  // Tırnak hatası düzeltildi
                    }
                }
            }
        }
        stage('dockerhuba push') {  // Doğru sırada kapatma parantezleri kullanıldı
            steps {
                script {
                    sh 'docker tag jenkins:latest emreyesilkaya/jenkins:latest'
                    sh 'docker push emreyesilkaya/jenkins:latest'
                }
            }
        }
    }
}