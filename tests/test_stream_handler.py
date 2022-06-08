from io import StringIO
import sys
import unittest
from unittest.mock import patch

from src.handlers import StreamHandler


class StreamHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.rene_message = "The amount to pay RENE is: 215 USD"
        self.astrid_message = "The amount to pay ASTRID is: 85 USD"
        self.handler = StreamHandler(StringIO())

    def test_rene_emit(self):
        self.handler.emit(self.rene_message)
        self.assertMultiLineEqual(
            self.handler.file.getvalue(), "The amount to pay RENE is: 215 USD\n"
        )

    def test_astrid_emit(self):
        self.handler.emit(self.astrid_message)
        self.assertMultiLineEqual(
            self.handler.file.getvalue(), "The amount to pay ASTRID is: 85 USD\n"
        )


if __name__ == "__main__":
    unittest.main()
