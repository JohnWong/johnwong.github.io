#!/usr/bin/python
import json
import shutil
import os
import time
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

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
        if config.get('inject'):
            for (inject_id, inject_config) in config['inject'].items():
                if self._temp.get(inject_config):
                    inject_content = self._temp.get(inject_config)
                else:
                    inject_content = self.readfile(self.dir + '/' + inject_config)
                result = result.replace('${' + inject_id + '}', inject_content)
            pass
        pass
        return result

    def builddata(self):
        list_file = os.path.join(self.datadir, 'list.json')
        if os.path.exists(list_file):
            shutil.copy(list_file, list_file + '.bak')
            list_json = json.loads(self.readfile(list_file))
        else:
            list_json = {}
            pass
        cat_list = [line for line in os.listdir(self.datadir) if line[:1]!='.' and os.path.isdir(os.path.join(self.datadir, line))]
        for cat in cat_list:
            if not list_json.has_key(cat):
                list_json[cat] = []
                pass
            self.buildcategory(list_json[cat], cat)
            pass
        self.data = list_json
        result = json.dumps(list_json, ensure_ascii=False)
        # print(result)
        self.writefile(os.path.join(self.datadir, 'list.json'), result)
        pass
        
    def buildcategory(self, cat_json, cat):
        cat_path = os.path.join(self.datadir, cat)
        self.buildsubcats(cat_json, cat_path)
        self.buildarticles(cat_json, cat_path)

    def buildsubcats(self, cat_json, cat_path):
        cat_list = [line for line in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, line))]
        # delete unexisted articles
        for k in range(len(cat_json) - 1, -1, -1):
            title = cat_json[k].get('title')
            if cat_json[k].get('list') != None:
                if title == None or not os.path.exists(os.path.join(cat_path, title)):
                    cat_json.pop(k)
                    pass
                pass
            pass
        pass
        for cat in cat_list:
            is_found = False
            for k in range(len(cat_json) - 1, -1, -1):
                if cat_json[k].get('title') == cat.decode('utf8'):
                    if is_found:
                        # delete repeated articles
                        cat_json.pop(k)
                    else:
                        is_found = True
                    pass
                pass
            
            if not is_found:
                # add new category
                print("Please input infomation for category: " + cat)
                thumb_url = raw_input("Please input thumbnail image url:")
                description = raw_input("Please input description:")
                cat_json.insert(0, {
                    "title": unicode(cat, 'utf8'),
                    "thumb_url": unicode(thumb_url, 'utf8'),
                    "description": unicode(description, 'utf8'),
                    "list":[]
                })
                self.buildarticles(cat_json[0]['list'], os.path.join(cat_path, cat))
                pass
            pass
        pass

    def buildarticles(self, cat_json, cat_path):
        article_list = [line[:-3] for line in os.listdir(cat_path) if line[-2:]=='md']
        # delete unexisted articles
        for k in range(len(cat_json) - 1, -1, -1):
            title = cat_json[k].get('title')
            if cat_json[k].get('list') == None:
                if title == None or not os.path.exists(os.path.join(cat_path, title + '.md')):
                    cat_json.pop(k)
                    pass
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
            
            if not is_found:
                # add new article
                print("Please input infomation for article: " + article)
                author = raw_input("Please input author name: (default: John Wong)")
                current_time = raw_input("Please input publish time: (default: now)")
                cover_url = raw_input("Please input cover image url:")
                thumb_url = raw_input("Please input thumbnail image url:")
                description = raw_input("Please input description:")
                for i in range(len(cat_json)):
                    if cat_json[i].get('list') == None:
                        break
                    pass

                cat_json.insert(i, {
                    "title": unicode(article, 'utf8'),
                    "author": unicode(author, 'utf8') if len(author) > 0 else u'John Wong',
                    "time": unicode(author, 'utf8') if len(current_time) > 0 else unicode(time.strftime("%m/%d %Y", time.localtime()), 'utf8'),
                    "cover_url": unicode(cover_url, 'utf8'),
                    "thumb_url": unicode(thumb_url, 'utf8'),
                    "description": unicode(description, 'utf8')
                })
                pass
            pass
        pass

    def buildindex(self):
        list_file = os.path.join(self.datadir, 'list-index.json')
        if os.path.exists(list_file):
            shutil.copy(list_file, list_file + '.bak')
            pass
        list_json = []
        for k in self.data:
            cat = self.data[k]
            for item in cat:
                if item.get('list') != None:
                    for subitem in item.get('list'):
                        subitem['category'] = k
                        list_json.insert(0, subitem)
                        pass
                    pass
                else:
                    item['category'] = k
                    list_json.insert(0, item)
                    pass
                pass
            pass
        sorted_list = self.sort(list_json)
        result = json.dumps({'Posts': sorted_list}, ensure_ascii=False)
        self.writefile(os.path.join(self.datadir, 'list-index.json'), result)
        pass

    def sort(self, itemlist):
        for item in itemlist:
            item['_time'] = time.strptime(item.get('time'),"%m/%d %Y")
            pass

        result = sorted(itemlist, cmp=None, key=lambda item : item['_time'], reverse=True)

        for item in result:
            item.pop('_time')
        return result
        

if __name__ == "__main__":
    blogBuiler = BlogBuiler()
    blogBuiler.buildtemplate()
    blogBuiler.builddata()
    blogBuiler.buildindex()
