# -*- coding:utf-8 -*-

import os

import requests

stand_country_list = [{'name': u'Taiwan', 'order': 6L, 'id': 1L}, {'name': u'Hong Kong', 'order': 7L, 'id': 2L},
                      {'name': u'China National', 'order': 2L, 'id': 3L}, {'name': u'China', 'order': 1L, 'id': 4L},
                      {'name': u'United States', 'order': 5L, 'id': 5L}, {'name': u'Macau', 'order': 0L, 'id': 6L},
                      {'name': u'China Country', 'order': 4L, 'id': 7L},
                      {'name': u'China Province', 'order': 3L, 'id': 8L}, {'name': u'Korea', 'order': 0L, 'id': 9L},
                      {'name': u'France', 'order': 15L, 'id': 10L}, {'name': u'India', 'order': 0L, 'id': 11L},
                      {'name': u'Yemen', 'order': 0L, 'id': 12L}, {'name': u'Singapore', 'order': 50L, 'id': 13L},
                      {'name': u'Syria', 'order': 0L, 'id': 14L}, {'name': u'Sudan', 'order': 0L, 'id': 15L},
                      {'name': u'United Kingdom', 'order': 35L, 'id': 16L},
                      {'name': u'United Arab Emirates', 'order': 0L, 'id': 17L},
                      {'name': u'Afghanistan', 'order': 0L, 'id': 18L},
                      {'name': u'Saudi Arabia', 'order': 0L, 'id': 19L}, {'name': u'Pakistan', 'order': 0L, 'id': 20L},
                      {'name': u'Qatar', 'order': 0L, 'id': 21L}, {'name': u'Iran', 'order': 0L, 'id': 22L},
                      {'name': u'Oman', 'order': 0L, 'id': 23L}, {'name': u'Japan', 'order': 40L, 'id': 24L},
                      {'name': u'Other', 'order': 0L, 'id': 25L}, {'name': u'Malaysia', 'order': 8L, 'id': 26L},
                      {'name': u'Kuwait', 'order': 0L, 'id': 27L}, {'name': u'Australia', 'order': 0L, 'id': 28L},
                      {'name': u'North Korea', 'order': 0L, 'id': 29L}, {'name': u'Russia', 'order': 0L, 'id': 30L},
                      {'name': u'Vietnam', 'order': 40L, 'id': 31L}, {'name': u'Canada', 'order': 10L, 'id': 32L},
                      {'name': u'Romania', 'order': 0L, 'id': 33L}, {'name': u'Bulgaria', 'order': 0L, 'id': 34L},
                      {'name': u'Philippines', 'order': 0L, 'id': 35L},
                      {'name': u'New Zealand', 'order': 0L, 'id': 36L}, {'name': u'Thailand', 'order': 0L, 'id': 37L},
                      {'name': u'Italy', 'order': 0L, 'id': 38L}, {'name': u'Turkey', 'order': 0L, 'id': 39L},
                      {'name': u'Germany', 'order': 0L, 'id': 40L}, {'name': u'Iraq', 'order': 0L, 'id': 41L},
                      {'name': u'South Korea', 'order': 30L, 'id': 42L}, {'name': u'Czech', 'order': 0L, 'id': 43L},
                      {'name': u'Poland', 'order': 0L, 'id': 44L}, {'name': u'Greece', 'order': 0L, 'id': 45L},
                      {'name': u'Switzerland', 'order': 0L, 'id': 46L}, {'name': u'Luxembourg', 'order': 0L, 'id': 47L},
                      {'name': u'Colombia', 'order': 0L, 'id': 48L}, {'name': u'Jordan', 'order': 0L, 'id': 49L},
                      {'name': u'Benin', 'order': 0L, 'id': 50L}, {'name': u'Spain', 'order': 0L, 'id': 51L},
                      {'name': u'Portugal', 'order': 0L, 'id': 52L}, {'name': u'Armenia', 'order': 0L, 'id': 53L},
                      {'name': u'American Samoa', 'order': 0L, 'id': 54L}, {'name': u'Croatia', 'order': 0L, 'id': 55L},
                      {'name': u'South Africa', 'order': 0L, 'id': 56L}, {'name': u'Israel', 'order': 0L, 'id': 57L},
                      {'name': u'Indonesia', 'order': 0L, 'id': 58L}, {'name': u'Ukraine', 'order': 0L, 'id': 59L},
                      {'name': u'The Somali Republic', 'order': 0L, 'id': 60L},
                      {'name': u'Montenegro', 'order': 0L, 'id': 61L}, {'name': u'Mexico', 'order': 0L, 'id': 62L},
                      {'name': u'Hungary', 'order': 0L, 'id': 63L}, {'name': u'Cyprus', 'order': 0L, 'id': 64L},
                      {'name': u'Somalia', 'order': 0L, 'id': 65L}, {'name': u'Netherlands', 'order': 0L, 'id': 66L},
                      {'name': u'Lebanon', 'order': 0L, 'id': 67L}, {'name': u'Egypt', 'order': 0L, 'id': 68L},
                      {'name': u'Libya', 'order': 0L, 'id': 69L}, {'name': u'Tunisia', 'order': 0L, 'id': 70L},
                      {'name': u'Algeria', 'order': 0L, 'id': 71L}, {'name': u'Marocco', 'order': 0L, 'id': 72L},
                      {'name': u'Belgium', 'order': 0L, 'id': 73L}, {'name': u'Brunei', 'order': 0L, 'id': 74L},
                      {'name': u'Brazil', 'order': 0L, 'id': 75L}, {'name': u'Crotone', 'order': 0L, 'id': 76L},
                      {'name': u'Bahrain', 'order': 0L, 'id': 77L}, {'name': u'Barcelona', 'order': 0L, 'id': 78L},
                      {'name': u'Uruguay', 'order': 0L, 'id': 79L}, {'name': u'Serbia', 'order': 0L, 'id': 80L},
                      {'name': u'Bosnia', 'order': 0L, 'id': 81L}, {'name': u'Chile', 'order': 0L, 'id': 82L},
                      {'name': u'Azerbaijan', 'order': 0L, 'id': 83L}, {'name': u'malta', 'order': 0L, 'id': 84L},
                      {'name': u'Argentina', 'order': 0L, 'id': 85L}, {'name': u'Albania', 'order': 0L, 'id': 86L},
                      {'name': u'Ireland', 'order': 0L, 'id': 87L}, {'name': u'Congo', 'order': 0L, 'id': 88L},
                      {'name': u'Bahamas', 'order': 0L, 'id': 89L}, {'name': u'Georgia', 'order': 0L, 'id': 90L},
                      {'name': u'Sri lanka', 'order': 0L, 'id': 91L}, {'name': u'Angola', 'order': 0L, 'id': 92L},
                      {'name': u'Denmark', 'order': 0L, 'id': 93L}, {'name': u'Haiti', 'order': 0L, 'id': 94L},
                      {'name': u'Nigeria', 'order': 0L, 'id': 95L}, {'name': u'Mali', 'order': 0L, 'id': 96L},
                      {'name': u'Kazakhstan', 'order': 0L, 'id': 97L}, {'name': u'Moldova', 'order': 0L, 'id': 98L},
                      {'name': u'Irland', 'order': 0L, 'id': 99L}, {'name': u'Honduras', 'order': 0L, 'id': 100L},
                      {'name': u'Kurdistan', 'order': 0L, 'id': 101L}, {'name': u'Sweden', 'order': 0L, 'id': 103L},
                      {'name': u'Myanmar', 'order': 0L, 'id': 104L}, {'name': u'CUBA', 'order': 0L, 'id': 105L},
                      {'name': u'Panam\xe1', 'order': 0L, 'id': 106L}, {'name': u'Barbados', 'order': 0L, 'id': 107L},
                      {'name': u'Jamaica', 'order': 0L, 'id': 108L}, {'name': u'norway', 'order': 0L, 'id': 109L},
                      {'name': u'Venezuela', 'order': 0L, 'id': 110L}, {'name': u'Ghana', 'order': 0L, 'id': 111L},
                      {'name': u'Cameroon', 'order': 0L, 'id': 112L}, {'name': u'Africa', 'order': 0L, 'id': 113L},
                      {'name': u'SUB', 'order': 0L, 'id': 114L}, {'name': u'Belarus', 'order': 0L, 'id': 115L},
                      {'name': u'Macedonia', 'order': 0L, 'id': 116L}, {'name': u'Paraguay', 'order': 0L, 'id': 117L},
                      {'name': u'Dominican Republic', 'order': 0L, 'id': 118L},
                      {'name': u'Costa Rica', 'order': 0L, 'id': 119L}, {'name': u'Slovakia', 'order': 0L, 'id': 120L},
                      {'name': u'kenya', 'order': 0L, 'id': 121L}, {'name': u'Mongolia', 'order': 0L, 'id': 123L},
                      {'name': u'Tanzania', 'order': 0L, 'id': 124L}, {'name': u'Bolivia', 'order': 0L, 'id': 125L},
                      {'name': u'Austria', 'order': 0L, 'id': 126L}, {'name': u'Cambodia', 'order': 0L, 'id': 128L},
                      {'name': u'Peru', 'order': 0L, 'id': 129L}, {'name': u'El Salvador', 'order': 0L, 'id': 130L},
                      {'name': u'GUATEMALA', 'order': 0L, 'id': 131L}]
