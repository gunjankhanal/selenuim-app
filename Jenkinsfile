pipeline {
    agent any

    stages {
        stage('Building') {
            steps {
                echo 'Building Maven Project....'
                sh 'sleep 6'
            }
        }
        
        stage('Testing') {
            steps {
                echo 'Integration Testing Done....'
                sh 'sleep 6'
            }
        }
        stage('Deployment to K8S') {
            steps {
                echo 'Deployment Done on Kubernetes Cluster'
                sh 'sleep 3'
            }
        }'
        stage('Send Email Altert') {
            steps {
                echo 'Email Alert done....'
                sh 'sleep 3'
            }
        }
    }
}
