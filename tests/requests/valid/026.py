# -*- coding: utf-8 -*-

request = {
    "method": "GET",
    "uri": uri("/test/unicode_header"),
    "version": (1, 1),
    "headers": [
        ("TEST", "test тест"),
    ],
    "body": b""
}
