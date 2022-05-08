pipeline {
    agent {
        label 'jenkins_docker'
    }

    stages {
        stage('build') {
            steps {
                sh 'docker build -t calc_image .'
            }
        }
        stage ('test') {
            steps {
                sh 'docker run calc_image python /app/test.py 1 2'
            }
        }
    }
}
