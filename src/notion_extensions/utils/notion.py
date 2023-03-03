from notion_client import Client


def get_client(token):
    return Client(auth=token)
