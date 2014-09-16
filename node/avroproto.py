import json
import logging
import avro.schema
from types import *
from avro_json_serializer import AvroJsonSerializer


class AvroProto(object):

    def __init__(self):
        self.log = logging.getLogger(
            '%s' % (self.__class__.__name__)
        )
        with open('proto/avro_hello.avsc', 'r') as data_file:
            jsondata = json.load(data_file)
            avro_schema = avro.schema.make_avsc_object(jsondata)
            self.serializerHello = AvroJsonSerializer(avro_schema)
        with open('proto/avro_page.avsc', 'r') as data_file:
            jsondata = json.load(data_file)
            avro_schema = avro.schema.make_avsc_object(jsondata)
            self.serializerPage = AvroJsonSerializer(avro_schema)

    def hello_json(self, pubkey, uri, guid, nickname):
        assert type(pubkey) is StringType, "pubkey is not a string: %r" % pubkey
        assert type(uri) is StringType, "uri is not a string: %r" % uri
        assert type(guid) is StringType, "guid is not a string: %r" % guid
        assert type(nickname) is StringType, "nickname is not a string: %r" % nickname
        return self.hello_json_raw({'type': 'hello',
                                    'pubkey': pubkey,
                                    'uri': uri,
                                    'senderGUID': guid,
                                    'senderNick': nickname})

    def hello_json_raw(self, json_data):
        try:
            return self.serializerHello.to_json(json_data)
        except Exception as e:
            self.log.error('Message Hello Schema Error %s' % e)
            raise

    def page_json_raw(self, json_data):
        try:
            return self.serializerPage.to_json(json_data)
        except Exception as e:
            self.log.error('Message Page Schema Error %s' % e)
            raise

avroproto = AvroProto()
