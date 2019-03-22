pipeline {
  agent any
  stages {
    stage('Print Start') {
      agent any
      steps {
        echo 'Starting the calculate prime benchmark.'
      }
    }
    stage('Calculate') {
      steps {
        sh '.prime.py -b'
      }
    }
    stage('Print Done') {
      steps {
        echo 'Done'
      }
    }
  }
}