from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter, Retry
import requests
import time
import json
import re

BASE_URL = 'https://bluearchive.wiki/wiki'
DEFAULT_TIMEOUT = 5


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def soupify(http, endpoint):
    result = http.get(BASE_URL + endpoint).text
    soup = bs(result, "html.parser")
    return soup


def get_character_names(http):
    result = soupify(http, '/Characters')
    result = result.find_all('tr')
    del result[0]

    character_names = []
    count = 0
    for row in result:
        print('生徒さんの名前を取得しています...(' + str(count) +
              '/' + str(len(result)) + ' names)', end='\r')
        names = row.find_all('td')[1].find('a').string
        character_names.append(names)
        count += 1

    print('生徒さんの名前を取得しています...(' + str(count) +
          '/' + str(len(result)) + ' キャラクター)')
    return character_names


def get_character_image(http, name):
    if ('Iroha' in name):
        return ''
    try:
        chrjson = {}
        result_avatar = soupify(
            http, '/File:' + name.replace(' ', '_') + '_00.png')
        image_avatar = result_avatar.find(
            'div', class_='fullImageLink').find('a')
        name = name.replace(" diorama", "")
        test = soupify(
                http, '/' + name + '/gallery')
        teest = test.find_all(
                'div', class_='thumb')
        i = 0
        while ('_99.png' not in str(teest[i])):
            target = 'src='
            idx = str(teest[i]).find(target)
            r = str(teest[i])[idx + 1:]
            target2 = '.png/'
            idx2 = r.find(target2)
            r2 = r[:idx2]
            result = r2.replace('rc="', '')
            result = result.replace('"', '')
            result = result.replace("/thumb", "")
            result = "https:" + result + '.png'
            if ('(' in name):
                target3 = ("%29")
                idx3 = result.find(target3)
                r3 = result[idx3 + 1:]
                r3 = r3.replace("diorama", "")
                r3 = r3.replace("29", "")
            else:
                target3 = ("/" + name)
                idx3 = result.find(target3)
                r3 = result[idx3 + 1:]
                r3 = r3.replace(name, "")
            r3 = r3.replace(".png", "")
            r3 = r3.replace("_", "")
            new_data = {
                r3: result
            }
            chrjson.update(new_data)
            i += 1
        else:
            target = 'src='
            idx = str(teest[i]).find(target)
            r = str(teest[i])[idx + 1:]
            target2 = '.png/'
            idx2 = r.find(target2)
            r2 = r[:idx2]
            result = r2.replace('rc="', '')
            result = result.replace('"', '')
            result = result.replace("/thumb", "")
            result = "https:" + result + '.png'
            if ('(' in name):
                target3 = ("%29")
                idx3 = result.find(target3)
                r3 = result[idx3 + 1:]
                r3 = r3.replace("diorama", "")
                r3 = r3.replace("29", "")
            else:
                target3 = ("/" + name)
                idx3 = result.find(target3)
                r3 = result[idx3 + 1:]
                r3 = r3.replace(name, "")
            r3 = r3.replace(".png", "")
            r3 = r3.replace("_", "")
            new_data = {
                r3: result
            }
            chrjson.update(new_data)
            i += 1
        return chrjson
    except requests.exceptions.Timeout:
        result_avatar = soupify(
            http, '/File:' + name.replace(' ', '_') + '_00.png')
        image_avatar = result_avatar.find(
            'div', class_='mw-file-description').find_all('a')
        return {'avatar': 'https:' + image_avatar['href']}
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)


def rename_character(name):
    name_alt = ""
    if re.search(r"(Bunny)", name):
        name_alt = name.replace("(Bunny)", "(Bunny Girl)")
    elif re.search(r"(Cheerleader)", name):
        name_alt = name.replace("(Cheerleader)", "(Cheerleader) diorama")
    elif re.search(r"(Kid)", name):
        name_alt = name.replace("(Kid)", "(Kid) diorama")
    elif re.search(r"(Riding)", name):
        name_alt = name
    elif re.search(r"(Aris)", name):
        name_alt = name.replace("(Aris)", "(Arisu)")
    elif re.search(r"(Sportswear)", name):
        if (('Azusa' not in name) and ('Haruna' not in name) and ('Mari' not in name) and ('Yuuka' not in name)):
            name_alt = name
        else:
            name_alt = name.replace("(Sportswear)", "(Sportswear) diorama")
    elif re.search(r"(New Year)", name):
        if (('Aru' not in name) and ('Haruka' not in name) and ('Izumi' not in name) and ('Junko' not in name) and ('Kayoko' not in name) and ('Mutsuki' not in name) and ('Serika' not in name)):
            name_alt = name.replace("(New Year)", "(New Year) diorama")
        else:
            name_alt = name
    elif re.search(r"(Swimsuit)", name):
        if (('Hanako' not in name) and ('Hinata' not in name) and ('Koharu' not in name) and ('Miyako' not in name) and ('Miyu' not in name) and ('Moe' not in name) and ('Saki' not in name) and ('Serika' not in name) and ('Shiroko' not in name)):
            name_alt = name.replace("(Swimsuit)", "(Swimsuit) diorama")
    elif re.search(r"(Hot Spring)", name):
        name_alt = name.replace("(Hot Spring)", "(Hot Spring) diorama")
    elif re.search(r"Miyu", name):
        name_alt = name.replace("Miyu", "Miyu diorama")
    elif re.search(r"(Christmas)", name):
        name_alt = name.replace("(Christmas)", "(Christmas) diorama")

    return name_alt


def main():
    http = requests.Session()
    retries = Retry(total=3, backoff_factor=1,
                    status_forcelist=[429, 500, 502, 503, 504])
    adapter = TimeoutHTTPAdapter(max_retries=retries)
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    character_names = get_character_names(http)
    count = 1
    result = {}

    for name in character_names:
        name_alt = rename_character(name)
        if(name_alt == ''):
            name_alt = name

        print(name + 'さんの立ち絵を取得しています...(' + str(count) +
              '/' + str(len(character_names)) + ' キャラクター)')
        name_alt_alt = name_alt.replace(" diorama", "")

        result[name_alt_alt if name_alt else name] = get_character_image(
            http, name_alt)
        count += 1
    json_object = json.dumps(result, indent=2)
    with open("student-images.json", "w") as outfile:
        outfile.write(json_object)
    print('正常に終了しました。')


if __name__ == '__main__':
    main()
