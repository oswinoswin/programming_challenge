#!/usr/bin/python3
import argparse
import datetime


def calculate_age(birth_date):
	now = datetime.datetime.now()
	delta =  now - birth_date
	return delta.total_seconds()

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("year")
	parser.add_argument("month")
	parser.add_argument("day")
	args = parser.parse_args()
	year = int(args.year)
	month = int(args.month)
	day = int(args.day)
	birth_date = datetime.datetime(year, month, day)
	print("Yous age in seconds: {}".format(calculate_age(birth_date)))
