pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                docker {
                    image 'emreyesilkaya/jenkins'
                }
            
            }
            steps{
                sh 'docker run -it emreyesilkaya/jenkins .'
            }
        }

     

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                
            }
        }
    }
} 