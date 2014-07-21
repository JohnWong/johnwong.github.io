import json
import shutil
import os
import codecs

class BlogBuiler:

    def __init__(self, name="config.json", dir="template", datadir="data"):
        self.dir = dir
        self.datadir = datadir
        self.config = json.loads(self.readfile(name))
        pass

    def buildtemplate(self):
        self._temp = {}
        build_config = self.config['template']
        for build_item in build_config:
            result = self.buildhtml(build_item['config'])
            self._temp[build_item['id']] = result
            if build_item['output'] == "true":
                with codecs.open(build_item['id'], 'w', encoding="utf-8") as f:
                    f.write(result)
        pass

    def readfile(self, file_name):
        with codecs.open(file_name, 'r',  encoding='utf-8') as f:
            return f.read()
        pass

    def buildhtml(self, config):
        result = self.readfile(self.dir + '/' + config['base'])
        if config.get('script'):
            scripts = ''
            for script in config.get('script'):
                scripts += '<script src="' + script + '"></script>'
            result = result.replace('${script}', scripts)
            pass
        for (inject_id, inject_config) in config['inject'].items():
            if self._temp.get(inject_config):
                inject_content = self._temp.get(inject_config)
            else:
                inject_content = self.readfile(self.dir + '/' + inject_config)
            result = result.replace('${' + inject_id + '}', inject_content)
        return result

    def buildData(self):
        list_file = self.datadir + '/' + 'list.json'
        if os.path.exists(list_file):
            shutil.copy(list_file, list_file + '.bak')
            list_json = json.loads(self.readfile(list_file))
        else:
            list_json = {}
            pass
        cat_list = [line for line in os.listdir(self.datadir) if line[:1]!='.' and os.path.isdir(self.datadir + '/' + line)]
        for cat in cat_list:
            if not list_json.has_key(cat):
                list_json[cat] = []
                pass
            print(len(list_json[cat]))
            self.buildCategory(list_json[cat], cat)
            print(len(list_json[cat]))
            for t in list_json[cat]:
                print(t)
            pass
        pass    

    def buildCategory(self, cat_json, cat):
        cat_path = self.datadir + '/' + cat
        article_list = [line[:-3] for line in os.listdir(cat_path) if line[-2:]=='md']
        # delete unexisted articles
        for article_json in cat_json:
            title = article_json.get('title')
            if title == None or not os.path.exists(cat_path + '/' + title + '.md'):
                cat_json.remove(article_json)
                pass
            pass

        
        for article in article_list:
            is_found = False
            for k in cat_json:
                print(k.get('title') == article.decode('utf8'), k.get('title'))
                if k.get('title') == article.decode('utf8'):
                    if is_found:
                        # delete repeated articles
                        cat_json.remove(k)
                    else:
                        is_found = True
                    pass
                pass
            pass
        pass

if __name__ == "__main__":
    blogBuiler = BlogBuiler()
    blogBuiler.buildtemplate()
    blogBuiler.buildData()