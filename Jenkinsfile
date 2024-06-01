pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "streamlit_dashboard"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout kode dari GitHub
                git url: 'https://github.com/aemull/Latihan_git_uhuy.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker Image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh """
                        docker ps -q --filter "name=$DOCKER_IMAGE" | grep -q . && docker stop $DOCKER_IMAGE || true
                        docker ps -aq --filter "name=$DOCKER_IMAGE" | grep -q . && docker rm $DOCKER_IMAGE || true
                    """

                    // Run Docker Container
                    sh 'docker run -d -p 8501:8501 --name $DOCKER_IMAGE $DOCKER_IMAGE'
                }
            }
        }
    }
}
