from pyrise import *
from datetime import datetime
import sched, time, pirate_speak
Highrise.set_server('froxy')
Highrise.auth('f4075d9e048c00bda63ec55794d02831')

deal_ids = []
new_deals = []
start_time = datetime.now()
s = sched.scheduler(time.time, time.sleep)
counter = 0
passive_aggressive = 0
def swag(sc, counter, passive_aggressive):
	msg = "Polling..."
	counter += 1
	deals = Deal.all()
	new_deals = []
	for deal in deals:
		if start_time < deal.created_at and not deal.id in deal_ids:
			deal_ids.append(deal.id)
			new_deals.append(deal)
			passive_aggressive = 0
			print "%s" % pirate_speak.translate(deal.name)
	if counter > 5:
		if passive_aggressive == 0:
			msg = "Getting bored here..."
			passive_aggressive += 1
			counter = 0
		elif passive_aggressive == 1:
			msg = "Nothing is happening!"
			passive_aggressive += 1
			counter = 0
		elif passive_aggressive == 2:
			msg = "Why am I still doing this?"
			passive_aggressive += 1
			counter = 0
		elif passive_aggressive == 3:
			msg = "What is my purpose? What is life?"
			passive_aggressive = 0
			counter = 0 
	print msg

	sc.enter(1, 1, swag, (sc, counter, passive_aggressive))

s.enter(1, 1, swag, (s, counter, passive_aggressive))
s.run()

