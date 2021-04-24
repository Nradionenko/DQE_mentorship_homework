pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        echo 'building the application'
      }
    }
    stage("test") {
      steps {
        echo 'testing the application'
            withPythonEnv('python3') {
              sh 'pip install pytest'
              sh 'pytest main.py'
    }
      }
    }
    stage("deploy") {
      steps {
        echo 'deploying the application'
      }
    }
  }
}
