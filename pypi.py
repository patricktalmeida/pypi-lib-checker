from lxml import html
import requests

def main():
    libs = []
    current_versions = {}
    with open('requirements.txt', "r") as reqs:
        for req in reqs:
            req = req.rstrip().split("==")
            libs.append(req[0])
            current_versions[req[0]] = req[1]

    new_versions = {}
    for lib in libs:
        page = requests.get(f'https://pypi.org/project/{lib}/', timeout=10)
        tree = html.fromstring(page.content)
        pypi = tree.xpath('//*[@id="content"]/div[1]/div/div[1]/h1/text()')

        for parser in pypi:
            result = ' '.join(parser.split(lib)).replace(' ', '').replace('\n', '')
            new_versions[lib] = result

    for key, value in new_versions.items():
        if current_versions[key] != value:
            print(f'*{key}* version:', 
                current_versions[key], 
                'is lower than', value
            ) 

if __name__ == '__main__':
    main()
