import unittest
import sys
import logging
from node.util import logmsg
from node.util import LogMsgType

logger = logging.getLogger()

class TestUtil(unittest.TestCase):
    
    def test_log_enum_error(self):
        with self.assertRaises(AttributeError):
            logmsg(logger.info,LogMsgType.ONMSG_NOT_EXIST, 'TEST HERE FOO')
            
    def test_log(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        try:
            logmsg(logger.info,LogMsgType.ONMSG, 'TEST HERE FOO')
            if not hasattr(sys.stdout, "getvalue"):
                self.fail("need to run in buffered mode")
            output = sys.stdout.getvalue().strip()
            self.assertEquals(output,'ONMSG : TEST HERE FOO')
        finally:
            logger.removeHandler(stream_handler)

if __name__ == '__main__':
    unittest.main()
