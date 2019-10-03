#!/usr/bin/env python

import json
import os

def list_users():
	data = {}
	data['user']=[]
	with open ('/etc/passwd', 'r') as users_list:
		for line in users_list:
			fields = line.split(":")
			
			data['user'].append({
								'username': fields[0],\
								'pass_validate': fields[1],\
								'uid': fields[2],\
								'gid': fields[3],\
								'gecos_description':fields[4]\
								})
	#return json.dumps(data)
	return data