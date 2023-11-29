#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0a257a2a-7973-4b48-847b-c78332e92881")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "dP68Q~N9eKTdH-T7vbGJpS0YoROtYBoarmdg8bBx")
    APP_TYPE = os.environ.get("MicrosoftAppType","MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId","")
