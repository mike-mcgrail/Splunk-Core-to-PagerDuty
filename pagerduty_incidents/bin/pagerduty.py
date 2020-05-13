import sys
import json
import urllib2
import os
import logging

from fnmatch import fnmatch


def send_notification(payload):
    settings = payload.get('configuration')

    logging.debug('Original Payload=%s' % payload)

    url = settings.get('integration_url_override')

    if not url:
        url = settings.get('integration_url')

    # check if only the integration key was given
    if len(url) == 32:
        url = 'https://events.pagerduty.com/integration/' + url + "/enqueue"

    del payload['session_key']

    try:
        name = settings.get('pagerduty_alert_name')
        pd_severity = settings.get('pagerduty_alert_severity')

        body_string = json.dumps(payload)
        body_load = json.loads(body_string)

        #Overwrite search_name with PD Saerch Name defined in alert
        body_load['search_name'] = name
        #PD uses ['result']['log_level'] for their severity. Create and set as PD Severity defined in alert
        body_load['result'] = {}
        body_load['result']['log_level'] = pd_severity

        body = json.dumps(body_load,ensure_ascii=False).encode('utf8')

    except:
        body = json.dumps(payload)

    req = urllib2.Request(url, body, {"Content-Type": "application/json"})

    try:
        proxy = "<proxy>:<port>"
        proxies = {"https":"https://%s" % proxy}
        proxy_support = urllib2.ProxyHandler(proxies)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        res = urllib2.urlopen(req)
        body = res.read()
        logging.info("INFO PagerDuty server responded with HTTP status=%d" % res.code)
        #logging.critical("DEBUG PagerDuty server response: %s" % json.dumps(body))
        return 200 <= res.code < 300
    except urllib2.HTTPError, e:
        logging.error("ERROR Error sending message: %s (%s)" % (e, str(dir(e))))
        logging.error("ERROR Server response: %s" % e.read())
        return False


def set_logfile():
    logfile=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', '..', '..', 'var', 'log', 'splunk', 'pagerduty.log'))
    return logfile


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        logfile = set_logfile()
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename=logfile, level=logging.ERROR)
        payload = json.loads(sys.stdin.read())

        success = send_notification(payload)
        if not success:
            logging.critical("FATAL Failed trying to incident alert")
            sys.exit(2)
        else:
            logging.info("INFO Incident alert notification successfully sent")
    else:
        logging.error("FATAL Unsupported execution mode (expected --execute flag)")
        sys.exit(1)
