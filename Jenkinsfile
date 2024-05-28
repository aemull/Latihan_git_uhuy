pipeline {
    agent any

    environment {
        // Definisikan variabel lingkungan yang diperlukan
        GIT_REPO = 'https://github.com/aemull/Latihan_git_uhuy'
        GIT_BRANCH = 'master'
        //APP_DIR = 'my_dashboard_app'
    }

    stages {
        
        stage('Clone Repository') {
            steps {
                // Cloning repository dari GitHub
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Menginstal dependencies yang diperlukan menggunakan pip
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Menjalankan tes (jika ada)
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                // Menjalankan aplikasi Streamlit
                sh 'streamlit run app.py'
            }
        }
    }

    post {
        always {
            // Membersihkan lingkungan kerja setelah selesai
            cleanWs()
        }
    }
}
