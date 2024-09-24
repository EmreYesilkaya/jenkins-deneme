pipeline {
    agent any
    stages {
        stage('Docker build') {
            steps {
                script {
                    sh 'docker build -t time-python . '
                    
                }
            }
        }
        stage ('docker run'){
           steps{
              script{
                sh'docker run -t time-python'
              }
         }

        }
    }
}