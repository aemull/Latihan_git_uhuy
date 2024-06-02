pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "streamlit_dashboard"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aemull/jkblc-devops.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh """
                        docker ps -q --filter "name=$DOCKER_IMAGE" | grep -q . && docker stop $DOCKER_IMAGE || true
                        docker ps -aq --filter "name=$DOCKER_IMAGE" | grep -q . && docker rm $DOCKER_IMAGE || true
                    """

                    sh 'docker run -d -p 8501:8501 --name $DOCKER_IMAGE $DOCKER_IMAGE'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh "docker rm -f $(docker ps -a -q --filter ancestor=$DOCKER_IMAGE)"
                    sh "docker rmi $DOCKER_IMAGE"
                }
            }
        }
    }
}
