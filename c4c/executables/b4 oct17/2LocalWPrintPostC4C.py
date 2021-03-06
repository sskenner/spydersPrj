import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
import re
import subprocess
from googleapiclient.discovery import build 
from itertools import repeat
from unidecode import unidecode
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import Request, urlopen


# AVAILABLE_TOKEN_SETS = {
#     'ess': {
#         'api_key': 'AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc',
#         'cse_id': '009043117829057268965:tgiqlni9v2w'
#     },
#     'ssk': {
#         'api_key': 'AIzaSyAn_YOSbC43zmv2cexCddaIYfJfMb9d08s',
#         'cse_id': '003565523015477317201:lwtcnf2u57i'
#     }
# }

# NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'ess'

# API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
# CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

# MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY = 10

# def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     return res['items']

results_from_GSE_query = [
    {
        "cacheId": "Fvb84kkh49QJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../eb6ff489-e6cc-4da4-94e6-c31e0586f681",
        "htmlFormattedUrl": "https://jobs.lever.co/.../eb6ff489-e6cc-4da4-94e6-c31e0586f681",
        "htmlSnippet": "Optimus Ride software <b>engineers</b> create the software at the heart of our vehicles <br>\nand systems. Our software needs to process complex dataflows and make&nbsp;...",
        "htmlTitle": "Optimus Ride Inc. - SOFTWARE <b>ENGINEER</b> \u2013 <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/optimusride/eb6ff489-e6cc-4da4-94e6-c31e0586f681",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/60f10e91-e949-488d-b597-97c108f7a8f8-1476304566772.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "112",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRIzogDKg8vaMM0QA1FH1YSilfr8SfoZNbMbhumsbPYjwA48ftNtUq6-Zg",
                    "width": "448"
                }
            ],
            "metatags": [
                {
                    "og:description": "Optimus Ride software engineers create the software at the heart of our vehicles and systems. Our software needs to process complex dataflows and make decisions with real world consequences. We are looking for engineers who bring fresh perspective from many different areas, including machine learning, perception, robotics, networking and data storage, real-time systems, UI and mobile. You will work with peers who cumulatively have decades of experience from places like Google X, SpaceX, iRobot, Rethink Robotics, Draper Laboratories, Zipcar, and have built self-driving vehicles, electric vehicles, manufacturing robots, surgical robots, autonomous drones, and more. Our team is focused on the fastest path to market, in order to maximize the benefits of self-driving technologies for all. To do this, we need our engineers to be versatile, have leadership qualities, and be enthusiastic about tackling problems across the full range of our systems. Working at Optimus Ride you will innovate wi",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/60f10e91-e949-488d-b597-97c108f7a8f8-1476304566772.png",
                    "og:image:height": "200",
                    "og:title": "Optimus Ride Inc. - SOFTWARE ENGINEER \u2013 C++",
                    "og:url": "https://jobs.lever.co/optimusride/eb6ff489-e6cc-4da4-94e6-c31e0586f681",
                    "twitter:description": "Optimus Ride software engineers create the software at the heart of our vehicles and systems. Our software needs to process complex dataflows and make decisions with real world consequences. We are looking for engineers who bring fresh perspective from many different areas, including machine learning, perception, robotics, networking and data storage, real-time systems, UI and mobile. You will work with peers who cumulatively have decades of experience from places like Google X, SpaceX, iRobot, Rethink Robotics, Draper Laboratories, Zipcar, and have built self-driving vehicles, electric vehicles, manufacturing robots, surgical robots, autonomous drones, and more. Our team is focused on the fastest path to market, in order to maximize the benefits of self-driving technologies for all. To do this, we need our engineers to be versatile, have leadership qualities, and be enthusiastic about tackling problems across the full range of our systems. Working at Optimus Ride you will innovate wi",
                    "twitter:title": "Optimus Ride Inc. - SOFTWARE ENGINEER \u2013 C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Optimus Ride software engineers create the software at the heart of our vehicles \nand systems. Our software needs to process complex dataflows and make\u00a0...",
        "title": "Optimus Ride Inc. - SOFTWARE ENGINEER \u2013 C++"
    },
    {
        "cacheId": "feSIbRvhCPQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../0ed8b33f-dc26-467f-a34f-080546b522a7",
        "htmlFormattedUrl": "https://jobs.lever.co/.../0ed8b33f-dc26-467f-a34f-080546b522a7",
        "htmlSnippet": "MZ Game Studio is seeking a highly skilled technical lead for the team of senior <br>\n<b>engineers</b> developing our next-gen game engine. In addition to being a primary&nbsp;...",
        "htmlTitle": "MZ - Principal Software <b>Engineer</b>, <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/0ed8b33f-dc26-467f-a34f-080546b522a7",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ Game Studio is seeking a highly skilled technical lead for the team of senior engineers developing our next-gen game engine. In addition to being a primary code contributor, the lead engineer is responsible for driving deliverables, providing technical guidance, performing code reviews, and ensuring that the team is operating as efficiently as possible. Qualified candidates must have previous experience leading game development teams, and must be proficient in writing highly optimized, extensible, and maintainable code under aggressive deadlines.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Principal Software Engineer, C++",
                    "og:url": "https://jobs.lever.co/machinezone/0ed8b33f-dc26-467f-a34f-080546b522a7",
                    "twitter:description": "MZ Game Studio is seeking a highly skilled technical lead for the team of senior engineers developing our next-gen game engine. In addition to being a primary code contributor, the lead engineer is responsible for driving deliverables, providing technical guidance, performing code reviews, and ensuring that the team is operating as efficiently as possible. Qualified candidates must have previous experience leading game development teams, and must be proficient in writing highly optimized, extensible, and maintainable code under aggressive deadlines.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Principal Software Engineer, C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "MZ Game Studio is seeking a highly skilled technical lead for the team of senior \nengineers developing our next-gen game engine. In addition to being a primary\u00a0...",
        "title": "MZ - Principal Software Engineer, C++"
    },
    {
        "cacheId": "7ZEmLw70cCsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../9d6944cc-9c88-43c9-8945-0330a5641390",
        "htmlFormattedUrl": "https://jobs.lever.co/.../9d6944cc-9c88-43c9-8945-0330a5641390",
        "htmlSnippet": "MZ Game Studio is seeking a highly skilled senior <b>engineer</b> to join our client <br>\nengine team. Qualified candidates will be responsible for developing the core&nbsp;...",
        "htmlTitle": "MZ - Senior Software <b>Engineer</b>, <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/9d6944cc-9c88-43c9-8945-0330a5641390",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ Game Studio is seeking a highly skilled senior engineer to join our client engine team. Qualified candidates will be responsible for developing the core technologies that drive our next-gen game engine. This person works closely with our team lead to define architectural vision for the engine and ensure that all code reinforces the conceptual integrity of that vision. Qualified candidates must be proficient in writing highly optimized, extensible and maintainable code under aggressive deadlines.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Software Engineer, C++",
                    "og:url": "https://jobs.lever.co/machinezone/9d6944cc-9c88-43c9-8945-0330a5641390",
                    "twitter:description": "MZ Game Studio is seeking a highly skilled senior engineer to join our client engine team. Qualified candidates will be responsible for developing the core technologies that drive our next-gen game engine. This person works closely with our team lead to define architectural vision for the engine and ensure that all code reinforces the conceptual integrity of that vision. Qualified candidates must be proficient in writing highly optimized, extensible and maintainable code under aggressive deadlines.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Software Engineer, C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "MZ Game Studio is seeking a highly skilled senior engineer to join our client \nengine team. Qualified candidates will be responsible for developing the core\u00a0...",
        "title": "MZ - Senior Software Engineer, C++"
    },
    {
        "cacheId": "KlZUoJAKOcMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/otto/1b33f43d-e661-4f24-9268-b694603f5723",
        "htmlFormattedUrl": "https://jobs.lever.co/otto/1b33f43d-e661-4f24-9268-b694603f5723",
        "htmlSnippet": "Software <b>Engineer</b> | <b>C++</b>, Python. San Francisco/Palo Alto. Software <b>Engineering</b>. <br>\nFull-time. Apply for this job. Otto is a team of the sharpest minds in&nbsp;...",
        "htmlTitle": "Otto - Careers - Software <b>Engineer</b> | <b>C++</b>, Python",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/otto/1b33f43d-e661-4f24-9268-b694603f5723",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6fcd6028-7eeb-4093-bb79-3ac600dbf938-1457398070097.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "130",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRxEOGVhSSO_L-VtVmXCh-3NmZ3bRqTV6pZQxljFBi6Rr_1To2jzECdmG3M",
                    "width": "388"
                }
            ],
            "metatags": [
                {
                    "og:description": "Otto is a team of the sharpest minds in autonomous technology who are driven to rethink transportation \u2013 not just improve it. And at the heart of Otto\u2019s vision is the belief that autonomous technology is the key to creating a more viable, efficient, and above all, safer, transportation future.  The Otto team consists of some of the world\u2019s leading technologists who are passionate about transforming transportation through emerging autonomous technology. The team is made up of veterans of autonomous tech who have come to Otto from other world changing companies like Apple, Cruise and Google.  As a software engineer, you will have an opportunity to work in a small team concentrated on the fields of 3D perception and computer vision. Our group works to develop core tools that focus on the topics of camera modeling, camera registration, camera tracking, image stabilization, and 3D reconstruction. Your responsibilities will include all aspects of software development from design to coding and testing. You\u2019l",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6fcd6028-7eeb-4093-bb79-3ac600dbf938-1457398070097.png",
                    "og:image:height": "200",
                    "og:title": "Otto - Careers - Software Engineer | C++, Python",
                    "og:url": "https://jobs.lever.co/otto/1b33f43d-e661-4f24-9268-b694603f5723",
                    "twitter:description": "Otto is a team of the sharpest minds in autonomous technology who are driven to rethink transportation \u2013 not just improve it. And at the heart of Otto\u2019s vision is the belief that autonomous technology is the key to creating a more viable, efficient, and above all, safer, transportation future.  The Otto team consists of some of the world\u2019s leading technologists who are passionate about transforming transportation through emerging autonomous technology. The team is made up of veterans of autonomous tech who have come to Otto from other world changing companies like Apple, Cruise and Google.  As a software engineer, you will have an opportunity to work in a small team concentrated on the fields of 3D perception and computer vision. Our group works to develop core tools that focus on the topics of camera modeling, camera registration, camera tracking, image stabilization, and 3D reconstruction. Your responsibilities will include all aspects of software development from design to coding and testing. You\u2019l",
                    "twitter:title": "Otto - Careers - Software Engineer | C++, Python",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer | C++, Python. San Francisco/Palo Alto. Software Engineering. \nFull-time. Apply for this job. Otto is a team of the sharpest minds in\u00a0...",
        "title": "Otto - Careers - Software Engineer | C++, Python"
    },
    {
        "cacheId": "pt3idhQ0vWAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175-fe090cb62d55",
        "htmlFormattedUrl": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175-fe090cb62d55",
        "htmlSnippet": "Avecto is a global leader in Privileged Elevation and Delegation Management. <br>\nSince 2008, the company has enabled over 8 million users to successfully work&nbsp;...",
        "htmlTitle": "Avecto - Software <b>Engineer</b> - <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175-fe090cb62d55",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528767450.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "109",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSumPri1vDbmLVUzT0XSNVQtHYE7xslAr8f5W71X3LzskONK_oHZEOTfKo",
                    "width": "460"
                }
            ],
            "metatags": [
                {
                    "og:description": "Due to tremendous growth, our Manchester office currently has an exciting opportunity for an experienced Software Engineer to join their extraordinarily successful Development Team. Our global Development team has an ambitious drive towards success and now due to our rapid growth we are looking to expand the team even further. The successful candidate will be a good communicator who works effectively as part of a high achieving team. They will be a self-starter and can demonstrate commitment to exceeding expectations and driving their own personal development. They will have excellent creativity and problem solving skills, and will strive to excel in a dynamic fast growing company.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528767450.png",
                    "og:image:height": "200",
                    "og:title": "Avecto - Software Engineer - C++",
                    "og:url": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175-fe090cb62d55",
                    "twitter:description": "Due to tremendous growth, our Manchester office currently has an exciting opportunity for an experienced Software Engineer to join their extraordinarily successful Development Team. Our global Development team has an ambitious drive towards success and now due to our rapid growth we are looking to expand the team even further. The successful candidate will be a good communicator who works effectively as part of a high achieving team. They will be a self-starter and can demonstrate commitment to exceeding expectations and driving their own personal development. They will have excellent creativity and problem solving skills, and will strive to excel in a dynamic fast growing company.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528998385.png",
                    "twitter:title": "Avecto - Software Engineer - C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Avecto is a global leader in Privileged Elevation and Delegation Management. \nSince 2008, the company has enabled over 8 million users to successfully work\u00a0...",
        "title": "Avecto - Software Engineer - C++"
    },
    {
        "cacheId": "_szmnVrXtfYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d.../",
        "htmlFormattedUrl": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d.../apply",
        "htmlSnippet": "Sr. Software <b>Engineer</b> (C#.net, <b>C++</b>, TCP/IP). San Leandro, CA. <b>Engineering</b> \u2013 <br>\n<b>Engineering</b> - Operations. Full-time. Submit your application. Resume/CV.",
        "htmlTitle": "thredUP - Sr. Software <b>Engineer</b> (C#.net, <b>C++</b>, TCP/IP)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d-2e2ba1b9ee29",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3949d724-5b2b-440d-a2fa-809407ef769f-1494860779713.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "92",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp4-R7uqwebQIikzMeg3Wxy85I9EkeIEj52r2k1OcJXWwVhTBClzc5GQ",
                    "width": "546"
                }
            ],
            "metatags": [
                {
                    "og:description": "About thredUP thredUP, based in San Francisco, is the leading online marketplace for buying and selling like-new women\u2019s and kids\u2019 clothing. thredUP was founded in 2009 and currently employs nearly 1,000 people across its corporate office and four distribution centers. To date, thredUP has raised $131 million from top-tier investors, most recently closing an $81M equity investment from Goldman Sachs. thredUP\u2019s mission is to inspire a new generation of consumers to think secondhand first. We are achieving this mission being the most convenient solution for busy moms to \u201cclean out\u201d their closets, get organized and do good in the process. thredUP also has the widest and most affordable selection of secondhand clothes in all the name brands customers want to own, in like-new condition. thredUP is growing rapidly, and has built a world-class team that includes investors and executives from Netflix, Virgin, DVF, GAP and Sephora. We are building the leader in the online secondhand apparel m",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3949d724-5b2b-440d-a2fa-809407ef769f-1494860779713.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "thredUP - Sr. Software Engineer (C#.net, C++, TCP/IP)",
                    "og:url": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d-2e2ba1b9ee29/apply",
                    "twitter:description": "About thredUP thredUP, based in San Francisco, is the leading online marketplace for buying and selling like-new women\u2019s and kids\u2019 clothing. thredUP was founded in 2009 and currently employs nearly 1,000 people across its corporate office and four distribution centers. To date, thredUP has raised $131 million from top-tier investors, most recently closing an $81M equity investment from Goldman Sachs. thredUP\u2019s mission is to inspire a new generation of consumers to think secondhand first. We are achieving this mission being the most convenient solution for busy moms to \u201cclean out\u201d their closets, get organized and do good in the process. thredUP also has the widest and most affordable selection of secondhand clothes in all the name brands customers want to own, in like-new condition. thredUP is growing rapidly, and has built a world-class team that includes investors and executives from Netflix, Virgin, DVF, GAP and Sephora. We are building the leader in the online secondhand apparel m",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3949d724-5b2b-440d-a2fa-809407ef769f-1494860086326.png",
                    "twitter:title": "thredUP - Sr. Software Engineer (C#.net, C++, TCP/IP)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Sr. Software Engineer (C#.net, C++, TCP/IP). San Leandro, CA. Engineering \u2013 \nEngineering - Operations. Full-time. Submit your application. Resume/CV.",
        "title": "thredUP - Sr. Software Engineer (C#.net, C++, TCP/IP)"
    },
    {
        "cacheId": "RFY5UZVjbnwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../31ece40d-f9f0-4208-95ce-6b0b082bd8f5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../31ece40d-f9f0-4208-95ce-6b0b082bd8f5",
        "htmlSnippet": "Genova Technologies has an immediate opening for a Software <b>Engineer</b> with C/<br>\nC++ and QT skills) for a long-term project at a client site in Moline, Illinois.",
        "htmlTitle": "Genova Technologies - Software <b>Engineer</b> (C/<b>C++</b>, QT)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/genovatech/31ece40d-f9f0-4208-95ce-6b0b082bd8f5",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1470156922557.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "167",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS78YDtyY3suTlG2gDqwn0q2rDRU_Vi4vmWxaLzPQgNKg18kp-BilptuT63",
                    "width": "302"
                }
            ],
            "metatags": [
                {
                    "og:description": "Genova Technologies has an immediate opening for a Software Engineer with C/C++ and QT skills) for a long-term project at a client site in Moline, Illinois. Description: \u00b7 Performs basic product design, testing and/or analysis work for a defined portion of a project. \u00b7 Operates in a team environment, providing input to design solutions and participating in design reviews. \u00b7 Develops recommendations within established guidelines; work and decisions are reviewed by supervisors before implementation. Responsibilities: \u00b7 Perform embedded systems engineering tasks including requirements analysis, operational concept development, system design, component integration, design reviews, and vehicle platform testing and problem solving. \u00b7 Perform functional and integration testing on the bench and on various models of Combines. \u00b7 Solve integration issues that involve multiple code modules, code bases, and/or multiple developers. \u00b7 D",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1470156922557.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Genova Technologies - Software Engineer (C/C++, QT)",
                    "og:url": "https://jobs.lever.co/genovatech/31ece40d-f9f0-4208-95ce-6b0b082bd8f5",
                    "twitter:description": "Genova Technologies has an immediate opening for a Software Engineer with C/C++ and QT skills) for a long-term project at a client site in Moline, Illinois. Description: \u00b7 Performs basic product design, testing and/or analysis work for a defined portion of a project. \u00b7 Operates in a team environment, providing input to design solutions and participating in design reviews. \u00b7 Develops recommendations within established guidelines; work and decisions are reviewed by supervisors before implementation. Responsibilities: \u00b7 Perform embedded systems engineering tasks including requirements analysis, operational concept development, system design, component integration, design reviews, and vehicle platform testing and problem solving. \u00b7 Perform functional and integration testing on the bench and on various models of Combines. \u00b7 Solve integration issues that involve multiple code modules, code bases, and/or multiple developers. \u00b7 D",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1490383577263.png",
                    "twitter:title": "Genova Technologies - Software Engineer (C/C++, QT)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Genova Technologies has an immediate opening for a Software Engineer with C/\nC++ and QT skills) for a long-term project at a client site in Moline, Illinois.",
        "title": "Genova Technologies - Software Engineer (C/C++, QT)"
    },
    {
        "cacheId": "Fm3yiVwh8A8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/optimusride/eb6ff489-e6cc-4da4-94e6.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/optimusride/eb6ff489-e6cc-4da4-94e6.../apply",
        "htmlSnippet": "SOFTWARE <b>ENGINEER</b> \u2013 <b>C++</b>. Boston, MA. <b>Engineering</b>. Full-time. Submit your <br>\napplication. Resume/CV. ATTACH RESUME/CV. Couldn&#39;t auto-read resume.",
        "htmlTitle": "Optimus Ride Inc. - SOFTWARE <b>ENGINEER</b> \u2013 <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/optimusride/eb6ff489-e6cc-4da4-94e6-c31e0586f681",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/60f10e91-e949-488d-b597-97c108f7a8f8-1476304566772.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "112",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRIzogDKg8vaMM0QA1FH1YSilfr8SfoZNbMbhumsbPYjwA48ftNtUq6-Zg",
                    "width": "448"
                }
            ],
            "metatags": [
                {
                    "og:description": "Optimus Ride software engineers create the software at the heart of our vehicles and systems. Our software needs to process complex dataflows and make decisions with real world consequences. We are looking for engineers who bring fresh perspective from many different areas, including machine learning, perception, robotics, networking and data storage, real-time systems, UI and mobile. You will work with peers who cumulatively have decades of experience from places like Google X, SpaceX, iRobot, Rethink Robotics, Draper Laboratories, Zipcar, and have built self-driving vehicles, electric vehicles, manufacturing robots, surgical robots, autonomous drones, and more. Our team is focused on the fastest path to market, in order to maximize the benefits of self-driving technologies for all. To do this, we need our engineers to be versatile, have leadership qualities, and be enthusiastic about tackling problems across the full range of our systems. Working at Optimus Ride you will innovate wi",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/60f10e91-e949-488d-b597-97c108f7a8f8-1476304566772.png",
                    "og:image:height": "200",
                    "og:title": "Optimus Ride Inc. - SOFTWARE ENGINEER \u2013 C++",
                    "og:url": "https://jobs.lever.co/optimusride/eb6ff489-e6cc-4da4-94e6-c31e0586f681/apply",
                    "twitter:description": "Optimus Ride software engineers create the software at the heart of our vehicles and systems. Our software needs to process complex dataflows and make decisions with real world consequences. We are looking for engineers who bring fresh perspective from many different areas, including machine learning, perception, robotics, networking and data storage, real-time systems, UI and mobile. You will work with peers who cumulatively have decades of experience from places like Google X, SpaceX, iRobot, Rethink Robotics, Draper Laboratories, Zipcar, and have built self-driving vehicles, electric vehicles, manufacturing robots, surgical robots, autonomous drones, and more. Our team is focused on the fastest path to market, in order to maximize the benefits of self-driving technologies for all. To do this, we need our engineers to be versatile, have leadership qualities, and be enthusiastic about tackling problems across the full range of our systems. Working at Optimus Ride you will innovate wi",
                    "twitter:title": "Optimus Ride Inc. - SOFTWARE ENGINEER \u2013 C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "SOFTWARE ENGINEER \u2013 C++. Boston, MA. Engineering. Full-time. Submit your \napplication. Resume/CV. ATTACH RESUME/CV. Couldn't auto-read resume.",
        "title": "Optimus Ride Inc. - SOFTWARE ENGINEER \u2013 C++"
    },
    {
        "cacheId": "FTOXFyXObgQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../604fb457-189c-4f7c-b8ea-70f7bdfbd69e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../604fb457-189c-4f7c-b8ea-70f7bdfbd69e",
        "htmlSnippet": "Genova Technologies has a unique opportunity in which we are seeking <br>\nexperienced embedded C, C++ and Linux, Software <b>Engineers</b>. If you are local or<br>\n&nbsp;...",
        "htmlTitle": "Genova Technologies - Software <b>Engineer</b> (Embedded C, <b>C++</b>, Linux)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/genovatech/604fb457-189c-4f7c-b8ea-70f7bdfbd69e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1470156922557.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "167",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS78YDtyY3suTlG2gDqwn0q2rDRU_Vi4vmWxaLzPQgNKg18kp-BilptuT63",
                    "width": "302"
                }
            ],
            "metatags": [
                {
                    "og:description": "\u201cFirst, solve the problem. Then, write the code\u201d Genova Technologies has a unique opportunity in which we are seeking experienced embedded C, C++ and Linux, Software Engineers. If you are local or interested in relocating to the Midwest, we encourage you to apply or reach out to our recruiting staff today. Genova Technologies, Inc. has been in business for 23+ years, and is an engineering services company that specializes in long-term, ongoing W2/benefit-eligible employment. We offer project-based employment to new employees and rotate projects as needed.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1470156922557.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Genova Technologies - Software Engineer (Embedded C, C++, Linux)",
                    "og:url": "https://jobs.lever.co/genovatech/604fb457-189c-4f7c-b8ea-70f7bdfbd69e",
                    "twitter:description": "\u201cFirst, solve the problem. Then, write the code\u201d Genova Technologies has a unique opportunity in which we are seeking experienced embedded C, C++ and Linux, Software Engineers. If you are local or interested in relocating to the Midwest, we encourage you to apply or reach out to our recruiting staff today. Genova Technologies, Inc. has been in business for 23+ years, and is an engineering services company that specializes in long-term, ongoing W2/benefit-eligible employment. We offer project-based employment to new employees and rotate projects as needed.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1490383577263.png",
                    "twitter:title": "Genova Technologies - Software Engineer (Embedded C, C++, Linux)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Genova Technologies has a unique opportunity in which we are seeking \nexperienced embedded C, C++ and Linux, Software Engineers. If you are local or\n\u00a0...",
        "title": "Genova Technologies - Software Engineer (Embedded C, C++, Linux)"
    },
    {
        "cacheId": "Jk1nQ-pIc_gJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/machinezone/9d6944cc-9c88-43c9.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/machinezone/9d6944cc-9c88-43c9.../apply",
        "htmlSnippet": "U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). Our company values diversity.",
        "htmlTitle": "MZ - Senior Software <b>Engineer</b>, <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/9d6944cc-9c88-43c9-8945-0330a5641390",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ Game Studio is seeking a highly skilled senior engineer to join our client engine team. Qualified candidates will be responsible for developing the core technologies that drive our next-gen game engine. This person works closely with our team lead to define architectural vision for the engine and ensure that all code reinforces the conceptual integrity of that vision. Qualified candidates must be proficient in writing highly optimized, extensible and maintainable code under aggressive deadlines.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Software Engineer, C++",
                    "og:url": "https://jobs.lever.co/machinezone/9d6944cc-9c88-43c9-8945-0330a5641390/apply",
                    "twitter:description": "MZ Game Studio is seeking a highly skilled senior engineer to join our client engine team. Qualified candidates will be responsible for developing the core technologies that drive our next-gen game engine. This person works closely with our team lead to define architectural vision for the engine and ensure that all code reinforces the conceptual integrity of that vision. Qualified candidates must be proficient in writing highly optimized, extensible and maintainable code under aggressive deadlines.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Software Engineer, C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). Our company values diversity.",
        "title": "MZ - Senior Software Engineer, C++"
    },
    {
        "cacheId": "IN93Sv7QhigJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175.../apply",
        "htmlSnippet": "Software <b>Engineer</b> - <b>C++</b>. UK, Manchester. <b>Engineering</b> \u2013 Development. Full <br>\nTime. Submit your application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn&#39;t&nbsp;...",
        "htmlTitle": "Avecto - Software <b>Engineer</b> - <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175-fe090cb62d55",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528767450.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "109",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSumPri1vDbmLVUzT0XSNVQtHYE7xslAr8f5W71X3LzskONK_oHZEOTfKo",
                    "width": "460"
                }
            ],
            "metatags": [
                {
                    "og:description": "Due to tremendous growth, our Manchester office currently has an exciting opportunity for an experienced Software Engineer to join their extraordinarily successful Development Team. Our global Development team has an ambitious drive towards success and now due to our rapid growth we are looking to expand the team even further. The successful candidate will be a good communicator who works effectively as part of a high achieving team. They will be a self-starter and can demonstrate commitment to exceeding expectations and driving their own personal development. They will have excellent creativity and problem solving skills, and will strive to excel in a dynamic fast growing company.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528767450.png",
                    "og:image:height": "200",
                    "og:title": "Avecto - Software Engineer - C++",
                    "og:url": "https://jobs.lever.co/avecto/f161101f-acaa-4b3c-a175-fe090cb62d55/apply",
                    "twitter:description": "Due to tremendous growth, our Manchester office currently has an exciting opportunity for an experienced Software Engineer to join their extraordinarily successful Development Team. Our global Development team has an ambitious drive towards success and now due to our rapid growth we are looking to expand the team even further. The successful candidate will be a good communicator who works effectively as part of a high achieving team. They will be a self-starter and can demonstrate commitment to exceeding expectations and driving their own personal development. They will have excellent creativity and problem solving skills, and will strive to excel in a dynamic fast growing company.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528998385.png",
                    "twitter:title": "Avecto - Software Engineer - C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer - C++. UK, Manchester. Engineering \u2013 Development. Full \nTime. Submit your application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn't\u00a0...",
        "title": "Avecto - Software Engineer - C++"
    },
    {
        "cacheId": "2Xy_5VYCscYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../88427e4e-6b6c-43b6-85ba-499b4831bdd6",
        "htmlFormattedUrl": "https://jobs.lever.co/.../88427e4e-6b6c-43b6-85ba-499b4831bdd6",
        "htmlSnippet": "Join and lead a small, productive team churning out correct, maintainable, high-<br>\nperformance, modern C++ to support Discord&#39;s ever growing feature set across a<br>\n&nbsp;...",
        "htmlTitle": "Discord - <b>Engineering</b> Manager - <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/discordapp/88427e4e-6b6c-43b6-85ba-499b4831bdd6",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/66fa13a6-de92-43a6-8864-d22a3870ffee-1478818530977.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "168",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT0TIXklmXsdZl7yEFMNKa5V1-ccaWP4iyf5XuHl7fsPWhhSAHrvu86x9MF",
                    "width": "300"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join and lead a small, productive team churning out correct, maintainable, high-performance, modern C++ to support Discord's ever growing feature set across a world of devices from traditional desktops to mobile and beyond.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/66fa13a6-de92-43a6-8864-d22a3870ffee-1478818530977.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Discord - Engineering Manager - C++",
                    "og:url": "https://jobs.lever.co/discordapp/88427e4e-6b6c-43b6-85ba-499b4831bdd6",
                    "twitter:description": "Join and lead a small, productive team churning out correct, maintainable, high-performance, modern C++ to support Discord's ever growing feature set across a world of devices from traditional desktops to mobile and beyond.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/66fa13a6-de92-43a6-8864-d22a3870ffee-1478818637962.png",
                    "twitter:title": "Discord - Engineering Manager - C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Join and lead a small, productive team churning out correct, maintainable, high-\nperformance, modern C++ to support Discord's ever growing feature set across a\n\u00a0...",
        "title": "Discord - Engineering Manager - C++"
    },
    {
        "cacheId": "6mJbSH1LTcIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/discordapp/88427e4e-6b6c-43b6-85ba.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/discordapp/88427e4e-6b6c-43b6-85ba.../apply",
        "htmlSnippet": "<b>Engineering</b> Manager - <b>C++</b>. San Francisco, CA. <b>Engineering</b>. Full-time. Submit <br>\nyour application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn&#39;t auto-read&nbsp;...",
        "htmlTitle": "Discord - <b>Engineering</b> Manager - <b>C++</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/discordapp/88427e4e-6b6c-43b6-85ba-499b4831bdd6/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/66fa13a6-de92-43a6-8864-d22a3870ffee-1478818530977.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "168",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT0TIXklmXsdZl7yEFMNKa5V1-ccaWP4iyf5XuHl7fsPWhhSAHrvu86x9MF",
                    "width": "300"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join and lead a small, productive team churning out correct, maintainable, high-performance, modern C++ to support Discord's ever growing feature set across a world of devices from traditional desktops to mobile and beyond.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/66fa13a6-de92-43a6-8864-d22a3870ffee-1478818530977.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Discord - Engineering Manager - C++",
                    "og:url": "https://jobs.lever.co/discordapp/88427e4e-6b6c-43b6-85ba-499b4831bdd6/apply",
                    "twitter:description": "Join and lead a small, productive team churning out correct, maintainable, high-performance, modern C++ to support Discord's ever growing feature set across a world of devices from traditional desktops to mobile and beyond.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/66fa13a6-de92-43a6-8864-d22a3870ffee-1478818637962.png",
                    "twitter:title": "Discord - Engineering Manager - C++",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Engineering Manager - C++. San Francisco, CA. Engineering. Full-time. Submit \nyour application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn't auto-read\u00a0...",
        "title": "Discord - Engineering Manager - C++"
    },
    {
        "cacheId": "Dx81o42LSpsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/yelp/53879e8d-690d-48f8-8419-62402d73dc6a",
        "htmlFormattedUrl": "https://jobs.lever.co/yelp/53879e8d-690d-48f8-8419-62402d73dc6a",
        "htmlSnippet": "<b>Engineering</b> and Product \u2013 College <b>Engineering</b> &amp; Product. Intern ... in your <br>\nfavorite modern programming language: Python, Ruby, Java, Objective-C, or <b>C++</b><br>\n.",
        "htmlTitle": "Yelp - Software <b>Engineer</b> - Intern - Fall",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/yelp/53879e8d-690d-48f8-8419-62402d73dc6a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441843879420.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "Yelp wants Fall interns to work side-by-side with our passionate, creative software developers. That's right, each intern at Yelp has a mentor and substantial projects to work on during their time here. We are looking for students who wish to gain experience at a growing company by working on projects used by millions of Yelpers and business owners. We use continuous deployment and A/B testing, so you would get to launch those projects and see results immediately. We take a lot of pride in the space we use at HQ for hosting meetup groups and tech talks. Yelp is looking for interns that want the chance to meet and greet with the best and most dynamic engineers, product managers, and leaders in the Valley. Are we looking for you? Great! Then check out our engineering teams and let us know what you are interested in working on. We would love to find out more about you.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441843879420.png",
                    "og:image:height": "200",
                    "og:title": "Yelp - Software Engineer - Intern - Fall",
                    "og:url": "https://jobs.lever.co/yelp/53879e8d-690d-48f8-8419-62402d73dc6a",
                    "twitter:description": "Yelp wants Fall interns to work side-by-side with our passionate, creative software developers. That's right, each intern at Yelp has a mentor and substantial projects to work on during their time here. We are looking for students who wish to gain experience at a growing company by working on projects used by millions of Yelpers and business owners. We use continuous deployment and A/B testing, so you would get to launch those projects and see results immediately. We take a lot of pride in the space we use at HQ for hosting meetup groups and tech talks. Yelp is looking for interns that want the chance to meet and greet with the best and most dynamic engineers, product managers, and leaders in the Valley. Are we looking for you? Great! Then check out our engineering teams and let us know what you are interested in working on. We would love to find out more about you.",
                    "twitter:title": "Yelp - Software Engineer - Intern - Fall",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Engineering and Product \u2013 College Engineering & Product. Intern ... in your \nfavorite modern programming language: Python, Ruby, Java, Objective-C, or C++\n.",
        "title": "Yelp - Software Engineer - Intern - Fall"
    },
    {
        "cacheId": "QA59H8uOSaAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../26eb3281-883f-4803-a37d-2b30dbbb224d",
        "htmlFormattedUrl": "https://jobs.lever.co/.../26eb3281-883f-4803-a37d-2b30dbbb224d",
        "htmlSnippet": "Are you interested in joining a group of highly talented <b>engineers</b> working on ... <br>\npurpose programming languages including but not limited to: Java, C/<b>C++</b>, or Go.",
        "htmlTitle": "Alluxio - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/alluxio/26eb3281-883f-4803-a37d-2b30dbbb224d",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/1f2442ab-8031-4df0-8cd9-f38a1de76d8f-1458828357731.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "105",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSe2ScUBXkNHmvmcJ1caHgXkAoYZnDAWikPqYXooINm0BbExIXFVK1y4EU",
                    "width": "479"
                }
            ],
            "metatags": [
                {
                    "og:description": "Are you interested in joining a group of highly talented engineers working on a project that is changing the world of storage systems? Alluxio' team consists of leaders, innovators, explorers, and risk-takers with extensive industry experience from top tech companies including Google, Palantir and VMWare and alumni from top computer science programs including CMU, Stanford and UC Berkeley. The company is backed by Andreessen-Horowitz and has been named a hot enterprise storage company to watch by Network World. As a software engineer at Alluxio you will be responsible for evolving the state-of-the-art Tachyon project, which is critical to the company's business. This role will provide you with a unique opportunity to impact the success of the company and to grow your career at a fast pace.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/1f2442ab-8031-4df0-8cd9-f38a1de76d8f-1458828357731.png",
                    "og:image:height": "200",
                    "og:title": "Alluxio - Software Engineer",
                    "og:url": "https://jobs.lever.co/alluxio/26eb3281-883f-4803-a37d-2b30dbbb224d",
                    "twitter:description": "Are you interested in joining a group of highly talented engineers working on a project that is changing the world of storage systems? Alluxio' team consists of leaders, innovators, explorers, and risk-takers with extensive industry experience from top tech companies including Google, Palantir and VMWare and alumni from top computer science programs including CMU, Stanford and UC Berkeley. The company is backed by Andreessen-Horowitz and has been named a hot enterprise storage company to watch by Network World. As a software engineer at Alluxio you will be responsible for evolving the state-of-the-art Tachyon project, which is critical to the company's business. This role will provide you with a unique opportunity to impact the success of the company and to grow your career at a fast pace.",
                    "twitter:title": "Alluxio - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Are you interested in joining a group of highly talented engineers working on ... \npurpose programming languages including but not limited to: Java, C/C++, or Go.",
        "title": "Alluxio - Software Engineer"
    },
    {
        "cacheId": "F9WIZC0vBB8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/genovatech/604fb457-189c-4f7c-b8ea.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/genovatech/604fb457-189c-4f7c-b8ea.../apply",
        "htmlSnippet": "Software <b>Engineer</b> (Embedded C, <b>C++</b>, Linux). Cedar Rapids, IA. Software <br>\n<b>Engineering</b>. Full-time. Submit your application. Resume/CV. ATTACH RESUME/<br>\nCV.",
        "htmlTitle": "Genova Technologies - Software <b>Engineer</b> (Embedded C, <b>C++</b>, Linux)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/genovatech/604fb457-189c-4f7c-b8ea-70f7bdfbd69e/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1470156922557.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "167",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS78YDtyY3suTlG2gDqwn0q2rDRU_Vi4vmWxaLzPQgNKg18kp-BilptuT63",
                    "width": "302"
                }
            ],
            "metatags": [
                {
                    "og:description": "\u201cFirst, solve the problem. Then, write the code\u201d Genova Technologies has a unique opportunity in which we are seeking experienced embedded C, C++ and Linux, Software Engineers. If you are local or interested in relocating to the Midwest, we encourage you to apply or reach out to our recruiting staff today. Genova Technologies, Inc. has been in business for 23+ years, and is an engineering services company that specializes in long-term, ongoing W2/benefit-eligible employment. We offer project-based employment to new employees and rotate projects as needed.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1470156922557.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Genova Technologies - Software Engineer (Embedded C, C++, Linux)",
                    "og:url": "https://jobs.lever.co/genovatech/604fb457-189c-4f7c-b8ea-70f7bdfbd69e/apply",
                    "twitter:description": "\u201cFirst, solve the problem. Then, write the code\u201d Genova Technologies has a unique opportunity in which we are seeking experienced embedded C, C++ and Linux, Software Engineers. If you are local or interested in relocating to the Midwest, we encourage you to apply or reach out to our recruiting staff today. Genova Technologies, Inc. has been in business for 23+ years, and is an engineering services company that specializes in long-term, ongoing W2/benefit-eligible employment. We offer project-based employment to new employees and rotate projects as needed.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f0decdc5-3c35-4801-8724-55b887ed0455-1490383577263.png",
                    "twitter:title": "Genova Technologies - Software Engineer (Embedded C, C++, Linux)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer (Embedded C, C++, Linux). Cedar Rapids, IA. Software \nEngineering. Full-time. Submit your application. Resume/CV. ATTACH RESUME/\nCV.",
        "title": "Genova Technologies - Software Engineer (Embedded C, C++, Linux)"
    },
    {
        "cacheId": "8UbfkA9RVyoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/zoox/c070988f-51af-49f6-a0e1-2756dbfcdc2f",
        "htmlFormattedUrl": "https://jobs.lever.co/zoox/c070988f-51af-49f6-a0e1-2756dbfcdc2f",
        "htmlSnippet": "The Firmware <b>Engineering</b> team at Zoox is responsible for bringing together the <br>\n... <b>engineering</b>, mechanical <b>engineering</b>, or related field; Fluent in C / <b>C++</b>&nbsp;...",
        "htmlTitle": "Zoox - Firmware <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/zoox/c070988f-51af-49f6-a0e1-2756dbfcdc2f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "183",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAkruyHxT8E9prOHuSspiQmEZjGkC1SWYHDhWOgBHmm7eEz0oEbgvKng0",
                    "width": "275"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Firmware Engineering team at Zoox is responsible for bringing together the computer science world with the automotive world in order to create an amazing product. As a firmware engineer, you should be passionate about developing production-quality code and designing a product that meets the high safety requirements needed for autonomous driving. Having an advanced degree is a plus but not mandatory. We are looking for a person that is focused and has experience shipping quality products.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Zoox - Firmware Engineer",
                    "og:url": "https://jobs.lever.co/zoox/c070988f-51af-49f6-a0e1-2756dbfcdc2f",
                    "twitter:description": "The Firmware Engineering team at Zoox is responsible for bringing together the computer science world with the automotive world in order to create an amazing product. As a firmware engineer, you should be passionate about developing production-quality code and designing a product that meets the high safety requirements needed for autonomous driving. Having an advanced degree is a plus but not mandatory. We are looking for a person that is focused and has experience shipping quality products.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498849198093.png",
                    "twitter:title": "Zoox - Firmware Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The Firmware Engineering team at Zoox is responsible for bringing together the \n... engineering, mechanical engineering, or related field; Fluent in C / C++\u00a0...",
        "title": "Zoox - Firmware Engineer"
    },
    {
        "cacheId": "1qp3NsxdMg0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../40ffcf93-5a9d-4157-a9e3-88738329be56",
        "htmlFormattedUrl": "https://jobs.lever.co/.../40ffcf93-5a9d-4157-a9e3-88738329be56",
        "htmlSnippet": "5+ years as a software <b>engineer</b> working with OOP languages such as: Python, <br>\nC#, <b>C++</b>, Java. Background in electrical <b>engineering</b>, applied math, gaming,&nbsp;...",
        "htmlTitle": "Tempo Automation - Senior Software <b>Engineer</b> (Factory Automation)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/tempoautomation/40ffcf93-5a9d-4157-a9e3-88738329be56",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/tempoautomationlogo.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "64",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTqy0euUBBsar9f7SInSE4tQPnw5ec5t6fP4GqEULWOxu-eACv5xQthqQ",
                    "width": "600"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join a growing team that's using software to revolutionize the world of electronics manufacturing! We are looking for talented developers who want to make it as fast and seamless as possible for electrical engineers to manufacture their designs, iterate on their ideas, and bring their products to market. This position offers the opportunity to work on CAD analysis tools and robotic factory automation software. A great candidate would have a passion for automating manual processes, building software that delights customers and interest in the hardware space. We are looking for a team player who will learn, coach, and help us make this incredible vision a reality. To learn more about working at Tempo, visit our careers page.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/tempoautomationlogo.png",
                    "og:image:height": "200",
                    "og:title": "Tempo Automation - Senior Software Engineer (Factory Automation)",
                    "og:url": "https://jobs.lever.co/tempoautomation/40ffcf93-5a9d-4157-a9e3-88738329be56",
                    "twitter:description": "Join a growing team that's using software to revolutionize the world of electronics manufacturing! We are looking for talented developers who want to make it as fast and seamless as possible for electrical engineers to manufacture their designs, iterate on their ideas, and bring their products to market. This position offers the opportunity to work on CAD analysis tools and robotic factory automation software. A great candidate would have a passion for automating manual processes, building software that delights customers and interest in the hardware space. We are looking for a team player who will learn, coach, and help us make this incredible vision a reality. To learn more about working at Tempo, visit our careers page.",
                    "twitter:title": "Tempo Automation - Senior Software Engineer (Factory Automation)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "5+ years as a software engineer working with OOP languages such as: Python, \nC#, C++, Java. Background in electrical engineering, applied math, gaming,\u00a0...",
        "title": "Tempo Automation - Senior Software Engineer (Factory Automation)"
    },
    {
        "cacheId": "sEnt9yZhqrgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../58d343d0-4aa6-4516-84c2-c542f68b649a",
        "htmlFormattedUrl": "https://jobs.lever.co/.../58d343d0-4aa6-4516-84c2-c542f68b649a",
        "htmlSnippet": "On the VOD team, you&#39;ll work closely with our other <b>engineering</b> and product ... <br>\nRuby, C, <b>C++</b>, Java, Scala; Strong organizational and communication skills&nbsp;...",
        "htmlTitle": "Twitch - Senior Software <b>Engineer</b> - VOD",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/58d343d0-4aa6-4516-84c2-c542f68b649a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch has over 100 million users, and the VOD team is responsible for building a new experience that helps Twitch users watch recorded video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming recorded video this year. Recently, we launched VOD upload, Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for product engineers that love delighting people with incredible products and user experiences. On the VOD team, you\u2019ll work closely with our other engineering and product teams to craft engaging consumer products, collect feedback, and iterate quickly. We value expertise in programming for the Web, microservices and Devops on AWS. If you are also comfortable with JS and crafting beautiful interfaces, even better! We are working on building unique VOD watching experiences that are uniquely Twitch. We aspire to change the way people consume and interact with video.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - VOD",
                    "og:url": "https://jobs.lever.co/twitch/58d343d0-4aa6-4516-84c2-c542f68b649a",
                    "twitter:description": "Twitch has over 100 million users, and the VOD team is responsible for building a new experience that helps Twitch users watch recorded video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming recorded video this year. Recently, we launched VOD upload, Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for product engineers that love delighting people with incredible products and user experiences. On the VOD team, you\u2019ll work closely with our other engineering and product teams to craft engaging consumer products, collect feedback, and iterate quickly. We value expertise in programming for the Web, microservices and Devops on AWS. If you are also comfortable with JS and crafting beautiful interfaces, even better! We are working on building unique VOD watching experiences that are uniquely Twitch. We aspire to change the way people consume and interact with video.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - VOD",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "On the VOD team, you'll work closely with our other engineering and product ... \nRuby, C, C++, Java, Scala; Strong organizational and communication skills\u00a0...",
        "title": "Twitch - Senior Software Engineer - VOD"
    },
    {
        "cacheId": "Z-uFhcEOifEJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/zoox/951cfc2d-c65b-49bd-b621-44fc22cd2672",
        "htmlFormattedUrl": "https://jobs.lever.co/zoox/951cfc2d-c65b-49bd-b621-44fc22cd2672",
        "htmlSnippet": "As our hardware design <b>engineer</b> supporting sensor development, you will be <br>\nwriting ... Electrical <b>engineering</b>, or related field; Fluency in C / modern <b>C++</b>11&nbsp;...",
        "htmlTitle": "Zoox - Hardware Design <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/zoox/951cfc2d-c65b-49bd-b621-44fc22cd2672",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "183",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAkruyHxT8E9prOHuSspiQmEZjGkC1SWYHDhWOgBHmm7eEz0oEbgvKng0",
                    "width": "275"
                }
            ],
            "metatags": [
                {
                    "og:description": "As our hardware design engineer supporting sensor development, you will be writing firmware in support of our hardware organization. This team is responsible for the design and development of Zoox's sensor technology and compute platform. At Zoox, you will collaborate with a team of world-class engineers with backgrounds in areas such as AI, robotics, mechatronics, and computer vision. You will learn new technologies while writing software that directly affects the real world. Working at Zoox gives you the chance to manifest your creativity and highly impact the final product.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Zoox - Hardware Design Engineer",
                    "og:url": "https://jobs.lever.co/zoox/951cfc2d-c65b-49bd-b621-44fc22cd2672",
                    "twitter:description": "As our hardware design engineer supporting sensor development, you will be writing firmware in support of our hardware organization. This team is responsible for the design and development of Zoox's sensor technology and compute platform. At Zoox, you will collaborate with a team of world-class engineers with backgrounds in areas such as AI, robotics, mechatronics, and computer vision. You will learn new technologies while writing software that directly affects the real world. Working at Zoox gives you the chance to manifest your creativity and highly impact the final product.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498849198093.png",
                    "twitter:title": "Zoox - Hardware Design Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As our hardware design engineer supporting sensor development, you will be \nwriting ... Electrical engineering, or related field; Fluency in C / modern C++11\u00a0...",
        "title": "Zoox - Hardware Design Engineer"
    },
    {
        "cacheId": "PdOdO7ZM40UJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../93ec7c7e-98d9-4920-934f-5ba9ecf206a9",
        "htmlFormattedUrl": "https://jobs.lever.co/.../93ec7c7e-98d9-4920-934f-5ba9ecf206a9",
        "htmlSnippet": "You must have a solid background in C/<b>C++</b>, Java, C# or comparable <br>\nprogramming language. You must have a history of building successful solutions <br>\nfrom&nbsp;...",
        "htmlTitle": "MZ - Principal Software <b>Engineer</b>, Infrastructure",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/93ec7c7e-98d9-4920-934f-5ba9ecf206a9",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "Satori is looking for a Principal Software Engineer to join our engineering team. You will be working with a group of world-class engineers, architects and product managers to build a scalable and high-performance breakthrough platform that will be leveraged by our external customers to build paradigm shifting applications and solutions. You must possess a solid understanding of ultra-large scale, ultra-high performance, multi-data center technologies and services. An obsession with engineering excellence, a natural tendency to self test your code before calling it done and a passion for building a quality user experience. You must have a solid background in C/C++, Java, C# or comparable programming language. You must have a history of building successful solutions from scratch at scale and the ability to quickly grasp unfamiliar technology and integrate it quickly into the solution implementation. You must be able to tech-lead an average to large team. You must know how to start a",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Principal Software Engineer, Infrastructure",
                    "og:url": "https://jobs.lever.co/machinezone/93ec7c7e-98d9-4920-934f-5ba9ecf206a9",
                    "twitter:description": "Satori is looking for a Principal Software Engineer to join our engineering team. You will be working with a group of world-class engineers, architects and product managers to build a scalable and high-performance breakthrough platform that will be leveraged by our external customers to build paradigm shifting applications and solutions. You must possess a solid understanding of ultra-large scale, ultra-high performance, multi-data center technologies and services. An obsession with engineering excellence, a natural tendency to self test your code before calling it done and a passion for building a quality user experience. You must have a solid background in C/C++, Java, C# or comparable programming language. You must have a history of building successful solutions from scratch at scale and the ability to quickly grasp unfamiliar technology and integrate it quickly into the solution implementation. You must be able to tech-lead an average to large team. You must know how to start a",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Principal Software Engineer, Infrastructure",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You must have a solid background in C/C++, Java, C# or comparable \nprogramming language. You must have a history of building successful solutions \nfrom\u00a0...",
        "title": "MZ - Principal Software Engineer, Infrastructure"
    },
    {
        "cacheId": "ELaHxUoOfPkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/zoox/2157ee7f-3b15-45cd-96ea-b76fc835d679",
        "htmlFormattedUrl": "https://jobs.lever.co/zoox/2157ee7f-3b15-45cd-96ea-b76fc835d679",
        "htmlSnippet": "QUALIFICATIONS. Bachelors degree in an <b>engineering</b>, math, or related field; <br>\nFluency in C / <b>C++</b>; Extensive experience with programming and algorithm <br>\ndesign&nbsp;...",
        "htmlTitle": "Zoox - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/zoox/2157ee7f-3b15-45cd-96ea-b76fc835d679",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "183",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAkruyHxT8E9prOHuSspiQmEZjGkC1SWYHDhWOgBHmm7eEz0oEbgvKng0",
                    "width": "275"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a software engineer at Zoox, you will collaborate with a team of world-class engineers with diverse backgrounds in areas such as AI, robotics, mechatronics, planning, machine learning, control, localization, computer vision, rendering, simulation, distributed computing, design, and automated testing. You will master new technologies while working on code, algorithms, and research in your area of expertise to create and refine key systems and move Zoox forward. Working at a startup gives you the chance to manifest your creativity and make highly impact the final product.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Zoox - Software Engineer",
                    "og:url": "https://jobs.lever.co/zoox/2157ee7f-3b15-45cd-96ea-b76fc835d679",
                    "twitter:description": "As a software engineer at Zoox, you will collaborate with a team of world-class engineers with diverse backgrounds in areas such as AI, robotics, mechatronics, planning, machine learning, control, localization, computer vision, rendering, simulation, distributed computing, design, and automated testing. You will master new technologies while working on code, algorithms, and research in your area of expertise to create and refine key systems and move Zoox forward. Working at a startup gives you the chance to manifest your creativity and make highly impact the final product.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498849198093.png",
                    "twitter:title": "Zoox - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "QUALIFICATIONS. Bachelors degree in an engineering, math, or related field; \nFluency in C / C++; Extensive experience with programming and algorithm \ndesign\u00a0...",
        "title": "Zoox - Software Engineer"
    },
    {
        "cacheId": "L2h-ZJ_XVn0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../faec32fa-4a76-4c99-bfec-d0b8a7cad6a9",
        "htmlFormattedUrl": "https://jobs.lever.co/.../faec32fa-4a76-4c99-bfec-d0b8a7cad6a9",
        "htmlSnippet": "We are at the beginning of this <b>engineering</b> journey and are looking for great ... <br>\nGo, or C/ <b>C++</b>; Solid understanding of basic systems operations (disk, network,&nbsp;...",
        "htmlTitle": "Confluent - Confluent Cloud <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/confluent/faec32fa-4a76-4c99-bfec-d0b8a7cad6a9",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/confluent_logo.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "70",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJwgg_YCM-2p-b-FGA3H3JKOD9u-SkbPFgfxpokm2MtFhU7xeyIm7dsOc",
                    "width": "328"
                }
            ],
            "metatags": [
                {
                    "og:description": "The next big goal for Confluent is to make it as easy as possible for anyone to use Confluent\u2019s products, including Kafka, to build their next killer streaming application. To do that we are building the Confluent Cloud which provides our products as a service in all the major public clouds. We are at the beginning of this engineering journey and are looking for great engineers to come join the world class team of engineers that are passionate about building and running large scale, multi-tenant distributed data systems for customers that expect a very high level of availability.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/confluent_logo.png",
                    "og:image:height": "200",
                    "og:title": "Confluent - Confluent Cloud Engineer",
                    "og:url": "https://jobs.lever.co/confluent/faec32fa-4a76-4c99-bfec-d0b8a7cad6a9",
                    "twitter:description": "The next big goal for Confluent is to make it as easy as possible for anyone to use Confluent\u2019s products, including Kafka, to build their next killer streaming application. To do that we are building the Confluent Cloud which provides our products as a service in all the major public clouds. We are at the beginning of this engineering journey and are looking for great engineers to come join the world class team of engineers that are passionate about building and running large scale, multi-tenant distributed data systems for customers that expect a very high level of availability.",
                    "twitter:title": "Confluent - Confluent Cloud Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are at the beginning of this engineering journey and are looking for great ... \nGo, or C/ C++; Solid understanding of basic systems operations (disk, network,\u00a0...",
        "title": "Confluent - Confluent Cloud Engineer"
    },
    {
        "cacheId": "xiBSutZWP9IJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
        "htmlSnippet": "As a Senior iOS Software <b>Engineer</b>, you will provide technical leadership and <br>\nmake ... of C/<b>C++</b>; Familiarity with web technologies and languages (HTTP, REST<br>\n,&nbsp;...",
        "htmlTitle": "Twitch - Senior iOS <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As a Senior iOS Software Engineer, you will provide technical leadership and make direct contributions to an app that is the portal to the Twitch community for millions of users.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior iOS Engineer",
                    "og:url": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
                    "twitter:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As a Senior iOS Software Engineer, you will provide technical leadership and make direct contributions to an app that is the portal to the Twitch community for millions of users.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior iOS Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Senior iOS Software Engineer, you will provide technical leadership and \nmake ... of C/C++; Familiarity with web technologies and languages (HTTP, REST\n,\u00a0...",
        "title": "Twitch - Senior iOS Engineer"
    },
    {
        "cacheId": "b_U0XLyXDnQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../569c9e5a-516e-4b9c-85f6-f1c0a44e9cbb",
        "htmlFormattedUrl": "https://jobs.lever.co/.../569c9e5a-516e-4b9c-85f6-f1c0a44e9cbb",
        "htmlSnippet": "Embedded Software <b>Engineer</b>, ADAS and Self Driving ... \u00b72+ years of experience <br>\nin multi-threaded software application using C, <b>C++</b>, Java. \u00b72+ years of&nbsp;...",
        "htmlTitle": "Faraday Future - Embedded Software <b>Engineer</b>, ADAS and Self ...",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/569c9e5a-516e-4b9c-85f6-f1c0a44e9cbb",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "200",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRMLgdzJ9p7OVcfhxA-sLzhziSZ3QW_QuFkRHJCamIy2dOxKa6cY27TAsw",
                    "width": "200"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Company: Faraday Future (FF) is a California-based mobility company, leveraging the latest technologies and world\u2019s best talent to realize exciting new possibilities in sustainable transportation. We\u2019re producing user-centric, technology-first vehicles to establish new paradigms in human-vehicle interaction. We\u2019re not just seeking to change how our cars work \u2013 we\u2019re seeking to change the way we drive. At FF, we\u2019re creating something new, something connected, and something with a global impact. Job Description \u00b7 Support porting, integration and optimization of new ADAS and Self-Driving application and infrastructure software into production embedded controllers with high-end multi-core processor(s) for automotive production application \u00b7 Support embedded systems architecture design in the domain controller \u00b7 Support the embedded system development environment, tools, design solutions and verification Responsibilities \u00b7 Support all activities in embedded software development cy",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Embedded Software Engineer, ADAS and Self Driving",
                    "og:url": "https://jobs.lever.co/faradayfuture/569c9e5a-516e-4b9c-85f6-f1c0a44e9cbb",
                    "twitter:description": "The Company: Faraday Future (FF) is a California-based mobility company, leveraging the latest technologies and world\u2019s best talent to realize exciting new possibilities in sustainable transportation. We\u2019re producing user-centric, technology-first vehicles to establish new paradigms in human-vehicle interaction. We\u2019re not just seeking to change how our cars work \u2013 we\u2019re seeking to change the way we drive. At FF, we\u2019re creating something new, something connected, and something with a global impact. Job Description \u00b7 Support porting, integration and optimization of new ADAS and Self-Driving application and infrastructure software into production embedded controllers with high-end multi-core processor(s) for automotive production application \u00b7 Support embedded systems architecture design in the domain controller \u00b7 Support the embedded system development environment, tools, design solutions and verification Responsibilities \u00b7 Support all activities in embedded software development cy",
                    "twitter:title": "Faraday Future - Embedded Software Engineer, ADAS and Self Driving",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Embedded Software Engineer, ADAS and Self Driving ... \u00b72+ years of experience \nin multi-threaded software application using C, C++, Java. \u00b72+ years of\u00a0...",
        "title": "Faraday Future - Embedded Software Engineer, ADAS and Self ..."
    },
    {
        "cacheId": "oL59lEO6QkkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/...ai.../e58723b5-6976-4624-9030-bb7fe2875b7d",
        "htmlFormattedUrl": "https://jobs.lever.co/...ai.../e58723b5-6976-4624-9030-bb7fe2875b7d",
        "htmlSnippet": "We are hiring a number of Software <b>Engineers</b> who will work alongside our <br>\nhardware ... Strong software design / <b>engineering</b> skills, C, <b>C++</b>, excellent <br>\ndebugging&nbsp;...",
        "htmlTitle": "Mythic - Compiler and Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mythic-ai.com/e58723b5-6976-4624-9030-bb7fe2875b7d",
        "pagemap": {
            "metatags": [
                {
                    "og:description": "We are hiring a number of Software Engineers who will work alongside our hardware team to enable execution of advanced AI algorithms on Mythic's hardware. This is the opportunity for those without data science experience to jump into the AI world at a company developing solutions 50x better than the competitors. We are building out tools, compilers, and diagnostics and want to add engineers to our team that have a variety of skills. This role will be responsible for validating hardware instruction sets and operating models, compiling and transforming neural networks onto the Mythic architecture, and developing tools and feedback mechanisms to improve neural network training and optimization. Compiler experience is a plus: while this role will not be responsible for building a full compiler for a high level language, it will leverage concepts and methodologies that are similar. However, our hardware and the challenges are unique enough that we will also consider those with strong core",
                    "og:image:height": "200",
                    "og:title": "Mythic - Compiler and Software Engineer",
                    "og:url": "https://jobs.lever.co/mythic-ai.com/e58723b5-6976-4624-9030-bb7fe2875b7d",
                    "twitter:description": "We are hiring a number of Software Engineers who will work alongside our hardware team to enable execution of advanced AI algorithms on Mythic's hardware. This is the opportunity for those without data science experience to jump into the AI world at a company developing solutions 50x better than the competitors. We are building out tools, compilers, and diagnostics and want to add engineers to our team that have a variety of skills. This role will be responsible for validating hardware instruction sets and operating models, compiling and transforming neural networks onto the Mythic architecture, and developing tools and feedback mechanisms to improve neural network training and optimization. Compiler experience is a plus: while this role will not be responsible for building a full compiler for a high level language, it will leverage concepts and methodologies that are similar. However, our hardware and the challenges are unique enough that we will also consider those with strong core",
                    "twitter:title": "Mythic - Compiler and Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are hiring a number of Software Engineers who will work alongside our \nhardware ... Strong software design / engineering skills, C, C++, excellent \ndebugging\u00a0...",
        "title": "Mythic - Compiler and Software Engineer"
    },
    {
        "cacheId": "ZePYSCpWJMcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
        "htmlSnippet": "Clients Platform &amp; Product Development \u2013 Clients <b>Engineering</b> ... knowledge of a <br>\nhigh-level programming language like JavaScript, <b>C++</b>, Java, Python, etc.",
        "htmlTitle": "Twitch - Senior Software <b>Engineer</b> - Internationalization",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Millions of visitors per month watch billions of minutes of video on Twitch around the world in many locales and languages on the web, mobile and gaming consoles. Our team builds the foundations that ensure overall product quality and functionality for all software development at Twitch, including bringing all our products to world readiness. Agile and effective collaboration with other teams is at the heart of our charter, our challenge and our passion. You are passionate about software development and delivering a great product to all users around the world. You, keep up-to-date with your craft but often dabble beyond; you are intellectually curious, inventive and eager to grow. You understand how code is written up and down the stack and how to build, integrate, test and deploy global-ready solutions with the latest tools and best practices. You are equally excited to build a minimum viable product quickly as you are cementing a proven feature in maintainable and tested code; you f",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Internationalization",
                    "og:url": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
                    "twitter:description": "Millions of visitors per month watch billions of minutes of video on Twitch around the world in many locales and languages on the web, mobile and gaming consoles. Our team builds the foundations that ensure overall product quality and functionality for all software development at Twitch, including bringing all our products to world readiness. Agile and effective collaboration with other teams is at the heart of our charter, our challenge and our passion. You are passionate about software development and delivering a great product to all users around the world. You, keep up-to-date with your craft but often dabble beyond; you are intellectually curious, inventive and eager to grow. You understand how code is written up and down the stack and how to build, integrate, test and deploy global-ready solutions with the latest tools and best practices. You are equally excited to build a minimum viable product quickly as you are cementing a proven feature in maintainable and tested code; you f",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Internationalization",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Clients Platform & Product Development \u2013 Clients Engineering ... knowledge of a \nhigh-level programming language like JavaScript, C++, Java, Python, etc.",
        "title": "Twitch - Senior Software Engineer - Internationalization"
    },
    {
        "cacheId": "7cAtbZZZzYYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../8576e056-74f8-4f55-9d8b-3bd100202345",
        "htmlFormattedUrl": "https://jobs.lever.co/.../8576e056-74f8-4f55-9d8b-3bd100202345",
        "htmlSnippet": "Proficient knowledge in Java/C/<b>C++</b>. Basic understanding of SQL. Experience <br>\nimplementing a business intelligence or reporting system. Strong understanding<br>\n&nbsp;...",
        "htmlTitle": "Drawbridge - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/drawbridge/8576e056-74f8-4f55-9d8b-3bd100202345",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwcwXStLSk03_g-LKG8cnhZOlvetfTK3WHqD394bjfElRrSCMigDtkqNXZ",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "About Drawbridge Drawbridge is the leading anonymized digital identity company, building patented cross-device technology that fundamentally changes the way brands connect with people. In fact, Drawbridge coined the term \u201ccross-device\u201d and has been a pioneer in cross-device identity. The company provides visibility into how consumers interact across devices along the path to purchase, giving marketers insight into both online and offline behavior to drive better results. The company is headquartered in Silicon Valley, is backed by Sequoia Capital, Kleiner Perkins Caufield Byers, and Northgate Capital, and has been named to the Inc. 5000 annual ranking of the fastest-growing companies in America for the past two years. For more information visit www.drawbridge.com.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Drawbridge - Software Engineer",
                    "og:url": "https://jobs.lever.co/drawbridge/8576e056-74f8-4f55-9d8b-3bd100202345",
                    "twitter:description": "About Drawbridge Drawbridge is the leading anonymized digital identity company, building patented cross-device technology that fundamentally changes the way brands connect with people. In fact, Drawbridge coined the term \u201ccross-device\u201d and has been a pioneer in cross-device identity. The company provides visibility into how consumers interact across devices along the path to purchase, giving marketers insight into both online and offline behavior to drive better results. The company is headquartered in Silicon Valley, is backed by Sequoia Capital, Kleiner Perkins Caufield Byers, and Northgate Capital, and has been named to the Inc. 5000 annual ranking of the fastest-growing companies in America for the past two years. For more information visit www.drawbridge.com.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725516278.png",
                    "twitter:title": "Drawbridge - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Proficient knowledge in Java/C/C++. Basic understanding of SQL. Experience \nimplementing a business intelligence or reporting system. Strong understanding\n\u00a0...",
        "title": "Drawbridge - Software Engineer"
    },
    {
        "cacheId": "W6f50jVmjowJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../f7d86a67-a3ba-45b4-b0c5-c5ed678a8ea4",
        "htmlFormattedUrl": "https://jobs.lever.co/.../f7d86a67-a3ba-45b4-b0c5-c5ed678a8ea4",
        "htmlSnippet": "Zipline is looking for a software <b>engineer</b> who is clever and fast at integrating ... <br>\nProduction-level Python, C, <b>C++</b>; Tool building in Linux and Bash; Making&nbsp;...",
        "htmlTitle": "Zipline - Software <b>Engineer</b> \u2013 Generalist",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/flyzipline/f7d86a67-a3ba-45b4-b0c5-c5ed678a8ea4",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/85e5c177-1c48-44f8-a814-d88bb0584f08-1470355906495.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "146",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRA1dg8b_I3I1YzLprkBF2fuxdzt0ROIC1l6DqgCae9_-jWOgMzL3AOeJo",
                    "width": "344"
                }
            ],
            "metatags": [
                {
                    "og:description": "Zipline is looking for a software engineer who is clever and fast at integrating systems, building tools, and solving hard problems.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/85e5c177-1c48-44f8-a814-d88bb0584f08-1470355906495.png",
                    "og:image:height": "200",
                    "og:title": "Zipline - Software Engineer \u2013 Generalist",
                    "og:url": "https://jobs.lever.co/flyzipline/f7d86a67-a3ba-45b4-b0c5-c5ed678a8ea4",
                    "twitter:description": "Zipline is looking for a software engineer who is clever and fast at integrating systems, building tools, and solving hard problems.",
                    "twitter:title": "Zipline - Software Engineer \u2013 Generalist",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Zipline is looking for a software engineer who is clever and fast at integrating ... \nProduction-level Python, C, C++; Tool building in Linux and Bash; Making\u00a0...",
        "title": "Zipline - Software Engineer \u2013 Generalist"
    },
    {
        "cacheId": "D7XmrAMwqEsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../546b332a-a932-4807-835f-03557428c7f3",
        "htmlFormattedUrl": "https://jobs.lever.co/.../546b332a-a932-4807-835f-03557428c7f3",
        "htmlSnippet": "As the Sr. Software <b>Engineer</b>, you&#39;ll be working with some of the industry&#39;s <br>\nbrightest ... o Python 2.7. o REST-API. o Embedded C. o Software <b>Engineering</b>. o <br>\n<b>C++</b>.",
        "htmlTitle": "Faraday Future - Senior Software <b>Engineer</b> - Tools",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/546b332a-a932-4807-835f-03557428c7f3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "Sr. Software Engineer \u2013 Tools The Company: Faraday Future (FF) is a California-based mobility company, leveraging the latest technologies and world\u2019s best talent to realize exciting new possibilities in sustainable transportation. We\u2019re producing user-centric, technology-first vehicles to establish new paradigms in human-vehicle interaction. We\u2019re not just seeking to change how our cars work \u2013 we\u2019re seeking to change the way we drive. At FF, we\u2019re creating something new, something connected, and something with a global impact. Position: Sr. Software Engineer \u2013 Tools Your Role: As the Sr. Software Engineer, you\u2019ll be working with some of the industry\u2019s brightest minds to design and author cutting edge tools, do test automation, and work with databases and APIs. Basically, you\u2019ll make sure that engineers have tested tools they need and that processes for doing this are automated. Basic Qualifications: \u00b7 Engineering Degree: preferably masters in Computer Science/Electrical E",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Senior Software Engineer - Tools",
                    "og:url": "https://jobs.lever.co/faradayfuture/546b332a-a932-4807-835f-03557428c7f3",
                    "twitter:description": "Sr. Software Engineer \u2013 Tools The Company: Faraday Future (FF) is a California-based mobility company, leveraging the latest technologies and world\u2019s best talent to realize exciting new possibilities in sustainable transportation. We\u2019re producing user-centric, technology-first vehicles to establish new paradigms in human-vehicle interaction. We\u2019re not just seeking to change how our cars work \u2013 we\u2019re seeking to change the way we drive. At FF, we\u2019re creating something new, something connected, and something with a global impact. Position: Sr. Software Engineer \u2013 Tools Your Role: As the Sr. Software Engineer, you\u2019ll be working with some of the industry\u2019s brightest minds to design and author cutting edge tools, do test automation, and work with databases and APIs. Basically, you\u2019ll make sure that engineers have tested tools they need and that processes for doing this are automated. Basic Qualifications: \u00b7 Engineering Degree: preferably masters in Computer Science/Electrical E",
                    "twitter:title": "Faraday Future - Senior Software Engineer - Tools",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As the Sr. Software Engineer, you'll be working with some of the industry's \nbrightest ... o Python 2.7. o REST-API. o Embedded C. o Software Engineering. o \nC++.",
        "title": "Faraday Future - Senior Software Engineer - Tools"
    },
    {
        "cacheId": "01JFClkI6RwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../2dfa5dd6-9175-4d80-8983-c68b2caf61ec",
        "htmlFormattedUrl": "https://jobs.lever.co/.../2dfa5dd6-9175-4d80-8983-c68b2caf61ec",
        "htmlSnippet": "Proficient knowledge in Java/C/<b>C++</b>. Basic understanding of SQL. Experience <br>\nimplementing a business intelligence or reporting system. Strong understanding<br>\n&nbsp;...",
        "htmlTitle": "Drawbridge - Hadoop SPARK <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/drawbridge/2dfa5dd6-9175-4d80-8983-c68b2caf61ec",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwcwXStLSk03_g-LKG8cnhZOlvetfTK3WHqD394bjfElRrSCMigDtkqNXZ",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "If you are a interested in Hadoop and want to have an impact on our Graph team, read on! About Drawbridge Drawbridge is the leading anonymized cross-device identity company building technology that fundamentally changes the way brands connect with people. The Drawbridge Connected Consumer Graph\u2122 includes more than one billion consumers across more than three billion devices, and was found by Nielsen to be up to 97.3% precise. Brands can work with Drawbridge in three ways: by licensing the Drawbridge Connected Consumer Graph for cross-device data applications; managing cross-device ad campaigns in real-time using the Drawbridge Cross-Device Platform; or working with Drawbridge to execute cross-device campaigns. The company is headquartered in Silicon Valley, is backed by Sequoia Capital, Kleiner Perkins Caufield and Byers, and Northgate Capital, and was named the fastest growing marketing and advertising company and sixth overall on the 2015 Inc. 5000 list. For more information visit",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Drawbridge - Hadoop SPARK Engineer",
                    "og:url": "https://jobs.lever.co/drawbridge/2dfa5dd6-9175-4d80-8983-c68b2caf61ec",
                    "twitter:description": "If you are a interested in Hadoop and want to have an impact on our Graph team, read on! About Drawbridge Drawbridge is the leading anonymized cross-device identity company building technology that fundamentally changes the way brands connect with people. The Drawbridge Connected Consumer Graph\u2122 includes more than one billion consumers across more than three billion devices, and was found by Nielsen to be up to 97.3% precise. Brands can work with Drawbridge in three ways: by licensing the Drawbridge Connected Consumer Graph for cross-device data applications; managing cross-device ad campaigns in real-time using the Drawbridge Cross-Device Platform; or working with Drawbridge to execute cross-device campaigns. The company is headquartered in Silicon Valley, is backed by Sequoia Capital, Kleiner Perkins Caufield and Byers, and Northgate Capital, and was named the fastest growing marketing and advertising company and sixth overall on the 2015 Inc. 5000 list. For more information visit",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725516278.png",
                    "twitter:title": "Drawbridge - Hadoop SPARK Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Proficient knowledge in Java/C/C++. Basic understanding of SQL. Experience \nimplementing a business intelligence or reporting system. Strong understanding\n\u00a0...",
        "title": "Drawbridge - Hadoop SPARK Engineer"
    },
    {
        "cacheId": "bWuAanfwM00J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../81ced80b-9b3a-40b8-8d5d-7297df8d876d",
        "htmlFormattedUrl": "https://jobs.lever.co/.../81ced80b-9b3a-40b8-8d5d-7297df8d876d",
        "htmlSnippet": "Join our <b>engineering</b> team to implement state of the art algorithms and add ... <br>\nvision and image processing, and have a strong background in modern <b>C++</b>.",
        "htmlTitle": "VideoStitch - Software <b>Engineer</b> (C++) - Graphics processing",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/videostitch/81ced80b-9b3a-40b8-8d5d-7297df8d876d",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/cb59f53a-c69c-4ac2-8f28-b07af9ec9655-1492158303087.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "123",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT4bdmJEJ2e9rWPjuCXfTBa9HAmWg4C48HjizGTmJkgxyYiOuCeItJzkcc",
                    "width": "410"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join our engineering team to implement state of the art algorithms and add features to our innovative software suite for VR video. Improve the performance of the current code base, going to higher frame rates, higher resolutions and lower hardware requirements. As a versatile software engineer, you are able to design new features in a clean architecture, optimize imaging algorithms and integrate changes of the core library into the user interface. Along your code you write unit, performance and regression tests, and don't shy away from fixing bugs, coaching others and participate in other development efforts. With the R&D team, you implement state of the art panoramic video stitching algorithms and you take care of the pipe line that processes dozens of high resolution frames of multiple cameras in real time. You are familiar with computer vision and image processing, and have a strong background in modern C++. You are comfortable with parallelism, theoretical computer science, algor",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/cb59f53a-c69c-4ac2-8f28-b07af9ec9655-1492158303087.png",
                    "og:image:height": "200",
                    "og:title": "VideoStitch - Software Engineer (C++) - Graphics processing",
                    "og:url": "https://jobs.lever.co/videostitch/81ced80b-9b3a-40b8-8d5d-7297df8d876d",
                    "twitter:description": "Join our engineering team to implement state of the art algorithms and add features to our innovative software suite for VR video. Improve the performance of the current code base, going to higher frame rates, higher resolutions and lower hardware requirements. As a versatile software engineer, you are able to design new features in a clean architecture, optimize imaging algorithms and integrate changes of the core library into the user interface. Along your code you write unit, performance and regression tests, and don't shy away from fixing bugs, coaching others and participate in other development efforts. With the R&D team, you implement state of the art panoramic video stitching algorithms and you take care of the pipe line that processes dozens of high resolution frames of multiple cameras in real time. You are familiar with computer vision and image processing, and have a strong background in modern C++. You are comfortable with parallelism, theoretical computer science, algor",
                    "twitter:title": "VideoStitch - Software Engineer (C++) - Graphics processing",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Join our engineering team to implement state of the art algorithms and add ... \nvision and image processing, and have a strong background in modern C++.",
        "title": "VideoStitch - Software Engineer (C++) - Graphics processing"
    },
    {
        "cacheId": "69SBRj9FW6EJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../94dbd55f-0810-436f-9f1d-bf1446b114ff",
        "htmlFormattedUrl": "https://jobs.lever.co/.../94dbd55f-0810-436f-9f1d-bf1446b114ff",
        "htmlSnippet": "BS in Software, Electrical, Computer <b>Engineering</b> or related. \u25cb Embedded <br>\nsoftware development experience, including experience in Java and C/<b>C++</b>.",
        "htmlTitle": "Faraday Future - Android Multimedia <b>Engineers</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/94dbd55f-0810-436f-9f1d-bf1446b114ff",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Company: Faraday Future is a California mobility company bringing a tech approach to clean transportation. At FF, we believe that by placing equal emphasis on automotive and technology disciplines, our team of experts is uniquely positioned to take a user-centric, technology-first approach to vehicle design with the ultimate aim of connecting the automotive experience with the rest of your life. Android Multimedia Engineer Your Role: We're looking for an experienced Android Multimedia Developer to join our team. The IoV (Internet of vehicle) Software Platform Team at Faraday Future is building a completely new generation \u201cinfotainment\u201d products with adhesive user experience. We'd like you to be a part of the revolution, and work together to invent, prototype, iterate, and ship software that matches the quality/experience of the internet giants, and leaves the traditional automotive industry in the rear view mirror. \u25cf Design and develop innovati",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Android Multimedia Engineers",
                    "og:url": "https://jobs.lever.co/faradayfuture/94dbd55f-0810-436f-9f1d-bf1446b114ff",
                    "twitter:description": "The Company: Faraday Future is a California mobility company bringing a tech approach to clean transportation. At FF, we believe that by placing equal emphasis on automotive and technology disciplines, our team of experts is uniquely positioned to take a user-centric, technology-first approach to vehicle design with the ultimate aim of connecting the automotive experience with the rest of your life. Android Multimedia Engineer Your Role: We're looking for an experienced Android Multimedia Developer to join our team. The IoV (Internet of vehicle) Software Platform Team at Faraday Future is building a completely new generation \u201cinfotainment\u201d products with adhesive user experience. We'd like you to be a part of the revolution, and work together to invent, prototype, iterate, and ship software that matches the quality/experience of the internet giants, and leaves the traditional automotive industry in the rear view mirror. \u25cf Design and develop innovati",
                    "twitter:title": "Faraday Future - Android Multimedia Engineers",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "BS in Software, Electrical, Computer Engineering or related. \u25cb Embedded \nsoftware development experience, including experience in Java and C/C++.",
        "title": "Faraday Future - Android Multimedia Engineers"
    },
    {
        "cacheId": "PCWCt8NgwVYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../948cfac4-9c81-44db-85d4-1f17e0887104",
        "htmlFormattedUrl": "https://jobs.lever.co/.../948cfac4-9c81-44db-85d4-1f17e0887104",
        "htmlSnippet": "-Experience with MATLAB, Python, Mathematica, or other scientific programming <br>\nlanguage. -Experience programming in C/<b>C++</b>. Programming for embedded&nbsp;...",
        "htmlTitle": "Nixie Labs - Systems <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/flynixie/948cfac4-9c81-44db-85d4-1f17e0887104",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/89a63f57-6391-4f35-af1b-24850b28eae1-1477418766858.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTe_NF0VjoiJRTMnDFPhdgzp_U0xO5ZGFNqG4Y2XOzMUfdMSM29h0NfYtNo",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "Nixie is a portable flying camera that captures candid shots of you in the moment, without interrupting the action. Nixie was the Grand Prize winner in Intel's Make-it-Wearable challenge. We presented a live demo in the CES 2015 Keynote with the CEO of Intel and won the event! Our technology pushes the boundaries of sensing, controls, autonomy, airframe, and safety design. With a huge amount of seed funding we are developing Nixie to deliver a unique product and user experience to mass consumer marketplace. A product that will allow users to capture and share engaging images and videos without having to experience life\u2019s best moments through a viewfinder. We are making making the unthinkable happen, so come join us! Responsibilities: Work with electrical engineers, mechanical engineers, scientists, and UI designers. Work cross functionally to reduce the weight of the structure, refine design, devices thermal management, ergonomics, and electronics integration. Be a big part of takin",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/89a63f57-6391-4f35-af1b-24850b28eae1-1477418766858.png",
                    "og:image:height": "200",
                    "og:title": "Nixie Labs - Systems Engineer",
                    "og:url": "https://jobs.lever.co/flynixie/948cfac4-9c81-44db-85d4-1f17e0887104",
                    "twitter:description": "Nixie is a portable flying camera that captures candid shots of you in the moment, without interrupting the action. Nixie was the Grand Prize winner in Intel's Make-it-Wearable challenge. We presented a live demo in the CES 2015 Keynote with the CEO of Intel and won the event! Our technology pushes the boundaries of sensing, controls, autonomy, airframe, and safety design. With a huge amount of seed funding we are developing Nixie to deliver a unique product and user experience to mass consumer marketplace. A product that will allow users to capture and share engaging images and videos without having to experience life\u2019s best moments through a viewfinder. We are making making the unthinkable happen, so come join us! Responsibilities: Work with electrical engineers, mechanical engineers, scientists, and UI designers. Work cross functionally to reduce the weight of the structure, refine design, devices thermal management, ergonomics, and electronics integration. Be a big part of takin",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/89a63f57-6391-4f35-af1b-24850b28eae1-1477418742461.png",
                    "twitter:title": "Nixie Labs - Systems Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "-Experience with MATLAB, Python, Mathematica, or other scientific programming \nlanguage. -Experience programming in C/C++. Programming for embedded\u00a0...",
        "title": "Nixie Labs - Systems Engineer"
    },
    {
        "cacheId": "_yDt2cAIXpkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../65f59d09-15b6-4654-a45e-53994965218f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../65f59d09-15b6-4654-a45e-53994965218f",
        "htmlSnippet": "Proficient knowledge in Java/C/<b>C++</b>. Basic understanding of SQL. Experience in <br>\nGraph Algorithms and Graph processing engines like Neo4j, Giraph, GraphX&nbsp;...",
        "htmlTitle": "Drawbridge - Sr. SPARK <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/drawbridge/65f59d09-15b6-4654-a45e-53994965218f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwcwXStLSk03_g-LKG8cnhZOlvetfTK3WHqD394bjfElRrSCMigDtkqNXZ",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Are you passionate about Big Data? This is a great opportunity for an outstanding candidate who wants to work with top notch engineers and is interested in building smart, scalable systems using Hadoop stack technologies! The ideal candidate will have a good understanding of MapReduce and the Hadoop stack . We are making decisions and predicting the future with data - if you want to work on bleeding-edge technology, handling tens of billions of transactions a day, this may be the opportunity for you!\" About Drawbridge Drawbridge is the leading anonymized digital identity company, building patented cross-device technology that fundamentally changes the way brands connect with people. In fact, Drawbridge coined the term \u201ccross-device\u201d and has been a pioneer in cross-device identity. The company provides visibility into how consumers interact across devices along the path to purchase, giving marketers insight into both online and offline behavior to drive better results. The company is h",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Drawbridge - Sr. SPARK Engineer",
                    "og:url": "https://jobs.lever.co/drawbridge/65f59d09-15b6-4654-a45e-53994965218f",
                    "twitter:description": "Are you passionate about Big Data? This is a great opportunity for an outstanding candidate who wants to work with top notch engineers and is interested in building smart, scalable systems using Hadoop stack technologies! The ideal candidate will have a good understanding of MapReduce and the Hadoop stack . We are making decisions and predicting the future with data - if you want to work on bleeding-edge technology, handling tens of billions of transactions a day, this may be the opportunity for you!\" About Drawbridge Drawbridge is the leading anonymized digital identity company, building patented cross-device technology that fundamentally changes the way brands connect with people. In fact, Drawbridge coined the term \u201ccross-device\u201d and has been a pioneer in cross-device identity. The company provides visibility into how consumers interact across devices along the path to purchase, giving marketers insight into both online and offline behavior to drive better results. The company is h",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725516278.png",
                    "twitter:title": "Drawbridge - Sr. SPARK Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Proficient knowledge in Java/C/C++. Basic understanding of SQL. Experience in \nGraph Algorithms and Graph processing engines like Neo4j, Giraph, GraphX\u00a0...",
        "title": "Drawbridge - Sr. SPARK Engineer"
    },
    {
        "cacheId": "SucfbyKoop8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../87481a21-900a-4a67-95be-778b7286e555",
        "htmlFormattedUrl": "https://jobs.lever.co/.../87481a21-900a-4a67-95be-778b7286e555",
        "htmlSnippet": "We&#39;re looking for a strong <b>Engineer</b> to join our Financial Foundry team to ... in a <br>\nmainstream programming language: Python, PHP, Ruby, C#, <b>C++</b>, Java, etc.",
        "htmlTitle": "Eventbrite - Software <b>Engineer</b> - Financial",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/87481a21-900a-4a67-95be-778b7286e555",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTTvFuICOfdvSfhbE4ObHsOali-3FCbYdpz22h0yVaHrVVzEgqRWhDCgXU",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "THE CHALLENGE Financial Engineering is incredibly important for any global marketplace. The success of the business as well as its customers depends on building and maintaining a best-in-class financial ecosystem that produces, monitors, and validates Eventbrite\u2019s data. We're looking for a strong Engineer to join our Financial Foundry team to help us take our financial platform to the next level. THE TEAM The Financial Foundry team is responsible for building infrastructure for, and maintaining the health of, the Eventbrite financial ecosystem. We are tasked with ensuring that Eventbrite's marketplace is as stable, scalable, and as accurate as possible. The team builds tools and processes to manipulate, move, audit, and reconcile financial data. We also consult other teams on best practices when working with high-risk data and code. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail togeth",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Software Engineer - Financial",
                    "og:url": "https://jobs.lever.co/eventbrite/87481a21-900a-4a67-95be-778b7286e555",
                    "twitter:description": "THE CHALLENGE Financial Engineering is incredibly important for any global marketplace. The success of the business as well as its customers depends on building and maintaining a best-in-class financial ecosystem that produces, monitors, and validates Eventbrite\u2019s data. We're looking for a strong Engineer to join our Financial Foundry team to help us take our financial platform to the next level. THE TEAM The Financial Foundry team is responsible for building infrastructure for, and maintaining the health of, the Eventbrite financial ecosystem. We are tasked with ensuring that Eventbrite's marketplace is as stable, scalable, and as accurate as possible. The team builds tools and processes to manipulate, move, audit, and reconcile financial data. We also consult other teams on best practices when working with high-risk data and code. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail togeth",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Software Engineer - Financial",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for a strong Engineer to join our Financial Foundry team to ... in a \nmainstream programming language: Python, PHP, Ruby, C#, C++, Java, etc.",
        "title": "Eventbrite - Software Engineer - Financial"
    },
    {
        "cacheId": "3UywsZWkSyUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../786045c4-5534-4d97-b04a-74771f6856bb",
        "htmlFormattedUrl": "https://jobs.lever.co/.../786045c4-5534-4d97-b04a-74771f6856bb",
        "htmlSnippet": "On the infra team, you&#39;ll work closely with our other <b>engineering</b> and product <br>\nteams ... Ruby, C, <b>C++</b>, Java, Scala; Strong organizational and communication <br>\nskills&nbsp;...",
        "htmlTitle": "Twitch - Senior Software <b>Engineer</b> - Infrastructure",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch has over 100 million users, and the Video Infra team is responsible for building infra services and tools to help scale and manage the infrastructure that powers Twitch\u2019s video. We\u2019re building a number of features to make Twitch the most compelling destination for video. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On the infra team, you\u2019ll work closely with our other engineering and product teams to craft engaging systems collect feedback, and iterate quickly. We value expertise in distributed systems, microservices and Devops on AWS. We are working on building an even more robust video system to scale twitch to the next level .",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Infrastructure",
                    "og:url": "https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb",
                    "twitter:description": "Twitch has over 100 million users, and the Video Infra team is responsible for building infra services and tools to help scale and manage the infrastructure that powers Twitch\u2019s video. We\u2019re building a number of features to make Twitch the most compelling destination for video. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On the infra team, you\u2019ll work closely with our other engineering and product teams to craft engaging systems collect feedback, and iterate quickly. We value expertise in distributed systems, microservices and Devops on AWS. We are working on building an even more robust video system to scale twitch to the next level .",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Infrastructure",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "On the infra team, you'll work closely with our other engineering and product \nteams ... Ruby, C, C++, Java, Scala; Strong organizational and communication \nskills\u00a0...",
        "title": "Twitch - Senior Software Engineer - Infrastructure"
    },
    {
        "cacheId": "TjPDxRe1ajYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../555fb249-80e0-4c22-9402-88ae3eb3edd2",
        "htmlFormattedUrl": "https://jobs.lever.co/.../555fb249-80e0-4c22-9402-88ae3eb3edd2",
        "htmlSnippet": "Android Framework <b>Engineers</b> ... Android Framework <b>Engineer</b> ... of experience <br>\nin Android Framework development, including experience in Java and C/<b>C++</b>.",
        "htmlTitle": "Faraday Future - Android Framework <b>Engineers</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/555fb249-80e0-4c22-9402-88ae3eb3edd2",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Company: Faraday Future is a California mobility company bringing a tech approach to clean transportation. At FF, we believe that by placing equal emphasis on automotive and technology disciplines, our team of experts is uniquely positioned to take a user-centric, technology-first approach to vehicle design with the ultimate aim of connecting the automotive experience with the rest of your life. Android Framework Engineer Your Role: We're looking for an experienced Android framework Developer to join our team. The IoV (Internet of vehicle) Software Platform Team at Faraday Future is building a completely new generation \u201cinfotainment\u201d products with adhesive user experience. We'd like you to be a part of the revolution, and work together to invent, prototype, iterate, and ship software that matches the quality/experience of the internet giants, and leaves the traditional automotive industry in the rear view mirror. \u25cf Design and develop innovative, custom",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Android Framework Engineers",
                    "og:url": "https://jobs.lever.co/faradayfuture/555fb249-80e0-4c22-9402-88ae3eb3edd2",
                    "twitter:description": "The Company: Faraday Future is a California mobility company bringing a tech approach to clean transportation. At FF, we believe that by placing equal emphasis on automotive and technology disciplines, our team of experts is uniquely positioned to take a user-centric, technology-first approach to vehicle design with the ultimate aim of connecting the automotive experience with the rest of your life. Android Framework Engineer Your Role: We're looking for an experienced Android framework Developer to join our team. The IoV (Internet of vehicle) Software Platform Team at Faraday Future is building a completely new generation \u201cinfotainment\u201d products with adhesive user experience. We'd like you to be a part of the revolution, and work together to invent, prototype, iterate, and ship software that matches the quality/experience of the internet giants, and leaves the traditional automotive industry in the rear view mirror. \u25cf Design and develop innovative, custom",
                    "twitter:title": "Faraday Future - Android Framework Engineers",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Android Framework Engineers ... Android Framework Engineer ... of experience \nin Android Framework development, including experience in Java and C/C++.",
        "title": "Faraday Future - Android Framework Engineers"
    },
    {
        "cacheId": "ovD-A_NvjNEJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../3cbe7706-c687-4981-8ddf-0d588f3c5bd2",
        "htmlFormattedUrl": "https://jobs.lever.co/.../3cbe7706-c687-4981-8ddf-0d588f3c5bd2",
        "htmlSnippet": "Site Reliability <b>Engineer</b> ... Technology - Platform \u2013 Site Reliability <b>Engineering</b> ... <br>\nExperience in one or more of C, <b>C++</b>, Java, Perl, Python, Go, and/or scripting&nbsp;...",
        "htmlTitle": "UpGuard - Site Reliability <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/upguard/3cbe7706-c687-4981-8ddf-0d588f3c5bd2",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f54d44cd-1035-4132-9f35-6c5fe7af9f13-1494695506045.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "112",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS9_Nsr8K2e_GMHstEzFpTRWUOAhik-g7x0V3OjlBNJu2bTkZviRXsMAg",
                    "width": "449"
                }
            ],
            "metatags": [
                {
                    "og:description": "At UpGuard, our Platform team handles scale, deployment, uptime, monitoring and infrastructure for both our cloud and enterprise appliance customers. We build autonomous, self-healing clusters of systems using distributed consensus protocols and containers. Our internal tools are built with open-source projects like CoreOS, Etcd, Docker, Fleet, and Kubernetes. We follow a strong release process and collaborate with the Engineering and Product teams. We've built continuous integration and delivery mechanisms (DevOps) and test the resilience of our systems often with live host reboots in production. We\u2019ve got experience building systems that scale and work across datacenter regions. We write code, so the ideal candidate will have experience in both systems and software development. Our goal is to create an SRE team that incorporate many of the attributes that Google describes in O'Reilly's \"Site Reliability Engineering\" book. We are looking for candidates who are fast learners, great",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f54d44cd-1035-4132-9f35-6c5fe7af9f13-1494695506045.png",
                    "og:image:height": "200",
                    "og:title": "UpGuard - Site Reliability Engineer",
                    "og:url": "https://jobs.lever.co/upguard/3cbe7706-c687-4981-8ddf-0d588f3c5bd2",
                    "twitter:description": "At UpGuard, our Platform team handles scale, deployment, uptime, monitoring and infrastructure for both our cloud and enterprise appliance customers. We build autonomous, self-healing clusters of systems using distributed consensus protocols and containers. Our internal tools are built with open-source projects like CoreOS, Etcd, Docker, Fleet, and Kubernetes. We follow a strong release process and collaborate with the Engineering and Product teams. We've built continuous integration and delivery mechanisms (DevOps) and test the resilience of our systems often with live host reboots in production. We\u2019ve got experience building systems that scale and work across datacenter regions. We write code, so the ideal candidate will have experience in both systems and software development. Our goal is to create an SRE team that incorporate many of the attributes that Google describes in O'Reilly's \"Site Reliability Engineering\" book. We are looking for candidates who are fast learners, great",
                    "twitter:title": "UpGuard - Site Reliability Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Site Reliability Engineer ... Technology - Platform \u2013 Site Reliability Engineering ... \nExperience in one or more of C, C++, Java, Perl, Python, Go, and/or scripting\u00a0...",
        "title": "UpGuard - Site Reliability Engineer"
    },
    {
        "cacheId": "NdTkbaj7sTUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../ca9acaea-b1f8-4a2c-8cb3-60c86899d928",
        "htmlFormattedUrl": "https://jobs.lever.co/.../ca9acaea-b1f8-4a2c-8cb3-60c86899d928",
        "htmlSnippet": "MZ is seeking an Application Security <b>Engineer</b> II that would report to the ... C/<b>C</b><br>\n<b>++</b>, Python, PHP, MySQL Skilled at use of reverse-<b>engineering</b> tools like IDA Pro<br>\n&nbsp;...",
        "htmlTitle": "MZ - Application Security <b>Engineer</b> II",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/ca9acaea-b1f8-4a2c-8cb3-60c86899d928",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ is seeking an Application Security Engineer II that would report to the Manager of Application Security. The ideal candidate will have strong communication skills, in depth knowledge of application security in both web and mobile, and enjoy finding vulnerabilities and \u201cbreaking code.\u201d You will be responsible for performing penetration tests to identify vulnerabilities, working closely with developers, and implementing security solutions that scale.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Application Security Engineer II",
                    "og:url": "https://jobs.lever.co/machinezone/ca9acaea-b1f8-4a2c-8cb3-60c86899d928",
                    "twitter:description": "MZ is seeking an Application Security Engineer II that would report to the Manager of Application Security. The ideal candidate will have strong communication skills, in depth knowledge of application security in both web and mobile, and enjoy finding vulnerabilities and \u201cbreaking code.\u201d You will be responsible for performing penetration tests to identify vulnerabilities, working closely with developers, and implementing security solutions that scale.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Application Security Engineer II",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "MZ is seeking an Application Security Engineer II that would report to the ... C/C\n++, Python, PHP, MySQL Skilled at use of reverse-engineering tools like IDA Pro\n\u00a0...",
        "title": "MZ - Application Security Engineer II"
    },
    {
        "cacheId": "cN4Pqkv58E4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../1d0f233d-30db-4b07-8ece-107172ff6f65",
        "htmlFormattedUrl": "https://jobs.lever.co/.../1d0f233d-30db-4b07-8ece-107172ff6f65",
        "htmlSnippet": "Satori is looking for a Senior Front End <b>Engineer</b> to join our <b>engineering</b> team. ... <br>\nXamarin C#),; Experience with strongly typed languages such as Java, <b>C++</b>, C#&nbsp;...",
        "htmlTitle": "MZ - Senior Front End <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/1d0f233d-30db-4b07-8ece-107172ff6f65",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "Satori is looking for a Senior Front End Engineer to join our engineering team. You will be working with a group of world-class engineers, architects and product managers to build real-time applications, dashboards and tools that will be used both internally and by our customers. You must have a solid understanding of Front End Web technologies, have a history of building successful Web-based solutions and take mock-ups to implementation. This role requires that you are a self-starter with the ability to deliver on time with quality and also handle multiple tasks simultaneously. We're a flat, lean, agile, self-governing team. We value transparency and trust. We continue to create purpose in our work, question the status quo, seek individual mastery and encourage autonomy.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Front End Engineer",
                    "og:url": "https://jobs.lever.co/machinezone/1d0f233d-30db-4b07-8ece-107172ff6f65",
                    "twitter:description": "Satori is looking for a Senior Front End Engineer to join our engineering team. You will be working with a group of world-class engineers, architects and product managers to build real-time applications, dashboards and tools that will be used both internally and by our customers. You must have a solid understanding of Front End Web technologies, have a history of building successful Web-based solutions and take mock-ups to implementation. This role requires that you are a self-starter with the ability to deliver on time with quality and also handle multiple tasks simultaneously. We're a flat, lean, agile, self-governing team. We value transparency and trust. We continue to create purpose in our work, question the status quo, seek individual mastery and encourage autonomy.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Front End Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Satori is looking for a Senior Front End Engineer to join our engineering team. ... \nXamarin C#),; Experience with strongly typed languages such as Java, C++, C#\u00a0...",
        "title": "MZ - Senior Front End Engineer"
    },
    {
        "cacheId": "Y9NXeAikR7gJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/zoox/a4268999-921d-479c-9017-3d856d58f563",
        "htmlFormattedUrl": "https://jobs.lever.co/zoox/a4268999-921d-479c-9017-3d856d58f563",
        "htmlSnippet": "At Zoox, you will be part of a team of world-class <b>engineers</b> with diverse ... degree <br>\nin an <b>engineering</b>, math, or related field; Fluency in C / <b>C++</b>, or Python&nbsp;...",
        "htmlTitle": "Zoox - Software <b>Engineer</b> - Tools",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/zoox/a4268999-921d-479c-9017-3d856d58f563",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "183",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAkruyHxT8E9prOHuSspiQmEZjGkC1SWYHDhWOgBHmm7eEz0oEbgvKng0",
                    "width": "275"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Zoox, you will be part of a team of world-class engineers with diverse backgrounds in areas such as AI, robotics, mechatronics, planning, machine learning, control, localization, computer vision, rendering, simulation, distributed computing, design, and automated testing. Our Tools Engineers act as a multiplier for all other teams' efficiency, build scalable systems that allow us to move quickly today, and stay ahead of the competition in the long run. You'll have the opportunity to work with a wide variety of technologies ranging from a full web stack, to desktop applications, to 3D rendering and more. Our Tools Engineers bring their expertise to each project they tackle, build both on-vehicle and off-vehicle systems as necessary, and always move Zoox forward. Working at a startup gives you the chance to manifest your creativity and highly impact the final product.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Zoox - Software Engineer - Tools",
                    "og:url": "https://jobs.lever.co/zoox/a4268999-921d-479c-9017-3d856d58f563",
                    "twitter:description": "At Zoox, you will be part of a team of world-class engineers with diverse backgrounds in areas such as AI, robotics, mechatronics, planning, machine learning, control, localization, computer vision, rendering, simulation, distributed computing, design, and automated testing. Our Tools Engineers act as a multiplier for all other teams' efficiency, build scalable systems that allow us to move quickly today, and stay ahead of the competition in the long run. You'll have the opportunity to work with a wide variety of technologies ranging from a full web stack, to desktop applications, to 3D rendering and more. Our Tools Engineers bring their expertise to each project they tackle, build both on-vehicle and off-vehicle systems as necessary, and always move Zoox forward. Working at a startup gives you the chance to manifest your creativity and highly impact the final product.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498849198093.png",
                    "twitter:title": "Zoox - Software Engineer - Tools",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "At Zoox, you will be part of a team of world-class engineers with diverse ... degree \nin an engineering, math, or related field; Fluency in C / C++, or Python\u00a0...",
        "title": "Zoox - Software Engineer - Tools"
    },
    {
        "cacheId": "a4AIBjsViLUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../249db327-4dbf-46c6-8650-1d2610c5e4db",
        "htmlFormattedUrl": "https://jobs.lever.co/.../249db327-4dbf-46c6-8650-1d2610c5e4db",
        "htmlSnippet": "Udacity is looking for people to join our <b>Engineering</b> team. ... work experience; <br>\nFamiliarity with programming languages such as C/<b>C++</b>, Python, Java or Perl.",
        "htmlTitle": "Udacity - Senior Software <b>Engineer</b>, AI",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/udacity/249db327-4dbf-46c6-8650-1d2610c5e4db",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1456507702873.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "Udacity's mission is to democratize education. We're an online learning platform offering groundbreaking education in fields such as artificial intelligence, machine learning, robotics, virtual reality, and more. Focused on self-empowerment through learning, Udacity is making innovative technologies such as self-driving cars available to a global community of aspiring technologists, while also enabling learners at all levels to skill up with essentials like programming, web and app development. Udacity is looking for people to join our Engineering team. If you love a challenge, and truly want to make a difference in the world, read on! Udacity is looking for a passionate, talented, and inventive Research Engineers with a strong machine learning background to massively accelerate student learning. Our mission is to provide an engaging and effective education to students on Udacity by applying and advancing the state-of-the-art in Natural Language Understanding (NLU) and Machine Learn",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1456507702873.png",
                    "og:image:height": "200",
                    "og:title": "Udacity - Senior Software Engineer, AI",
                    "og:url": "https://jobs.lever.co/udacity/249db327-4dbf-46c6-8650-1d2610c5e4db",
                    "twitter:description": "Udacity's mission is to democratize education. We're an online learning platform offering groundbreaking education in fields such as artificial intelligence, machine learning, robotics, virtual reality, and more. Focused on self-empowerment through learning, Udacity is making innovative technologies such as self-driving cars available to a global community of aspiring technologists, while also enabling learners at all levels to skill up with essentials like programming, web and app development. Udacity is looking for people to join our Engineering team. If you love a challenge, and truly want to make a difference in the world, read on! Udacity is looking for a passionate, talented, and inventive Research Engineers with a strong machine learning background to massively accelerate student learning. Our mission is to provide an engaging and effective education to students on Udacity by applying and advancing the state-of-the-art in Natural Language Understanding (NLU) and Machine Learn",
                    "twitter:title": "Udacity - Senior Software Engineer, AI",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Udacity is looking for people to join our Engineering team. ... work experience; \nFamiliarity with programming languages such as C/C++, Python, Java or Perl.",
        "title": "Udacity - Senior Software Engineer, AI"
    },
    {
        "cacheId": "jBb9HfUtyJMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/cask/03ad27af-19bb-46ba-8f52-e248a58ed15a",
        "htmlFormattedUrl": "https://jobs.lever.co/cask/03ad27af-19bb-46ba-8f52-e248a58ed15a",
        "htmlSnippet": "You&#39;ll apply your knowledge of software design principles, systems programming, <br>\nalgorithms, data structures, Java and C/<b>C++</b>. You&#39;ll also contribute to and work&nbsp;...",
        "htmlTitle": "Cask - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cask/03ad27af-19bb-46ba-8f52-e248a58ed15a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/Cask.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "115",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu02WIePqHJi0W-RXc2QitmWZOhNZBo5wBfhHGT3fOw5vYXjhzJhwODQ",
                    "width": "439"
                }
            ],
            "metatags": [
                {
                    "og:description": "Developing the Cask Data Application Platform, CDAP, presents complex distributed computing challenges. You\u2019ll have the opportunity to implement complex algorithms on the Hadoop/HBase/YARN/Twill stack. You\u2019ll apply your knowledge of software design principles, systems programming, algorithms, data structures, Java and C/C++. You\u2019ll also contribute to and work with the Open Source development community. The ideal candidate will be able to scope and frame undefined problems using intuition, common sense, relevant data, and strong academic knowledge of computer science (algorithms, data structures, etc.). You will be asked to lead the design and implementation of key features and components of the Cask platform.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/Cask.png",
                    "og:image:height": "200",
                    "og:title": "Cask - Software Engineer",
                    "og:url": "https://jobs.lever.co/cask/03ad27af-19bb-46ba-8f52-e248a58ed15a",
                    "twitter:description": "Developing the Cask Data Application Platform, CDAP, presents complex distributed computing challenges. You\u2019ll have the opportunity to implement complex algorithms on the Hadoop/HBase/YARN/Twill stack. You\u2019ll apply your knowledge of software design principles, systems programming, algorithms, data structures, Java and C/C++. You\u2019ll also contribute to and work with the Open Source development community. The ideal candidate will be able to scope and frame undefined problems using intuition, common sense, relevant data, and strong academic knowledge of computer science (algorithms, data structures, etc.). You will be asked to lead the design and implementation of key features and components of the Cask platform.",
                    "twitter:title": "Cask - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You'll apply your knowledge of software design principles, systems programming, \nalgorithms, data structures, Java and C/C++. You'll also contribute to and work\u00a0...",
        "title": "Cask - Software Engineer"
    },
    {
        "cacheId": "ZRJ5FvGpMVEJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
        "htmlSnippet": "On this team, you&#39;ll work closely with our other <b>engineering</b> and product ... Ruby, <br>\nC, <b>C++</b>, Java, Scala; 4+ years of experience building consumer-facing web&nbsp;...",
        "htmlTitle": "Twitch - Senior Backend <b>Engineer</b> - Live Video Product",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch has over 100 million users, and the Live Video Product team is responsible for building products that improve the experience of watching live video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On this team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in building applications for the Web, comfort working throughout the stack, and an understanding of product concerns. Currently, we\u2019re focused on driving real-time interaction between broadcasters and viewers and building a live video watching experience that is uniquely Twitch.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Backend Engineer - Live Video Product",
                    "og:url": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
                    "twitter:description": "Twitch has over 100 million users, and the Live Video Product team is responsible for building products that improve the experience of watching live video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On this team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in building applications for the Web, comfort working throughout the stack, and an understanding of product concerns. Currently, we\u2019re focused on driving real-time interaction between broadcasters and viewers and building a live video watching experience that is uniquely Twitch.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Backend Engineer - Live Video Product",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "On this team, you'll work closely with our other engineering and product ... Ruby, \nC, C++, Java, Scala; 4+ years of experience building consumer-facing web\u00a0...",
        "title": "Twitch - Senior Backend Engineer - Live Video Product"
    },
    {
        "cacheId": "jg7-GsuYY10J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../aad08d39-0c00-4c3a-b0eb-b41c38b225a3",
        "htmlFormattedUrl": "https://jobs.lever.co/.../aad08d39-0c00-4c3a-b0eb-b41c38b225a3",
        "htmlSnippet": "BS in Electrical or Computer <b>Engineering</b>; Highly proficient in programming <br>\nFPGAs; Expert in <b>C++</b>; 4 years of industry experience; Image processing <br>\nexperience.",
        "htmlTitle": "Luminar - Electrical <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/luminartech/aad08d39-0c00-4c3a-b0eb-b41c38b225a3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "89",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSFvf6FeCSFHt31BBS3B_ZWXQoYUt_5mNAAv__XU_Fd4rLXnz05WEurVA",
                    "width": "568"
                }
            ],
            "metatags": [
                {
                    "og:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeing applicants for an Electrical Engineer in Orlando, FL.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Luminar - Electrical Engineer",
                    "og:url": "https://jobs.lever.co/luminartech/aad08d39-0c00-4c3a-b0eb-b41c38b225a3",
                    "twitter:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeing applicants for an Electrical Engineer in Orlando, FL.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499973943868.png",
                    "twitter:title": "Luminar - Electrical Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "BS in Electrical or Computer Engineering; Highly proficient in programming \nFPGAs; Expert in C++; 4 years of industry experience; Image processing \nexperience.",
        "title": "Luminar - Electrical Engineer"
    },
    {
        "cacheId": "re4ece5a_mkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../72e5bdd8-0373-4714-a90e-7aebbb61b181",
        "htmlFormattedUrl": "https://jobs.lever.co/.../72e5bdd8-0373-4714-a90e-7aebbb61b181",
        "htmlSnippet": "We care a lot about finding the best <b>engineers</b>, writing correct software, using the <br>\nright ... Experience with a compiled language, such as C, <b>C++</b>, or Java; Good&nbsp;...",
        "htmlTitle": "Everlaw - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "129",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE",
                    "width": "389"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join a growing, venture-funded startup! You'll be developing core components of our litigation infrastructure, an online platform for lawyers to review, analyze, and collaborate on millions of documents. Tackling litigation with technology is a surprisingly deep challenge, and it requires in-depth computer science, including machine learning, data visualization, search, distributed systems, databases, real-time collaboration, nifty user interfaces, and more. We're looking for full-stack generalists. We value great CS fundamentals, native ability, and humility, over experience with any particular platform, technology, or specialization. If you happen to have a specialty, we'll put that to use -- but we won't restrict you to that area. We care a lot about finding the best engineers, writing correct software, using the right tools for the job, and avoiding dogma. As a result we've been able to build quite a bit of sophisticated technology with a small, talented team. It's the kind",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png",
                    "og:image:height": "200",
                    "og:title": "Everlaw - Software Engineer",
                    "og:url": "https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181",
                    "twitter:description": "Join a growing, venture-funded startup! You'll be developing core components of our litigation infrastructure, an online platform for lawyers to review, analyze, and collaborate on millions of documents. Tackling litigation with technology is a surprisingly deep challenge, and it requires in-depth computer science, including machine learning, data visualization, search, distributed systems, databases, real-time collaboration, nifty user interfaces, and more. We're looking for full-stack generalists. We value great CS fundamentals, native ability, and humility, over experience with any particular platform, technology, or specialization. If you happen to have a specialty, we'll put that to use -- but we won't restrict you to that area. We care a lot about finding the best engineers, writing correct software, using the right tools for the job, and avoiding dogma. As a result we've been able to build quite a bit of sophisticated technology with a small, talented team. It's the kind",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png",
                    "twitter:title": "Everlaw - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We care a lot about finding the best engineers, writing correct software, using the \nright ... Experience with a compiled language, such as C, C++, or Java; Good\u00a0...",
        "title": "Everlaw - Software Engineer"
    },
    {
        "cacheId": "Apn_VR8pVwoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/altspace/2dfe09ff-ea9c-4d4d-a3a1-b56df5f088e8",
        "htmlFormattedUrl": "https://jobs.lever.co/altspace/2dfe09ff-ea9c-4d4d-a3a1-b56df5f088e8",
        "htmlSnippet": "We are looking for an Real-time Networking <b>Engineer</b> who knows their way <br>\naround ... Multiplayer networking protocols &amp; algorithms; C/<b>C++</b>; TCP(UDP)/IP&nbsp;...",
        "htmlTitle": "AltspaceVR - Real-time Networking <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/altspace/2dfe09ff-ea9c-4d4d-a3a1-b56df5f088e8",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e4d03c9c-8816-4448-9668-ac7eddd8f362-1500333842699.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTegq_oTzfUPUnfPuXGOMle3kuUa7QTNrgp02-ZAIkZ3FZwRVjyeSQ0Nu1h",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "Want the challenge of building large scale persistent environments used for live collaboration in VR and powered by web technologies? We are looking for an Real-time Networking Engineer who knows their way around building networked simulations. You\u2019ll be responsible for developing our core technology to enable social interaction, synchronized web browsing, movie watching, and gaming all from within VR. AltspaceVR is a virtual reality software company building a new communication platform. It is now used by people in over 150 countries to share a variety of experiences and interact in the most natural and fulfilling way possible online. We are a relatively small (and thoughtfully growing) team of 37. To that end, our Engineering team looks for experienced, smart, and well-grounded individuals who: can thrive in an environment that is fast-paced but not brutally so; are bleeding-edge but well-versed in solid startup engineering principles (clean code and an inclination toward shipping",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e4d03c9c-8816-4448-9668-ac7eddd8f362-1500333842699.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "AltspaceVR - Real-time Networking Engineer",
                    "og:url": "https://jobs.lever.co/altspace/2dfe09ff-ea9c-4d4d-a3a1-b56df5f088e8",
                    "twitter:description": "Want the challenge of building large scale persistent environments used for live collaboration in VR and powered by web technologies? We are looking for an Real-time Networking Engineer who knows their way around building networked simulations. You\u2019ll be responsible for developing our core technology to enable social interaction, synchronized web browsing, movie watching, and gaming all from within VR. AltspaceVR is a virtual reality software company building a new communication platform. It is now used by people in over 150 countries to share a variety of experiences and interact in the most natural and fulfilling way possible online. We are a relatively small (and thoughtfully growing) team of 37. To that end, our Engineering team looks for experienced, smart, and well-grounded individuals who: can thrive in an environment that is fast-paced but not brutally so; are bleeding-edge but well-versed in solid startup engineering principles (clean code and an inclination toward shipping",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e4d03c9c-8816-4448-9668-ac7eddd8f362-1500333819485.png",
                    "twitter:title": "AltspaceVR - Real-time Networking Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are looking for an Real-time Networking Engineer who knows their way \naround ... Multiplayer networking protocols & algorithms; C/C++; TCP(UDP)/IP\u00a0...",
        "title": "AltspaceVR - Real-time Networking Engineer"
    },
    {
        "cacheId": "AuaDPtOuSzcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../4863a428-9036-4cba-a749-4187dd4048d1",
        "htmlFormattedUrl": "https://jobs.lever.co/.../4863a428-9036-4cba-a749-4187dd4048d1",
        "htmlSnippet": "We&#39;re looking for a Data <b>Engineer</b> who is driven to solve hard problems\u2014 the <br>\nharder, the better. We&#39;re ... Experience with Python, Javascript, SQL, and <b>C++</b>.",
        "htmlTitle": "Blend - Data <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/blendlabs/4863a428-9036-4cba-a749-4187dd4048d1",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "163",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Blend, we\u2019re dedicated to improving lending. We\u2019re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime\u2014their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We're looking for a Data Engineer who is driven to solve hard problems\u2014 the harder, the better. We\u2019re motivated by the fact that our product won\u2019t just affect the lives of a few people in the Bay Area\u2014 it affects people all over the U.S., not to mention a foundational part of the U.S. economy. As an early Data Engineer, you can define how we instrument our data infrastructure to influence the entire industry. Your contributions to Blend\u2019s data architecture and infrastructure will shape the company\u2019s ability to",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Blend - Data Engineer",
                    "og:url": "https://jobs.lever.co/blendlabs/4863a428-9036-4cba-a749-4187dd4048d1",
                    "twitter:description": "At Blend, we\u2019re dedicated to improving lending. We\u2019re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime\u2014their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We're looking for a Data Engineer who is driven to solve hard problems\u2014 the harder, the better. We\u2019re motivated by the fact that our product won\u2019t just affect the lives of a few people in the Bay Area\u2014 it affects people all over the U.S., not to mention a foundational part of the U.S. economy. As an early Data Engineer, you can define how we instrument our data infrastructure to influence the entire industry. Your contributions to Blend\u2019s data architecture and infrastructure will shape the company\u2019s ability to",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png",
                    "twitter:title": "Blend - Data Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for a Data Engineer who is driven to solve hard problems\u2014 the \nharder, the better. We're ... Experience with Python, Javascript, SQL, and C++.",
        "title": "Blend - Data Engineer"
    },
    {
        "cacheId": "AeeYcGEdYBQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../78f4206b-7813-4d92-b220-c87b3b75fbc0",
        "htmlFormattedUrl": "https://jobs.lever.co/.../78f4206b-7813-4d92-b220-c87b3b75fbc0",
        "htmlSnippet": "Hear from the Mendoza <b>Engineering</b> team and meet Ariel Chiat, <b>Engineering</b> ... in <br>\na mainstream programming language: Python, PHP, Ruby, C#, <b>C++</b>, Java, etc.",
        "htmlTitle": "Eventbrite - Senior Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/78f4206b-7813-4d92-b220-c87b3b75fbc0",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTTvFuICOfdvSfhbE4ObHsOali-3FCbYdpz22h0yVaHrVVzEgqRWhDCgXU",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "THE TEAM We opened our Mendoza office two years ago, merging with Eventioz, a local company, and we are looking to grow our amazing southeast engineering team. Hear from the Mendoza Engineering team and meet Ariel Chiat, Engineering Manager in Mendoza. Our primary stack is Python, Django, and Celery, all running on AWS with a MySQL backend. Some of the other tools that we use are Redis, RabbitMQ, Cassandra, Hbase, Hive, Backbone, Sass, Git, and an endless supply of coffee. Haven\u2019t worked with these technologies before? This is an amazing chance to jump in and learn. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail together, and actively develop their careers. Weekly demos, tech talks, and quarterly hackathons are at the core of how we\u2019ve built our team and product.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Senior Software Engineer",
                    "og:url": "https://jobs.lever.co/eventbrite/78f4206b-7813-4d92-b220-c87b3b75fbc0",
                    "twitter:description": "THE TEAM We opened our Mendoza office two years ago, merging with Eventioz, a local company, and we are looking to grow our amazing southeast engineering team. Hear from the Mendoza Engineering team and meet Ariel Chiat, Engineering Manager in Mendoza. Our primary stack is Python, Django, and Celery, all running on AWS with a MySQL backend. Some of the other tools that we use are Redis, RabbitMQ, Cassandra, Hbase, Hive, Backbone, Sass, Git, and an endless supply of coffee. Haven\u2019t worked with these technologies before? This is an amazing chance to jump in and learn. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail together, and actively develop their careers. Weekly demos, tech talks, and quarterly hackathons are at the core of how we\u2019ve built our team and product.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Senior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Hear from the Mendoza Engineering team and meet Ariel Chiat, Engineering ... in \na mainstream programming language: Python, PHP, Ruby, C#, C++, Java, etc.",
        "title": "Eventbrite - Senior Software Engineer"
    },
    {
        "cacheId": "5BB1a70iTJ8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../469cc833-1bb2-48e7-8152-c7f90fbf7b7d",
        "htmlFormattedUrl": "https://jobs.lever.co/.../469cc833-1bb2-48e7-8152-c7f90fbf7b7d",
        "htmlSnippet": "The L1/L2 BBU Junior Software <b>Engineer</b> will be responsible for the design of ... <br>\nan <b>engineering</b> capacity developing Linux software in C or <b>C++</b>, with a focus on&nbsp;...",
        "htmlTitle": "JMA Wireless - L1/L2 LTE BBU Junior Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/jmawireless/469cc833-1bb2-48e7-8152-c7f90fbf7b7d",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/45a32d89-7197-4692-a811-2b71d80f8d5f-1498594225058.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "163",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7AW5pVzdmLe4I6B3-qj54I60oYCvOcbHA_zphyjdaivU_kBfdPOdfU4Y",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "JMA Wireless is the leading global innovator in mobile wireless connectivity solutions that assure infrastructure reliability, streamline service operations, and maximize wireless performance. Employing powerful, patented innovations their solutions portfolio is proven to lower the cost of operations while ensuring lifetime quality levels in equipment and unrivaled performance for coverage and high-speed mobile data. JMA Wireless solutions cover macro infrastructure, outdoor and indoor distributed antenna systems and small cell solutions. JMA Wireless corporate headquarters are located in Liverpool, NY, with manufacturing, R&D, and sales operations in over 20 locations worldwide. The L1/L2 BBU Junior Software Engineer will be responsible for the design of Layer 1 and Layer 2 features of the LTE eNodeB baseband unit (BBU). The person in this role will be part of an internal development team, with members located in Italy and the US, focused on new software engineering for the LTE eNode",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/45a32d89-7197-4692-a811-2b71d80f8d5f-1498594225058.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "JMA Wireless - L1/L2 LTE BBU Junior Software Engineer",
                    "og:url": "https://jobs.lever.co/jmawireless/469cc833-1bb2-48e7-8152-c7f90fbf7b7d",
                    "twitter:description": "JMA Wireless is the leading global innovator in mobile wireless connectivity solutions that assure infrastructure reliability, streamline service operations, and maximize wireless performance. Employing powerful, patented innovations their solutions portfolio is proven to lower the cost of operations while ensuring lifetime quality levels in equipment and unrivaled performance for coverage and high-speed mobile data. JMA Wireless solutions cover macro infrastructure, outdoor and indoor distributed antenna systems and small cell solutions. JMA Wireless corporate headquarters are located in Liverpool, NY, with manufacturing, R&D, and sales operations in over 20 locations worldwide. The L1/L2 BBU Junior Software Engineer will be responsible for the design of Layer 1 and Layer 2 features of the LTE eNodeB baseband unit (BBU). The person in this role will be part of an internal development team, with members located in Italy and the US, focused on new software engineering for the LTE eNode",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/45a32d89-7197-4692-a811-2b71d80f8d5f-1498594125112.png",
                    "twitter:title": "JMA Wireless - L1/L2 LTE BBU Junior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The L1/L2 BBU Junior Software Engineer will be responsible for the design of ... \nan engineering capacity developing Linux software in C or C++, with a focus on\u00a0...",
        "title": "JMA Wireless - L1/L2 LTE BBU Junior Software Engineer"
    },
    {
        "cacheId": "Z9iJllvaCKwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
        "htmlSnippet": "We are rapidly expanding the <b>engineering</b> team at Twitch to deal with <br>\nchallenging ... Java, Javascript, C, <b>C++</b>; Excellent verbal and written <br>\ncommunication skills&nbsp;...",
        "htmlTitle": "Twitch - Senior Network Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. By joining the Network Development team, as a Sr. Network Software Engineer, you can help shape the future of network automation at Twitch.The Network Development team is responsible for building the framework and tooling for network: automation, orchestration, visualization, and alerting. This framework enables other teams to: increase efficiency, leverage network telemetry in their algorithms, and allows the Twitch network to dynamically react to c",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Network Software Engineer",
                    "og:url": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
                    "twitter:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. By joining the Network Development team, as a Sr. Network Software Engineer, you can help shape the future of network automation at Twitch.The Network Development team is responsible for building the framework and tooling for network: automation, orchestration, visualization, and alerting. This framework enables other teams to: increase efficiency, leverage network telemetry in their algorithms, and allows the Twitch network to dynamically react to c",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Network Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are rapidly expanding the engineering team at Twitch to deal with \nchallenging ... Java, Javascript, C, C++; Excellent verbal and written \ncommunication skills\u00a0...",
        "title": "Twitch - Senior Network Software Engineer"
    },
    {
        "cacheId": "_TUDufe6PKYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../35a5b9b4-94ea-4501-8006-2c42ed1461ca",
        "htmlFormattedUrl": "https://jobs.lever.co/.../35a5b9b4-94ea-4501-8006-2c42ed1461ca",
        "htmlSnippet": "Forward Networks is looking for an experienced software <b>engineer</b> with ... you <br>\nshould know at least one object-oriented language (Java, Scala, <b>C++</b>, or C#).",
        "htmlTitle": "Forward Networks - Software <b>Engineer</b> (Networking)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/forwardnetworks/35a5b9b4-94ea-4501-8006-2c42ed1461ca",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/Forward-Networks-cropped.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "111",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSboYCZWMa7jwL0ctQejdgflap1RdRFfi-4P3gFOSoEHcsCMKD9YO6qFdc",
                    "width": "453"
                }
            ],
            "metatags": [
                {
                    "og:description": "Forward Networks is looking for an experienced software engineer with networking device expertise to help us build, manage, and test our product. Forward Networks is a fast growing startup working to revolutionize the way network operators and engineers build and maintain large-scale networks. We've created a game-changing networking solution that CIOs and CSOs from Fortune 100 companies have called \"magic\". We're looking for goal-oriented candidates with an entrepreneurial mindset and interest in career advancement to help contribute to our growth.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/Forward-Networks-cropped.png",
                    "og:image:height": "200",
                    "og:title": "Forward Networks - Software Engineer (Networking)",
                    "og:url": "https://jobs.lever.co/forwardnetworks/35a5b9b4-94ea-4501-8006-2c42ed1461ca",
                    "twitter:description": "Forward Networks is looking for an experienced software engineer with networking device expertise to help us build, manage, and test our product. Forward Networks is a fast growing startup working to revolutionize the way network operators and engineers build and maintain large-scale networks. We've created a game-changing networking solution that CIOs and CSOs from Fortune 100 companies have called \"magic\". We're looking for goal-oriented candidates with an entrepreneurial mindset and interest in career advancement to help contribute to our growth.",
                    "twitter:title": "Forward Networks - Software Engineer (Networking)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Forward Networks is looking for an experienced software engineer with ... you \nshould know at least one object-oriented language (Java, Scala, C++, or C#).",
        "title": "Forward Networks - Software Engineer (Networking)"
    },
    {
        "cacheId": "0MeYm259ADgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a8415a97-3c2b-43e5-bed3-f065052512a4",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a8415a97-3c2b-43e5-bed3-f065052512a4",
        "htmlSnippet": "We&#39;re looking for a lead computer vision <b>engineer</b> (visioneer? your call) to <br>\ntranslate ... with robotics, ROS, Gazebo, OpenCV and/or PCL; Fluency in C / <b>C++</b><br>\n&nbsp;...",
        "htmlTitle": "Carbon Robotics - Perception <b>Engineer</b> (Computer Vision)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/carbonrobotics/a8415a97-3c2b-43e5-bed3-f065052512a4",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/56c195c6-97e4-4762-ad10-0a37b6506ffb-1468960957314.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQsPX8hIzfBDOBRbJIlsa1UFUsIOlW5uIA6w1tr9xVIrWBZxnhAPouwSp4_",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Who We Are We build highly intelligent robotic arms that automate tasks no human was born to do. With computer vision and machine intelligence, we make it easy for anyone to program tasks in a matter of hours instead of weeks, while our platform enables developers to build the next generation of robotic applications. We\u2019re scrappy, we\u2019re focused, and we\u2019re out to change the face of robotics. What You\u2019ll Be Doing We're looking for a lead computer vision engineer (visioneer? your call) to translate pixels to millimeters and help our robots understand the world around them. You\u2019ll be building the architecture that lets our robots recognize features and geometry, measure distances, react to obstructions, and work side by side with people in industrial environments. You\u2019ll collaborate frequently with the controls and motion planning teams to integrate visual feedback into our motion routines, and work with our mechatronics team to design a highly accurate camera system.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/56c195c6-97e4-4762-ad10-0a37b6506ffb-1468960957314.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Carbon Robotics - Perception Engineer (Computer Vision)",
                    "og:url": "https://jobs.lever.co/carbonrobotics/a8415a97-3c2b-43e5-bed3-f065052512a4",
                    "twitter:description": "Who We Are We build highly intelligent robotic arms that automate tasks no human was born to do. With computer vision and machine intelligence, we make it easy for anyone to program tasks in a matter of hours instead of weeks, while our platform enables developers to build the next generation of robotic applications. We\u2019re scrappy, we\u2019re focused, and we\u2019re out to change the face of robotics. What You\u2019ll Be Doing We're looking for a lead computer vision engineer (visioneer? your call) to translate pixels to millimeters and help our robots understand the world around them. You\u2019ll be building the architecture that lets our robots recognize features and geometry, measure distances, react to obstructions, and work side by side with people in industrial environments. You\u2019ll collaborate frequently with the controls and motion planning teams to integrate visual feedback into our motion routines, and work with our mechatronics team to design a highly accurate camera system.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/56c195c6-97e4-4762-ad10-0a37b6506ffb-1468960948388.png",
                    "twitter:title": "Carbon Robotics - Perception Engineer (Computer Vision)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for a lead computer vision engineer (visioneer? your call) to \ntranslate ... with robotics, ROS, Gazebo, OpenCV and/or PCL; Fluency in C / C++\n\u00a0...",
        "title": "Carbon Robotics - Perception Engineer (Computer Vision)"
    },
    {
        "cacheId": "D_pSJ4qNrTYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/lastline/c1ab9eb8-df8a-4d0f-9b4c-2b0aa7a6729a",
        "htmlFormattedUrl": "https://jobs.lever.co/lastline/c1ab9eb8-df8a-4d0f-9b4c-2b0aa7a6729a",
        "htmlSnippet": "Software <b>Engineer</b> - C++ / Sandbox Development Team ... Strong proficiency in <b>C</b><br>\n<b>++</b>, with fair knowledge of the language specification; Thorough knowledge of&nbsp;...",
        "htmlTitle": "Lastline - Software <b>Engineer</b> - C++ / Sandbox Development Team",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/lastline/c1ab9eb8-df8a-4d0f-9b4c-2b0aa7a6729a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/fe3d35b8-d0e1-422d-a2b1-5d4680ce9bd5-1470360607117.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "78",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRmDQAxMV0jsg1JZYMzEB9DQm_xkq4pSIzEcIGOnTu5-4cCSZ7gtOJ-Jg",
                    "width": "399"
                }
            ],
            "metatags": [
                {
                    "og:description": "JOB DESCRIPTION: Is C++ your bread and butter? Passionate about Cyber Security? Ready to take your career to a whole new level? Lastline Inc., an established leader in advanced malware and breach detection, is conducting a round of hiring due to growth and recent funding. Join our team of world renowned cyber security experts and help design, build, and maintain the next generation Lastline Advanced Malware Analysis system. It incorporates the advantages of both Full System Emulator and Hypervisor technologies and supports multiple operation systems. Our goal is simple: to be the best in advanced malware detection.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/fe3d35b8-d0e1-422d-a2b1-5d4680ce9bd5-1470360607117.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Lastline - Software Engineer - C++ / Sandbox Development Team",
                    "og:url": "https://jobs.lever.co/lastline/c1ab9eb8-df8a-4d0f-9b4c-2b0aa7a6729a",
                    "twitter:description": "JOB DESCRIPTION: Is C++ your bread and butter? Passionate about Cyber Security? Ready to take your career to a whole new level? Lastline Inc., an established leader in advanced malware and breach detection, is conducting a round of hiring due to growth and recent funding. Join our team of world renowned cyber security experts and help design, build, and maintain the next generation Lastline Advanced Malware Analysis system. It incorporates the advantages of both Full System Emulator and Hypervisor technologies and supports multiple operation systems. Our goal is simple: to be the best in advanced malware detection.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/fe3d35b8-d0e1-422d-a2b1-5d4680ce9bd5-1470360602174.png",
                    "twitter:title": "Lastline - Software Engineer - C++ / Sandbox Development Team",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer - C++ / Sandbox Development Team ... Strong proficiency in C\n++, with fair knowledge of the language specification; Thorough knowledge of\u00a0...",
        "title": "Lastline - Software Engineer - C++ / Sandbox Development Team"
    },
    {
        "cacheId": "fTOXlzFUSDIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/zoox/d960f33a-fb68-4f15-8034-6c09efdb0668",
        "htmlFormattedUrl": "https://jobs.lever.co/zoox/d960f33a-fb68-4f15-8034-6c09efdb0668",
        "htmlSnippet": "Bachelors degree in an <b>engineering</b>, math, or related field; Fluency in C / <b>C++</b>, or <br>\nPython; Extensive experience with programming and algorithm design; Strong&nbsp;...",
        "htmlTitle": "Zoox - Software <b>Engineer</b> - Infrastructure",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/zoox/d960f33a-fb68-4f15-8034-6c09efdb0668",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "183",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAkruyHxT8E9prOHuSspiQmEZjGkC1SWYHDhWOgBHmm7eEz0oEbgvKng0",
                    "width": "275"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Zoox. you will be responsible for solving challenging distributed systems problems and scaling state of the art algorithms. You will be working with cutting edge hardware and pushing systems to their limits. Zoox is a robotics company, and our ethos of automation extends throughout the infrastructure components we build. Working at a startup gives you the chance to manifest your creativity and highly impact the final product.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498846147991.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Zoox - Software Engineer - Infrastructure",
                    "og:url": "https://jobs.lever.co/zoox/d960f33a-fb68-4f15-8034-6c09efdb0668",
                    "twitter:description": "At Zoox. you will be responsible for solving challenging distributed systems problems and scaling state of the art algorithms. You will be working with cutting edge hardware and pushing systems to their limits. Zoox is a robotics company, and our ethos of automation extends throughout the infrastructure components we build. Working at a startup gives you the chance to manifest your creativity and highly impact the final product.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5f6f9bef-3957-46f7-b87d-c490e24027b1-1498849198093.png",
                    "twitter:title": "Zoox - Software Engineer - Infrastructure",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Bachelors degree in an engineering, math, or related field; Fluency in C / C++, or \nPython; Extensive experience with programming and algorithm design; Strong\u00a0...",
        "title": "Zoox - Software Engineer - Infrastructure"
    },
    {
        "cacheId": "vZPaX1dzKIYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../eb5c45a9-c385-427b-b35a-242a72dd1268",
        "htmlFormattedUrl": "https://jobs.lever.co/.../eb5c45a9-c385-427b-b35a-242a72dd1268",
        "htmlSnippet": "You can learn more about the team from some of our <b>engineers</b>. ... applications in <br>\na mainstream programming language: Python, PHP, Ruby, C#, <b>C++</b>, Java, etc.",
        "htmlTitle": "Eventbrite - Software <b>Engineer</b> - Back End",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/eb5c45a9-c385-427b-b35a-242a72dd1268",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTTvFuICOfdvSfhbE4ObHsOali-3FCbYdpz22h0yVaHrVVzEgqRWhDCgXU",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "THE CHALLENGE Last year at Eventbrite organizers created 3 million events and we processed 150 million tickets. Behind all of those tickets and events is a number of teams working together to keep our product scalable and available as we grow. The Segment Services team is responsible for a number of the core services that help make Eventbrite successful, and we want you to be a part of that success. THE TEAM Our team is responsible for the APIs and services that our organizers depend upon. We have a few core services that are our primary responsibility, but we also work closely with other teams to help them meet their needs and goals. Getting to work this team means getting to touch a wide array of the pieces that make up Eventbrite. You can learn more about the team from some of our engineers. THE ROLE In this role you\u2019ll work closely with a small team of bright, dedicated engineers improving some of our most core services, and providing valuable feedback to the rest of the compa",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Software Engineer - Back End",
                    "og:url": "https://jobs.lever.co/eventbrite/eb5c45a9-c385-427b-b35a-242a72dd1268",
                    "twitter:description": "THE CHALLENGE Last year at Eventbrite organizers created 3 million events and we processed 150 million tickets. Behind all of those tickets and events is a number of teams working together to keep our product scalable and available as we grow. The Segment Services team is responsible for a number of the core services that help make Eventbrite successful, and we want you to be a part of that success. THE TEAM Our team is responsible for the APIs and services that our organizers depend upon. We have a few core services that are our primary responsibility, but we also work closely with other teams to help them meet their needs and goals. Getting to work this team means getting to touch a wide array of the pieces that make up Eventbrite. You can learn more about the team from some of our engineers. THE ROLE In this role you\u2019ll work closely with a small team of bright, dedicated engineers improving some of our most core services, and providing valuable feedback to the rest of the compa",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Software Engineer - Back End",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You can learn more about the team from some of our engineers. ... applications in \na mainstream programming language: Python, PHP, Ruby, C#, C++, Java, etc.",
        "title": "Eventbrite - Software Engineer - Back End"
    },
    {
        "cacheId": "FWP11B-32uQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
        "htmlSnippet": "We&#39;re looking for <b>engineers</b> that love solving hard technical problems related to ... <br>\nbut much of our work will be in <b>C++</b>, so you&#39;ll have to be willing to roll up your&nbsp;...",
        "htmlTitle": "Twitch - Senior Software <b>Engineer</b> - Commerce",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Commerce",
                    "og:url": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
                    "twitter:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Commerce",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for engineers that love solving hard technical problems related to ... \nbut much of our work will be in C++, so you'll have to be willing to roll up your\u00a0...",
        "title": "Twitch - Senior Software Engineer - Commerce"
    },
    {
        "cacheId": "_eEO-lltRMkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/hike/9aaa7f99-a1f3-4155-af84-835fc009ae0e",
        "htmlFormattedUrl": "https://jobs.lever.co/hike/9aaa7f99-a1f3-4155-af84-835fc009ae0e",
        "htmlSnippet": "As a Lead <b>Engineering</b> Manager you manage your project goals, contribute to ... <br>\nexperience; Programming experience in either Java, Objective-C or <b>C++</b>.",
        "htmlTitle": "hike - Lead <b>Engineering</b> Manager",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/hike/9aaa7f99-a1f3-4155-af84-835fc009ae0e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f6d4e595-0ca3-4bd9-afd7-ec9512b619c5-1460349403303.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "105",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTdqTu4o196XHLwuur6glsmW3OBeVl8jib0iRqwD2rRQH9Yw7agmtOPJg",
                    "width": "479"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Hike, the job of a Software Engineer (SDE) goes beyond just development. Engineering Managers not only provide core engineering leadership to major projects, but also manage a team of engineers. You not only optimise your own code but make sure engineers are able to optimise theirs. As a Lead Engineering Manager you manage your project goals, contribute to product strategy and help develop the organisation in a deeper sense. Engineering teams work all across the company, in multiple areas areas such as information retrieval, large-scale system design, networking, security, data compression, user interface design; the list goes on and is growing every day. Operating with scale and speed, our software engineers are just getting started -- and as a manager, you guide the way. You will lead the Messaging Stack Engineering team at Hike As the Lead Engineering Manager, you work on the full stack and own several major feature tracks. You will also be responsible for working with multiple",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f6d4e595-0ca3-4bd9-afd7-ec9512b619c5-1460349403303.png",
                    "og:image:height": "200",
                    "og:title": "hike - Lead Engineering Manager",
                    "og:url": "https://jobs.lever.co/hike/9aaa7f99-a1f3-4155-af84-835fc009ae0e",
                    "twitter:description": "At Hike, the job of a Software Engineer (SDE) goes beyond just development. Engineering Managers not only provide core engineering leadership to major projects, but also manage a team of engineers. You not only optimise your own code but make sure engineers are able to optimise theirs. As a Lead Engineering Manager you manage your project goals, contribute to product strategy and help develop the organisation in a deeper sense. Engineering teams work all across the company, in multiple areas areas such as information retrieval, large-scale system design, networking, security, data compression, user interface design; the list goes on and is growing every day. Operating with scale and speed, our software engineers are just getting started -- and as a manager, you guide the way. You will lead the Messaging Stack Engineering team at Hike As the Lead Engineering Manager, you work on the full stack and own several major feature tracks. You will also be responsible for working with multiple",
                    "twitter:title": "hike - Lead Engineering Manager",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Lead Engineering Manager you manage your project goals, contribute to ... \nexperience; Programming experience in either Java, Objective-C or C++.",
        "title": "hike - Lead Engineering Manager"
    },
    {
        "cacheId": "MBseu7BcYlcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../028dab2f-4eab-49f4-a893-0919ecec43d5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../028dab2f-4eab-49f4-a893-0919ecec43d5",
        "htmlSnippet": "As an infrastructure <b>engineer</b> you will be working on Apache Kafka that powers ... <br>\nor C/ <b>C++</b>; Bachelor&#39;s degree in Computer Science or similar field or equivalent&nbsp;...",
        "htmlTitle": "Confluent - Infrastructure <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/confluent/028dab2f-4eab-49f4-a893-0919ecec43d5",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/confluent_logo.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "70",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJwgg_YCM-2p-b-FGA3H3JKOD9u-SkbPFgfxpokm2MtFhU7xeyIm7dsOc",
                    "width": "328"
                }
            ],
            "metatags": [
                {
                    "og:description": "As an infrastructure engineer you will be working on Apache Kafka that powers hundreds of billions of events a day at top companies like Netflix, LinkedIn, and Uber. If you love building distributed systems and are passionate about open source, then you will fit right in.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/confluent_logo.png",
                    "og:image:height": "200",
                    "og:title": "Confluent - Infrastructure Engineer",
                    "og:url": "https://jobs.lever.co/confluent/028dab2f-4eab-49f4-a893-0919ecec43d5",
                    "twitter:description": "As an infrastructure engineer you will be working on Apache Kafka that powers hundreds of billions of events a day at top companies like Netflix, LinkedIn, and Uber. If you love building distributed systems and are passionate about open source, then you will fit right in.",
                    "twitter:title": "Confluent - Infrastructure Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As an infrastructure engineer you will be working on Apache Kafka that powers ... \nor C/ C++; Bachelor's degree in Computer Science or similar field or equivalent\u00a0...",
        "title": "Confluent - Infrastructure Engineer"
    },
    {
        "cacheId": "qD23C6_ULZUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../d90c05af-6d54-4fe5-954d-26a73c1645f4",
        "htmlFormattedUrl": "https://jobs.lever.co/.../d90c05af-6d54-4fe5-954d-26a73c1645f4",
        "htmlSnippet": "As a Senior SQA <b>Engineer</b> you have an amazing opportunity to shape the ... <br>\nKnowledge of programming languages (e.g., JAVA, C, <b>C++</b>, JavaScript, Ruby, etc<br>\n.)&nbsp;...",
        "htmlTitle": "KeepTruckin - Senior SQA <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/keeptruckin/d90c05af-6d54-4fe5-954d-26a73c1645f4",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/929b350a-5ba5-4026-bb4f-0187a71d1371-1487288167719.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcReux21EcElRNdqzUTZpg2TNQX4I1XtIkkQ0_FVw7v65Hky8sYowyjY6tc",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "KeepTruckin is on a mission to improve the efficiency of America\u2019s trucking industry by connecting the millions of drivers and vehicles that haul freight on our roads. We are backed by Google Ventures and Index Ventures. In 2015, the U.S. Department of Transportation announced regulation that will require 4.5 million interstate truck drivers to use an Electronic Logging Device (ELD) to record their hours of service with the goal of improving road safety and reducing the paperwork burden on the industry. With the leading ELD in the market, KeepTruckin is poised to build the largest network of connected commercial vehicles in the world. The massive data generated from this network presents an opportunity to fundamentally change the way the trucking market operates. As a Senior SQA Engineer you have an amazing opportunity to shape the way we develop and execute our KeepTruckin QA strategy. We are looking for candidates with strong Software Quality Assurance backgrounds and who are natu",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/929b350a-5ba5-4026-bb4f-0187a71d1371-1487288167719.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "KeepTruckin - Senior SQA Engineer",
                    "og:url": "https://jobs.lever.co/keeptruckin/d90c05af-6d54-4fe5-954d-26a73c1645f4",
                    "twitter:description": "KeepTruckin is on a mission to improve the efficiency of America\u2019s trucking industry by connecting the millions of drivers and vehicles that haul freight on our roads. We are backed by Google Ventures and Index Ventures. In 2015, the U.S. Department of Transportation announced regulation that will require 4.5 million interstate truck drivers to use an Electronic Logging Device (ELD) to record their hours of service with the goal of improving road safety and reducing the paperwork burden on the industry. With the leading ELD in the market, KeepTruckin is poised to build the largest network of connected commercial vehicles in the world. The massive data generated from this network presents an opportunity to fundamentally change the way the trucking market operates. As a Senior SQA Engineer you have an amazing opportunity to shape the way we develop and execute our KeepTruckin QA strategy. We are looking for candidates with strong Software Quality Assurance backgrounds and who are natu",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/929b350a-5ba5-4026-bb4f-0187a71d1371-1487288162889.png",
                    "twitter:title": "KeepTruckin - Senior SQA Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Senior SQA Engineer you have an amazing opportunity to shape the ... \nKnowledge of programming languages (e.g., JAVA, C, C++, JavaScript, Ruby, etc\n.)\u00a0...",
        "title": "KeepTruckin - Senior SQA Engineer"
    },
    {
        "cacheId": "BL-RJqFtxgMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../b02d4f67-53e2-43f0-bb80-ae2d2048ab35",
        "htmlFormattedUrl": "https://jobs.lever.co/.../b02d4f67-53e2-43f0-bb80-ae2d2048ab35",
        "htmlSnippet": "We need a diverse, core group of <b>engineers</b> to design, fabricate, and test ... <br>\nProgramming experience on Linux in Python, C, <b>C++</b>, Verilog, or VHDL. <br>\nFamiliarity&nbsp;...",
        "htmlTitle": "Neuralink - Software <b>Engineer</b>, Embedded Systems &amp; Firmware",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/neuralink/b02d4f67-53e2-43f0-bb80-ae2d2048ab35",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/0cead90f-848e-4ca8-951c-3c83185ca755-1490642922085.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUmSdd5UkOGWkQm-Q3KXeLk7IS51MVgQfQSvsFkdZRXVSsFb4nOS2NNpo",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "Neuralink is developing ultra high bandwidth brain-machine interfaces to connect humans and computers. We\u2019re building a team of multidisciplinary experts and doers who are dedicated to changing the world. We need a diverse, core group of engineers to design, fabricate, and test next-generation medical robotics. We want embedded engineers with specialities, hybrid mechanical-software-electricals engineers, generalists and people we haven\u2019t thought of yet. The ideal candidates are people who get excited about building things, are highly analytical, and enjoy tackling new problems regularly. Our robotics integrate actuated devices with microelectromechanical systems as well as novel surgical procedures. These applications place strong emphasis on high-precision, high-repeatability mechanical motion, as well as high reliability and fail-safe design. Projects you might work on include writing the code that runs \"on head\" mediating between the physical bio-device interface and the high lev",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/0cead90f-848e-4ca8-951c-3c83185ca755-1490642922085.png",
                    "og:image:height": "200",
                    "og:title": "Neuralink - Software Engineer, Embedded Systems & Firmware",
                    "og:url": "https://jobs.lever.co/neuralink/b02d4f67-53e2-43f0-bb80-ae2d2048ab35",
                    "twitter:description": "Neuralink is developing ultra high bandwidth brain-machine interfaces to connect humans and computers. We\u2019re building a team of multidisciplinary experts and doers who are dedicated to changing the world. We need a diverse, core group of engineers to design, fabricate, and test next-generation medical robotics. We want embedded engineers with specialities, hybrid mechanical-software-electricals engineers, generalists and people we haven\u2019t thought of yet. The ideal candidates are people who get excited about building things, are highly analytical, and enjoy tackling new problems regularly. Our robotics integrate actuated devices with microelectromechanical systems as well as novel surgical procedures. These applications place strong emphasis on high-precision, high-repeatability mechanical motion, as well as high reliability and fail-safe design. Projects you might work on include writing the code that runs \"on head\" mediating between the physical bio-device interface and the high lev",
                    "twitter:title": "Neuralink - Software Engineer, Embedded Systems & Firmware",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We need a diverse, core group of engineers to design, fabricate, and test ... \nProgramming experience on Linux in Python, C, C++, Verilog, or VHDL. \nFamiliarity\u00a0...",
        "title": "Neuralink - Software Engineer, Embedded Systems & Firmware"
    },
    {
        "cacheId": "P7CIbyyutesJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../9d68024e-1c4e-491f-a4df-354ba1cf3420",
        "htmlFormattedUrl": "https://jobs.lever.co/.../9d68024e-1c4e-491f-a4df-354ba1cf3420",
        "htmlSnippet": "We are looking for Software <b>Engineers</b> to work across our <b>engineering</b> teams to <br>\n... Experience with languages such as Python, <b>C++</b>, Java, or Go (Our backend is<br>\n&nbsp;...",
        "htmlTitle": "Bluecore - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/bluecore/9d68024e-1c4e-491f-a4df-354ba1cf3420",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1449095834323.jpg"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "106",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSCdZ_g57BBmoRytYIOPtbxU-kFxhrR6ZzmBOS5ULINeOM8nc-4L5viVFE",
                    "width": "477"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Bluecore we empower digital marketers with the tools to quickly and easily identify targeted audiences from large datasets and reach individual customers with personalized content. Our customers include some of the largest digital retail brands in the nation, and every day we ingest and process millions of events in real-time so that the underlying data can be queried for a variety of use cases. As we continue to add customers we are continuously re-evaluating our infrastructure and making it more robust and scalable. We\u2019ve been around since 2013 and are one of the fastest growing SaaS startups in NYC during that timeframe. We are looking for Software Engineers to work across our engineering teams to build web applications and backend systems that perform at scale. The ideal candidate is adept at writing robust, extensible, and efficient code and has a knack for solving complex problems with simple solutions. While our stack consists primarily of Python on the backend and React",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1449095834323.jpg",
                    "og:image:height": "200",
                    "og:title": "Bluecore - Software Engineer",
                    "og:url": "https://jobs.lever.co/bluecore/9d68024e-1c4e-491f-a4df-354ba1cf3420",
                    "twitter:description": "At Bluecore we empower digital marketers with the tools to quickly and easily identify targeted audiences from large datasets and reach individual customers with personalized content. Our customers include some of the largest digital retail brands in the nation, and every day we ingest and process millions of events in real-time so that the underlying data can be queried for a variety of use cases. As we continue to add customers we are continuously re-evaluating our infrastructure and making it more robust and scalable. We\u2019ve been around since 2013 and are one of the fastest growing SaaS startups in NYC during that timeframe. We are looking for Software Engineers to work across our engineering teams to build web applications and backend systems that perform at scale. The ideal candidate is adept at writing robust, extensible, and efficient code and has a knack for solving complex problems with simple solutions. While our stack consists primarily of Python on the backend and React",
                    "twitter:title": "Bluecore - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are looking for Software Engineers to work across our engineering teams to \n... Experience with languages such as Python, C++, Java, or Go (Our backend is\n\u00a0...",
        "title": "Bluecore - Software Engineer"
    },
    {
        "cacheId": "DORid9Wz230J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../645b2623-b4f7-43f5-b55b-e6a6a41b1c3e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../645b2623-b4f7-43f5-b55b-e6a6a41b1c3e",
        "htmlSnippet": "We are looking for full-stack <b>engineers</b> who are excited about working on <br>\nproducts ... Software <b>engineering</b> experience in any of the following languages: C<br>\n/<b>C++</b>,&nbsp;...",
        "htmlTitle": "STRATIM - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/stratim/645b2623-b4f7-43f5-b55b-e6a6a41b1c3e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b31f78df-4562-4e18-8c2e-ba3097688fc6-1495647248246.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "133",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQHpI3EiCcMeoooGeKe7a13xCW41NQIXUNzFq1aYfeOpnxfxv6DMRtbwsBF",
                    "width": "377"
                }
            ],
            "metatags": [
                {
                    "og:description": "Who we are: At STRATIM we believe that vehicles are going to start to do things themselves, that car ownership will shift from the individual to the corporation and that mobility will become experience driven. Most importantly, these seismic shifts are creating massive operational complexity that can only be solved with highly sophisticated software married to highly integrated physical assets. Who you are: We are looking for full-stack engineers who are excited about working on products in a rapidly evolving market for our customers, somebody who is excited about helping our engineering team evolve with industry best practices and somebody who likes working in a fast-paced collaborative environment that focuses on delivering product feature sets. You will be joining our data platform team mainly focused on building out shared data services. Requirements: - Software engineering experience in any of the following languages: C/C++, Java, JavaScript, Python/Django, Ruby/Ru",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b31f78df-4562-4e18-8c2e-ba3097688fc6-1495647248246.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "STRATIM - Software Engineer",
                    "og:url": "https://jobs.lever.co/stratim/645b2623-b4f7-43f5-b55b-e6a6a41b1c3e",
                    "twitter:description": "Who we are: At STRATIM we believe that vehicles are going to start to do things themselves, that car ownership will shift from the individual to the corporation and that mobility will become experience driven. Most importantly, these seismic shifts are creating massive operational complexity that can only be solved with highly sophisticated software married to highly integrated physical assets. Who you are: We are looking for full-stack engineers who are excited about working on products in a rapidly evolving market for our customers, somebody who is excited about helping our engineering team evolve with industry best practices and somebody who likes working in a fast-paced collaborative environment that focuses on delivering product feature sets. You will be joining our data platform team mainly focused on building out shared data services. Requirements: - Software engineering experience in any of the following languages: C/C++, Java, JavaScript, Python/Django, Ruby/Ru",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/b31f78df-4562-4e18-8c2e-ba3097688fc6-1495647236066.png",
                    "twitter:title": "STRATIM - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are looking for full-stack engineers who are excited about working on \nproducts ... Software engineering experience in any of the following languages: C\n/C++,\u00a0...",
        "title": "STRATIM - Software Engineer"
    },
    {
        "cacheId": "mdXrqbhrCAoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../f79e50f3-289a-4a66-83e6-e9a9ea0079a5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../f79e50f3-289a-4a66-83e6-e9a9ea0079a5",
        "htmlSnippet": "As an Engagement <b>Engineer</b> at CiBO you&#39;ll be part of a larger team of developers <br>\n... Experience with at least one of each of an object oriented {Scala, Java, <b>C++</b>,&nbsp;...",
        "htmlTitle": "CiBO Technologies - Engagement <b>Engineer</b> - Cambridge",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cibotechnologies/f79e50f3-289a-4a66-83e6-e9a9ea0079a5",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "121",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSkmNvkyMjhJq32mxdKanJki0nAy_6paCQ_h3P1jKJ5K5DpyaPXOcgPUQ",
                    "width": "415"
                }
            ],
            "metatags": [
                {
                    "og:description": "As an Engagement Engineer at CiBO you\u2019ll be part of a larger team of developers, data scientists, agronomists, and remote sensing experts. EE\u2019s spend at least 40% of their time deployed from farm fields to wall street working directly with customers to propose, design, rapidly prototype and build custom, enterprise-grade applications. We don\u2019t just provide software tools, we are responsible end-to-end for improving our customers\u2019 businesses. EE\u2019s are supported by our core platform team and library of components to simulate, optimize and aggregate outcomes of all aspects of agriculture, but also know when to just \u201cmake it work.\u201d As engineers, we believe in types, tests, FP, and automation. CiBO runs on Scala in AWS, with sprinklings of R. Qualifications Solid foundation in computer science, including algorithms and data structures Significant experience with professional software engineering, including automated testing, Agile, pair programming, refactoring, relational databases, and",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png",
                    "og:image:height": "200",
                    "og:title": "CiBO Technologies - Engagement Engineer - Cambridge",
                    "og:url": "https://jobs.lever.co/cibotechnologies/f79e50f3-289a-4a66-83e6-e9a9ea0079a5",
                    "twitter:description": "As an Engagement Engineer at CiBO you\u2019ll be part of a larger team of developers, data scientists, agronomists, and remote sensing experts. EE\u2019s spend at least 40% of their time deployed from farm fields to wall street working directly with customers to propose, design, rapidly prototype and build custom, enterprise-grade applications. We don\u2019t just provide software tools, we are responsible end-to-end for improving our customers\u2019 businesses. EE\u2019s are supported by our core platform team and library of components to simulate, optimize and aggregate outcomes of all aspects of agriculture, but also know when to just \u201cmake it work.\u201d As engineers, we believe in types, tests, FP, and automation. CiBO runs on Scala in AWS, with sprinklings of R. Qualifications Solid foundation in computer science, including algorithms and data structures Significant experience with professional software engineering, including automated testing, Agile, pair programming, refactoring, relational databases, and",
                    "twitter:title": "CiBO Technologies - Engagement Engineer - Cambridge",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As an Engagement Engineer at CiBO you'll be part of a larger team of developers \n... Experience with at least one of each of an object oriented {Scala, Java, C++,\u00a0...",
        "title": "CiBO Technologies - Engagement Engineer - Cambridge"
    },
    {
        "cacheId": "Q51oEA-WB0QJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445",
        "htmlSnippet": "As a Software <b>Engineer</b> at Twitch, some things you may be working on are: ... in <br>\nat least one of the following languages: Javascript, Ruby, Python, Go, or <b>C++</b>&nbsp;...",
        "htmlTitle": "Twitch - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you\u2019re a smart engineer who\u2019s capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you. As a Software Engineer at Twitch, some things you may be working on are: Our chat system, which supports millions of concurrent users Our video distribution system, which is one of the largest in the world Elegant, highly-available web services to support one of our many front end platforms Front end web engineering that is functional, beautiful, and delightful Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4 Building new features that millions of users will be seeing Helping build robust deployment tools to help us move forward rapidly Building great tools that lets us support our custom",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Software Engineer",
                    "og:url": "https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445",
                    "twitter:description": "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you\u2019re a smart engineer who\u2019s capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you. As a Software Engineer at Twitch, some things you may be working on are: Our chat system, which supports millions of concurrent users Our video distribution system, which is one of the largest in the world Elegant, highly-available web services to support one of our many front end platforms Front end web engineering that is functional, beautiful, and delightful Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4 Building new features that millions of users will be seeing Helping build robust deployment tools to help us move forward rapidly Building great tools that lets us support our custom",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Software Engineer at Twitch, some things you may be working on are: ... in \nat least one of the following languages: Javascript, Ruby, Python, Go, or C++\u00a0...",
        "title": "Twitch - Software Engineer"
    },
    {
        "cacheId": "UoyD3BfQeZ4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../408a8d17-4404-432a-9b1b-af1da5c49791",
        "htmlFormattedUrl": "https://jobs.lever.co/.../408a8d17-4404-432a-9b1b-af1da5c49791",
        "htmlSnippet": "Proficient knowledge in Java/C/<b>C++</b>. Basic understanding of SQL. Experience in <br>\nGraph Algorithms and Graph processing engines like Neo4j, Giraph, GraphX&nbsp;...",
        "htmlTitle": "Drawbridge - Senior Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/drawbridge/408a8d17-4404-432a-9b1b-af1da5c49791",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwcwXStLSk03_g-LKG8cnhZOlvetfTK3WHqD394bjfElRrSCMigDtkqNXZ",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Are you passionate about Big Data? This is a great opportunity for an outstanding candidate who wants to work with top notch engineers and is interested in building smart, scalable systems using Hadoop stack technologies! The ideal candidate will have a good understanding of MapReduce and the Hadoop stack . We are making decisions and predicting the future with data - if you want to work on bleeding-edge technology, handling tens of billions of transactions a day, this may be the opportunity for you!\" About Drawbridge Drawbridge is the leading anonymized digital identity company, building patented cross-device technology that fundamentally changes the way brands connect with people. In fact, Drawbridge coined the term \u201ccross-device\u201d and has been a pioneer in cross-device identity. The company provides visibility into how consumers interact across devices along the path to purchase, giving marketers insight into both online and offline behavior to drive better results. The company is h",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725526521.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Drawbridge - Senior Software Engineer",
                    "og:url": "https://jobs.lever.co/drawbridge/408a8d17-4404-432a-9b1b-af1da5c49791",
                    "twitter:description": "Are you passionate about Big Data? This is a great opportunity for an outstanding candidate who wants to work with top notch engineers and is interested in building smart, scalable systems using Hadoop stack technologies! The ideal candidate will have a good understanding of MapReduce and the Hadoop stack . We are making decisions and predicting the future with data - if you want to work on bleeding-edge technology, handling tens of billions of transactions a day, this may be the opportunity for you!\" About Drawbridge Drawbridge is the leading anonymized digital identity company, building patented cross-device technology that fundamentally changes the way brands connect with people. In fact, Drawbridge coined the term \u201ccross-device\u201d and has been a pioneer in cross-device identity. The company provides visibility into how consumers interact across devices along the path to purchase, giving marketers insight into both online and offline behavior to drive better results. The company is h",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/868efa4f-ba00-4f2b-b6c1-b0102048378c-1490725516278.png",
                    "twitter:title": "Drawbridge - Senior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Proficient knowledge in Java/C/C++. Basic understanding of SQL. Experience in \nGraph Algorithms and Graph processing engines like Neo4j, Giraph, GraphX\u00a0...",
        "title": "Drawbridge - Senior Software Engineer"
    },
    {
        "cacheId": "u6O0aV7Bw3EJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../739ec8dd-5d50-4c38-949e-b7485653ec86",
        "htmlFormattedUrl": "https://jobs.lever.co/.../739ec8dd-5d50-4c38-949e-b7485653ec86",
        "htmlSnippet": "Site Reliability <b>Engineer</b>. San Francisco, CA ... You&#39;re a programmer, and <br>\nproficient in either C, <b>C++</b>, Python, Perl, PHP, Ruby, or the like. You&#39;re familiar <br>\nwith&nbsp;...",
        "htmlTitle": "Creative Market - Site Reliability <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/creativemarket/739ec8dd-5d50-4c38-949e-b7485653ec86",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/8aa36117-4e98-402f-840a-de3de20f2942-1495061536581.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "116",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRXPwUOeyzXjbDS69phkiz_gbOZ5WjEEgG86yngNrWnie3fk1RK11tA4Q",
                    "width": "300"
                }
            ],
            "metatags": [
                {
                    "og:description": "Thank you for your interest in joining our Web Operations team at Creative Market, where you'll help independent creators make a living doing what they love! Every day, thousands of customers use Creative Market to buy ready-to-use design content (fonts, graphics, templates, website themes, 3d models, etc) directly from top designers around the world. Join the team to help us continue our meteoric growth, and your work will be used by millions of people every month. As an SRE, you'll help maintain our fantastic uptime, wave the Infrastructure as Code flag, work with our product engineering teams to deliver great new features, and work closely with our engineering leadership on special projects. This is a full-time position. Remote opportunities are available, but you must be able to work in the United States.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/8aa36117-4e98-402f-840a-de3de20f2942-1495061536581.png",
                    "og:image:height": "200",
                    "og:title": "Creative Market - Site Reliability Engineer",
                    "og:url": "https://jobs.lever.co/creativemarket/739ec8dd-5d50-4c38-949e-b7485653ec86",
                    "twitter:description": "Thank you for your interest in joining our Web Operations team at Creative Market, where you'll help independent creators make a living doing what they love! Every day, thousands of customers use Creative Market to buy ready-to-use design content (fonts, graphics, templates, website themes, 3d models, etc) directly from top designers around the world. Join the team to help us continue our meteoric growth, and your work will be used by millions of people every month. As an SRE, you'll help maintain our fantastic uptime, wave the Infrastructure as Code flag, work with our product engineering teams to deliver great new features, and work closely with our engineering leadership on special projects. This is a full-time position. Remote opportunities are available, but you must be able to work in the United States.",
                    "twitter:title": "Creative Market - Site Reliability Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Site Reliability Engineer. San Francisco, CA ... You're a programmer, and \nproficient in either C, C++, Python, Perl, PHP, Ruby, or the like. You're familiar \nwith\u00a0...",
        "title": "Creative Market - Site Reliability Engineer"
    },
    {
        "cacheId": "yN9hFfM7CsEJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/quora/4ea5b0e2-b570-439f-a3a1-1f3010422273",
        "htmlFormattedUrl": "https://jobs.lever.co/quora/4ea5b0e2-b570-439f-a3a1-1f3010422273",
        "htmlSnippet": "We are looking for an experienced Machine Learning <b>engineer</b> to join our ... <br>\nbuilding end to end Machine Learning systems; Knowledge of Python or <b>C++</b>, or <br>\nthe&nbsp;...",
        "htmlTitle": "Quora - Software <b>Engineer</b> - Machine Learning",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/quora/4ea5b0e2-b570-439f-a3a1-1f3010422273",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/QuoraScreenLogo_512.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "130",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJ-yjNaab7m8RV39v1PFEJ5d3Gj8vgVY6GAp3a3yYULv7VYvNs-AFNvvbw",
                    "width": "387"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are looking for an experienced Machine Learning engineer to join our growing engineering team. At Quora, we use Machine Learning in almost every part of the product - feed ranking, answer ranking, search, topic and user recommendations, spam detection etc. As a Machine Learning expert, you will have a unique opportunity to have high impact by advancing these systems, as well as uncovering new opportunities to apply Machine Learning to the Quora product. You will also play a key role in developing tools and abstractions that our other developers would build on top of.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/QuoraScreenLogo_512.png",
                    "og:image:height": "200",
                    "og:title": "Quora - Software Engineer - Machine Learning",
                    "og:url": "https://jobs.lever.co/quora/4ea5b0e2-b570-439f-a3a1-1f3010422273",
                    "twitter:description": "We are looking for an experienced Machine Learning engineer to join our growing engineering team. At Quora, we use Machine Learning in almost every part of the product - feed ranking, answer ranking, search, topic and user recommendations, spam detection etc. As a Machine Learning expert, you will have a unique opportunity to have high impact by advancing these systems, as well as uncovering new opportunities to apply Machine Learning to the Quora product. You will also play a key role in developing tools and abstractions that our other developers would build on top of.",
                    "twitter:title": "Quora - Software Engineer - Machine Learning",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are looking for an experienced Machine Learning engineer to join our ... \nbuilding end to end Machine Learning systems; Knowledge of Python or C++, or \nthe\u00a0...",
        "title": "Quora - Software Engineer - Machine Learning"
    },
    {
        "cacheId": "xWHauW6FFCUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../af2c3060-f4d6-45b5-b808-9f7353e1f07f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../af2c3060-f4d6-45b5-b808-9f7353e1f07f",
        "htmlSnippet": "<b>Engineering</b> &amp; Modeling \u2013 Inventory Performance ... systems; Hands-on <br>\nexperience creating high performance programs in <b>C++</b>, Java or similar <br>\nlanguage(s).",
        "htmlTitle": "Quantcast - Senior Software <b>Engineer</b>, Inventory Performance",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/quantcast/af2c3060-f4d6-45b5-b808-9f7353e1f07f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e6f46c3e-9ac6-490b-9b2a-f12d164a38a6-1501869306542.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "146",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSH7zjIGCEKUniZRDLo08yh086rw527mRVkLZkVss3kN5WHXqG7SbG1KZyv",
                    "width": "344"
                }
            ],
            "metatags": [
                {
                    "og:description": "Quantcast is a large scale, data driven organization that lives and breathes data, processing well over 2 million transactions a second. Quantcast engineers leverage our large datasets, computational power and analytic tools to build high quality and diverse products that support Quantcast\u2019s position as a world-class leader in online advertising. The Inventory Performance team\u2019s mission is two-fold: to drive improved performance for advertisers by delivering relevant advertising across the digital advertising ecosystem and to build defenses in order to protect our clients against fraudsters trying to siphon money out of the advertising space. We are looking for top-tier talent with strong engineering and big data experience to help lead our efforts in designing, implementing and operating large scale ML systems in a production environment.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e6f46c3e-9ac6-490b-9b2a-f12d164a38a6-1501869306542.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Quantcast - Senior Software Engineer, Inventory Performance",
                    "og:url": "https://jobs.lever.co/quantcast/af2c3060-f4d6-45b5-b808-9f7353e1f07f",
                    "twitter:description": "Quantcast is a large scale, data driven organization that lives and breathes data, processing well over 2 million transactions a second. Quantcast engineers leverage our large datasets, computational power and analytic tools to build high quality and diverse products that support Quantcast\u2019s position as a world-class leader in online advertising. The Inventory Performance team\u2019s mission is two-fold: to drive improved performance for advertisers by delivering relevant advertising across the digital advertising ecosystem and to build defenses in order to protect our clients against fraudsters trying to siphon money out of the advertising space. We are looking for top-tier talent with strong engineering and big data experience to help lead our efforts in designing, implementing and operating large scale ML systems in a production environment.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e6f46c3e-9ac6-490b-9b2a-f12d164a38a6-1501614259019.png",
                    "twitter:title": "Quantcast - Senior Software Engineer, Inventory Performance",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Engineering & Modeling \u2013 Inventory Performance ... systems; Hands-on \nexperience creating high performance programs in C++, Java or similar \nlanguage(s).",
        "title": "Quantcast - Senior Software Engineer, Inventory Performance"
    },
    {
        "cacheId": "GEO7XSjxwI8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../33686f4d-c9c7-458f-b255-b38c580cead4",
        "htmlFormattedUrl": "https://jobs.lever.co/.../33686f4d-c9c7-458f-b255-b38c580cead4",
        "htmlSnippet": "MZ is seeking a Senior Application Security <b>Engineer</b> who is driven to work on ... <br>\nC/<b>C++</b>, PHP, Erlang, Lua, and Python are highly valued, but others will help too.",
        "htmlTitle": "MZ - Senior Application Security <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/33686f4d-c9c7-458f-b255-b38c580cead4",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ is seeking a Senior Application Security Engineer who is driven to work on some of the most challenging security problems. You will use your skills to secure products running on large and complex technology stacks. The role is flexible and will be shaped around your strengths, with either a focus on penetration testing and code review, or developing tools (static/dynamic analyzers, fuzzers, etc.).",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Application Security Engineer",
                    "og:url": "https://jobs.lever.co/machinezone/33686f4d-c9c7-458f-b255-b38c580cead4",
                    "twitter:description": "MZ is seeking a Senior Application Security Engineer who is driven to work on some of the most challenging security problems. You will use your skills to secure products running on large and complex technology stacks. The role is flexible and will be shaped around your strengths, with either a focus on penetration testing and code review, or developing tools (static/dynamic analyzers, fuzzers, etc.).",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Application Security Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "MZ is seeking a Senior Application Security Engineer who is driven to work on ... \nC/C++, PHP, Erlang, Lua, and Python are highly valued, but others will help too.",
        "title": "MZ - Senior Application Security Engineer"
    },
    {
        "cacheId": "Kz0FRRWAE6sJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../fd27b4e5-f57e-44c3-94ee-29dda2129673",
        "htmlFormattedUrl": "https://jobs.lever.co/.../fd27b4e5-f57e-44c3-94ee-29dda2129673",
        "htmlSnippet": "To ensure our success, we employ a variety of <b>engineering</b> methodologies to <br>\nensure ... Help architect a large software system, written in <b>C++</b>, C#, and Python,<br>\n&nbsp;...",
        "htmlTitle": "Plethora - Computational Geometry Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/plethora/fd27b4e5-f57e-44c3-94ee-29dda2129673",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1483574051428.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "66",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ8L6cPsHN4Q8TN2em6nj99HiXdkARMvEPzha67AaHYmgDLx_SlURaFVQ",
                    "width": "600"
                }
            ],
            "metatags": [
                {
                    "og:description": "Plethora is building the future of manufacturing - a new kind of automated factory that turns digital designs into physical products in days, not months with our internally developed software and fully-integrated factory system. We are a uniquely ambitious company funded by some of the biggest names, such as Founders Fund, Lux Capital, Google, and Autodesk. Our organization is already impacting the short-run manufacturing space, with a category-leading NPS, in the $21B addressable market that is ripe for disruption. We\u2019re looking for a Computational Geometry Software Developer to help build the automated software pipeline that generates manufacturing instructions. This system determines the precise strategy necessary to build a customer part, from the toolpaths to the custom workholdings. As you can imagine, building a software-powered factory is a tricky process. To ensure our success, we employ a variety of engineering methodologies to ensure the correctness and safety of our sys",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1483574051428.png",
                    "og:image:height": "200",
                    "og:title": "Plethora - Computational Geometry Software Engineer",
                    "og:url": "https://jobs.lever.co/plethora/fd27b4e5-f57e-44c3-94ee-29dda2129673",
                    "twitter:description": "Plethora is building the future of manufacturing - a new kind of automated factory that turns digital designs into physical products in days, not months with our internally developed software and fully-integrated factory system. We are a uniquely ambitious company funded by some of the biggest names, such as Founders Fund, Lux Capital, Google, and Autodesk. Our organization is already impacting the short-run manufacturing space, with a category-leading NPS, in the $21B addressable market that is ripe for disruption. We\u2019re looking for a Computational Geometry Software Developer to help build the automated software pipeline that generates manufacturing instructions. This system determines the precise strategy necessary to build a customer part, from the toolpaths to the custom workholdings. As you can imagine, building a software-powered factory is a tricky process. To ensure our success, we employ a variety of engineering methodologies to ensure the correctness and safety of our sys",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1479853206515.png",
                    "twitter:title": "Plethora - Computational Geometry Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "To ensure our success, we employ a variety of engineering methodologies to \nensure ... Help architect a large software system, written in C++, C#, and Python,\n\u00a0...",
        "title": "Plethora - Computational Geometry Software Engineer"
    },
    {
        "cacheId": "Ns2nByHSX1oJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../55bcc68b-f7ba-448f-bb02-033537547b33",
        "htmlFormattedUrl": "https://jobs.lever.co/.../55bcc68b-f7ba-448f-bb02-033537547b33",
        "htmlSnippet": "Software <b>Engineer</b>. Santa Fe, NM. <b>Engineering</b> ... learning; Google Cloud/AWS; <br>\nAPI; Platform experience; C/<b>C++</b>; Web services (e.g., REST, JSON, XML).",
        "htmlTitle": "Descartes Labs - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/descarteslabs.com/55bcc68b-f7ba-448f-bb02-033537547b33",
        "pagemap": {
            "metatags": [
                {
                    "og:description": "Redefine the limits of \u201cBig Data.\u201d Our peta-scale, cloud-based processing architecture provides daily challenges and opportunities for innovation. Your Python must be very strong, along with excellent debugging and optimization skills. Pluses: parallel computing, machine learning, Google Cloud/AWS, Geographic Information Systems and GDAL.",
                    "og:image:height": "200",
                    "og:title": "Descartes Labs - Software Engineer",
                    "og:url": "https://jobs.lever.co/descarteslabs.com/55bcc68b-f7ba-448f-bb02-033537547b33",
                    "twitter:description": "Redefine the limits of \u201cBig Data.\u201d Our peta-scale, cloud-based processing architecture provides daily challenges and opportunities for innovation. Your Python must be very strong, along with excellent debugging and optimization skills. Pluses: parallel computing, machine learning, Google Cloud/AWS, Geographic Information Systems and GDAL.",
                    "twitter:title": "Descartes Labs - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer. Santa Fe, NM. Engineering ... learning; Google Cloud/AWS; \nAPI; Platform experience; C/C++; Web services (e.g., REST, JSON, XML).",
        "title": "Descartes Labs - Software Engineer"
    },
    {
        "cacheId": "Tp6l7ksyIxoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../f765bf93-3ee0-4d0d-b3dc-1e53cc156ca9",
        "htmlFormattedUrl": "https://jobs.lever.co/.../f765bf93-3ee0-4d0d-b3dc-1e53cc156ca9",
        "htmlSnippet": "The Software <b>Engineers</b> on the Data team are in charge of designing, ... <b>C++</b>, C#, <br>\nJava and/or Scala; Experience designing and implementing Big Data solutions&nbsp;...",
        "htmlTitle": "Chan Zuckerberg Initiative - Software <b>Engineer</b>, Data - Science",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/chanzuckerberg/f765bf93-3ee0-4d0d-b3dc-1e53cc156ca9",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5677ff2b-be2c-49e7-b0cb-7e33c18149dd-1493236538696.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "163",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRdCHgppwc8MOqFqW3hAcr3_owpCjGPmF3A_F-wGQp3jtzkEXsdcvuNbBA",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Chan Zuckerberg Initiative is dedicated to advancing human potential and promoting equal opportunity through technology, grantmaking, impact investing, policy, and advocacy work. We look for bold ideas \u2014 regardless of structure and stage \u2014 and help them scale by pairing world-class engineers with subject matter experts to build tools that accelerate the pace of social progress. WHAT WE BELIEVE We engage directly in the communities we serve because no one understands how to address our society\u2019s challenges better than those who live them everyday. These partners help us identify problems and opportunities, learn fast and iterate toward our audacious goals for the next century. We strive to be humble, empathetic and scrappy life-long learners who work collaboratively to develop community-centered solutions. We believe that high-performing teams include people from different backgrounds and experiences who can challenge each other's assumptions with fresh perspectives. To that en",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5677ff2b-be2c-49e7-b0cb-7e33c18149dd-1493236538696.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Chan Zuckerberg Initiative - Software Engineer, Data - Science",
                    "og:url": "https://jobs.lever.co/chanzuckerberg/f765bf93-3ee0-4d0d-b3dc-1e53cc156ca9",
                    "twitter:description": "The Chan Zuckerberg Initiative is dedicated to advancing human potential and promoting equal opportunity through technology, grantmaking, impact investing, policy, and advocacy work. We look for bold ideas \u2014 regardless of structure and stage \u2014 and help them scale by pairing world-class engineers with subject matter experts to build tools that accelerate the pace of social progress. WHAT WE BELIEVE We engage directly in the communities we serve because no one understands how to address our society\u2019s challenges better than those who live them everyday. These partners help us identify problems and opportunities, learn fast and iterate toward our audacious goals for the next century. We strive to be humble, empathetic and scrappy life-long learners who work collaboratively to develop community-centered solutions. We believe that high-performing teams include people from different backgrounds and experiences who can challenge each other's assumptions with fresh perspectives. To that en",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5677ff2b-be2c-49e7-b0cb-7e33c18149dd-1467045375869.png",
                    "twitter:title": "Chan Zuckerberg Initiative - Software Engineer, Data - Science",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The Software Engineers on the Data team are in charge of designing, ... C++, C#, \nJava and/or Scala; Experience designing and implementing Big Data solutions\u00a0...",
        "title": "Chan Zuckerberg Initiative - Software Engineer, Data - Science"
    },
    {
        "cacheId": "g0gGYXdt4kMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/lytro/4187e774-b233-4946-9265-a64c2de2ccae",
        "htmlFormattedUrl": "https://jobs.lever.co/lytro/4187e774-b233-4946-9265-a64c2de2ccae",
        "htmlSnippet": "The Immerge team is expanding and looking for a skilled software <b>engineer</b> to <br>\njoin us. ... A minimum of 5 years software development experience in <b>C++</b>.",
        "htmlTitle": "Lytro - Visual Effects Software <b>Engineer</b>, VR",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/lytro/4187e774-b233-4946-9265-a64c2de2ccae",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/d6da15bc-1f00-436d-8782-0d62df041b27-1478026956796.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "98",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSRVhMtzsHuJ-2IsXcgv2fwbG3lI-YoliXpgM3GEVRSfOpdexNKOX9yqZY",
                    "width": "300"
                }
            ],
            "metatags": [
                {
                    "og:description": "About Lytro: Lytro is revolutionizing high-end content creation for Virtual Reality and Cinema with the world\u2019s first professional Light Field solutions. We are backed by top-tier VCs including Andreessen-Horowitz, Greylock Partners, NEA, and North Bridge Venture Partners and have built a world-class team and dynamic culture driven by innovation and collaboration. About The Team: Lytro Immerge is the world\u2019s first professional Light Field solution for Virtual Reality. From our novel multi-camera rig/array capture system to our rendering, post production tools, and playback environment, Lytro Immerge provides content creators the ability to achieve lifelike presence through capturing the world in six degrees of freedom (6DoF). The system captures live action video for virtual reality with true stereo, parallax and realistic lighting offering viewers more freedom of movement, superior image quality, and ultimately a much more immersive experience. About The Opportunity: The Immerge",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/d6da15bc-1f00-436d-8782-0d62df041b27-1478026956796.png",
                    "og:image:height": "200",
                    "og:title": "Lytro - Visual Effects Software Engineer, VR",
                    "og:url": "https://jobs.lever.co/lytro/4187e774-b233-4946-9265-a64c2de2ccae",
                    "twitter:description": "About Lytro: Lytro is revolutionizing high-end content creation for Virtual Reality and Cinema with the world\u2019s first professional Light Field solutions. We are backed by top-tier VCs including Andreessen-Horowitz, Greylock Partners, NEA, and North Bridge Venture Partners and have built a world-class team and dynamic culture driven by innovation and collaboration. About The Team: Lytro Immerge is the world\u2019s first professional Light Field solution for Virtual Reality. From our novel multi-camera rig/array capture system to our rendering, post production tools, and playback environment, Lytro Immerge provides content creators the ability to achieve lifelike presence through capturing the world in six degrees of freedom (6DoF). The system captures live action video for virtual reality with true stereo, parallax and realistic lighting offering viewers more freedom of movement, superior image quality, and ultimately a much more immersive experience. About The Opportunity: The Immerge",
                    "twitter:title": "Lytro - Visual Effects Software Engineer, VR",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The Immerge team is expanding and looking for a skilled software engineer to \njoin us. ... A minimum of 5 years software development experience in C++.",
        "title": "Lytro - Visual Effects Software Engineer, VR"
    },
    {
        "cacheId": "N1vekZ4tTt4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../db43fdbd-80a6-4b58-99d9-0aff3d89dcc5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../db43fdbd-80a6-4b58-99d9-0aff3d89dcc5",
        "htmlSnippet": "Product Development \u2013 Product <b>Engineering</b>. Full-time ... Influence software <br>\n<b>engineering</b> best practices within the team ... Deft programming skills in PHP, C/<b>C</b><br>\n<b>++</b>.",
        "htmlTitle": "HealthEngine - Senior <b>Engineer</b> - Full Stack",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/healthengine/db43fdbd-80a6-4b58-99d9-0aff3d89dcc5",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e21f9af0-62d2-478c-a370-9d809e0fc948-1485230901032.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "160",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT6wAJLn1YZi03G5Z88nyzhlWT0PkpZgaIk4XFWElfG9es6CtFrjH-2F2Ip",
                    "width": "315"
                }
            ],
            "metatags": [
                {
                    "og:description": "About Us HealthEngine is an established startup, changing the face of health access across Australia. As Australia's leading health appointment marketplace, we help millions of Australians find and book health appointments, 24/7. We combine two of Australia's fastest growing industries, Health and Technology. It is an exciting time to be joining HealthEngine - a new direction, new products, a new office, and this awesome opportunity to join the ever-expanding HealthEngine tribe as a Senior Full Stack Engineer. About You Your Responsibilities: \u00b7 Design, develop, test, deploy, maintain and improve HealthEngine products and product features \u00b7 Influence software engineering best practices within the team \u00b7 Support and help the progression of other software engineers Preferred Capability: \u00b7 Deft programming skills in PHP, C/C++ \u00b7 Black belt skills with PostgresSQL, MySQL, MSSQL \u00b7 Ninja like web and front end programming skills in HTML, CS",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e21f9af0-62d2-478c-a370-9d809e0fc948-1485230901032.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "HealthEngine - Senior Engineer - Full Stack",
                    "og:url": "https://jobs.lever.co/healthengine/db43fdbd-80a6-4b58-99d9-0aff3d89dcc5",
                    "twitter:description": "About Us HealthEngine is an established startup, changing the face of health access across Australia. As Australia's leading health appointment marketplace, we help millions of Australians find and book health appointments, 24/7. We combine two of Australia's fastest growing industries, Health and Technology. It is an exciting time to be joining HealthEngine - a new direction, new products, a new office, and this awesome opportunity to join the ever-expanding HealthEngine tribe as a Senior Full Stack Engineer. About You Your Responsibilities: \u00b7 Design, develop, test, deploy, maintain and improve HealthEngine products and product features \u00b7 Influence software engineering best practices within the team \u00b7 Support and help the progression of other software engineers Preferred Capability: \u00b7 Deft programming skills in PHP, C/C++ \u00b7 Black belt skills with PostgresSQL, MySQL, MSSQL \u00b7 Ninja like web and front end programming skills in HTML, CS",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e21f9af0-62d2-478c-a370-9d809e0fc948-1485230827682.png",
                    "twitter:title": "HealthEngine - Senior Engineer - Full Stack",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Product Development \u2013 Product Engineering. Full-time ... Influence software \nengineering best practices within the team ... Deft programming skills in PHP, C/C\n++.",
        "title": "HealthEngine - Senior Engineer - Full Stack"
    },
    {
        "cacheId": "8OwYvyHpSF8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../bb9c4fc4-115e-4ff7-b151-ad905ed16d41",
        "htmlFormattedUrl": "https://jobs.lever.co/.../bb9c4fc4-115e-4ff7-b151-ad905ed16d41",
        "htmlSnippet": "Software <b>Engineer</b> \u2013 Full-Stack &amp; Product Design ... users; Python, SQL, Linux, C, <br>\n<b>C++</b>, Swift, and Bash; Human-Robot interaction design; Can design for scale.",
        "htmlTitle": "Zipline - Software <b>Engineer</b> \u2013 Full-Stack &amp; Product Design",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/flyzipline/bb9c4fc4-115e-4ff7-b151-ad905ed16d41",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/85e5c177-1c48-44f8-a814-d88bb0584f08-1470355906495.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "146",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRA1dg8b_I3I1YzLprkBF2fuxdzt0ROIC1l6DqgCae9_-jWOgMzL3AOeJo",
                    "width": "344"
                }
            ],
            "metatags": [
                {
                    "og:description": "Zipline is looking for a full-stack developer with a strong instinct for product design to build systems that empower our operations around the world and allow our global customers to interact with Zipline.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/85e5c177-1c48-44f8-a814-d88bb0584f08-1470355906495.png",
                    "og:image:height": "200",
                    "og:title": "Zipline - Software Engineer \u2013 Full-Stack & Product Design",
                    "og:url": "https://jobs.lever.co/flyzipline/bb9c4fc4-115e-4ff7-b151-ad905ed16d41",
                    "twitter:description": "Zipline is looking for a full-stack developer with a strong instinct for product design to build systems that empower our operations around the world and allow our global customers to interact with Zipline.",
                    "twitter:title": "Zipline - Software Engineer \u2013 Full-Stack & Product Design",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer \u2013 Full-Stack & Product Design ... users; Python, SQL, Linux, C, \nC++, Swift, and Bash; Human-Robot interaction design; Can design for scale.",
        "title": "Zipline - Software Engineer \u2013 Full-Stack & Product Design"
    },
    {
        "cacheId": "qfZG3LN0gPIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../d7ff0e0f-4825-459a-bdf0-39f56e35a34c",
        "htmlFormattedUrl": "https://jobs.lever.co/.../d7ff0e0f-4825-459a-bdf0-39f56e35a34c",
        "htmlSnippet": "Position: Software Validation <b>Engineer</b> ... Executing software validation test <br>\nprocedures and developing <b>engineering</b> ... Excellent coding skills in C, <b>C++</b>.",
        "htmlTitle": "Faraday Future - Software Validation <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/d7ff0e0f-4825-459a-bdf0-39f56e35a34c",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Company: Faraday Future is a California mobility company bringing a tech approach to clean transportation. At FF, we believe that by placing equal emphasis on automotive and technology disciplines, our team of experts is uniquely positioned to take a user-centric, technology-first approach to vehicle design with the ultimate aim of connecting the automotive experience with the rest of your life. Position: Software Validation Engineer Your Role: \u2022 Perform independent product testing including performing Software Requirements Specification reviews and analysis. \u2022 Designing, developing and implementing software validation test strategy, test plans, test automation scripts and test procedures to validate the product. \u2022 Executing software validation test procedures and developing engineering specifications and automated bench set-ups and debugging product related issues. \u2022 Participating in software validation test procedure peer reviews, identifying",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Software Validation Engineer",
                    "og:url": "https://jobs.lever.co/faradayfuture/d7ff0e0f-4825-459a-bdf0-39f56e35a34c",
                    "twitter:description": "The Company: Faraday Future is a California mobility company bringing a tech approach to clean transportation. At FF, we believe that by placing equal emphasis on automotive and technology disciplines, our team of experts is uniquely positioned to take a user-centric, technology-first approach to vehicle design with the ultimate aim of connecting the automotive experience with the rest of your life. Position: Software Validation Engineer Your Role: \u2022 Perform independent product testing including performing Software Requirements Specification reviews and analysis. \u2022 Designing, developing and implementing software validation test strategy, test plans, test automation scripts and test procedures to validate the product. \u2022 Executing software validation test procedures and developing engineering specifications and automated bench set-ups and debugging product related issues. \u2022 Participating in software validation test procedure peer reviews, identifying",
                    "twitter:title": "Faraday Future - Software Validation Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Position: Software Validation Engineer ... Executing software validation test \nprocedures and developing engineering ... Excellent coding skills in C, C++.",
        "title": "Faraday Future - Software Validation Engineer"
    },
    {
        "cacheId": "mSUrWP7sJjkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../cd806c6b-d47e-493c-be5e-ed09a40d9fcc",
        "htmlFormattedUrl": "https://jobs.lever.co/.../cd806c6b-d47e-493c-be5e-ed09a40d9fcc",
        "htmlSnippet": "Ph.D with a minimum 2+ years of experience desired; Experience with C/<b>C++</b>, <br>\nrapid prototype and implementation on different platforms; Experience in&nbsp;...",
        "htmlTitle": "Faraday Future - Battery Control/Algorithm <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/cd806c6b-d47e-493c-be5e-ed09a40d9fcc",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "\u00b7 Develop multi-scale new performance, aging, electrical-thermal model for Li-ion and high-energy batteries. \u00b7 Develop advanced state/parameter estimation algorithm for nonlinear system and charging strategies for Li-ion batteries \u00b7 Simulate the developed algorithm and model in MATLAB and Simulink environment \u00b7 Perform numerical simulations to identify performance limitation, optimize cell designs, and development novel battery management systems \u00b7 Collaborate with experimental data for model characterization",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Battery Control/Algorithm Engineer",
                    "og:url": "https://jobs.lever.co/faradayfuture/cd806c6b-d47e-493c-be5e-ed09a40d9fcc",
                    "twitter:description": "\u00b7 Develop multi-scale new performance, aging, electrical-thermal model for Li-ion and high-energy batteries. \u00b7 Develop advanced state/parameter estimation algorithm for nonlinear system and charging strategies for Li-ion batteries \u00b7 Simulate the developed algorithm and model in MATLAB and Simulink environment \u00b7 Perform numerical simulations to identify performance limitation, optimize cell designs, and development novel battery management systems \u00b7 Collaborate with experimental data for model characterization",
                    "twitter:title": "Faraday Future - Battery Control/Algorithm Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Ph.D with a minimum 2+ years of experience desired; Experience with C/C++, \nrapid prototype and implementation on different platforms; Experience in\u00a0...",
        "title": "Faraday Future - Battery Control/Algorithm Engineer"
    },
    {
        "cacheId": "ZKPkX8sAU-EJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../9035fc10-77fa-4785-8010-43831ede5c53",
        "htmlFormattedUrl": "https://jobs.lever.co/.../9035fc10-77fa-4785-8010-43831ede5c53",
        "htmlSnippet": "MZ is looking for a Senior Frontend <b>Engineer</b> to join our Advertising ... (Java, <br>\nXamarin C#); Experience with strongly typed languages such as Java, <b>C++</b>, C#&nbsp;...",
        "htmlTitle": "MZ - Senior Frontend <b>Engineer</b>, Marketing",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/9035fc10-77fa-4785-8010-43831ede5c53",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ is looking for a Senior Frontend Engineer to join our Advertising Technology Engineering team. You will be working with a group of world-class engineers, architects and product managers to build real-time applications, dashboards and tools that will be used internally and by our customers. You must have a solid understanding of Front End Web technologies and have a history of building successful Web-based solutions and take mockups to implementation. This role requires that you are a self-starter with the ability to deliver on time with quality and also handle multiple tasks simultaneously. We're a flat, lean, agile, self-governing team. We value transparency and trust. We continue to create purpose in our work, question the status quo, seek individual mastery and encourage autonomy.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Frontend Engineer, Marketing",
                    "og:url": "https://jobs.lever.co/machinezone/9035fc10-77fa-4785-8010-43831ede5c53",
                    "twitter:description": "MZ is looking for a Senior Frontend Engineer to join our Advertising Technology Engineering team. You will be working with a group of world-class engineers, architects and product managers to build real-time applications, dashboards and tools that will be used internally and by our customers. You must have a solid understanding of Front End Web technologies and have a history of building successful Web-based solutions and take mockups to implementation. This role requires that you are a self-starter with the ability to deliver on time with quality and also handle multiple tasks simultaneously. We're a flat, lean, agile, self-governing team. We value transparency and trust. We continue to create purpose in our work, question the status quo, seek individual mastery and encourage autonomy.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Frontend Engineer, Marketing",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "MZ is looking for a Senior Frontend Engineer to join our Advertising ... (Java, \nXamarin C#); Experience with strongly typed languages such as Java, C++, C#\u00a0...",
        "title": "MZ - Senior Frontend Engineer, Marketing"
    },
    {
        "cacheId": "DOuz0nr_lFkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../182ff62a-657f-4178-a85c-1fa64918b019",
        "htmlFormattedUrl": "https://jobs.lever.co/.../182ff62a-657f-4178-a85c-1fa64918b019",
        "htmlSnippet": "MZ Game Studio is seeking a highly skilled Senior Build and Tools <b>Engineer</b> to ... <br>\nExperience programming in C/<b>C++</b>, Lua, PHP, Obj-C, or Java; Experience with&nbsp;...",
        "htmlTitle": "MZ - Senior Build <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/182ff62a-657f-4178-a85c-1fa64918b019",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "MZ Game Studio is seeking a highly skilled Senior Build and Tools Engineer to support its development teams and ensure their build pipelines are running as efficiently as possible. Build and Tools engineers work closely with both software engineers and product managers to provide build support from development to product release. Success in this role requires a passion to continually improve processes and optimize inefficiencies.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Build Engineer",
                    "og:url": "https://jobs.lever.co/machinezone/182ff62a-657f-4178-a85c-1fa64918b019",
                    "twitter:description": "MZ Game Studio is seeking a highly skilled Senior Build and Tools Engineer to support its development teams and ensure their build pipelines are running as efficiently as possible. Build and Tools engineers work closely with both software engineers and product managers to provide build support from development to product release. Success in this role requires a passion to continually improve processes and optimize inefficiencies.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Build Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "MZ Game Studio is seeking a highly skilled Senior Build and Tools Engineer to ... \nExperience programming in C/C++, Lua, PHP, Obj-C, or Java; Experience with\u00a0...",
        "title": "MZ - Senior Build Engineer"
    },
    {
        "cacheId": "9pLUye6zw_QJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../750bd4ea-a345-45e0-9d05-1e3a181ffb83",
        "htmlFormattedUrl": "https://jobs.lever.co/.../750bd4ea-a345-45e0-9d05-1e3a181ffb83",
        "htmlSnippet": "... complex software/Linux faults. Within Dev Services we are looking for a <br>\nrelease <b>engineer</b> to support and enhance the build infrastructure for our Python/C<br>\n/<b>C++</b>&nbsp;...",
        "htmlTitle": "Rotor Studios - DevOps <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/rotorstudios/750bd4ea-a345-45e0-9d05-1e3a181ffb83",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b7a83a7a-b150-45de-8b3a-8eff1c0aa355-1472435524080.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "264",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS2zJP_ZPXE4_q0saDM8fhVyiZptw74UDUvJXr4X_ZyT0wUo3f9GND3qAM_",
                    "width": "191"
                }
            ],
            "metatags": [
                {
                    "og:description": "We\u2019re looking for an DEVOPS ENGINEER! The main focus of this role will be to work with developers and IT to ensure tool and support for version control, ticketing, build systems, software installation, testing infrastructure, code review, devops automation, database, authentication/authorisation, platform stacks, license policy and complex software/Linux faults. Within Dev Services we are looking for a release engineer to support and enhance the build infrastructure for our Python/C/C++.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b7a83a7a-b150-45de-8b3a-8eff1c0aa355-1472435524080.png",
                    "og:image:height": "200",
                    "og:title": "Rotor Studios - DevOps Engineer",
                    "og:url": "https://jobs.lever.co/rotorstudios/750bd4ea-a345-45e0-9d05-1e3a181ffb83",
                    "twitter:description": "We\u2019re looking for an DEVOPS ENGINEER! The main focus of this role will be to work with developers and IT to ensure tool and support for version control, ticketing, build systems, software installation, testing infrastructure, code review, devops automation, database, authentication/authorisation, platform stacks, license policy and complex software/Linux faults. Within Dev Services we are looking for a release engineer to support and enhance the build infrastructure for our Python/C/C++.",
                    "twitter:title": "Rotor Studios - DevOps Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... complex software/Linux faults. Within Dev Services we are looking for a \nrelease engineer to support and enhance the build infrastructure for our Python/C\n/C++\u00a0...",
        "title": "Rotor Studios - DevOps Engineer"
    },
    {
        "cacheId": "hvR82k33zE0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
        "htmlSnippet": "We&#39;re looking for a software <b>engineer</b> who gets why the story, &quot;I bought a sub <br>\nusing ... maintainable, scalable services in at least one of: Ruby/Rails, C/<b>C++</b>, Go.",
        "htmlTitle": "Twitch - Senior Software <b>Engineer</b> - Payments",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We're looking for a software engineer who gets why the story, \"I bought a sub using my favorite streamer's sub button so I can talk in sub-only chat\" starts off looking simple, but isn't. You like wrangling existing technologies together to solve business problems. Maybe you've built an e-commerce site or two. On our team, you'll specialize in payments and related products like emotes and Turbo. Together, we're transforming the gaming world, $4.99 at a time.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Payments",
                    "og:url": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
                    "twitter:description": "Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We're looking for a software engineer who gets why the story, \"I bought a sub using my favorite streamer's sub button so I can talk in sub-only chat\" starts off looking simple, but isn't. You like wrangling existing technologies together to solve business problems. Maybe you've built an e-commerce site or two. On our team, you'll specialize in payments and related products like emotes and Turbo. Together, we're transforming the gaming world, $4.99 at a time.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Payments",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for a software engineer who gets why the story, \"I bought a sub \nusing ... maintainable, scalable services in at least one of: Ruby/Rails, C/C++, Go.",
        "title": "Twitch - Senior Software Engineer - Payments"
    },
    {
        "cacheId": "J-A9ZrjA-cEJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a111c9b9-ddcd-4ea4-8d46-856041680367?...",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a111c9b9-ddcd-4ea4-8d46-856041680367?...",
        "htmlSnippet": "We&#39;re looking for an <b>engineer</b> capable of supporting the Operations team and ... <br>\nExperience with C, <b>C++</b>, as well as scripting languages such as Python, Bash,&nbsp;...",
        "htmlTitle": "Density - Manufacturing Test <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/density/a111c9b9-ddcd-4ea4-8d46-856041680367?lever-source=jobs",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/cdbcbd9e-c7b7-4c3b-80bc-9d00b5745d0f-1464905769165.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "113",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQASIuuji8_Hpnj07mP7tsiQcr38q4c0LvwTnz_vtmh579fZnmk5Yt_QQ",
                    "width": "445"
                }
            ],
            "metatags": [
                {
                    "og:description": "When someone installs Density in a location, they get access to real time, accurate people count. While the experience is magical to a customer, the process involved in accomplishing it is complex. Consistently delivering a high-quality product requires a well-devised and thoughtfully-implemented test strategy, and the Manufacturing Test Engineer is responsible for just that. We\u2019re looking for an engineer capable of supporting the Operations team and contract manufacturers in hardware bring-up, debug, validation and qualifying of new product functionalities, and releasing cost effective production test solutions into mass production. We\u2019re looking for someone with in-depth knowledge of the electronics SMT/TH assembly process and product manufacturability, as well as a strong grasp of embedded hardware systems architecture. If you\u2019re excited by developing and performing Lab and Mass Production intent type testing for various sensing-devices through characterization, calibration, and t",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/cdbcbd9e-c7b7-4c3b-80bc-9d00b5745d0f-1464905769165.png",
                    "og:image:height": "200",
                    "og:title": "Density - Manufacturing Test Engineer",
                    "og:url": "https://jobs.lever.co/density/a111c9b9-ddcd-4ea4-8d46-856041680367",
                    "twitter:description": "When someone installs Density in a location, they get access to real time, accurate people count. While the experience is magical to a customer, the process involved in accomplishing it is complex. Consistently delivering a high-quality product requires a well-devised and thoughtfully-implemented test strategy, and the Manufacturing Test Engineer is responsible for just that. We\u2019re looking for an engineer capable of supporting the Operations team and contract manufacturers in hardware bring-up, debug, validation and qualifying of new product functionalities, and releasing cost effective production test solutions into mass production. We\u2019re looking for someone with in-depth knowledge of the electronics SMT/TH assembly process and product manufacturability, as well as a strong grasp of embedded hardware systems architecture. If you\u2019re excited by developing and performing Lab and Mass Production intent type testing for various sensing-devices through characterization, calibration, and t",
                    "twitter:title": "Density - Manufacturing Test Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for an engineer capable of supporting the Operations team and ... \nExperience with C, C++, as well as scripting languages such as Python, Bash,\u00a0...",
        "title": "Density - Manufacturing Test Engineer"
    },
    {
        "cacheId": "NrvoAl61D5YJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../9804c73d-0b88-4ca5-8ad2-583776006acc",
        "htmlFormattedUrl": "https://jobs.lever.co/.../9804c73d-0b88-4ca5-8ad2-583776006acc",
        "htmlSnippet": "Expertise in C/<b>C++</b>, Python, Java, OpenGL. \u00b7 Experience in one or more of the <br>\nfollowing areas related to sensor fusion for ADAS and Autonomous Driving.",
        "htmlTitle": "Faraday Future - Sensor Fusion Algorithm <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/faradayfuture/9804c73d-0b88-4ca5-8ad2-583776006acc",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "200",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRMLgdzJ9p7OVcfhxA-sLzhziSZ3QW_QuFkRHJCamIy2dOxKa6cY27TAsw",
                    "width": "200"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Company: Faraday Future (FF) is a California-based mobility company, leveraging the latest technologies and world\u2019s best talent to realize exciting new possibilities in sustainable transportation. We\u2019re producing user-centric, technology-first vehicles to establish new paradigms in human-vehicle interaction. We\u2019re not just seeking to change how our cars work \u2013 we\u2019re seeking to change the way we drive. At FF, we\u2019re creating something new, something connected, and something with a global impact. Job Description \u00b7 This person will develop sensor fusion and object detection algorithms as part of the perception team for ADAS and Self-Driving in a very fast moving environment. Responsibilities \u00b7 Create, develop, invent, validate and integrate sensor fusion and object detection algorithms for autonomous vehicles. \u00b7 Generate intellectual property for the company. \u00b7 From the feature definitions and higher level requirements, develop engineering requirement",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1441842243319.png",
                    "og:image:height": "200",
                    "og:title": "Faraday Future - Sensor Fusion Algorithm Engineer",
                    "og:url": "https://jobs.lever.co/faradayfuture/9804c73d-0b88-4ca5-8ad2-583776006acc",
                    "twitter:description": "The Company: Faraday Future (FF) is a California-based mobility company, leveraging the latest technologies and world\u2019s best talent to realize exciting new possibilities in sustainable transportation. We\u2019re producing user-centric, technology-first vehicles to establish new paradigms in human-vehicle interaction. We\u2019re not just seeking to change how our cars work \u2013 we\u2019re seeking to change the way we drive. At FF, we\u2019re creating something new, something connected, and something with a global impact. Job Description \u00b7 This person will develop sensor fusion and object detection algorithms as part of the perception team for ADAS and Self-Driving in a very fast moving environment. Responsibilities \u00b7 Create, develop, invent, validate and integrate sensor fusion and object detection algorithms for autonomous vehicles. \u00b7 Generate intellectual property for the company. \u00b7 From the feature definitions and higher level requirements, develop engineering requirement",
                    "twitter:title": "Faraday Future - Sensor Fusion Algorithm Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Expertise in C/C++, Python, Java, OpenGL. \u00b7 Experience in one or more of the \nfollowing areas related to sensor fusion for ADAS and Autonomous Driving.",
        "title": "Faraday Future - Sensor Fusion Algorithm Engineer"
    },
    {
        "cacheId": "IBn3b-YbEocJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../cf1ffed7-0224-431a-8c19-ab4f2645423b",
        "htmlFormattedUrl": "https://jobs.lever.co/.../cf1ffed7-0224-431a-8c19-ab4f2645423b",
        "htmlSnippet": "As Lead Information Security <b>Engineer</b> you will help ensure that our software, <br>\nsystems, and ... Software development experience in C/<b>C++</b>, Java and/or PHP.",
        "htmlTitle": "HealthEngine - Lead Information Security <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/healthengine/cf1ffed7-0224-431a-8c19-ab4f2645423b",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e21f9af0-62d2-478c-a370-9d809e0fc948-1485230901032.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "160",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT6wAJLn1YZi03G5Z88nyzhlWT0PkpZgaIk4XFWElfG9es6CtFrjH-2F2Ip",
                    "width": "315"
                }
            ],
            "metatags": [
                {
                    "og:description": "HealthEngine is an established startup, and leading marketplace for health appointments in Australia. We believe there\u2019s no such thing as a \u201csafe system\u201d \u2014 only safer systems. Help us protect and harden computer systems and network devices against attack, and fulfil our mission to empower patients. As Lead Information Security Engineer you will help ensure that our software, systems, and integrations are designed and implemented to the highest security standards. Bonus if familiar with our tech stack: LAPP Stack (Linux, Apache, PostgreSQL, PHP), Javascript, AWS (EC2, S3, Redshift, Lambda), Git, Redis, Memcache, Varnish, ElasticSearch, Node.js, Ansible, Vagrant, Kibana. Leveraging your technical expertise you will: - Assess, understand, and communicate the risks associated with complex large-scale projects. - Work with engineers to design and build proactive methods to enhance our security posture. - Perform offensive security exercises to test security controls and detection capabil",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e21f9af0-62d2-478c-a370-9d809e0fc948-1485230901032.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "HealthEngine - Lead Information Security Engineer",
                    "og:url": "https://jobs.lever.co/healthengine/cf1ffed7-0224-431a-8c19-ab4f2645423b",
                    "twitter:description": "HealthEngine is an established startup, and leading marketplace for health appointments in Australia. We believe there\u2019s no such thing as a \u201csafe system\u201d \u2014 only safer systems. Help us protect and harden computer systems and network devices against attack, and fulfil our mission to empower patients. As Lead Information Security Engineer you will help ensure that our software, systems, and integrations are designed and implemented to the highest security standards. Bonus if familiar with our tech stack: LAPP Stack (Linux, Apache, PostgreSQL, PHP), Javascript, AWS (EC2, S3, Redshift, Lambda), Git, Redis, Memcache, Varnish, ElasticSearch, Node.js, Ansible, Vagrant, Kibana. Leveraging your technical expertise you will: - Assess, understand, and communicate the risks associated with complex large-scale projects. - Work with engineers to design and build proactive methods to enhance our security posture. - Perform offensive security exercises to test security controls and detection capabil",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e21f9af0-62d2-478c-a370-9d809e0fc948-1485230827682.png",
                    "twitter:title": "HealthEngine - Lead Information Security Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As Lead Information Security Engineer you will help ensure that our software, \nsystems, and ... Software development experience in C/C++, Java and/or PHP.",
        "title": "HealthEngine - Lead Information Security Engineer"
    },
    {
        "cacheId": "JBtUBl-NeH8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a5288360-8e81-40ba-9959-b6a1dd35313f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a5288360-8e81-40ba-9959-b6a1dd35313f",
        "htmlSnippet": "BioDigital is looking for a Full Stack <b>Engineer</b> to help build our flagship product, ... <br>\nPostgreSQL, HTML/CSS, JavaScript, C/<b>C++</b>, Objective C, Java, Angular JS&nbsp;...",
        "htmlTitle": "BioDigital - Full Stack <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/biodigital/a5288360-8e81-40ba-9959-b6a1dd35313f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/BioDigital_Logo.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "91",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCLp26ksVdUKG7uNAMNd7Ti3kjYjpmsP8reGNCbphrgZLsnDx67AiqdQ",
                    "width": "555"
                }
            ],
            "metatags": [
                {
                    "og:description": "BioDigital is revolutionizing the way people understand their health and the human body. The BioDigital Human is a comprehensive digital 3D human body accessible through the Web and mobile apps - think Google Earth meets the human body. Winner of the 2015 Webby for Health, the platform is being used by pharmaceutical companies, medical device manufacturers and publishers to translate complex medical concepts into educational tools that allow users to learn about anatomy, disease, and treatments in a manner that resembles life itself. This tight-knit team of engineers, 3D animators, scientists, and entrepreneurs is passionately working to transform health education. BioDigital is looking for a Full Stack Engineer to help build our flagship product, a cutting-edge 3D visualization platform, the BioDigital Human. The ideal candidate has extensive experience writing production-quality code, building and working with RESTful APIs, has worked in cloud based environments like AWS, likes be",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/BioDigital_Logo.png",
                    "og:image:height": "200",
                    "og:title": "BioDigital - Full Stack Engineer",
                    "og:url": "https://jobs.lever.co/biodigital/a5288360-8e81-40ba-9959-b6a1dd35313f",
                    "twitter:description": "BioDigital is revolutionizing the way people understand their health and the human body. The BioDigital Human is a comprehensive digital 3D human body accessible through the Web and mobile apps - think Google Earth meets the human body. Winner of the 2015 Webby for Health, the platform is being used by pharmaceutical companies, medical device manufacturers and publishers to translate complex medical concepts into educational tools that allow users to learn about anatomy, disease, and treatments in a manner that resembles life itself. This tight-knit team of engineers, 3D animators, scientists, and entrepreneurs is passionately working to transform health education. BioDigital is looking for a Full Stack Engineer to help build our flagship product, a cutting-edge 3D visualization platform, the BioDigital Human. The ideal candidate has extensive experience writing production-quality code, building and working with RESTful APIs, has worked in cloud based environments like AWS, likes be",
                    "twitter:title": "BioDigital - Full Stack Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "BioDigital is looking for a Full Stack Engineer to help build our flagship product, ... \nPostgreSQL, HTML/CSS, JavaScript, C/C++, Objective C, Java, Angular JS\u00a0...",
        "title": "BioDigital - Full Stack Engineer"
    },
    {
        "cacheId": "Tl98vMx9eLQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../564d8411-89c3-4009-b2e5-6901699d8527",
        "htmlFormattedUrl": "https://jobs.lever.co/.../564d8411-89c3-4009-b2e5-6901699d8527",
        "htmlSnippet": "We&#39;re looking for a skilled Senior Software <b>Engineer</b> to join our team. ... for <br>\nShaper Origin and future products using <b>C++</b>, Qt and QtQuick; Modify and <br>\nimprove&nbsp;...",
        "htmlTitle": "Shaper - Senior Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/shapertools/564d8411-89c3-4009-b2e5-6901699d8527",
        "pagemap": {
            "metatags": [
                {
                    "og:description": "Shaper is developing a revolutionary line of computer-augmented power tools, starting with a handheld CNC router called Origin. We're looking for a skilled Senior Software Engineer to join our team. You\u2019ll work on the platform and application that enables users to interact with their tools in dramatically new ways. You should be familiar with C/C++ development on Linux, and have knowledge of\u2014or be eager to learn\u2014the Qt toolkit.",
                    "og:image:height": "200",
                    "og:title": "Shaper - Senior Software Engineer",
                    "og:url": "https://jobs.lever.co/shapertools/564d8411-89c3-4009-b2e5-6901699d8527",
                    "twitter:description": "Shaper is developing a revolutionary line of computer-augmented power tools, starting with a handheld CNC router called Origin. We're looking for a skilled Senior Software Engineer to join our team. You\u2019ll work on the platform and application that enables users to interact with their tools in dramatically new ways. You should be familiar with C/C++ development on Linux, and have knowledge of\u2014or be eager to learn\u2014the Qt toolkit.",
                    "twitter:title": "Shaper - Senior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We're looking for a skilled Senior Software Engineer to join our team. ... for \nShaper Origin and future products using C++, Qt and QtQuick; Modify and \nimprove\u00a0...",
        "title": "Shaper - Senior Software Engineer"
    },
    {
        "cacheId": "-6iYVFOqe9wJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../657fc242-62b2-4d5c-a8f2-da8a17049ecd",
        "htmlFormattedUrl": "https://jobs.lever.co/.../657fc242-62b2-4d5c-a8f2-da8a17049ecd",
        "htmlSnippet": "Software <b>Engineer</b> - Computer Vision ... well architected code; High proficiency in <br>\n<b>C++</b>; Ability to thrive in a fast paced, collaborative, small team environment.",
        "htmlTitle": "Skydio - Software <b>Engineer</b> - Computer Vision",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/skydio/657fc242-62b2-4d5c-a8f2-da8a17049ecd",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1442970549235.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "143",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTankq7NzUBbv_kMxHiAbukQ9rrCLEdMMQ7tCZbhPPIRJvNjFewz_6W2wMM",
                    "width": "353"
                }
            ],
            "metatags": [
                {
                    "og:description": "The core of our system is the computer vision algorithms that allow drones to understand the world around them. You\u2019ll architect and implement the algorithms that run on every drone powered by Skydio as part of a world class computer vision team with researchers who have pushed the state of the art in academia and industry. We\u2019re looking for people who bring together an understanding of the relevant theory, solid software skills, and an ability to drive through to working solutions.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1442970549235.png",
                    "og:image:height": "200",
                    "og:title": "Skydio - Software Engineer - Computer Vision",
                    "og:url": "https://jobs.lever.co/skydio/657fc242-62b2-4d5c-a8f2-da8a17049ecd",
                    "twitter:description": "The core of our system is the computer vision algorithms that allow drones to understand the world around them. You\u2019ll architect and implement the algorithms that run on every drone powered by Skydio as part of a world class computer vision team with researchers who have pushed the state of the art in academia and industry. We\u2019re looking for people who bring together an understanding of the relevant theory, solid software skills, and an ability to drive through to working solutions.",
                    "twitter:title": "Skydio - Software Engineer - Computer Vision",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Software Engineer - Computer Vision ... well architected code; High proficiency in \nC++; Ability to thrive in a fast paced, collaborative, small team environment.",
        "title": "Skydio - Software Engineer - Computer Vision"
    },
    {
        "cacheId": "NQWMhDgMCqEJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../8796fa63-6750-401d-bb3f-d1c7f732f6b1",
        "htmlFormattedUrl": "https://jobs.lever.co/.../8796fa63-6750-401d-bb3f-d1c7f732f6b1",
        "htmlSnippet": "We are seeking a Software <b>Engineer</b> with a generalist/fullstack orientation to join <br>\n... languages: Python/Django, C/<b>C++</b>, Java, JavaScript, Ruby/Ruby on Rails.",
        "htmlTitle": "Capsule - Full Stack <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/capsulecares/8796fa63-6750-401d-bb3f-d1c7f732f6b1",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/74ba5341-4657-4551-94e1-b24af4cfbc48-1463287177215.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "132",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjk7SCjqJB1LzDFYZShu_aR1rYY6SY6ltpevFVa7xuZ3YWYC_9lx7xKLKa",
                    "width": "320"
                }
            ],
            "metatags": [
                {
                    "og:description": "Capsule is a healthcare technology company reconnecting medication to the healthcare system. We are rebuilding the $425bn pharmacy industry from the inside out \u2013 the things you see and the things you don\u2019t see. Our team makes the same promise to each other as the one we\u2019ve made to our customers: everybody needs some looking after sometimes. We're the type of team that is there to lend a helping hand to each other. We\u2019ll never lose sight of the fact that behind all of the complexity of healthcare we\u2019re just people looking after other people. We\u2019re a relentlessly positive and optimistic crew, looking for other passionate, curious, and resourceful people. If you\u2019re a data-driven long-term thinker and you think you can help lead Capsule as we build an iconic and enduring brand, we want to hear from you. Capsule is backed by Thrive Capital and some of the most successful healthcare executives in the country. Our investors have also backed Instagram, Oscar Health, Warby Parker, Harry\u2019s",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/74ba5341-4657-4551-94e1-b24af4cfbc48-1463287177215.png",
                    "og:image:height": "200",
                    "og:title": "Capsule - Full Stack Engineer",
                    "og:url": "https://jobs.lever.co/capsulecares/8796fa63-6750-401d-bb3f-d1c7f732f6b1",
                    "twitter:description": "Capsule is a healthcare technology company reconnecting medication to the healthcare system. We are rebuilding the $425bn pharmacy industry from the inside out \u2013 the things you see and the things you don\u2019t see. Our team makes the same promise to each other as the one we\u2019ve made to our customers: everybody needs some looking after sometimes. We're the type of team that is there to lend a helping hand to each other. We\u2019ll never lose sight of the fact that behind all of the complexity of healthcare we\u2019re just people looking after other people. We\u2019re a relentlessly positive and optimistic crew, looking for other passionate, curious, and resourceful people. If you\u2019re a data-driven long-term thinker and you think you can help lead Capsule as we build an iconic and enduring brand, we want to hear from you. Capsule is backed by Thrive Capital and some of the most successful healthcare executives in the country. Our investors have also backed Instagram, Oscar Health, Warby Parker, Harry\u2019s",
                    "twitter:title": "Capsule - Full Stack Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are seeking a Software Engineer with a generalist/fullstack orientation to join \n... languages: Python/Django, C/C++, Java, JavaScript, Ruby/Ruby on Rails.",
        "title": "Capsule - Full Stack Engineer"
    },
    {
        "cacheId": "KKk1mIgltLMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
        "htmlSnippet": "Twitch&#39;s Video Client <b>Engineering</b> team is looking for experienced video <br>\n<b>engineers</b> ... Strong background in C/<b>C++</b>; Experience with multithreaded <br>\nprogramming,&nbsp;...",
        "htmlTitle": "Twitch - Senior Software <b>Engineer</b> - Video Client",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch\u2019s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Video Client",
                    "og:url": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
                    "twitter:description": "Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch\u2019s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Video Client",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Twitch's Video Client Engineering team is looking for experienced video \nengineers ... Strong background in C/C++; Experience with multithreaded \nprogramming,\u00a0...",
        "title": "Twitch - Senior Software Engineer - Video Client"
    },
    {
        "cacheId": "Ve1u_Yt6ARcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../3cf89af8-21c0-4463-a1d3-21f04c1254bf",
        "htmlFormattedUrl": "https://jobs.lever.co/.../3cf89af8-21c0-4463-a1d3-21f04c1254bf",
        "htmlSnippet": "The Senior Site Reliability <b>Engineer</b> plays a major role across the Operations <br>\nteam ... programming mastery across a variety of languages (Python, PHP, C/<b>C++</b><br>\n,&nbsp;...",
        "htmlTitle": "MZ - Senior Site Reliability <b>Engineer</b> - <b>Engineering</b> Operations",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/machinezone/3cf89af8-21c0-4463-a1d3-21f04c1254bf",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "177",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDWgKB_LCHNiqBB0pybCPEuN7snsRTE2ug9whJHxN4YYsoVumtnkXOPb8P",
                    "width": "284"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Senior Site Reliability Engineer plays a major role across the Operations team and MZ overall. You\u2019ll be tasked with maintaining our complex infrastructure and optimizing our environment for maximum uptime. You\u2019ll also monitor and build out our systems to ensure health and scalability in a fast paced environment and you\u2019ll have a strong say in our infrastructure decisions moving forward. This is your chance to be a part of mobile history!",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873753963.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "MZ - Senior Site Reliability Engineer - Engineering Operations",
                    "og:url": "https://jobs.lever.co/machinezone/3cf89af8-21c0-4463-a1d3-21f04c1254bf",
                    "twitter:description": "The Senior Site Reliability Engineer plays a major role across the Operations team and MZ overall. You\u2019ll be tasked with maintaining our complex infrastructure and optimizing our environment for maximum uptime. You\u2019ll also monitor and build out our systems to ensure health and scalability in a fast paced environment and you\u2019ll have a strong say in our infrastructure decisions moving forward. This is your chance to be a part of mobile history!",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/52dab9d9-2c7a-4c87-91f6-eb8555ae268d-1494873744080.png",
                    "twitter:title": "MZ - Senior Site Reliability Engineer - Engineering Operations",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The Senior Site Reliability Engineer plays a major role across the Operations \nteam ... programming mastery across a variety of languages (Python, PHP, C/C++\n,\u00a0...",
        "title": "MZ - Senior Site Reliability Engineer - Engineering Operations"
    },
    {
        "cacheId": "ujXW9reMdCoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
        "htmlSnippet": "As a Senior Software <b>Engineer</b> in Test for Core Payments team, you will be <br>\nworking ... level in one or more of the following language: Go, Ruby, Java, C/<b>C++</b><br>\n&nbsp;...",
        "htmlTitle": "Twitch - Senior Quality <b>Engineer</b> - Core Payments",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Quality Engineer - Core Payments",
                    "og:url": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
                    "twitter:description": "Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Quality Engineer - Core Payments",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Senior Software Engineer in Test for Core Payments team, you will be \nworking ... level in one or more of the following language: Go, Ruby, Java, C/C++\n\u00a0...",
        "title": "Twitch - Senior Quality Engineer - Core Payments"
    },
    {
        "cacheId": "eCviBu15kwMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/be52afaa-e86e-4f0d-966e-1fe9fbff8366",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/be52afaa-e86e-4f0d-966e-1fe9fbff8366",
        "htmlSnippet": "Twitch&#39;s Video Client <b>Engineering</b> team is looking for experienced iOS and video <br>\n... Strong background in C/<b>C++</b>; Experience with multithreaded programming,&nbsp;...",
        "htmlTitle": "Twitch - Software <b>Engineer</b> - iOS Video Client",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/be52afaa-e86e-4f0d-966e-1fe9fbff8366",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is building the future of interactive entertainment, and video is at the very core of that vision. Twitch\u2019s Video Client Engineering team is looking for experienced iOS and video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As an video engineer on the iOS platform, you will be helping shape the future of the Twitch playback experience used by millions of users on all the iOS devices. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Software Engineer - iOS Video Client",
                    "og:url": "https://jobs.lever.co/twitch/be52afaa-e86e-4f0d-966e-1fe9fbff8366",
                    "twitter:description": "Twitch is building the future of interactive entertainment, and video is at the very core of that vision. Twitch\u2019s Video Client Engineering team is looking for experienced iOS and video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As an video engineer on the iOS platform, you will be helping shape the future of the Twitch playback experience used by millions of users on all the iOS devices. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Software Engineer - iOS Video Client",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Twitch's Video Client Engineering team is looking for experienced iOS and video \n... Strong background in C/C++; Experience with multithreaded programming,\u00a0...",
        "title": "Twitch - Software Engineer - iOS Video Client"
    },
    {
        "cacheId": "M2jEpYDr-sIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../7af8f796-e956-4438-8607-ebc63b9c2d2f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../7af8f796-e956-4438-8607-ebc63b9c2d2f",
        "htmlSnippet": "\ufeffWe are seeking extraordinarily talented <b>engineers</b> with a passion for ... <br>\nconcurrency, and correctness using programming languages such as: C/<b>C++</b>, <br>\nJava, Go,&nbsp;...",
        "htmlTitle": "The Voleon Group - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/voleon/7af8f796-e956-4438-8607-ebc63b9c2d2f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "153",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6",
                    "width": "330"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are seeking extraordinarily talented engineers with a passion for developing well-designed software systems that scale and can be easily maintained. You should be a self-starter who can gather project requirements, translate them into a rational software design, reason effectively about supporting or dependent technologies, and communicate effectively with teammates. Our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png",
                    "og:image:height": "200",
                    "og:title": "The Voleon Group - Software Engineer",
                    "og:url": "https://jobs.lever.co/voleon/7af8f796-e956-4438-8607-ebc63b9c2d2f",
                    "twitter:description": "We are seeking extraordinarily talented engineers with a passion for developing well-designed software systems that scale and can be easily maintained. You should be a self-starter who can gather project requirements, translate them into a rational software design, reason effectively about supporting or dependent technologies, and communicate effectively with teammates. Our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development.",
                    "twitter:title": "The Voleon Group - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are seeking extraordinarily talented engineers with a passion for ... \nconcurrency, and correctness using programming languages such as: C/C++, \nJava, Go,\u00a0...",
        "title": "The Voleon Group - Software Engineer"
    },
    {
        "cacheId": "NoKjweCRrhsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../7a2cf40e-ab26-4b14-ae1d-0919625816ce",
        "htmlFormattedUrl": "https://jobs.lever.co/.../7a2cf40e-ab26-4b14-ae1d-0919625816ce",
        "htmlSnippet": "As a Software <b>Engineer</b> you will build products for human-driven analysis of real-<br>\nworld ... Proficiency with programming languages such as Java, <b>C++</b>, Python,&nbsp;...",
        "htmlTitle": "Palantir Technologies - Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/palantir/7a2cf40e-ab26-4b14-ae1d-0919625816ce",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b8300af6-ed1c-4d0b-8956-cee7839555b9-1461255924321.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "A World-Changing Company At Palantir, we\u2019re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us. The Role Our engineers are involved in all parts of the product lifecycle: idea generation, design, prototyping, planning, execution, and shipping. Our work starts with brainstorming to discover, explore, and understand our customer\u2019s greatest challenges in the visual and technical spaces. Then we code. A lot. Finally, we continuously ship and iterate on products that have a direct impact on some of the world\u2019s hardest problems. As a Software Engineer you will build products for human-driven analysis of real-world data. These products must handle messy data at scale, all while ma",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b8300af6-ed1c-4d0b-8956-cee7839555b9-1461255924321.png",
                    "og:image:height": "200",
                    "og:title": "Palantir Technologies - Software Engineer",
                    "og:url": "https://jobs.lever.co/palantir/7a2cf40e-ab26-4b14-ae1d-0919625816ce",
                    "twitter:description": "A World-Changing Company At Palantir, we\u2019re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us. The Role Our engineers are involved in all parts of the product lifecycle: idea generation, design, prototyping, planning, execution, and shipping. Our work starts with brainstorming to discover, explore, and understand our customer\u2019s greatest challenges in the visual and technical spaces. Then we code. A lot. Finally, we continuously ship and iterate on products that have a direct impact on some of the world\u2019s hardest problems. As a Software Engineer you will build products for human-driven analysis of real-world data. These products must handle messy data at scale, all while ma",
                    "twitter:title": "Palantir Technologies - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Software Engineer you will build products for human-driven analysis of real-\nworld ... Proficiency with programming languages such as Java, C++, Python,\u00a0...",
        "title": "Palantir Technologies - Software Engineer"
    },
    {
        "cacheId": "Pj0bG0XtXqYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/zee.../7213de0d-ad6c-4106-b3d6-269574c99fd3",
        "htmlFormattedUrl": "https://jobs.lever.co/zee.../7213de0d-ad6c-4106-b3d6-269574c99fd3",
        "htmlSnippet": "We are actively building a team of world-class <b>engineers</b> who have ... with ARM <br>\nprocessors); C and <b>C++</b>, and some scripting language (Python, Go, etc.)&nbsp;...",
        "htmlTitle": "Zee.Aero - Embedded Software <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/zee.aero/7213de0d-ad6c-4106-b3d6-269574c99fd3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/8028f167-fc4a-4972-9c43-74b8e1e9966c-1467765900798.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "181",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS17zAYCSZ5xqyVqXy5w6ZGPMQoWA45F7qqikYm6xe-ar7GUr4ijle159s",
                    "width": "164"
                }
            ],
            "metatags": [
                {
                    "og:description": "Zee Aero, a division of Kitty Hawk, is developing revolutionary aircraft concepts, working at the intersection of aerodynamics, advanced manufacturing, and electric propulsion. We are actively building a team of world-class engineers who have experience in fields ranging from power electronics to aerodynamics. We are currently seeking software engineers to join our software and avionics group, which builds the core fly-by-wire-system that controls our aircraft. You are mission driven and comfortable working in a small team, with an audacious, loosely-specified plan. You will chip in to do anything and everything to advance our mission as quickly as possible. You figure out what needs to be done, check assumptions, and do it. You are passionate about writing flight code and also about improving our development processes. What is most important is a stated track record and passion for learning. This position is based in Mountain View, CA, but you will have the option to work from our",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/8028f167-fc4a-4972-9c43-74b8e1e9966c-1467765900798.png",
                    "og:image:height": "200",
                    "og:title": "Zee.Aero - Embedded Software Engineer",
                    "og:url": "https://jobs.lever.co/zee.aero/7213de0d-ad6c-4106-b3d6-269574c99fd3",
                    "twitter:description": "Zee Aero, a division of Kitty Hawk, is developing revolutionary aircraft concepts, working at the intersection of aerodynamics, advanced manufacturing, and electric propulsion. We are actively building a team of world-class engineers who have experience in fields ranging from power electronics to aerodynamics. We are currently seeking software engineers to join our software and avionics group, which builds the core fly-by-wire-system that controls our aircraft. You are mission driven and comfortable working in a small team, with an audacious, loosely-specified plan. You will chip in to do anything and everything to advance our mission as quickly as possible. You figure out what needs to be done, check assumptions, and do it. You are passionate about writing flight code and also about improving our development processes. What is most important is a stated track record and passion for learning. This position is based in Mountain View, CA, but you will have the option to work from our",
                    "twitter:title": "Zee.Aero - Embedded Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are actively building a team of world-class engineers who have ... with ARM \nprocessors); C and C++, and some scripting language (Python, Go, etc.)\u00a0...",
        "title": "Zee.Aero - Embedded Software Engineer"
    },
    {
        "cacheId": "2WW3uQvLSr8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../fbf6927c-901d-416e-a3b7-48626d95b04c",
        "htmlFormattedUrl": "https://jobs.lever.co/.../fbf6927c-901d-416e-a3b7-48626d95b04c",
        "htmlSnippet": "Data <b>Engineer</b> - Senior Consultant - Chicago. Chicago, IL. SL : Data <b>Engineering</b> <br>\n... Programming / Scripting (Python, Java, C/<b>C++</b>, Scala, Bash, Korn Shell)&nbsp;...",
        "htmlTitle": "Clarity Insights - Data <b>Engineer</b> - Senior Consultant - Chicago",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/clarity/fbf6927c-901d-416e-a3b7-48626d95b04c",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3cfbb468-6115-4780-ac48-fed6e10cf617-1491245257573.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "176",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkbyDJfNDNNJNICXL-QVoXFwE8jyTaHlUXFKFOykYnFfTM7hBoUuiYWwW9",
                    "width": "287"
                }
            ],
            "metatags": [
                {
                    "og:description": "Do you have a passion for data? Clarity Insights is a leading professional services firm focused exclusively on data and analytics. We own our solutions, providing business and technology landscape review, gap analysis, and go-forward strategy for our clients, in addition to implementing the future-state vision. We are... \u2022 The Industry-recognized data and analytics leaders \u2022 Passionate problem solvers across a broad spectrum of technologies and industries \u2022 Value seekers for measurable business outcomes \u2022 Continuous learners through training and education \u2022 Focused on a work-life balance with an unlimited paid time off policy Data engineers are challenged with building the next generation of data solutions for many of the most high-profile and technologically-advanced organizations nationally. Our engagements typically target a variety of use cases across data engineering, data science, data governance, and visualization.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3cfbb468-6115-4780-ac48-fed6e10cf617-1491245257573.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Clarity Insights - Data Engineer - Senior Consultant - Chicago",
                    "og:url": "https://jobs.lever.co/clarity/fbf6927c-901d-416e-a3b7-48626d95b04c",
                    "twitter:description": "Do you have a passion for data? Clarity Insights is a leading professional services firm focused exclusively on data and analytics. We own our solutions, providing business and technology landscape review, gap analysis, and go-forward strategy for our clients, in addition to implementing the future-state vision. We are... \u2022 The Industry-recognized data and analytics leaders \u2022 Passionate problem solvers across a broad spectrum of technologies and industries \u2022 Value seekers for measurable business outcomes \u2022 Continuous learners through training and education \u2022 Focused on a work-life balance with an unlimited paid time off policy Data engineers are challenged with building the next generation of data solutions for many of the most high-profile and technologically-advanced organizations nationally. Our engagements typically target a variety of use cases across data engineering, data science, data governance, and visualization.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3cfbb468-6115-4780-ac48-fed6e10cf617-1489788229451.png",
                    "twitter:title": "Clarity Insights - Data Engineer - Senior Consultant - Chicago",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Data Engineer - Senior Consultant - Chicago. Chicago, IL. SL : Data Engineering \n... Programming / Scripting (Python, Java, C/C++, Scala, Bash, Korn Shell)\u00a0...",
        "title": "Clarity Insights - Data Engineer - Senior Consultant - Chicago"
    },
    {
        "cacheId": "-6ppDHOSvn4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/hike/2d9fbb37-0946-412c-a7f7-7ef7395d92de",
        "htmlFormattedUrl": "https://jobs.lever.co/hike/2d9fbb37-0946-412c-a7f7-7ef7395d92de",
        "htmlSnippet": "At Hike, the job of a <b>Engineering</b> Manager goes beyond just development. <br>\n<b>Engineering</b> ... Programming experience in either Java, Objective-C or <b>C++</b>.",
        "htmlTitle": "hike - <b>Engineering</b> Manager",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/hike/2d9fbb37-0946-412c-a7f7-7ef7395d92de",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f6d4e595-0ca3-4bd9-afd7-ec9512b619c5-1460349403303.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "105",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTdqTu4o196XHLwuur6glsmW3OBeVl8jib0iRqwD2rRQH9Yw7agmtOPJg",
                    "width": "479"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Hike, the job of a Engineering Manager goes beyond just development. Engineering Managers not only provide core engineering leadership to major projects, but also manage a team of engineers. You not only optimise your own code but make sure engineers are able to optimise theirs. As a Lead Engineering Manager you manage your project goals, contribute to product strategy and help develop the organisation in a deeper sense. Engineering teams work all across the company, in multiple areas areas such as information retrieval, large-scale system design, networking, searching and ranking, machine learning, natural language processing, user interface design; the list goes on and is growing every day. Operating with scale and speed, our software engineers are just getting started -- and as a manager, you guide the way. You will lead the Stickers team at Hike As the Lead Engineering Manager, you work on the full stack and own several major feature tracks. You will also be responsible for wor",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f6d4e595-0ca3-4bd9-afd7-ec9512b619c5-1460349403303.png",
                    "og:image:height": "200",
                    "og:title": "hike - Engineering Manager",
                    "og:url": "https://jobs.lever.co/hike/2d9fbb37-0946-412c-a7f7-7ef7395d92de",
                    "twitter:description": "At Hike, the job of a Engineering Manager goes beyond just development. Engineering Managers not only provide core engineering leadership to major projects, but also manage a team of engineers. You not only optimise your own code but make sure engineers are able to optimise theirs. As a Lead Engineering Manager you manage your project goals, contribute to product strategy and help develop the organisation in a deeper sense. Engineering teams work all across the company, in multiple areas areas such as information retrieval, large-scale system design, networking, searching and ranking, machine learning, natural language processing, user interface design; the list goes on and is growing every day. Operating with scale and speed, our software engineers are just getting started -- and as a manager, you guide the way. You will lead the Stickers team at Hike As the Lead Engineering Manager, you work on the full stack and own several major feature tracks. You will also be responsible for wor",
                    "twitter:title": "hike - Engineering Manager",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "At Hike, the job of a Engineering Manager goes beyond just development. \nEngineering ... Programming experience in either Java, Objective-C or C++.",
        "title": "hike - Engineering Manager"
    },
    {
        "cacheId": "lfts3iC_kBMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/daqri.../7364133f-879f-489b-9006-36a3f391c699",
        "htmlFormattedUrl": "https://jobs.lever.co/daqri.../7364133f-879f-489b-9006-36a3f391c699",
        "htmlSnippet": "As the Electrical <b>Engineer</b> you will apply research to the planning, design, ... 3-5 <br>\nyears of programming experience in MATLAB, C, <b>C++</b>, or PCB layout tools.",
        "htmlTitle": "DAQRI - Electrical <b>Engineer</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/daqri.com/7364133f-879f-489b-9006-36a3f391c699",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/31b5a499-c665-4126-824c-bf71b8bf2f18-1502387035271.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "162",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSQPsjCjJo300gVB9BbQeMkLHrlvuumWlcwdsp7OxsT2Ft1jHPsUmRF32_k",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "Our current project is to create LiDAR using our software defined light. As the Electrical Engineer you will apply research to the planning, design, development, and testing of electromechanical systems and instruments. Your work will include but not limited to: research, planning, testing and data analysis. You will be responsible for system level design and management of novel LiDAR applications.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31b5a499-c665-4126-824c-bf71b8bf2f18-1502387035271.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "DAQRI - Electrical Engineer",
                    "og:url": "https://jobs.lever.co/daqri.com/7364133f-879f-489b-9006-36a3f391c699",
                    "twitter:description": "Our current project is to create LiDAR using our software defined light. As the Electrical Engineer you will apply research to the planning, design, development, and testing of electromechanical systems and instruments. Your work will include but not limited to: research, planning, testing and data analysis. You will be responsible for system level design and management of novel LiDAR applications.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31b5a499-c665-4126-824c-bf71b8bf2f18-1499980215880.png",
                    "twitter:title": "DAQRI - Electrical Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As the Electrical Engineer you will apply research to the planning, design, ... 3-5 \nyears of programming experience in MATLAB, C, C++, or PCB layout tools.",
        "title": "DAQRI - Electrical Engineer"
    }
]

# #local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

#Post GSE query
# def get_job_listings_from_google(number_of_listings_to_get = 100):
#     return_value = []
#     for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#         return_value.extend(do_google_search(
#             # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#             search_term='site:jobs.lever.co go engineer',
#             api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
#             num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#             # start=1))
#             start=search_result_number_from_which_api_query_results_start))
#     return return_value[:number_of_listings_to_get]

def save_gse_call_results(listings):
    with open('finalResults.txt','a+') as f:
        f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
                indent = 4))

def send_job_listings_to_codeforcash(listings):
    for listing in range(len(listings)):
        data_to_send_in_request_body = {
            "key": CODEFORCASH_API_KEY,
            "title": listings[listing]["title"],
            "website": listings[listing]["link"],
            # "description": listings[listing]["snippet"],
            "description": "",
            "utc_datetime": datetime.datetime.utcnow().isoformat(),
            "lat": "",
            "lng": "",
            "country": "",
            "employment_type": "",
            "remote_ok": "",
            "time_commitment": ""
        }
        data_send_job_lisitings_to_codeforcash = json.dumps(data_to_send_in_request_body)
        data_of_each_listing = json.loads(data_send_job_lisitings_to_codeforcash)

        try:
            html = urllib.request.urlopen(data_of_each_listing["website"]).read()
        except urllib.error.HTTPError as e:
            print(e)
        else:
            only_tag_class = SoupStrainer("div", {"class" : "section-wrapper page-full-width"})
            soup = BeautifulSoup(html, "html.parser", parse_only=only_tag_class)
            htmlDecode = soup.encode('utf-8').decode('utf-8', 'ignore')
            
            f = open('Lynx.htm','w')
            try:
                f.write(htmlDecode)
            except:
                print('POTENTIAL ENCODE ERROR')
            f.close()

            #refactor as functions
            web_data = ''
            cmd = 'lynx -dump -width 1024 -nolist -notitle \"{0}\"'.format('./Lynx.htm')
            lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            web_data = lynx.stdout.read()
            web_data = web_data.decode('utf-8', 'replace')

            #test print url and lynx formatted description
            print(data_of_each_listing["website"], web_data)            

            data_to_send_in_request_body["description"] = web_data

            for data_key in data_to_send_in_request_body:
                # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8').decode('utf-8')
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            #test print json formatted complete listing
            print(data_to_send_in_request_body)

        # post to c4c    
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        
        with open('responseFromCodeforcash','ab+') as f:
            pickle.dump(response_per_post, f)
if
 __name__ == '__main__':
    save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
