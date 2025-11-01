import valkey

valkey_connection = valkey.Valkey(host='localhost', port=6379, db=0)

def main():
    valkey_connection.lpush("test_queue", "Hello")
    print("Push successful!")


if __name__ == "__main__":
    main()
