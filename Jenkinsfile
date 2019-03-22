pipeline {
  agent any
  stages {
    stage('Calculate') {
      steps {
        echo 'Starting calculate prime.'
        sh './prime.py -b'
        echo 'Done.'
      }
    }
  }
}