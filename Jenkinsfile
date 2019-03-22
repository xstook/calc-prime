pipeline {
  agent any
  stages {
    stage('Calculate') {
      steps {
        sh './prime.py -b'
      }
    }
  }
}