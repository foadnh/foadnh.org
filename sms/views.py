from lxml import etree
<<<<<<< HEAD
=======
from django.template import RequestContext, Context, loader
from django.http import HttpResponse
>>>>>>> 37383e42227a9ca158ad2dfda4d9acaab5ba98d3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def index(request, contact='Ava'):
	contact = contact.replace('_', ' ')
#	contact = 'Ava'
	tree = etree.parse('sms/sms.xml')
	root = tree.getroot()
	ava = root.findall("*[@contact_name='"+contact+"']")
	messages = [{
		'body': sms.attrib['body'],
		'date': sms.attrib['readable_date'],
		'type': sms.attrib['type']
		} for sms in ava]

<<<<<<< HEAD
	c = {
		'messages': messages,
		'contact': contact,
		'count': len(ava)
	}
	return render_to_response('sms/index.html', c, context_instance=RequestContext(request))
=======
	t = loader.get_template('sms/index.html')
#	c = RequestContext(request, {
#		'messages': messages,
#		'contact': 'Ava'
#	})
	c = Context({
		'messages': messages,
		'contact': contact,
		'count': len(ava)
	})
#	return HttpResponse(t.render(c))
	return render_to_response('sms/index.html', {'messages': messages, 'contact': contact, 'count': len(ava)}, context_instance=RequestContext(request))
>>>>>>> 37383e42227a9ca158ad2dfda4d9acaab5ba98d3
