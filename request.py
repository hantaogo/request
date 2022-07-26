# coding=utf-8
from __future__ import unicode_literals
from requests import Request, Session
import json
import time
import codecs
import sys

def doRequest(url, method = 'GET', payload = {}, query = {}, headers = {}, timeout = 10, encoding = 'utf8', logFile=None, outputFile=None, pretty=False):
	t1 = time.time()

	data = json.dumps(payload)

	session = Session()

	req = Request(method, url, data=data, headers=headers, params=query)

	prepped = session.prepare_request(req)

	resp = session.send(prepped, timeout=timeout, verify=True, proxies={ 'http': None, 'https': None })	

	resp.encoding = encoding
	
	t2 = time.time()

	dt = t2 - t1

	logFile.write('%s|STATUS:%s|TIME:%s\n' % (url, resp.status_code, dt))

	if pretty:
		outputFile.write(json.dumps(resp.json(), ensure_ascii=False, indent=4, sort_keys=True))
	else:
		outputFile.write(resp.text)

if __name__ == '__main__':
	configPath = './config.json'
	if len(sys.argv) >= 2:
		configPath = sys.argv[1]
	try:
		with codecs.open(configPath, 'r', 'utf8') as configFile:
			config = json.loads(configFile.read())
			with codecs.open(config.get('log'), 'a', 'utf8') as logFile:
				with codecs.open(config.get('output'), 'w+', 'utf8') as outputFile:
					doRequest(
						config.get('url') or '',
						method=config.get('method') or 'get',
						payload=config.get('data') or {},
						query=config.get('params') or {},
						headers=config.get('headers') or {},
						timeout=config.get('timeout') or 10,
						encoding=config.get('encoding') or 'utf8',
						logFile=logFile,
						outputFile=outputFile,
						pretty=config.get('pretty') or False)
	except Exception as e:
		print('error: %s' % str(e))