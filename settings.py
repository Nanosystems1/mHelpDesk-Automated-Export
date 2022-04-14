# -*- coding: utf-8 -*-
# filename          : settings.py
# description       : Different options for main.py
# author            : Ian Ault
# email             : service@nanosystems1.com
# date              : 04-11-2022
# version           : v1.0
# usage             : python main.py
# notes             : This file should not be run directly
# license           : MIT
# py version        : 3.10.2
#==============================================================================
# Sets the browser option "--headless", this will prevent the browser from
# opening a GUI window.
# Because of this, the "--disable-gpu" flag is also enabled when HEADLESS is
# set to True.
# The default value is True.
HEADLESS = False

# Starting link to begin crawling invoices
LINK = "https://secure1.mhelpdesk.com/Modules/Accounting/Invoices_Page.aspx?mhd_enc=x3bLL/enJTFdtFnkyW7OOA=="

# Login Information for mHelpDesk (not implimented)
EMAIL_ADDRESS = None
PASSWORD = None
