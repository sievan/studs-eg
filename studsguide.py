from pyrise import *
from datetime import datetime
import sched, time
Highrise.set_server('froxy')
Highrise.auth('f4075d9e048c00bda63ec55794d02831')

deal_ids = []
start_time = datetime.now()
s = sched.scheduler(time.time, time.sleep)
def swag(sc):
	print "Polling..."
	deals = Deal.all()
	for deal in deals:
		if start_time < deal.created_at and not deal.id in deal_ids:
			deal_ids.append(deal.id)
			print "%s" % "Deal '" + deal.name + "' added."
	sc.enter(5, 1, swag, (sc,))

s.enter(5, 1, swag, (s,))
s.run()

