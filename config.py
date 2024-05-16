#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "8c5246b2-711d-4c66-9d3e-a52d795384d6")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "xXV8Q~R~3OPNr4uKh6ISgSqCA22ZKqH07pq3CanH")
