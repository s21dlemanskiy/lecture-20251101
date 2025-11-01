import valkey

# Подключение к Valkey
valkey_connection = valkey.Valkey(host='localhost', port=6379, db=0, decode_responses=True)

pubsub = valkey_connection.pubsub()
pubsub.subscribe('my_queue')

print("Ожидание сообщений...")
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Получено: {message['data']}")