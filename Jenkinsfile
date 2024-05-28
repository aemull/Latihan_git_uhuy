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

        stage('Setup Virtual Environment') {
            steps {
                // Membuat dan mengaktifkan virtual environment
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                // Menginstal dependencies yang diperlukan menggunakan pip
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                // Menjalankan aplikasi Streamlit
                sh '''
                . venv/bin/activate
                streamlit run app.py --server.port 8501
                '''
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
