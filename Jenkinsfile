pipeline {
    agent any

    // Определяем параметр ENV с двумя возможными значениями: dev и prod
    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Выберите среду для деплоя')
    }

    stages {
        stage('Preparation') {
            steps {
                script {
                    echo "=============================="
                    echo "   Deploying to ${params.ENV}   "
                    echo "=============================="
                }
            }
        }

        stage('Clean Workspace') {
            steps {
                // Очищаем рабочую директорию перед клонированием/копированием
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                // Клонируем репозиторий заново (можно, если нужно)
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/RuCatGH/time-metrics-app.git']]
                ])
            }
        }
        stage('Deploy via SSH') {
            steps {
                // Используем Publish Over SSH
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'prod-server',   // имя, указанное в глобальных настройках
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**/*',   // все файлы из workspace
                                    removePrefix: '',      // без удаления префиксов
                                    remoteDirectory: '',   // можно оставить пустым, если указан Remote Directory глобально
                                    execCommand: """
                                        # Этот блок выполнится на удалённом сервере после копирования
                                        echo "Files were copied to ${params.ENV} environment"
                                    """.stripIndent()
                                )
                            ],
                            usePromotionTimestamp: false,
                            verbose: true
                        )
                    ]
                )
            }
        }
    }

    post {
        success {
            echo "Деплой ${params.ENV} ENV завершён успешно."
        }
        failure {
            echo "Деплой ${params.ENV} ENV завершился с ошибкой."
        }
    }
}
