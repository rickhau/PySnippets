#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This code snippet is to get filesize

import os

if __name__ == "__main__":
    filename = 'getFileSize.py'
    print os.path.getsize(filename)
    print os.stat(filename).st_size
