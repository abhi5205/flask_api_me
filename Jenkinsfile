pipeline {
    agent  any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                echo 'Building your flask docker image...'
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Run container') {
            steps {
                echo 'cleaning up old container and starting app...'
                sh 'docker rm -f flask-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-container my-flask-app'
            }
       }
    }

    post {
        success {
            echo 'Bro, it worked your app is live'
        }
        failure {
            echo 'something went wrong. check the logs'
        }
    }
}
