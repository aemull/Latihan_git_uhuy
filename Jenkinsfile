pipeline {
    agent any

    environment {
        // Definisikan variabel lingkungan yang diperlukan
        GIT_REPO = 'https://github.com/aemull/Latihan_git_uhuy'
        GIT_BRANCH = 'master'
        DOCKER_IMAGE = 'finance_app:latest'
        DOCKER_CONTAINER_NAME = 'my_dashboard_app_container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning repository dari GitHub
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                // Membangun Docker image
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Menghentikan dan menghapus container yang berjalan sebelumnya
                    sh """
                    if [ \$(docker ps -aq -f name=${DOCKER_CONTAINER_NAME}) ]; then
                        docker stop ${DOCKER_CONTAINER_NAME}
                        docker rm ${DOCKER_CONTAINER_NAME}
                    fi
                    """
                    // Menjalankan container baru dari image yang telah dibangun
                    sh "docker run -d --name ${DOCKER_CONTAINER_NAME} -p 8501:8501 ${DOCKER_IMAGE}"
                }
            }
        }
    }
}
