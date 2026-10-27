pipeline {
  agent any
  parameters {
    choice(name: 'VERSION', choices: ['v1', 'v2', 'v3'], description: 'Version to build')
  }
  environment {
    IMAGE = "aditya12317/grade-system:${params.VERSION}"
    PATH = "/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:${env.PATH}"
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: "${params.VERSION}", url: 'https://github.com/aditya0043501/grade-system.git'
      }
    }
    stage('Docker Build') {
      steps { sh "docker build -t ${IMAGE} ." }
    }
    stage('Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
            usernameVariable: 'U', passwordVariable: 'P')]) {
          sh 'echo $P | docker login -u $U --password-stdin'
          sh "docker push ${IMAGE}"
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps { sh "kubectl apply -f k8s/${params.VERSION}.yaml" }
    }
  }
}
