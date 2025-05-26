#!/bin/bash

# Запускаем Flask-приложение в фоне
nohup python app.py > app.log 2>&1 &
APP_PID=$!
sleep 3  # Ждём, пока сервер запустится

# Выполняем запрос
RESPONSE=$(curl -s http://127.0.0.1:5000/time)
TIME=$(echo "$RESPONSE" | jq -r '.time')

# Останавливаем сервер
kill $APP_PID

# Проверяем результат
if [[ "$TIME" =~ ^[0-9]+$ && "$TIME" -gt 0 ]]; then
  echo "✅ Test passed: /time returned valid Unix time: $TIME"
  exit 0
else
  echo "❌ Test failed: /time returned invalid time: $TIME"
  cat app.log
  exit 1
fi
