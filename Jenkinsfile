pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo aplicación (simulado)...'
                sh 'echo Compilando código fuente'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas (simulado)...'
                sh 'echo Ejecutando pruebas unitarias y de seguridad'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación (simulado)...'
                sh 'echo Desplegando versión en entorno de producción local'
            }
        }
    }
}