epg_country_list = [{'code': u'AU', 'name': 'Australia'}, {'code': u'BR', 'name': 'Brazil'},
                    {'code': u'CA', 'name': 'Canada'}, {'code': u'CN', 'name': 'China'},
                    {'code': u'DE', 'name': 'Germany'}, {'code': u'FR', 'name': 'France'},
                    {'code': u'GB', 'name': 'United Kingdom of Great Britain and Northern Ireland'},
                    {'code': u'HK', 'name': 'Hong Kong'}, {'code': u'ID', 'name': 'Indonesia'},
                    {'code': u'IN', 'name': 'India'}, {'code': u'JP', 'name': 'Japan'},
                    {'code': u'KR', 'name': 'Korea'}, {'code': u'MY', 'name': 'Malaysia'},
                    {'code': u'NZ', 'name': 'New Zealand'}, {'code': u'PH', 'name': 'Philippines'},
                    {'code': u'RU', 'name': 'Russian Federation'}, {'code': u'SG', 'name': 'Singapore'},
                    {'code': u'TH', 'name': 'Thailand'}, {'code': u'TW', 'name': 'Taiwan'},
                    {'code': u'US', 'name': 'US'}, {'code': u'VN', 'name': 'Viet Nam'},
                    {'code': u'ZA', 'name': 'South Africa'}]

