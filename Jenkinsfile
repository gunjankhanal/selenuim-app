pipeline {
    agent {label node_a}

    stages {
        stage('Git Version') {
            steps {
                echo 'Git Version....'
                sh 'git version'
            }
        }
        
        stage('Java Version') {
            steps {
                echo 'Java Version....'
                sh 'java --version'
            }
        }
        stage('See Running COntainers') {
            steps {
                echo 'See Running COntainers'
                sh 'docker ps'
            }
        }
        stage('Send Email Altert') {
            steps {
                echo 'Email Alert done....'
                sh 'sleep 3'
            }
        }
    }
}
