from lxml import etree
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

@login_required
def index(request, contact='Ava'):
	contact = contact.replace('_', ' ')
	tree = etree.parse('sms/sms.xml')
	root = tree.getroot()
	ava = root.findall("*[@contact_name='"+contact+"']")
	messages = [{
		'body': sms.attrib['body'],
		'date': sms.attrib['readable_date'],
		'type': sms.attrib['type']
		} for sms in ava]

	c = {
		'messages': messages,
		'contact': contact,
		'count': len(ava)
	}
	return render_to_response('sms/index.html', c, context_instance=RequestContext(request))
