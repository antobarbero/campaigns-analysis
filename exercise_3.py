import csv


def get_campaigns(filename):
	with open(filename) as csvfile:
		return list(csv.DictReader(csvfile))


def order_by_payout(filename):
	"""
	Returns a list of campaigns ID's, order by payout from highest to lowest
	"""
	campaigns = get_campaigns(filename)
		
	values = {c["id"]: c['payout'] for c in campaigns}
	campaigns = [int(key) for key in sorted(values, key=values.get, reverse=True)]

	return campaigns


def order_by_total_payout(filename):
	"""
	Returns a list of campaigns ID's, order by total payout from highest to
	lowest
	>>> total_payout = payout * installs
	"""
	campaigns = get_campaigns(filename)

	values = {c["id"]: float(c['payout'].replace(',', '.')) * int(c['installs'])for c in campaigns}
	campaigns = [int(key) for key in sorted(values, key=values.get, reverse=True)]
	
	return campaigns


def order_by_cr(filename):
	"""
	Returns a list of campaigns ID's, order by conversion rate (CR) from highest
	to lowest
	>>> CR = impressions / installs
	"""
	campaigns = get_campaigns(filename)
	
	values = {c["id"]: int(c['impressions']) / int(c['installs']) for c in campaigns}
	campaigns = [int(key) for key in sorted(values, key=values.get, reverse=True)]

	return campaigns


if __name__ == '__main__':
	payout_order = [17, 14, 22, 7, 11, 15, 23, 13, 18, 12, 6, 1, 3, 10, 25, 24, 21, 16, 20, 5, 4, 8, 9, 19, 2]
	total_payout_order = [ 15, 11, 18, 7 , 14, 21 , 3 , 6 , 25, 13 , 16 , 5 , 24 , 20, 17, 23, 1 , 10, 8 , 9 , 19, 12, 4 , 22, 2]
	#cr_order = [ 11, 15, 18, 25, 21, 7, 8, 24, 6 , 14, 3 , 9 , 5 , 16, 19, 10, 20, 2 , 13 , 4 , 17, 1, 23, 12, 22]
	# I replaced the variable cr_order because the old one was sorted from lowest to the highest,
	# and the assignment ask from highest to lowest
	cr_order = [22, 12, 23, 1, 17, 4, 13, 2, 20, 10, 19, 16, 5, 9, 3, 14, 6, 24, 8, 7, 21, 25, 18, 15, 11]

	assert order_by_payout('campaigns.csv') == payout_order
	assert order_by_total_payout('campaigns.csv') == total_payout_order
	assert order_by_cr('campaigns.csv') == cr_order
