def get_area_dict():
    with open('./config/area.txt', 'r') as a:
        area = {}
        for line in a.readlines():
            if line[0] != '#' and line != '\n':
                code, areaname = line.split()
                area[code] = areaname
    return area


def get_header():
    with open('./config/headers.txt', 'r') as c:
        header = {}
        for line in c.readlines():
            name, value = line.strip().split(':', 1)
            header[name] = value
    return header


def get_body():
    with open('./config/body.txt', 'r') as b:
        body = {}
        for line in b.readlines():
            name, value = line.strip().split(':', 1)
            body[name] = value
    return body

area = get_area_dict()
header = get_header()
body = get_body()
url = "http://ucadmin.ewt360.com/Member/Edit/8922973"