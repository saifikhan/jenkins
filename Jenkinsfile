pipeline {
    agent any 
    stages {
        stage('run') {
            steps {
                echo 'python script execution BEGIN'
                sh -c 'python env.py'
                echo 'python script execution END'
            }
        }
    }
}
