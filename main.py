# -*- coding:utf-8 -*-

import os

import requests

stand_country_list = [u'Taiwan', u'Hong Kong', u'China National', u'China', u'United States', u'Macau',
                      u'China Country', u'China Province', u'Korea', u'France', u'India', u'Yemen', u'Singapore',
                      u'Syria', u'Sudan', u'United Kingdom', u'United Arab Emirates', u'Afghanistan', u'Saudi Arabia',
                      u'Pakistan', u'Qatar', u'Iran', u'Oman', u'Japan', u'Other', u'Malaysia', u'Kuwait', u'Australia',
                      u'North Korea', u'Russia', u'Vietnam', u'Canada', u'Romania', u'Bulgaria', u'Philippines',
                      u'New Zealand', u'Thailand', u'Italy', u'Turkey', u'Germany', u'Iraq', u'South Korea', u'Czech',
                      u'Poland', u'Greece', u'Switzerland', u'Luxembourg', u'Colombia', u'Jordan', u'Benin', u'Spain',
                      u'Portugal', u'Armenia', u'American Samoa', u'Croatia', u'South Africa', u'Israel', u'Indonesia',
                      u'Ukraine', u'The Somali Republic', u'Montenegro', u'Mexico', u'Hungary', u'Cyprus', u'Somalia',
                      u'Netherlands', u'Lebanon', u'Egypt', u'Libya', u'Tunisia', u'Algeria', u'Marocco', u'Belgium',
                      u'Brunei', u'Brazil', u'Crotone', u'Bahrain', u'Barcelona', u'Uruguay', u'Serbia', u'Bosnia',
                      u'Chile', u'Azerbaijan', u'malta', u'Argentina', u'Albania', u'Ireland', u'Congo', u'Bahamas',
                      u'Georgia', u'Sri lanka', u'Angola', u'Denmark', u'Haiti', u'Nigeria', u'Mali', u'Kazakhstan',
                      u'Moldova', u'Irland', u'Honduras', u'Kurdistan', u'Sweden', u'Myanmar', u'CUBA', u'Panam\xe1',
                      u'Barbados', u'Jamaica', u'norway', u'Venezuela', u'Ghana', u'Cameroon', u'Africa', u'SUB',
                      u'Belarus', u'Macedonia', u'Paraguay', u'Dominican Republic', u'Costa Rica', u'Slovakia',
                      u'kenya', u'Mongolia', u'Tanzania', u'Bolivia', u'Austria', u'Cambodia', u'Peru', u'El Salvador',
                      u'GUATEMALA']
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

stand_country_list = sorted(stand_country_list)
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
        url_list.append("https://epg.pw/test_channels_%s.m3u" % country.lower().replace(" ", "_"))
        url_list.append("https://epg.pw/test_channels_%s.txt" % country.lower().replace(" ", "_"))

    for url in url_list:
        try:
            print("download url %s" % url)
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split("/")[-1].replace("test", "iptv")
                with open(os.path.join(os.getcwd(), "%s" % file_name), 'wb') as f:
                    f.write(response.content)
                print("finished download url %s" % url)
            else:
                print ("can not fetch url %s" % url)
        except Exception as e:
            print(e, url)


def download_xmltv_files():
    url_list = ["https://epg.pw/xmltv/epg.xml.gz",
                "https://epg.pw/xmltv/epg_lite.xml",
                "https://epg.pw/xmltv/epg_lite.xml.gz",
                ]
    for country in epg_country_list:
        if country['code'] not in ['RU']:
            url_list.append("https://epg.pw/xmltv/epg_%s.xml" % country['code'])
        url_list.append("https://epg.pw/xmltv/epg_%s.xml.gz" % country['code'])

    for url in url_list:
        try:
            print("download url %s" % url)
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split("/")[-1]
                with open(os.path.join(os.getcwd(), "%s" % file_name), 'wb') as f:
                    f.write(response.content)
                print("finished download url %s" % url)
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
