import os

def main():
    print('Hello from the python file - script1.py')
    # receive .env variables from ./script1.yml
    token = os.environ.get('API_TOKEN_1')
    if not token:
        raise RuntimeError('NOT FOUND - API_TOKEN_1')
    print(f"api_token_1 found with value: {token}")

if __name__ == '__main__':
    main()
