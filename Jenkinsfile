pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo imagen Docker (simulado)...'
                sh '''
                    echo "Compilando código fuente"
                    echo "docker build -t app-vulnerable:latest ."
                '''
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Ejecutando escaneo de seguridad con OWASP ZAP (simulado)...'
                sh '''
                    echo "docker run --rm zaproxy/zap-stable zap-baseline.py -t http://localhost:5000 -r zap-report.html"
                    echo "Generando reporte zap-report.html (simulado)"
                '''
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
                sh '''
                    echo "docker run -d --name app-vulnerable -p 5000:5000 app-vulnerable:latest"
                    echo "Aplicación desplegada en entorno local (simulado)"
                '''
            }
        }
    }
}
