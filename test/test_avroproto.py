import unittest
from avro.io import AvroTypeException
import json
from node.avroproto import avroproto

class AvroTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_hello = """
                            {"pubkey": "04e504778536438e3883a2f8f64fd4c08036607a7bb8dbe210f8d0e2ea2597607640245062ae52c51808ebf7b57eb52d6bbe928045c6d9919d531afcbf23051b32", "senderGUID": "f703dd9e1efae617fc905f1f267a720d77930f98", 
                            "senderNick": "Seed 2 - Test Notary", 
                            "uri": "tcp://seed1.openbazaar.org:12345", 
                            "type": "hello"}
                            """

        cls.test_page = r"""
                            {"senderGUID": "38f2294d84c192e606b234739b5004297ccebf76",
                            "senderNick": "seed.openlabs.co",
                            "bitmessage": "",
                            "text": "products and services are not genuine",
                            "uri": "tcp://104.131.22.22:12345",
                            "arbiter_description": "",
                            "email": "",
                            "nickname": "seed.openlabs.co",
                            "arbiter": "True",
                            "notary": "True",
                            "guid": "e0215090f679d22b22d69801f1b673411a43882e",
                            "type": "page",
                            "sin": "9xHVXHRQkubTwb2opviBaeVgSodrEWeNx5q85D",
                            "PGPPubKey": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQENBFQIbmcBCADZoHhayGUpSdWkanTk+DghE9eHbSKNLUJzp7PY5Qg1CvkcaO8i\ntbMJDpaPVslVidNXCjfdJl71PwjJ6vFvXzISptYyH6gkS5uN18Fg+vg3gmT2NNB9\n3wbQmF31w+Sep/C2d1LF4EsgG6nuDFHBgbQTEkHCsYNIBj6Vo2sVbEKg9howAZ+7\nu6KGY8YdTKpPjWxjUrydhS8RsMfZijWaRgndwvSAQA8WmfMF6P71Q99lpvN1QEvE\nKFv72WwZp30t6EBl0Mf888KckINQrv5WbZ5ISJSTunZxZF0qqH5Gr0AK1xconmQ1\nJr3d68ju/NjGZzOSOfRI146CiERkM7lhjzwdABEBAAG0PkF1dG9nZW5lcmF0ZWQg\nS2V5IChBdXRvZ2VuZXJhdGVkIGJ5IE9wZW4gQmF6YWFyKSA8Z2Z5QGdmeS5jb20+\niQE4BBMBAgAiBQJUCG5nAhsvBgsJCAcDAgYVCAIJCgsEFgIDAQIeAQIXgAAKCRDI\nfUVKhctcFJaoCADUguGz427fJfeMRNPxqQ9xL24iDPebKHFDTIDpnD7P+kSw3asR\nagGvhdz3UCBjO9fka7p1NAZSNLXDTYK+0OnJ8/SsOsjdc5PM2OjXLQWCoFdzEhda\n7d9v9xlSRvUj9KTgXHyK/vj1EaN5HdUWCbqr3WKrS6GHKlHORpXvutwEw7l1/vmf\nrAXpBSzuEbSzjpK6E2zK/P11rY1a+GA8ebL3xd2nTi5On5PI7PnRiE1anUSQS4xL\nDpcEZT4SLOBgrLUr/ySzATCIe4Yx6bdEpKhzCY4stdhH2Bol8RByTFDVmQiB7BDY\njyPGr+53jeOt5DlyQD1XRJxE7N6dKxuRj/b8\n=alnh\n-----END PGP PUBLIC KEY BLOCK-----\n", "pubkey": "046a8988427dd298bee0792c8b5d02debe26b66d5975049dc1695b8c4b24ceffd14d6b256541a2144dbf1ac3ebf3b6ebc884cefdb15d06cf61ae44647f5890bb6d"}
                            """

    def testHelloSerialize(self):
        obj = json.loads(self.test_hello)
        self.assertEqual(json.loads(avroproto.hello_json("04e504778536438e3883a2f8f64fd4c08036607a7bb8dbe210f8d0e2ea2597607640245062ae52c51808ebf7b57eb52d6bbe928045c6d9919d531afcbf23051b32",
                                                         "tcp://seed1.openbazaar.org:12345", "f703dd9e1efae617fc905f1f267a720d77930f98", "Seed 2 - Test Notary")), obj)
    def testHelloJsonWrongArgument(self):
        x = {"04e50e", "tcp://seed1.openbazaar.org:12345", "f703dd9e1efae617fc905f1f267a720d77930f98", "Seed 2 - Test Notary"}
        self.assertRaises(TypeError, avroproto.hello_json, x)

    def testHelloJsonWrongArgumentType(self):
        x = {300, "tcp://seed1.openbazaar.org:12345", "f703dd9e1efae617fc905f1f267a720d77930f98", "Seed 2 - Test Notary"}
        self.assertRaises(TypeError, avroproto.hello_json, x)

    def testPageSerialize(self):
        obj = json.loads(self.test_page)
        self.assertEqual(json.loads(avroproto.page_json_raw(obj)), obj)

    def testHelloSerializeError(self):
        obj1 = json.loads(self.test_hello)
        obj1['type'] = 'hello-request-foo'
        self.assertRaises(AvroTypeException, avroproto.hello_json_raw, obj1)

    def testPageSerializeError(self):
        obj = json.loads(self.test_page)
        obj['type'] = 'page-foo'
        self.assertRaises(AvroTypeException, avroproto.page_json_raw, obj)
