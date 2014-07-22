#!/usr/bin/python
import json
import shutil
import os
import time
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

    def writefile(self, file_name, content):
        with codecs.open(file_name, 'w',  encoding='utf-8') as f:
            return f.write(content)
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
            self.buildCategory(list_json[cat], cat)
            # for t in list_json[cat]:
            #     print(t)
            # pass
        pass
        result = json.dumps(list_json, ensure_ascii=False)
        print(result)
        self.writefile(self.datadir + '/' + 'test.json', result)

    def buildCategory(self, cat_json, cat):
        cat_path = self.datadir + '/' + cat
        article_list = [line[:-3] for line in os.listdir(cat_path) if line[-2:]=='md']
        # delete unexisted articles
        for k in range(len(cat_json) - 1, -1, -1):
            title = cat_json[k].get('title')
            if title == None or not os.path.exists(cat_path + '/' + title + '.md'):
                cat_json.pop(k)
                pass
            pass
        pass
        
        for article in article_list:
            is_found = False
            for k in range(len(cat_json) - 1, -1, -1):
                if cat_json[k].get('title') == article.decode('utf8'):
                    if is_found:
                        # delete repeated articles
                        cat_json.pop(k)
                    else:
                        is_found = True
                    pass
                pass
            pass
            if not is_found:
                # add new article
                author = raw_input("Please input author name:")
                current_time = raw_input("Please input publish time:")
                cover_url = raw_input("Please input cover image url:")
                thumb_url = raw_input("Please input thumbnail image url:")
                description = raw_input("Please input description:")
                cat_json.insert(0, {
                    u"title": unicode(article, 'utf8'),
                    u"author": unicode(author, 'utf8') if len(author) > 0 else u'John Wong',
                    u"time": unicode(author, 'utf8') if len(current_time) > 0 else unicode(time.strftime("%H:%M:%S %m/%d %Y", time.localtime()), 'utf8'),
                    u"cover_url": unicode(cover_url, 'utf8'),
                    u"thumb_url": unicode(thumb_url, 'utf8'),
                    u"description": unicode(description, 'utf8')
                })
                pass
        pass

if __name__ == "__main__":
    blogBuiler = BlogBuiler()
    blogBuiler.buildtemplate()
    blogBuiler.buildData()