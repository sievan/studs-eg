from pyrise import *
import sched, time
Highrise.set_server('froxy')
Highrise.auth('f4075d9e048c00bda63ec55794d02831')

deal_ids = []
new_deals = []
s = sched.scheduler(time.time, time.sleep)
def swag(sc):
	print "Polling..."
	deals = Deal.all()
	new_deals = []
	for deal in deals:
		if not deal.id in deal_ids:
			deal_ids.append(deal.id)
			new_deals.append(deal)
			print "%s" % deal.name
	sc.enter(5, 1, swag, (sc,))

s.enter(5, 1, swag, (s,))
s.run()

