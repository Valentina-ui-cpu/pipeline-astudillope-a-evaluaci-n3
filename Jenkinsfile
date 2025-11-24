pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo imagen Docker...'
                sh '''
                    echo "Compilando código fuente y construyendo imagen Docker"
                    docker build -t app-vulnerable:latest .
                '''
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Ejecutando escaneo de seguridad con OWASP ZAP...'
                sh '''
                    # Escaneo baseline con ZAP usando la imagen oficial
                    # (se asume que la app corre en http://localhost:5000)
                    docker run --rm -v $(pwd):/zap/wrk/ zaproxy/zap-stable \
                      zap-baseline.py -t http://host.docker.internal:5000 \
                      -r zap-report.html || true
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
                echo 'Desplegando aplicación en entorno local...'
                sh '''
                    docker rm -f app-vulnerable || true
                    docker run -d --name app-vulnerable -p 5000:5000 app-vulnerable:latest
                '''
            }
        }
    }
}

