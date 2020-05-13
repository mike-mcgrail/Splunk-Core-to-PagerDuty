# Splunk-Core-to-PagerDuty
Core Splunk to PagerDuty Alerts

## This is a port of the PagerDuty App for Splunk at https://splunkbase.splunk.com/app/3013/
## Modifications:
1. Changed PRINT statements to logging. C'mon PagerDuty...this is Splunk after all
2. Routing traffic through proxy
3. Add optional alert rename, defaults to Splunk search name
4. Add PD severity option, defaults to Critical

## Install Instructions:
1. Copy pagerduty_incidents directory to Search Head $SPLUNK_HOME/etc/apps/ (for search head cluster, untar to $SPLUNK_HOME/etc/shcluster/apps/)
2. Create (or retrieve your already existing) PagerDuty Splunk integration key following the vendor instructions.
3. Modify /local/alert_actions.conf to include the key from step 2
4. In our environment, we use PagerDuty serverity critical and warning. If you need more options, modify /pagerduty_incidents/default/data/ui/alerts/pagerduty.html
5. Modify /bin/pagerduty.py to include your proxy name and port. Or, if your Splunk search head(s) can reach the Internet directly, remove the proxy lines.
6. Restart Splunk (or push search head cluster bundle from deployer)
7. Upon creating PagerDuty alert action, there are two new fields: PagerDuty alert title (text box which defaults to Splunk alert name token) and PagerDuty alert severity (drop-down)