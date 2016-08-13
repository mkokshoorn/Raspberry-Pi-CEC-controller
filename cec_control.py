'''
Developer: M. Kokshoorn  
Date:  22/02/2015

Set of Python fucntions/wrappers for "cec-client", developped 
for use on a Rasberry Pi to control/detect HDMI connected devices.

More about cec-client ultilit and installation instructions at: 
https://github.com/Pulse-Eight/libcec 

'''

import subprocess

def get_power_status(dev=0):
	cmd='echo "pow %i" | cec-client -d 1 -s "standby 0" RPI'%dev
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	out, err = p.communicate()
	return 'on' in out.split(' ')[-1]


def set_power_status(set_value,dev=0):
	if(set_value):
		cmd='echo "on %i" | cec-client -d 1 -s "standby 0" RPI'%dev
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
		out, err = p.communicate()
	else:
		cmd='echo "standby %i" | cec-client -d 1 -s "standby 0" RPI'%dev
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
		out, err = p.communicate()

def set_active():
	cmd='echo "as" | cec-client -d 1 -s "standby 0" RPI'
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	out, err = p.communicate()

		
def get_devices():
	cmd='echo "scan" | cec-client -d 1 -s "standby 0" RPI'
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	out, err = p.communicate()
	return out

def get_ps4_power():
	out= get_devices()
	out_lines=out.split('\n')
	try:
		index=out_lines.index('osd string:    PlayStation 4')
		line=out_lines[index-4]
		num_1=line.index('#')+1
		num_2=line.index(':')
		dev_num=line[num_1:num_2]
		return get_power_status(dev=int(dev_num))
	except:
		print "No PS4 found!"

def set_ps4_power(set_value):
	out= get_devices()
	out_lines=out.split('\n')
	try:
		index=out_lines.index('osd string:    PlayStation 4')
		line=out_lines[index-4]
		num_1=line.index('#')+1
		num_2=line.index(':')
		dev_num=line[num_1:num_2]
		print "Ps4 found on dev "+dev
		set_power_status(set_value,dev=int(dev_num))
	except:
		print "No PS4 found!"



