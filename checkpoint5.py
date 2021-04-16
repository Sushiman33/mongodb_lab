from pymongo import MongoClient
from random import randint
from datetime import datetime
client = MongoClient('localhost', 27017)

db = client.mongo_db_lab
definitions = db.definitions


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    index = randint(0,definitions.count_documents({})-1)
    definitions.update_one({'word':definitions.find()[index]['word']},
       {'$push':{'dates':str(datetime.utcnow())}})
    doc = definitions.find()[index]
    print("word: \"{}\"".format(doc['word']))
    print("defintion: \"{}\"".format(doc['definition']))
    print("dates: {}".format(', '.join(doc['dates'])))
    return


if __name__ == '__main__':
    random_word_requester()
