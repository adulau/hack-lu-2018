---
layout: splash
title: MISP Summit #0x04 - Monday 15 October (from 14:00 to 18:00) at hack.lu 2018
excerpt: "MISP Threat Intelligence Summit 0x04 at hack.lu 2018. Practical threat intelligence and information sharing for everyone."
modified: 2018-04-09T19:44:38.564948-04:00
header:
  overlay_image: /images/misp-long.png
  overlay_filter: 0.4 # same as adding an opacity of 0.5 to a black background
---

MISP Summit 04
--------------

![MISP logo](https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/logos/misp-logo.png)

On Monday 15 October 2018 from 14:00 to 18:00 (the day before hack.lu), the 4th [MISP(Malware Information Sharing Platform & Threat Sharing
) threat intelligence](http://www.misp-project.org/) summit will take place.


[MISP](http://www.misp-project.org/) is an advanced platform for sharing, storing and correlating Indicators of Compromises from attacks and cyber security threats.
Discover how MISP is used today in multiple organisations. Not only to store, share, collaborate on cyber security indicators, but also to use a threat intelligence platform
to support analysts, knowledge base and sharing of information.

The objective of the summit is openly discuss about the current usage of MISP, the future developments and the integration with the overall security ecosystems.

Agenda
------

The MISP Summit will take place from 14:00 to 19:00, Monday 15 October 2018.

{: class="table table-striped"}

| Time | Talks and Speakers |
|:----:|:------------------:|
| 14:00 | [Central Intelligence Vetting Platform - Routing threat intelligence centrally](https://2018.hack.lu/misp-summit/#central-intelligence-vetting-platform---routing-threat-intelligence-centrally) ([Raphael Otto](https://2018.hack.lu/misp-summit/#Raphael+Otto), [George Sedky](https://2018.hack.lu/misp-summit/#George+Sedky)) |
| 14:25 | [IoC generation from tweet texts](https://2018.hack.lu/misp-summit/#ioc-generation-from-tweet-texts) ([Fernando Alves](https://2018.hack.lu/misp-summit/#Fernando+Alves)) |
| 14:50 | [Building a Security Ecosystem with MISP and McAfee](https://2018.hack.lu/misp-summit/#building-a-security-ecosystem-with-misp-and-mcafee) ([Martin Ohl](https://2018.hack.lu/misp-summit/#Martin+Ohl)) |
| 15:15 | [MISP Project talk 2](https://2018.hack.lu/misp-summit/#MISP+Project+talk+2) ([info](https://2018.hack.lu/misp-summit/#info)) |
| 15:45 | [MISP Project talk 1](https://2018.hack.lu/misp-summit/#MISP+Project+talk+1) ([info](https://2018.hack.lu/misp-summit/#info)) |
| 16:10 | [misp42splunk](https://2018.hack.lu/misp-summit/#misp42splunk) ([Rémi Ségui]()) |
| 16:20 | TrendMicro - How to integrate MISP with local APT detection systems - Olivier Bertrand |
| 16:40 | [From Twitter to MISP: A way to catch and qualify IOCs](https://2018.hack.lu/misp-summit/#from-twitter-to-misp-a-way-to-catch-and-qualify-iocs) ([Sebastien Larinier](https://2018.hack.lu/misp-summit/#Sebastien+Larinier)),  Ambroise Terrier|
| 17:20 | [Master of Clusters](https://2018.hack.lu/misp-summit/#master-of-clusters) ([Andrea Garavaglia](https://2018.hack.lu/misp-summit/#Andrea+Garavaglia)) |
| 17:40 | [Cruising Ocean Threat Without Sinking Using TheHive, Cortex & MISP](https://2018.hack.lu/misp-summit/#cruising-ocean-threat-without-sinking-using-thehive-cortex--misp) ([Saâd Kadhi](https://2018.hack.lu/misp-summit/#Sa%C3%A2d+Kadhi)) |
| 18:00 | [Logistical Budget: Can we quantitatively compare APTs with MISP](https://2018.hack.lu/misp-summit/#logistical-budget-can-we-quantitatively-compare-apts-with-misp) ([Eireann Leverett](https://2018.hack.lu/misp-summit/#Eireann+Leverett), [Bruce Stenning](https://2018.hack.lu/misp-summit/#Bruce+Stenning)) |
| 18:20 | Enrichment and Quality IoC Creation from OSINT -  Rui Azevedo |
| 18:40 | MISP Project future |

{: class="table"}

[Call For Papers for the MISP threat intelligence submit](https://cfp.hack.lu/misp0x4/) is closed and we welcomed all contributions to gather use cases, best practices, new developments, creative approaches in threat intelligence and especially users of the MISP platform.


Talks
-----

## Central Intelligence Vetting Platform - Routing threat intelligence centrally

We created a software named *Central Intelligence Vetting Platform* which aims to help intelligence analysts to vet and route threat intelligence data centrally, across multiple distributed MISP instances.

by Raphael Otto and George Sedky

## IoC generation from tweet texts

This talk describes how to create Indicators of Compromise from tweets. The IoCs are further enriched using a Named Entity Recognizer to select relevant elements from the tweet text.

by Fernando Alves

## Cruising Ocean Threat Without Sinking Using TheHive, Cortex & MISP

TheHive, Cortex and MISP is **highly integrated**, free, open source stack used by many teams to perform CTI & DFIR related activities. In this talk we'll cover
old & new features to demonstrate the power of the trio.

by Saâd Kadhi

## misp42splunk

misp42splunk app connects MISP and Splunk. The app is designed to be easy to install, set up and maintain using the Splunk GUI
without editing directly files. You can use as many MISP instances as you like; one being defined at setup time to be the default instance.

The main use cases are:

MISP to SPLUNK: get MISP event attributes into Splunk search pipeline: | mispgetioc params | .... see
MISP for SPLUNK: 2 Splunk alert actions are available to directly create events or increment attribute sighting in a MISP instance.

BONUS: You can also create Splunk alert action to create The Hive alerts

by Rémi Séguy

## Logistical Budget: Can we quantitatively compare APTs with MISP

Non technical people want to know if Energetic Bear is more of a threat than Cleaver. They don't have the skill to judge, and they do so by newspaper reports. Can we do better?

by Eireann Leverett and Bruce Stenning

## From Twitter to MISP: A way to catch and qualify IOCs

We present our project to collect IOCs on Twitter to MISP and how to create a community to share tools, to qualify IOCs and share the data.

by Sebastien Larinier and Ambroise Terrier

## Building a Security Ecosystem with MISP and McAfee

This session will examine a reference architecture that enables automated threat hunting and incident response using OpenDXL and the MISP Threat Intelligence Platforms.

by Martin Ohl

## Master of Clusters

An approach to malware clustering using an integration of MISP, cuckoo, Malpedia.

by [Andrea Garavaglia](https://www.linkedin.com/in/andrea-garavaglia-4931969/)

## Enrichment and Quality IoC Creation from OSINT

In this presentation we propose an approach to generate threat intelligence of quality based on collected OSINT feeds that can later be used in defensive infrastructures, such as IDSs and SIEMs. The approach was implemented in a platform using MISP and assessed with 34 OSINT feeds. The platform was able to create enriched IoCs that allowed identification of cyber-attacks previously not possible by analyzing the IoCs individually.

by Rui Azevedo

Where
-----

The MISP summit will take place at [Parc Hotel](http://www.parc-hotel.lu/), Luxembourg.

Who
---

Everyone interested (developers, contributors, users and future users) in the MISP platform is welcome.

The access to the MISP Summit is free. You just need to [register online](https://www.eventbrite.com/e/misp-threat-intelligence-summit-0x4-tickets-46481482365) (it's only the access to the MISP summit).

Sponsors
--------

![](https://www.misp-project.org/assets/images/logo.png)
![](https://www.misp-project.org/assets/images/en_cef.png)