stand_country_list = sorted(stand_country_list, key=lambda x: x['name'])
epg_country_list = sorted(epg_country_list, key=lambda x: x['code'])


def download_m3u_files():
    url_list = ["https://epg.pw/test_channels.m3u",
                "https://epg.pw/test_channels_banned_cn.m3u",
                "https://epg.pw/test_channels_all.m3u",
                "https://epg.pw/test_channels_unknown.m3u",
                "https://epg.pw/test_channels.txt",
                "https://epg.pw/test_channels_banned_cn.txt",
                "https://epg.pw/test_channels_all.txt",
                "https://epg.pw/test_channels_unknown.txt",
                ]
    for country in stand_country_list:
        url_list.append("https://epg.pw/test_channels_%s.m3u" % country['name'].lower().replace(" ", "_"))
        url_list.append("https://epg.pw/test_channels_%s.txt" % country['name'].lower().replace(" ", "_"))

    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split("/")[-1].replace("test", "iptv")
                with open(os.path.join(os.getcwd(), "./m3u/%s" % file_name), 'w') as f:
                    f.write(response.content)
                print ("downloaded url %s" % url)
            else:
                print ("can not fetch url %s" % url)
        except Exception as e:
            print(e, url)


def download_xmltv_files():
    url_list = ["https://epg.pw/xmltv/epg.xml",
                "https://epg.pw/xmltv/epg.xml.gz",
                ]
    for country in epg_country_list:
        url_list.append("https://epg.pw/xmltv/epg_%s.xml" % country['code'])
        url_list.append("https://epg.pw/xmltv/epg_%s.xml.gz" % country['code'])

    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split("/")[-1]
                with open(os.path.join(os.getcwd(), "./epg/%s" % file_name), 'w') as f:
                    f.write(response.content)
                print ("downloaded url %s" % url)
            else:
                print ("can not fetch url %s" % url)
        except Exception as e:
            print(e, url)


def download_files():
    print("start to download the xmltv")
    download_xmltv_files()
    print("start to download the m3u")
    download_m3u_files()


download_files()
