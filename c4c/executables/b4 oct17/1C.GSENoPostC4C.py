import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
import re
import subprocess
from googleapiclient.discovery import build 
from itertools import repeat
from unidecode import unidecode
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import Request, urlopen


AVAILABLE_TOKEN_SETS = {
    'ess': {
        'api_key': 'AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc',
        'cse_id': '009043117829057268965:tgiqlni9v2w'
    },
    'ssk': {
        'api_key': 'AIzaSyAn_YOSbC43zmv2cexCddaIYfJfMb9d08s',
        'cse_id': '003565523015477317201:lwtcnf2u57i'
    }
}

NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'ess'

API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY = 10

CSE_SEARCH_TERM_PREFIX = 'engineer software site:jobs.lever.co/'

# clients = ['brightedge']
# clients = ['brightedge', 'voleon']
clients = ['brightedge', 'blendlabs', 'voleon']

# def pass_different_clients():
#     for client in clients:
#         cse_search_term = CSE_SEARCH_TERM_PREFIX + client
#         print(cse_search_term)
#         get_job_listings_from_google(cse_search_term)


# def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     # print(res['items'])
#     print(res['queries']['request'][0]['totalResults'])
#     return res['items']

results_from_GSE_query = [
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - Software Engineer',
    'htmlTitle': 'The Voleon Group - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/voleon/7af8f796-e956-4438-8607-ebc63b9c2d2f',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are seeking extraordinarily talented engineers with a passion for developing \nwell-designed software systems that scale and can be easily maintained.',
    'htmlSnippet': '\ufeffWe are seeking extraordinarily talented <b>engineers</b> with a passion for developing <br>\nwell-designed <b>software</b> systems that scale and can be easily maintained.',
    'cacheId': 'M2jEpYDr-sIJ',
    'formattedUrl': 'https://jobs.lever.co/.../7af8f796-e956-4438-8607-ebc63b9c2d2f',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../7af8f796-e956-4438-8607-ebc63b9c2d2f',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - Software Engineer',
          'twitter:description': "We are seeking extraordinarily talented engineers with a passion for developing well-designed software systems that scale and can be easily maintained. You should be a self-starter who can gather project requirements, translate them into a rational software design, reason effectively about supporting or dependent technologies, and communicate effectively with teammates. Our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development.",
          'og:title': 'The Voleon Group - Software Engineer',
          'og:description': "We are seeking extraordinarily talented engineers with a passion for developing well-designed software systems that scale and can be easily maintained. You should be a self-starter who can gather project requirements, translate them into a rational software design, reason effectively about supporting or dependent technologies, and communicate effectively with teammates. Our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development.",
          'og:url': 'https://jobs.lever.co/voleon/7af8f796-e956-4438-8607-ebc63b9c2d2f',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - Senior Software Engineer',
    'htmlTitle': 'The Voleon Group - Senior <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/voleon/a4453137-a5c4-4811-886d-d53f7bb6bfbb',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are seeking extraordinary engineers with a proven track record of writing \ncorrect, well designed software, solving difficult problems, and delivering \ncomplex\xa0...',
    'htmlSnippet': 'We are seeking extraordinary <b>engineers</b> with a proven track record of writing <br>\ncorrect, well designed <b>software</b>, solving difficult problems, and delivering <br>\ncomplex&nbsp;...',
    'cacheId': 'l94gPBhsUUwJ',
    'formattedUrl': 'https://jobs.lever.co/.../a4453137-a5c4-4811-886d-d53f7bb6bfbb',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../a4453137-a5c4-4811-886d-d53f7bb6bfbb',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - Senior Software Engineer',
          'twitter:description': "We are seeking extraordinary engineers with a proven track record of writing correct, well designed software, solving difficult problems, and delivering complex projects on time. You should preferably have experience designing and implementing fault-tolerant distributed systems. Experience with building large-scale data infrastructure, stream processing systems, or latency-sensitive programs is a bonus. Successful candidates will possess superior problem solving skills, a strong grasp of CS fundamentals, and solid engineering instincts. Our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development. Required Skills and Qualifications: · Bachelor's degree in Computer Science or related technical discipline (i.e. Physics, M",
          'og:title': 'The Voleon Group - Senior Software Engineer',
          'og:description': "We are seeking extraordinary engineers with a proven track record of writing correct, well designed software, solving difficult problems, and delivering complex projects on time. You should preferably have experience designing and implementing fault-tolerant distributed systems. Experience with building large-scale data infrastructure, stream processing systems, or latency-sensitive programs is a bonus. Successful candidates will possess superior problem solving skills, a strong grasp of CS fundamentals, and solid engineering instincts. Our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development. Required Skills and Qualifications: · Bachelor's degree in Computer Science or related technical discipline (i.e. Physics, M",
          'og:url': 'https://jobs.lever.co/voleon/a4453137-a5c4-4811-886d-d53f7bb6bfbb',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - Senior Software Engineer',
    'htmlTitle': 'The Voleon Group - Senior <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/voleon/a4453137-a5c4-4811-886d-d53f7bb6bfbb/apply',
    'displayLink': 'jobs.lever.co',
    'snippet': "Senior Software Engineer. Berkeley. Software. Full-time. Submit your application. \nResume/CV ✱. ATTACH RESUME/CV. Couldn't auto-read resume. Analyzing\xa0...",
    'htmlSnippet': 'Senior <b>Software Engineer</b>. Berkeley. <b>Software</b>. Full-time. Submit your application. <br>\nResume/CV ✱. ATTACH RESUME/CV. Couldn&#39;t auto-read resume. Analyzing&nbsp;...',
    'cacheId': 'ZaW8BdQFiJ0J',
    'formattedUrl': 'https://jobs.lever.co/voleon/a4453137-a5c4-4811-886d.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/a4453137-a5c4-4811-886d.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - Senior Software Engineer',
          'twitter:description': "We are seeking extraordinary engineers with a proven track record of writing correct, well designed software, solving difficult problems, and delivering complex projects on time. You should preferably have experience designing and implementing fault-tolerant distributed systems. Experience with building large-scale data infrastructure, stream processing systems, or latency-sensitive programs is a bonus. Successful candidates will possess superior problem solving skills, a strong grasp of CS fundamentals, and solid engineering instincts. As a key part of our growing success, our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development. Required Skills and Qualifications: · Bachelor's degree in Computer Science or related",
          'og:title': 'The Voleon Group - Senior Software Engineer',
          'og:description': "We are seeking extraordinary engineers with a proven track record of writing correct, well designed software, solving difficult problems, and delivering complex projects on time. You should preferably have experience designing and implementing fault-tolerant distributed systems. Experience with building large-scale data infrastructure, stream processing systems, or latency-sensitive programs is a bonus. Successful candidates will possess superior problem solving skills, a strong grasp of CS fundamentals, and solid engineering instincts. As a key part of our growing success, our software engineering team has developed and continues to innovate on a variety of cutting-edge technologies and supporting infrastructure. Some examples would include, but aren't limited to, our trading infrastructure; efficient, distributed computing and data processing; and a flexible pipeline for model development. Required Skills and Qualifications: · Bachelor's degree in Computer Science or related",
          'og:url': 'https://jobs.lever.co/voleon/a4453137-a5c4-4811-886d-d53f7bb6bfbb/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - DevOps Engineer',
    'htmlTitle': 'The Voleon Group - DevOps <b>Engineer</b>',
    'link': 'https://jobs.lever.co/voleon/7a4a4939-b56c-4376-9c0b-b6a68e68efab',
    'displayLink': 'jobs.lever.co',
    'snippet': 'The DevOps Engineer will work with the software engineering, research, and IT \nteams to ensure that the software we create is of high quality and is deployed\xa0...',
    'htmlSnippet': 'The DevOps <b>Engineer</b> will work with the <b>software engineering</b>, research, and IT <br>\nteams to ensure that the <b>software</b> we create is of high quality and is deployed&nbsp;...',
    'cacheId': 'fOENfnus8pQJ',
    'formattedUrl': 'https://jobs.lever.co/.../7a4a4939-b56c-4376-9c0b-b6a68e68efab',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../7a4a4939-b56c-4376-9c0b-b6a68e68efab',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - DevOps Engineer',
          'twitter:description': "The DevOps Engineer will work with the software engineering, research, and IT teams to ensure that the software we create is of high quality and is deployed and supported in an efficient and reproducible way. You will support Voleon's build processes and continuous delivery tools, manage software development tools, and automate systems and operations.",
          'og:title': 'The Voleon Group - DevOps Engineer',
          'og:description': "The DevOps Engineer will work with the software engineering, research, and IT teams to ensure that the software we create is of high quality and is deployed and supported in an efficient and reproducible way. You will support Voleon's build processes and continuous delivery tools, manage software development tools, and automate systems and operations.",
          'og:url': 'https://jobs.lever.co/voleon/7a4a4939-b56c-4376-9c0b-b6a68e68efab',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'DevOps Engineer. BerkeleyITFull-time. Legal. Apply · Legal Counsel ... Senior \nSoftware Engineer. BerkeleySoftwareFull-time · Apply · Software Engineer.',
    'htmlSnippet': 'DevOps <b>Engineer</b>. BerkeleyITFull-time. Legal. Apply &middot; Legal Counsel ... Senior <br>\n<b>Software Engineer</b>. Berkeley<b>Software</b>Full-time &middot; Apply &middot; <b>Software Engineer</b>.',
    'cacheId': 'GWZahajiYo0J',
    'formattedUrl': 'https://jobs.lever.co/voleon/',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=commitment&location=Berkeley',
    'displayLink': 'jobs.lever.co',
    'snippet': 'DevOps Engineer. BerkeleyITFull-time · Apply · Equities Trading Supervisor ... \nSenior Software Engineer. BerkeleySoftwareFull-time · Apply · Software Engineer\n.',
    'htmlSnippet': 'DevOps <b>Engineer</b>. BerkeleyITFull-time &middot; Apply &middot; Equities Trading Supervisor ... <br>\nSenior <b>Software Engineer</b>. Berkeley<b>Software</b>Full-time &middot; Apply &middot; <b>Software Engineer</b><br>\n.',
    'cacheId': 'vwxGrcIojrkJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&location=Berkeley',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&amp;location=Berkeley',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - Equities Trading Supervisor',
    'htmlTitle': 'The Voleon Group - Equities Trading Supervisor',
    'link': 'https://jobs.lever.co/voleon/4900a95d-22c4-4b4f-a071-76ed7b15a253',
    'displayLink': 'jobs.lever.co',
    'snippet': 'The trading staff collaborates with the research and software teams to improve ... \nand provide insight on equities markets to researchers and software engineers.',
    'htmlSnippet': 'The trading staff collaborates with the research and <b>software</b> teams to improve ... <br>\nand provide insight on equities markets to researchers and <b>software engineers</b>.',
    'cacheId': 'Tue-lajZIsgJ',
    'formattedUrl': 'https://jobs.lever.co/.../4900a95d-22c4-4b4f-a071-76ed7b15a253',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../4900a95d-22c4-4b4f-a071-76ed7b15a253',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - Equities Trading Supervisor',
          'twitter:description': 'We are a science-driven systematic trading firm, built on the principle that statistical machine learning provides the best solutions to the scientific problems we must solve. The trading staff collaborates with the research and software teams to improve execution and implement new trading strategies. We are looking for a candidate to supervise our systematic trading program in the U.S. and European equities markets. A trading supervisor monitors high-volume execution algorithms and portfolio risk while tracking real-time market developments. The supervisor will become an expert in market microstructure and provide insight on equities markets to researchers and software engineers. A self-motivated and inquisitive personality is required. The firm’s operations are built on proprietary software, so a desire to take initiative will provide the opportunity for advancement and to improve the existing systems. While this role is based out of our Berkeley offices, it requires working Europ',
          'og:title': 'The Voleon Group - Equities Trading Supervisor',
          'og:description': 'We are a science-driven systematic trading firm, built on the principle that statistical machine learning provides the best solutions to the scientific problems we must solve. The trading staff collaborates with the research and software teams to improve execution and implement new trading strategies. We are looking for a candidate to supervise our systematic trading program in the U.S. and European equities markets. A trading supervisor monitors high-volume execution algorithms and portfolio risk while tracking real-time market developments. The supervisor will become an expert in market microstructure and provide insight on equities markets to researchers and software engineers. A self-motivated and inquisitive personality is required. The firm’s operations are built on proprietary software, so a desire to take initiative will provide the opportunity for advancement and to improve the existing systems. While this role is based out of our Berkeley offices, it requires working Europ',
          'og:url': 'https://jobs.lever.co/voleon/4900a95d-22c4-4b4f-a071-76ed7b15a253',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?team=Software',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Senior Software Engineer. BerkeleySoftwareFull-time · Apply · Software Engineer\n. BerkeleySoftwareFull-time · The Voleon Group Home Page · Jobs powered\xa0...',
    'htmlSnippet': 'Senior <b>Software Engineer</b>. Berkeley<b>Software</b>Full-time &middot; Apply &middot; <b>Software Engineer</b><br>\n. Berkeley<b>Software</b>Full-time &middot; The Voleon Group Home Page &middot; Jobs powered&nbsp;...',
    'cacheId': '3el_veO5F_0J',
    'formattedUrl': 'https://jobs.lever.co/voleon/?team=Software',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?team=<b>Software</b>',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - Fund Accountant',
    'htmlTitle': 'The Voleon Group - Fund Accountant',
    'link': 'https://jobs.lever.co/voleon/da1525cc-4161-4399-a813-d7a08f3e5d27',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Experience working with enterprise-level accounting software and developing \nefficient, automated processes. Ability to produce complete, accurate, and\xa0...',
    'htmlSnippet': 'Experience working with enterprise-level accounting <b>software</b> and developing <br>\nefficient, automated processes. Ability to produce complete, accurate, and&nbsp;...',
    'cacheId': 'ErOAhE-bI9IJ',
    'formattedUrl': 'https://jobs.lever.co/.../da1525cc-4161-4399-a813-d7a08f3e5d27',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../da1525cc-4161-4399-a813-d7a08f3e5d27',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - Fund Accountant',
          'twitter:description': 'We are seeking an exceptionally passionate and detail-oriented finance professional to serve as a Fund Accountant. Reporting to the Director of Finance and collaborating with compliance, reporting, and investor relations, the Fund Accountant will maintain the accuracy of the financial books and records of our investment funds across multiple asset classes and geographies. Working closely with our service providers and ensuring policies and internal control standards are being followed, you will be responsible for developing and monitoring daily/monthly reconciliations between internal records, prime brokers/counterparties, banks, and fund administrator; properly booking accruals, transactions, and entries in the internal accounting system; production of monthly Net Asset Value and allocation packages, including calculations of management and incentive fees; and general fund finance operations, including paying expenses, assisting in the margin call process, confirming settlement activ',
          'og:title': 'The Voleon Group - Fund Accountant',
          'og:description': 'We are seeking an exceptionally passionate and detail-oriented finance professional to serve as a Fund Accountant. Reporting to the Director of Finance and collaborating with compliance, reporting, and investor relations, the Fund Accountant will maintain the accuracy of the financial books and records of our investment funds across multiple asset classes and geographies. Working closely with our service providers and ensuring policies and internal control standards are being followed, you will be responsible for developing and monitoring daily/monthly reconciliations between internal records, prime brokers/counterparties, banks, and fund administrator; properly booking accruals, transactions, and entries in the internal accounting system; production of monthly Net Asset Value and allocation packages, including calculations of management and incentive fees; and general fund finance operations, including paying expenses, assisting in the margin call process, confirming settlement activ',
          'og:url': 'https://jobs.lever.co/voleon/da1525cc-4161-4399-a813-d7a08f3e5d27',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group - Member of Research Staff',
    'htmlTitle': 'The Voleon Group - Member of Research Staff',
    'link': 'https://jobs.lever.co/voleon/1f654a56-1ae9-4529-bc75-2f7699642495',
    'displayLink': 'jobs.lever.co',
    'snippet': '... engineering, or operations research, then we encourage you to contact us. ... \nProgramming experience and interest in software development techniques.',
    'htmlSnippet': '... <b>engineering</b>, or operations research, then we encourage you to contact us. ... <br>\nProgramming experience and interest in <b>software</b> development techniques.',
    'cacheId': 'KXk9vApoVpMJ',
    'formattedUrl': 'https://jobs.lever.co/.../1f654a56-1ae9-4529-bc75-2f7699642495',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../1f654a56-1ae9-4529-bc75-2f7699642495',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group - Member of Research Staff',
          'twitter:description': "As Voleon continues to grow, we are actively seeking world-class machine learning scientists, statisticians, and technical innovators to join our ranks. Join us in developing predictive models and other components of automated trading systems. You will be at the forefront of modern statistical machine learning innovation, applying novel research to large, high-dimensional data sets. The work will range from data preparation to model development to production software implementation. Voleon employees are smart, driven, and curious. We hire top performers from university programs as well as talented professionals from academia and industry. While many of our employees are already leaders in their fields, they have a thirst for innovation and are driven to creatively solve complex problems. Teamwork is paramount at Voleon, and maintaining a collaborative and collegial culture is central to our company's philosophy. We hire on the basis of exceptional talent. If you excel in a technical",
          'og:title': 'The Voleon Group - Member of Research Staff',
          'og:description': "As Voleon continues to grow, we are actively seeking world-class machine learning scientists, statisticians, and technical innovators to join our ranks. Join us in developing predictive models and other components of automated trading systems. You will be at the forefront of modern statistical machine learning innovation, applying novel research to large, high-dimensional data sets. The work will range from data preparation to model development to production software implementation. Voleon employees are smart, driven, and curious. We hire top performers from university programs as well as talented professionals from academia and industry. While many of our employees are already leaders in their fields, they have a thirst for innovation and are driven to creatively solve complex problems. Teamwork is paramount at Voleon, and maintaining a collaborative and collegial culture is central to our company's philosophy. We hire on the basis of exceptional talent. If you excel in a technical",
          'og:url': 'https://jobs.lever.co/voleon/1f654a56-1ae9-4529-bc75-2f7699642495',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?team=Recruiting',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Recruiting. All · Finance/Operations · IT · Legal · \nRecruiting · RnD · Software · Trading. Commitment. All · Full-time. Recruiting. \nApply\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Recruiting. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; <br>\nRecruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Recruiting. <br>\nApply&nbsp;...',
    'cacheId': '566mUM8svZkJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?team=Recruiting',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?team=Recruiting',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=location&team=RnD',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. RnD. All · Finance/Operations · IT · Legal · Recruiting \n· RnD · Software · Trading. Commitment. All · Full-time. Berkeley. Apply\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. RnD. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; Recruiting <br>\n&middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Berkeley. Apply&nbsp;...',
    'cacheId': 'wsg4oD3ZKIQJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=location&team=RnD',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=location&amp;team=RnD',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=location&team=Recruiting',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Recruiting. All · Finance/Operations · IT · Legal · \nRecruiting · RnD · Software · Trading. Commitment. All · Full-time. Berkeley. Apply\n\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Recruiting. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; <br>\nRecruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Berkeley. Apply<br>\n&nbsp;...',
    'cacheId': '7A4egqL0LHMJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=location&team=Recruiting',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=location&amp;team=Recruiting',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?team=Legal',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Legal. All · Finance/Operations · IT · Legal · \nRecruiting · RnD · Software · Trading. Commitment. All · Full-time. Legal. Apply\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Legal. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; <br>\nRecruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Legal. Apply&nbsp;...',
    'cacheId': '2ZsOZxKJwlgJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?team=Legal',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?team=Legal',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=commitment&team=RnD',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. RnD. All · Finance/Operations · IT · Legal · Recruiting \n· RnD · Software · Trading. Commitment. All · Full-time. Full-time. Apply\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. RnD. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; Recruiting <br>\n&middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Full-time. Apply&nbsp;...',
    'cacheId': 'QYFgPB6kb1UJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&team=RnD',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&amp;team=RnD',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=location&team=Finance%2FOperations',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Finance/Operations. All · Finance/Operations · IT · \nLegal · Recruiting · RnD · Software · Trading. Commitment. All · Full-time. \nBerkeley.',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Finance/Operations. All &middot; Finance/Operations &middot; IT &middot; <br>\nLegal &middot; Recruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. <br>\nBerkeley.',
    'cacheId': 'edoJ5u0OUEkJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=location&team...',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=location&amp;team...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=commitment&team=Finance%2FOperations',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Finance/Operations. All · Finance/Operations · IT · \nLegal · Recruiting · RnD · Software · Trading. Commitment. All · Full-time. Full-\ntime.',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Finance/Operations. All &middot; Finance/Operations &middot; IT &middot; <br>\nLegal &middot; Recruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Full-<br>\ntime.',
    'cacheId': 'dMr8TEtJnTIJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&team...',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&amp;team...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?team=Finance%2FOperations',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Finance/Operations. All · Finance/Operations · IT · Legal · Recruiting · RnD · \nSoftware · Trading. Commitment. All · Full-time. Finance/Operations. Apply\xa0...',
    'htmlSnippet': 'Finance/Operations. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; Recruiting &middot; RnD &middot; <br>\n<b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Finance/Operations. Apply&nbsp;...',
    'cacheId': 'fgupQyIa0CgJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?team=Finance%2FOperations',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?team=Finance%2FOperations',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=commitment&team=Legal',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Legal. All · Finance/Operations · IT · Legal · \nRecruiting · RnD · Software · Trading. Commitment. All · Full-time. Full-time. Apply\n\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Legal. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; <br>\nRecruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Full-time. Apply<br>\n&nbsp;...',
    'cacheId': 'dhQnQADMryMJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&team=Legal',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&amp;team=Legal',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=commitment&team=Recruiting',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Recruiting. All · Finance/Operations · IT · Legal · \nRecruiting · RnD · Software · Trading. Commitment. All · Full-time. Full-time. Apply\n\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Recruiting. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; <br>\nRecruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Full-time. Apply<br>\n&nbsp;...',
    'cacheId': '2jfsfLFurhgJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&team=Recruiting',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=commitment&amp;team=Recruiting',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?team=RnD',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. RnD. All · Finance/Operations · IT · Legal · Recruiting \n· RnD · Software · Trading. Commitment. All · Full-time. RnD. Apply\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. RnD. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; Recruiting <br>\n&middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. RnD. Apply&nbsp;...',
    'cacheId': 'LOydGchPDwkJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?team=RnD',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?team=RnD',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'The Voleon Group',
    'htmlTitle': 'The Voleon Group',
    'link': 'https://jobs.lever.co/voleon/?by=location&team=Legal',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Filter by: City. All · Berkeley. Legal. All · Finance/Operations · IT · Legal · \nRecruiting · RnD · Software · Trading. Commitment. All · Full-time. Berkeley. Apply\n\xa0...',
    'htmlSnippet': 'Filter by: City. All &middot; Berkeley. Legal. All &middot; Finance/Operations &middot; IT &middot; Legal &middot; <br>\nRecruiting &middot; RnD &middot; <b>Software</b> &middot; Trading. Commitment. All &middot; Full-time. Berkeley. Apply<br>\n&nbsp;...',
    'cacheId': 'q_O_fKfmKwgJ',
    'formattedUrl': 'https://jobs.lever.co/voleon/?by=location&team=Legal',
    'htmlFormattedUrl': 'https://jobs.lever.co/voleon/?by=location&amp;team=Legal',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '330',
          'height': '153',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTZowYJxkXz0fGDTvVqF2dr_IRAFQFr9KSz425qnmsoB3xPmMArC2Rzvpp6'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'The Voleon Group',
          'twitter:description': 'Job openings at The Voleon Group',
          'og:title': 'The Voleon Group jobs',
          'og:description': 'Job openings at The Voleon Group',
          'og:url': 'https://jobs.lever.co/voleon',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/3b9df4d1-8342-4deb-8976-b664c5d59682-1460752797439.png'
        }
      ]
    }
  }
]

