#!/usr/bin/env python
# pip install -r requirements.txt
# -*- coding: utf-8 -*-

import ConfigParser
import twitter
import sys
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse
import argparse
import warnings

if not sys.warnoptions:
	warnings.simplefilter("ignore")

def the_args():

	example = '''\n

Example:

python %s -repourl https://www.github.com/user/repo
''' % (sys.argv[0])

	parser = argparse.ArgumentParser(
		description="Post latest repo commit message to twitter",epilog=example,formatter_class=argparse.RawTextHelpFormatter)

	required = parser.add_argument_group('required arguments')

	required.add_argument(
		'-repourl', help='URL to repo, i.e., https://www.github.com/user/repo',required=True)

	args = parser.parse_args()

	repourl = args.repourl

	return repourl + "/commit/master"

repourl = the_args()

def get_msg(repourl):

	url = repourl
	req = urllib2.Request(url)
	req.add_header(
		'User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; da; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)')
	response = urllib2.urlopen(req)
	lines = response.readlines()
	soup = BeautifulSoup(str(lines))

	for line in lines:
		if "<title>" in line:
			sys.stdout = open('message.txt','w')
			print line.replace("<title>","").replace("</title>","").strip()
			urll = soup.find("meta", {"property": "og:url"})
			print (urlparse(str(urll)).path).replace('<meta content="',"").replace('" property=',"").replace('"og:url"/>',"").strip()
			sys.stdout.close()

def send_msg():

	reload(sys)
	sys.setdefaultencoding('utf-8')

	config = ConfigParser.ConfigParser()
	config.readfp(open('config'))

	message = open(config.get('main', 'message')).read().split('\n', 1)

	api = twitter.Api(consumer_key=config.get('main','api_key'),
		consumer_secret=config.get('main','api_secret_key'),
		access_token_key=config.get('main', 'access_token'),
		access_token_secret=config.get('main', 'access_token_secret'))

	tweet = "%s" % " ".join(message).strip()
	send_message = api.PostUpdate(tweet)
	print "Sent message: \n" + tweet

def main():
	get_msg(repourl)
	send_msg()

if __name__ == "__main__":
	main()
