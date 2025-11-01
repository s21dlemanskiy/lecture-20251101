import valkey
import time

# Подключение к Valkey
valkey_connection = valkey.Valkey(host='localhost', port=6379, db=0, decode_responses=True)

channel = 'my_queue'

for i in range(10):
    message = f"Сообщение {i}"
    valkey_connection.publish(channel, message)
    print(f"Отправлено: {message}")
    time.sleep(1)