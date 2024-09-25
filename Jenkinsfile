pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          serviceAccountName: jenkins
          containers:
          - name: kubectl
            image: bitnami/kubectl:latest
            command:
            - cat
            tty: true
          - name: docker
            image: docker:latest
            command:
            - cat
            tty: true
            volumeMounts:
            - name: docker-sock
              mountPath: /var/run/docker.sock
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock
      '''
    }
  }
  
  environment {
    DOCKER_IMAGE = "emreyesilkaya/jenkins"
    DOCKER_TAG = "${BUILD_NUMBER}"
  }
  
  stages {
    stage('Docker Build ve Push') {
      steps {
        container('docker') {
          withCredentials([usernamePassword(credentialsId: 'df4ec335-a92d-46a8-ae3a-5c7b852481bc', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            sh '''
              echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
              docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
              docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
            '''
          }
        }
      }
    }
    
    stage('Kubernetes Deploy') {
      steps {
        container('kubectl') {
          sh '''
            kubectl set image deployment/your-deployment-name your-container-name=${DOCKER_IMAGE}:${DOCKER_TAG}
            kubectl rollout status deployment/your-deployment-name
          '''
        }
      }
    }
  }
}