import library


def save(code, error_message, ip, url):
    string = library.get_date_time()
    if code == 404:
        string = ip + '\t' +  url + '\t' + string + '\t' + error_message + '\n'
        file = open('storage/errors/404.data', 'a')
        file.write(string)
        file.close()