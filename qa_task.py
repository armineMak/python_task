import argparse
import requests
import lxml.html
import re
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

try:
	parser = argparse.ArgumentParser()
	parser.add_argument('--url', help='web page url', required=True)
	args = parser.parse_args()
	print(args.url)

	regex = re.compile(
		r'^(?:http|ftp)s?://'
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
		r'localhost|'
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
		r'(?::\d+)?'
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	if re.match(regex, args.url) is None:
		raise Exception("Invalid URL. Please enter valid URL")

	response = requests.get(args.url, verify=False)
	tree = lxml.html.fromstring(response.text)
	img_elem = tree.xpath('//img')
	print("Here are numbers of the images on the HTML: ", len(img_elem))
	form_elem = tree.xpath('//form[@method="get"]')
	form_elem1 = tree.xpath('//form[@method="GET"]')
	get_method = form_elem + form_elem1
	print("Here are numbers of the form get method: ", get_method)

except requests.exceptions.ConnectionError as e:
	requests.status_code = "Connection refused"
	print("Connection refused")
except Exception as err:
	print(err)