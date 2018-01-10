#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LPS33HW: MEMS pressure sensor: 260-1260 hPa absolute digital output barometer with water-resistant package"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	INTERRUPT_CFG = 11
	THS_P_L = 12
	THS_P_H = 13
	WHO_AM_I = 15
	CTRL_REG1 = 16
	CTRL_REG2 = 17
	CTRL_REG3 = 18
	FIFO_CTRL = 20
	REF_P_XL = 21
	REF_P_L = 22
	REF_P_H = 23
	RPDS_L = 24
	RPDS_H = 25
	RES_CONF = 26
	INT_SOURCE = 37
	FIFO_STATUS = 38
	STATUS = 39
	PRESS_OUT_XL = 40
	PRESS_OUT_L = 41
	PRESS_OUT_H = 42
	TEMP_OUT_L = 43
	TEMP_OUT_H = 44
	LPFP_RES = 51
