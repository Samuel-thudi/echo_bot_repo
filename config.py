#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "40351e5d-934c-4a15-99c9-8499d98a1ca2")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "GS58Q~5pqt31koSlkxuJiNwcuOdhzIm2mnM8pca9")
    APP_TYPE = os.environ.get("MicrosoftAppType","MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId","")
