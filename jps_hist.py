# raj@indix.com

import subprocess
from collections import defaultdict
import time
import requests 
import json

print "enter process id:"
process_id = raw_input()
process_id = process_id.strip()
cmd = ['jmap -histo %s | head -20' % process_id]
hist_instance = defaultdict(list)
hist_bytes = defaultdict(list)

while True:
	try:
		# r = requests.get("http://localhost:50030/jobtracker.jsp")
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE, shell=True)
		out, err = p.communicate()
		out = out.split("\n")[3:]
		out = map(lambda x: filter(lambda x:x!='', x.split(" ")), out)
		out = filter(lambda x: len(x) >0, out)

		for entry in out:
			hist_instance[entry[3]].append(entry[1])
			hist_bytes[entry[3]].append(entry[2])
		print "sleeping for 10 sec"
		time.sleep(10)
	except:
		print "bytes"
		for k, v in hist_bytes.iteritems():
			print "%s\t%s" % (k, "\t".join(v))
		print 
		print "instance"	
		for k, v in hist_instance.iteritems():
			print "%s\t%s" % (k, "\t".join(v))
		break
