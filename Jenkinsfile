pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "emreyesilkaya/jenkins"
        DOCKER_TAG = "${BUILD_NUMBER}"
        KUBECONFIG = credentials('kubeconfig-credentials-id') // Kubeconfig credential
    }
    
    stages {
        // Ortam Değişkenlerini Kontrol Et
        stage('Environment Check') {
            steps {
                sh 'printenv'
            }
        }

        // Kubectl'in Kurulu Olduğunu Kontrol Et
        stage('Check Kubectl Installation') {
            steps {
                script {
                    def kubectlCheck = sh(script: 'which kubectl', returnStatus: true)
                    if (kubectlCheck != 0) {
                        error "kubectl not found, exiting."
                    } else {
                        echo "kubectl is installed."
                    }
                }
            }
        }

        // Eğer Kubectl Yüklü Değilse Yükle
        stage('Install Kubectl if Not Installed') {
            steps {
                script {
                    def kubectlCheck = sh(script: 'which kubectl', returnStatus: true)
                    if (kubectlCheck != 0) {
                        echo "Installing kubectl..."
                        sh '''
                        curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                        chmod +x kubectl
                        sudo mv kubectl /usr/local/bin/
                        '''
                    } else {
                        echo "kubectl is already installed."
                    }
                }
            }
        }

        // Docker İmajını Build Et
        stage('Docker Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        // Docker Hub'a Giriş Yap
        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin'
                }
            }
        }

        // Docker İmajını Push Et
        stage('Docker Push') {
            steps {
                sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }

        // Kubernetes'e Deploy Et
        stage('Kubernetes Deploy') {
            steps {
                script {
                    // Kubeconfig dosyasını kullanarak Kubernetes cluster'ına bağlanma
                    def deployCmd = "kubectl --kubeconfig=${KUBECONFIG} set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}"
                    
                    // Kubectl komutunu çalıştır
                    sh deployCmd
                }
            }
        }
    }

    post {
        always {
            // Docker'dan Logout Yap
            sh 'docker logout'
        }
    }
}