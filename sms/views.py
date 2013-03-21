from lxml import etree
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from projectroot import projectRoot

@login_required
def index(request, contact='Ava', smsStart='1', smsEnd='50', step = 50):
	contact = contact.replace('_', ' ')
	smsStart = int(smsStart) - 1 
	smsEnd = int(smsEnd)
	tree = etree.parse(projectRoot + 'sms/sms.xml')
	root = tree.getroot()
	ava = root.findall("*[@contact_name='"+contact+"']")
	messages = [{
		'body': sms.attrib['body'],
		'date': sms.attrib['readable_date'],
		'type': sms.attrib['type']
		} for sms in ava[smsStart:smsEnd]]
	
	if smsStart < step:
		prevLink = None
	elif smsStart >= step:
		prevLink = str(smsStart - step + 1) + '/' + str((smsEnd/step - 1)*step)
	else:
		prevLink = '1/' + str(step)

	if smsEnd == len(ava):
		nextLink = None
	elif smsEnd + step <= len(ava) + 1:
		nextLink = str(smsStart + step + 1) + '/' + str(smsEnd + step)
	else:
		nextLink = str(smsStart + step + 1) + '/' + str(len(ava))
	
	c = {
		'messages': messages,
		'contact': contact,
		'count': len(ava),
		'prevLink': prevLink,
		'nextLink': nextLink,
	}
	return render_to_response('sms/index.html', c, context_instance=RequestContext(request))
