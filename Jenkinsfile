pipeline {
    agent any

    environment {
        // Definisikan variabel lingkungan yang diperlukan
        GIT_REPO = 'https://github.com/aemull/Latihan_git_uhuy.git'
        GIT_BRANCH = 'master'
        IMAGE_NAME = 'my_dashboard_app'
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
                // Build Docker image
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Menjalankan container di latar belakang
                    sh "docker run -d -p 8501:8501 --name my_dashboard_container ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        always {
            // Membersihkan lingkungan kerja setelah selesai
            cleanWs()
        }
        success {
            // Membersihkan container Docker sebelumnya
            script {
                sh "docker rm -f my_dashboard_container || true"
            }
        }
        failure {
            // Membersihkan container Docker jika build gagal
            script {
                sh "docker rm -f my_dashboard_container || true"
            }
        }
    }
}
