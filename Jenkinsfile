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
                sh 'docker run --rm -v $(pwd)/app:/app python /app/test.py'
            }
        }
    }
}
