pipeline {
    agent {
        label 'jenkins_docker'
    }

    stages {
        stage('build') {
            steps {
                sh 'docker pull python:3.9'
            }
        }
        stage ('test') {
            steps {
                sh 'docker run --rm -v $(pwd)/app:/app python:3.9 python /app/test.py'
            }
        }
    }
    post {
        always {echo 'This is always'}
        failure {echo 'This is failure'}
        success {echo 'This is success'}
    }
}
