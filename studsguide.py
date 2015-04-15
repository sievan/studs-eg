from pyrise import *

Highrise.set_server('https://edgeguideab.highrisehq.com')
Highrise.auth('f4075d9e048c00bda63ec55794d02831')

deal = Deal.all()
for deal in deal:
	print "%s" % deal.name
