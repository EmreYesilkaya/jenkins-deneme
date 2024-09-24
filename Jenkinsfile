pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
metadata:
  name: kaniko
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
      - name: jenkins-docker-cfg
        mountPath: /kaniko/.docker
  volumes:
  - name: jenkins-docker-cfg
    secret:
      secretName: docker-credentials
      items:
        - key: .dockerconfigjson
          path: config.json
'''
        }
    }
    stages {
        stage('Build and Push with Kaniko') {
            steps {
                container('kaniko') {
                    script {
                        sh '''
                        /kaniko/executor --context `pwd` \
                                         --destination emreyesilkaya/my-python-app:${BUILD_NUMBER} \
                                         --destination emreyesilkaya/my-python-app:latest
                        '''
                    }
                }
            }
        }
    }
}