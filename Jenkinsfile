pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'mywebapp:latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aemull/Latihan_git_uhuy.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").run("-d -p 8501:8501")
                }
            }
        }
    }
}
