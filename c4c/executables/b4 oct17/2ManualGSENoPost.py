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
# clients = ['brightedge', 'blendlabs', 'voleon']

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
    'title': 'Blend - Software Engineer - Customer Integrations',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - Customer Integrations',
    'link': 'https://jobs.lever.co/blendlabs/39352b26-1e12-4e64-9971-9f5464d43d9e',
    'displayLink': 'jobs.lever.co',
    'snippet': "At Blend, we're dedicated to improving lending. We are a financial technology \ncompany with a product that affects the most important purchase most people will\n\xa0...",
    'htmlSnippet': 'At Blend, we&#39;re dedicated to improving lending. We are a financial technology <br>\ncompany with a product that affects the most important purchase most people will<br>\n&nbsp;...',
    'cacheId': 'ATsAbjJ6cggJ',
    'formattedUrl': 'https://jobs.lever.co/.../39352b26-1e12-4e64-9971-9f5464d43d9e',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../39352b26-1e12-4e64-9971-9f5464d43d9e',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - Customer Integrations',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We are a financial technology company with a product that affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product provides a clear and guided path to a new home, and for lenders, it streamlines their work process, enabling employees to spend more time assisting customers, rather than performing repetitive or manual tasks. By aligning and modernizing the mortgage industry, and consumer finance more generally, we believe everybody wins. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area— it affects people all over the U.S., not to mention a foundational part of the U.S. economy. We’re looking for talented software developers who are driven to understand how complex systems work and enjoy solving challenging problems to join our diverse and growing team. As a Software Engineer on our Client Integrations team, you will be respo',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - Customer Integrations',
          'og:description': 'At Blend, we’re dedicated to improving lending. We are a financial technology company with a product that affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product provides a clear and guided path to a new home, and for lenders, it streamlines their work process, enabling employees to spend more time assisting customers, rather than performing repetitive or manual tasks. By aligning and modernizing the mortgage industry, and consumer finance more generally, we believe everybody wins. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area— it affects people all over the U.S., not to mention a foundational part of the U.S. economy. We’re looking for talented software developers who are driven to understand how complex systems work and enjoy solving challenging problems to join our diverse and growing team. As a Software Engineer on our Client Integrations team, you will be respo',
          'og:url': 'https://jobs.lever.co/blendlabs/39352b26-1e12-4e64-9971-9f5464d43d9e',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer',
    'htmlTitle': 'Blend - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/blendlabs/ecccb3f7-d3d7-41fb-b2fb-32352c578813',
    'displayLink': 'jobs.lever.co',
    'snippet': "At Blend, we're dedicated to improving lending. We're an enterprise technology \ncompany, but our product affects the most important purchase most people will\xa0...",
    'htmlSnippet': 'At Blend, we&#39;re dedicated to improving lending. We&#39;re an enterprise technology <br>\ncompany, but our product affects the most important purchase most people will&nbsp;...',
    'cacheId': 'GFMVjP3SiB4J',
    'formattedUrl': 'https://jobs.lever.co/.../ecccb3f7-d3d7-41fb-b2fb-32352c578813',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../ecccb3f7-d3d7-41fb-b2fb-32352c578813',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. We’re looking for talented software engineers to join our diverse and fast-growing engineering team. As a',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. We’re looking for talented software engineers to join our diverse and fast-growing engineering team. As a',
          'og:url': 'https://jobs.lever.co/blendlabs/ecccb3f7-d3d7-41fb-b2fb-32352c578813',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer - Security',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - Security',
    'link': 'https://jobs.lever.co/blendlabs/2490113b-ccc0-496a-86fc-ee70d6948249',
    'displayLink': 'jobs.lever.co',
    'snippet': "At Blend, we're dedicated to improving lending. We're an enterprise technology \ncompany, but our product affects the most important purchase most people will\xa0...",
    'htmlSnippet': 'At Blend, we&#39;re dedicated to improving lending. We&#39;re an enterprise technology <br>\ncompany, but our product affects the most important purchase most people will&nbsp;...',
    'cacheId': 'xVhTRHxTzGQJ',
    'formattedUrl': 'https://jobs.lever.co/.../2490113b-ccc0-496a-86fc-ee70d6948249',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../2490113b-ccc0-496a-86fc-ee70d6948249',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - Security',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. At Blend, Security Engineers are software engineers who focus on security (no security experience required',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - Security',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. At Blend, Security Engineers are software engineers who focus on security (no security experience required',
          'og:url': 'https://jobs.lever.co/blendlabs/2490113b-ccc0-496a-86fc-ee70d6948249',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer - QA Automation',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - QA Automation',
    'link': 'https://jobs.lever.co/blendlabs/15ab8eae-1793-46ff-a7d9-3a3d86e3240c',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Software Engineer - QA Automation. San Francisco. Engineering ... As a QA \nAutomation Engineer you will work with QA and Engineering to design, \nimplement,\xa0...',
    'htmlSnippet': '<b>Software Engineer</b> - QA Automation. San Francisco. <b>Engineering</b> ... As a QA <br>\nAutomation <b>Engineer</b> you will work with QA and <b>Engineering</b> to design, <br>\nimplement,&nbsp;...',
    'cacheId': 'JxoU--s65DMJ',
    'formattedUrl': 'https://jobs.lever.co/.../15ab8eae-1793-46ff-a7d9-3a3d86e3240c',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../15ab8eae-1793-46ff-a7d9-3a3d86e3240c',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - QA Automation',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. As a QA Automation Engineer you will work with QA and Engineering to design, implement, and grow the tests',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - QA Automation',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. As a QA Automation Engineer you will work with QA and Engineering to design, implement, and grow the tests',
          'og:url': 'https://jobs.lever.co/blendlabs/15ab8eae-1793-46ff-a7d9-3a3d86e3240c',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer - Infrastructure',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - Infrastructure',
    'link': 'https://jobs.lever.co/blendlabs/65f01c7d-290c-4759-8bd1-c1a4cc39e32f',
    'displayLink': 'jobs.lever.co',
    'snippet': "We need someone who's driven to solve hard problems—the harder the better. \nWe're motivated by the fact that our product won't just affect the lives of a few\xa0...",
    'htmlSnippet': 'We need someone who&#39;s driven to solve hard problems—the harder the better. <br>\nWe&#39;re motivated by the fact that our product won&#39;t just affect the lives of a few&nbsp;...',
    'cacheId': 'JTzqfBPDjEoJ',
    'formattedUrl': 'https://jobs.lever.co/.../65f01c7d-290c-4759-8bd1-c1a4cc39e32f',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../65f01c7d-290c-4759-8bd1-c1a4cc39e32f',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - Infrastructure',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is solving significant infrastructure challenges as we expand from processing thousands to millions',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - Infrastructure',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is solving significant infrastructure challenges as we expand from processing thousands to millions',
          'og:url': 'https://jobs.lever.co/blendlabs/65f01c7d-290c-4759-8bd1-c1a4cc39e32f',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer - Applications Specialist',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - Applications Specialist',
    'link': 'https://jobs.lever.co/blendlabs/9ba069e4-088e-4840-bf04-dbc0db5cddd0',
    'displayLink': 'jobs.lever.co',
    'snippet': "At Blend, we're dedicated to improving lending. We are a financial technology \ncompany with a product that affects the most important purchase most people will\n\xa0...",
    'htmlSnippet': 'At Blend, we&#39;re dedicated to improving lending. We are a financial technology <br>\ncompany with a product that affects the most important purchase most people will<br>\n&nbsp;...',
    'cacheId': 'b5auSVlZgkkJ',
    'formattedUrl': 'https://jobs.lever.co/.../9ba069e4-088e-4840-bf04-dbc0db5cddd0',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../9ba069e4-088e-4840-bf04-dbc0db5cddd0',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - Applications Specialist',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We are a financial technology company with a product that affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product provides a clear and guided path to a new home, and for lenders, it streamlines their work process, enabling employees to spend more time assisting customers, rather than performing repetitive or manual tasks. By aligning and modernizing the mortgage industry, and consumer finance more generally, we believe everybody wins. We’re looking for talented software developers, analysts, and scientists, who are driven to understand how complex systems work and who enjoy solving challenging problems to join our diverse and fast-growing engineering team. As an Applications Engineer, you will be responsible for the end to end technical implementation of new features, understanding the business logic of our product, developing a broad base of knowledge about the information that',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - Applications Specialist',
          'og:description': 'At Blend, we’re dedicated to improving lending. We are a financial technology company with a product that affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product provides a clear and guided path to a new home, and for lenders, it streamlines their work process, enabling employees to spend more time assisting customers, rather than performing repetitive or manual tasks. By aligning and modernizing the mortgage industry, and consumer finance more generally, we believe everybody wins. We’re looking for talented software developers, analysts, and scientists, who are driven to understand how complex systems work and who enjoy solving challenging problems to join our diverse and fast-growing engineering team. As an Applications Engineer, you will be responsible for the end to end technical implementation of new features, understanding the business logic of our product, developing a broad base of knowledge about the information that',
          'og:url': 'https://jobs.lever.co/blendlabs/9ba069e4-088e-4840-bf04-dbc0db5cddd0',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer - IT',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - IT',
    'link': 'https://jobs.lever.co/blendlabs/1b59bf97-8997-4f33-a643-b98ccdf957a3',
    'displayLink': 'jobs.lever.co',
    'snippet': "At Blend, we're dedicated to improving lending. We're an enterprise technology \ncompany, and our product affects the most important purchase most people will\xa0...",
    'htmlSnippet': 'At Blend, we&#39;re dedicated to improving lending. We&#39;re an enterprise technology <br>\ncompany, and our product affects the most important purchase most people will&nbsp;...',
    'cacheId': 'mw63zP05pPIJ',
    'formattedUrl': 'https://jobs.lever.co/.../1b59bf97-8997-4f33-a643-b98ccdf957a3',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../1b59bf97-8997-4f33-a643-b98ccdf957a3',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - IT',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, and our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that automate repetitive tasks and let employees spend their time helping customers. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is seeking an IT Engineer who can develop and implement an identity and access management system. This includes',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - IT',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, and our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that automate repetitive tasks and let employees spend their time helping customers. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is seeking an IT Engineer who can develop and implement an identity and access management system. This includes',
          'og:url': 'https://jobs.lever.co/blendlabs/1b59bf97-8997-4f33-a643-b98ccdf957a3',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Software Engineer - Infrastructure',
    'htmlTitle': 'Blend - <b>Software Engineer</b> - Infrastructure',
    'link': 'https://jobs.lever.co/blendlabs/65f01c7d-290c-4759-8bd1-c1a4cc39e32f/apply',
    'displayLink': 'jobs.lever.co',
    'snippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). Our company values diversity.',
    'htmlSnippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). Our company values diversity.',
    'cacheId': 'n_K1vW8NjkkJ',
    'formattedUrl': 'https://jobs.lever.co/blendlabs/65f01c7d-290c-4759-8bd1.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/blendlabs/65f01c7d-290c-4759-8bd1.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Software Engineer - Infrastructure',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is solving significant infrastructure challenges as we expand from processing thousands to millions',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Software Engineer - Infrastructure',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is solving significant infrastructure challenges as we expand from processing thousands to millions',
          'og:url': 'https://jobs.lever.co/blendlabs/65f01c7d-290c-4759-8bd1-c1a4cc39e32f/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Solutions Engineer',
    'htmlTitle': 'Blend - Solutions <b>Engineer</b>',
    'link': 'https://jobs.lever.co/blendlabs/8b497735-06da-4097-932e-9d6c468f5246',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As a Solutions Engineer on our Integrations team, you will be responsible for ... \nLead/Engineer, Partner Engineer, Solution Architect, Software Consultant,\xa0...',
    'htmlSnippet': 'As a Solutions <b>Engineer</b> on our Integrations team, you will be responsible for ... <br>\nLead/<b>Engineer</b>, Partner <b>Engineer</b>, Solution Architect, <b>Software</b> Consultant,&nbsp;...',
    'cacheId': 'hSzmlhEPMHYJ',
    'formattedUrl': 'https://jobs.lever.co/.../8b497735-06da-4097-932e-9d6c468f5246',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../8b497735-06da-4097-932e-9d6c468f5246',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Solutions Engineer',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area— it affects people all over the U.S., not to mention a foundational part of the U.S. economy. We’re looking for talented technical integration leads who are driven to understand how complex systems work and enjoy utilizing a consultative approach to solve challenging problems. As a Solutions Engineer on our Integrations team, you will be responsible for end-to-end technical implementation of the Blend plat',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Solutions Engineer',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area— it affects people all over the U.S., not to mention a foundational part of the U.S. economy. We’re looking for talented technical integration leads who are driven to understand how complex systems work and enjoy utilizing a consultative approach to solve challenging problems. As a Solutions Engineer on our Integrations team, you will be responsible for end-to-end technical implementation of the Blend plat',
          'og:url': 'https://jobs.lever.co/blendlabs/8b497735-06da-4097-932e-9d6c468f5246',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Data Engineer',
    'htmlTitle': 'Blend - Data <b>Engineer</b>',
    'link': 'https://jobs.lever.co/blendlabs/4863a428-9036-4cba-a749-4187dd4048d1',
    'displayLink': 'jobs.lever.co',
    'snippet': "We're looking for a Data Engineer who is driven to solve hard problems— the \nharder, the better. We're motivated by the fact that our product won't just affect the\n\xa0...",
    'htmlSnippet': 'We&#39;re looking for a Data <b>Engineer</b> who is driven to solve hard problems— the <br>\nharder, the better. We&#39;re motivated by the fact that our product won&#39;t just affect the<br>\n&nbsp;...',
    'cacheId': 'AuaDPtOuSzcJ',
    'formattedUrl': 'https://jobs.lever.co/.../4863a428-9036-4cba-a749-4187dd4048d1',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../4863a428-9036-4cba-a749-4187dd4048d1',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Data Engineer',
          'twitter:description': "At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We're looking for a Data Engineer who is driven to solve hard problems— the harder, the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area— it affects people all over the U.S., not to mention a foundational part of the U.S. economy. As an early Data Engineer, you can define how we instrument our data infrastructure to influence the entire industry. Your contributions to Blend’s data architecture and infrastructure will shape the company’s ability to",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Data Engineer',
          'og:description': "At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We're looking for a Data Engineer who is driven to solve hard problems— the harder, the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area— it affects people all over the U.S., not to mention a foundational part of the U.S. economy. As an early Data Engineer, you can define how we instrument our data infrastructure to influence the entire industry. Your contributions to Blend’s data architecture and infrastructure will shape the company’s ability to",
          'og:url': 'https://jobs.lever.co/blendlabs/4863a428-9036-4cba-a749-4187dd4048d1',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Security Engineering Manager',
    'htmlTitle': 'Blend - Security <b>Engineering</b> Manager',
    'link': 'https://jobs.lever.co/blendlabs/446e9ce4-9265-43bc-bab5-ad4e256020ee',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Blend is seeking an Security Engineering Manager to mentor and grow the ... \npeople manager who can mentor a team of 8+ engineers; Hands on software\xa0...',
    'htmlSnippet': 'Blend is seeking an Security <b>Engineering</b> Manager to mentor and grow the ... <br>\npeople manager who can mentor a team of 8+ <b>engineers</b>; Hands on <b>software</b>&nbsp;...',
    'cacheId': '6MsgGz1CInYJ',
    'formattedUrl': 'https://jobs.lever.co/.../446e9ce4-9265-43bc-bab5-ad4e256020ee',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../446e9ce4-9265-43bc-bab5-ad4e256020ee',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Security Engineering Manager',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, and our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that automate repetitive tasks and let employees spend their time helping customers. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is seeking an Security Engineering Manager to mentor and grow the information security engineering team. Blend’',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Security Engineering Manager',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, and our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that automate repetitive tasks and let employees spend their time helping customers. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. Blend is seeking an Security Engineering Manager to mentor and grow the information security engineering team. Blend’',
          'og:url': 'https://jobs.lever.co/blendlabs/446e9ce4-9265-43bc-bab5-ad4e256020ee',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Sales Engineer (East)',
    'htmlTitle': 'Blend - Sales <b>Engineer</b> (East)',
    'link': 'https://jobs.lever.co/blendlabs/8945512c-a9d8-4c56-9080-d27eeb2324dd',
    'displayLink': 'jobs.lever.co',
    'snippet': "As a Sales Engineer, you'll be an instrumental part of the sales team at Blend. ... \n2+ years in a similar client-facing role at an enterprise software company; World\xa0...",
    'htmlSnippet': 'As a Sales <b>Engineer</b>, you&#39;ll be an instrumental part of the sales team at Blend. ... <br>\n2+ years in a similar client-facing role at an enterprise <b>software</b> company; World&nbsp;...',
    'cacheId': 'DMQ6gw6tFg8J',
    'formattedUrl': 'https://jobs.lever.co/.../8945512c-a9d8-4c56-9080-d27eeb2324dd',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../8945512c-a9d8-4c56-9080-d27eeb2324dd',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Sales Engineer (East)',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. As a Sales Engineer, you’ll be an instrumental part of the sales team at Blend. You will leverage strong t',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Sales Engineer (East)',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. As a Sales Engineer, you’ll be an instrumental part of the sales team at Blend. You will leverage strong t',
          'og:url': 'https://jobs.lever.co/blendlabs/8945512c-a9d8-4c56-9080-d27eeb2324dd',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Deployment Lead',
    'htmlTitle': 'Blend - Deployment Lead',
    'link': 'https://jobs.lever.co/blendlabs/46aec184-6bae-4b56-b88b-49f6e26adca8',
    'displayLink': 'jobs.lever.co',
    'snippet': '... Manager, Forward Deployed Engineer, Client Solutions or Professional \nServices Lead) ... 5+ years relevant experience with full lifecycle package \nsoftware\xa0...',
    'htmlSnippet': '... Manager, Forward Deployed <b>Engineer</b>, Client Solutions or Professional <br>\nServices Lead) ... 5+ years relevant experience with full lifecycle package <br>\n<b>software</b>&nbsp;...',
    'cacheId': 'A0vzAYEFp9MJ',
    'formattedUrl': 'https://jobs.lever.co/.../46aec184-6bae-4b56-b88b-49f6e26adca8',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../46aec184-6bae-4b56-b88b-49f6e26adca8',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Deployment Lead',
          'twitter:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. As a Deployment Lead, you will understand Blend’s platform and the client’s needs to help deliver a soluti',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Deployment Lead',
          'og:description': 'At Blend, we’re dedicated to improving lending. We’re an enterprise technology company, but our product affects the most important purchase most people will make in their lifetime—their home. For homebuyers, our product means a clear, guided path to a new home. For lenders, it means modern, easy-to-use tools that let employees spend their time helping customers, rather than on repetitive, manual tasks. By aligning and modernizing this archaic industry, we believe everybody wins. We need someone who’s driven to solve hard problems—the harder the better. We’re motivated by the fact that our product won’t just affect the lives of a few people in the Bay Area—it affects people all over America, not to mention a foundational part of the U.S. economy. Founded in 2012 by former Palantir leaders, we’re currently backed by Founders Fund, Andreessen Horowitz and other prominent investors. As a Deployment Lead, you will understand Blend’s platform and the client’s needs to help deliver a soluti',
          'og:url': 'https://jobs.lever.co/blendlabs/46aec184-6bae-4b56-b88b-49f6e26adca8',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Blend - Security Analyst',
    'htmlTitle': 'Blend - Security Analyst',
    'link': 'https://jobs.lever.co/blendlabs/0491a753-cc20-4245-8c05-e9a1c64e1027',
    'displayLink': 'jobs.lever.co',
    'snippet': 'At Blend, top engineers and designers from Palantir, Google, Stanford, and ... as \na system administrator or software developer; BA/BS or 4+ relevant experience\xa0...',
    'htmlSnippet': 'At Blend, top <b>engineers</b> and designers from Palantir, Google, Stanford, and ... as <br>\na system administrator or <b>software</b> developer; BA/BS or 4+ relevant experience&nbsp;...',
    'cacheId': 'cZuQGbZCStkJ',
    'formattedUrl': 'https://jobs.lever.co/.../0491a753-cc20-4245-8c05-e9a1c64e1027',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../0491a753-cc20-4245-8c05-e9a1c64e1027',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Blend - Security Analyst',
          'twitter:description': "Blend is fixing the lending experience for one of the most important purchases people make - their home. Home lending is a $10 trillion vertical that hasn’t kept pace with technology, so we’re bringing banks and their customers the software and tools they deserve. At Blend, top engineers and designers from Palantir, Google, Stanford, and Caltech have joined forces with industry experts from firms like CoreLogic to disrupt the archaic systems in use today. We're founded by former Palantir engineers and backed by Peter Thiel, Andreessen Horowitz, and other prominent investors. As the Security Analyst , you will ensure Blend's compliance with security commitments and best practices. You will lead, develop, implement or manage on-going controls to meet security standards such as ISO 27001 and SOC 2 control objectives. You will be responsible for testing, documenting, evaluating, and remediating internal controls and collaborating with internal and external audit teams, IT management, and",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png',
          'og:title': 'Blend - Security Analyst',
          'og:description': "Blend is fixing the lending experience for one of the most important purchases people make - their home. Home lending is a $10 trillion vertical that hasn’t kept pace with technology, so we’re bringing banks and their customers the software and tools they deserve. At Blend, top engineers and designers from Palantir, Google, Stanford, and Caltech have joined forces with industry experts from firms like CoreLogic to disrupt the archaic systems in use today. We're founded by former Palantir engineers and backed by Peter Thiel, Andreessen Horowitz, and other prominent investors. As the Security Analyst , you will ensure Blend's compliance with security commitments and best practices. You will lead, develop, implement or manage on-going controls to meet security standards such as ISO 27001 and SOC 2 control objectives. You will be responsible for testing, documenting, evaluating, and remediating internal controls and collaborating with internal and external audit teams, IT management, and",
          'og:url': 'https://jobs.lever.co/blendlabs/0491a753-cc20-4245-8c05-e9a1c64e1027',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png'
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
    
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        
        with open('responseFromCodeforcash','ab+') as f:
            pickle.dump(response_per_post, f)

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
        
