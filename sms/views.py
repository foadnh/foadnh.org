from lxml import etree
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from projectroot import projectRoot

@login_required
def index(request, contactURL='Ava', smsStart='1', step='50'):
	contact = contactURL.replace('_', ' ')
	step = int(step)
	smsStart = int(smsStart) - 1
	smsEnd = smsStart + step

	tree = etree.parse(projectRoot + 'sms/sms.xml')
	root = tree.getroot()
	xmlMessages = root.findall("*[@contact_name='"+contact+"']")
	messages = [{
		'body': xmlMessages[i].attrib['body'],
		'date': xmlMessages[i].attrib['readable_date'],
		'type': xmlMessages[i].attrib['type'],
		'index': i + 1
		} for i in range(smsStart,smsEnd)]
	
	smsLen = len(xmlMessages)

	if smsStart == 0:
		prevLink = None
	elif smsStart < step:
		prevLink = contactURL + '/1/' + str(step) + '/'
	else:
		prevLink = contactURL + '/' + str(smsStart-step+1) + '/' + str(step)+'/'

	if smsEnd >= smsLen:
		nextLink = None
#	elif smsEnd + step <= smsLen + 1:
#		nextLink = contactURL + '/' + str(smsStart+step+1) + '/' + str(step)+'/'
#	else:
#		nextLink = contactURL + '/' + str(smsStart+step+1) + '/' 
#		nextLink += str(smsLen)
	else:
		nextLink = contactURL + '/' + str(smsStart+step+1) + '/' + str(step)+'/'
	
	c = {
		'messages': messages,
		'contact': contact,
		'contactURL': contactURL,
		'smsLen': smsLen,
		'prevLink': prevLink,
		'nextLink': nextLink,
		'smsStart': smsStart + 1,
	}
	return render_to_response('sms/index.html', c, context_instance=RequestContext(request))
