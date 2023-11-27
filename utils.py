import functools

import pymongo

from pusher import Pusher


@functools.lru_cache(maxsize=None)
def get_mongodb_client():
    from djoser.conf import settings
    client = pymongo.MongoClient(
        settings.MONGO_HOST,
        settings.MONGO_PORT,
        username=settings.MONGO_USER,
        password=settings.MONGO_PASSWORD,
    )
    return client[settings.MONGO_DB]


@functools.lru_cache()
def get_pusher():
    client = Pusher(
        '1184761',
        key='abcac9dd524eef266863',
        secret='f373f63b0c90067512f6',
        cluster='eu',
    )
    return client


if __name__ == '__main__':
    p = get_pusher()
    p.trigger('channel_1','notification', {'user_id':1,'message':'Salut utilisateurs'})