# #local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

# def get_job_listings_from_google(cse_search_term, number_of_listings_to_get = 100):
#     return_value = []
#     try:
#         for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#             return_value.extend(do_google_search(
#                 # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#                 # 'site:jobs.lever.co "c++" +engineer'
#                 search_term=cse_search_term,
#                 api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN, num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#                 # start=1))
#                 start=search_result_number_from_which_api_query_results_start))
#     except:
#         pass
#     print(return_value[:number_of_listings_to_get])
#     return return_value[:number_of_listings_to_get]

# def save_gse_call_results(listings):
#     with open('finalResults.txt','a+') as f:
#         f.write(json.dumps(get_job_listings_from_google()), sort_keys = True,
#                 indent = 4)

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
            print(data_of_each_listing["website"])
            print(web_data)

            data_to_send_in_request_body["description"] = web_data

            for data_key in data_to_send_in_request_body:
                # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8').decode('utf-8')
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            #test print json formatted complete listing
            print(data_to_send_in_request_body)
    
        # response_per_post = requests.post(
        #     url=CODEFORCASH_BASE_URL+'/api/metum/create',
        #     data=data_to_send_in_request_body)
        
        # with open('responseFromCodeforcash','ab+') as f:
        #     pickle.dump(response_per_post, f)

if __name__ == '__main__':
    send_job_listings_to_codeforcash(get_job_listings_from_google())
    # send_job_listings_to_codeforcash(pass_different_clients())
    
    # get_job_listings_from_google(pass_different_clients())
    
    # save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google(pass_different_clients())))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
