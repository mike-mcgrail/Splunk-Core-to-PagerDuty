PagerDuty is an agile incident management solution that integrates with IT Ops and DevOps monitoring stacks to improve operational reliability and agility. With 300+ integrations, automated scheduling, advance reporting and guaranteed reliability, PagerDuty is trusted by 10,000+ organizations globally to increase business and employee efficiency.

The PagerDuty App enables Splunk customers to deliver faster response times to service disruptions. Specifically, joint PagerDuty and Splunk customers are able to:

- Allow PagerDuty to leverage the Splunk Alerts framework with one click, which saves users significant time and energy
- Connect a single Splunk instance to multiple PagerDuty services or accounts, which allows users to tailor their Splunk alerts in PagerDuty to their specific needs and workflow
- Streamline and group incident data within PagerDuty, which reduces alert noise and information overload by allowing users to group incidents in a manner that makes sense to them

## App Description

The purpose of this app is to setup custom alert actions that forward to PagerDuty

## Installation Instructions

* Install via the Splunk Web Admin
* Configure using the full integration url or the integration key supplied after adding the splunk service in the PagerDuty Admin.
* Integration Guide can be found here https://www.pagerduty.com/docs/guides/splunk-integration-guide/

## Dependencies

N/A

## Where to install

The app needs to be installed on the search heads.

## Features

Easily integrates with PagerDuty’s event API to handle oncall alert triggers.

##Support

Website: https://support.pagerduty.com
Email: support@pagerduty.com
Licence: Default Splunkbase license

## Open Source Libraries

No external open source libraries

## Change Log:

### Version 1.5

Removed session key from logging and sending to PagerDuty for Splunk Cloud Compatibility

### Version 1.4

Fixed URL error

### Version 1.3

Updated expected URL for Splunk Cloud Compatibility

### Version 1.2

Updated version number for v7.2 compatibility

### Version 1.1

Changes for certification

### Version 1.0

Initial Release
