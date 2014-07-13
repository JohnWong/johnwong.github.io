import json
import codecs

class BlogBuiler:

    def __init__(self, name="config.json", dir="template"):
        self.dir = dir
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


if __name__ == "__main__":
    blogBuiler = BlogBuiler()
    blogBuiler.buildtemplate()
