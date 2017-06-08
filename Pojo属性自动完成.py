# POJO Property Auto Generate
# encoding:utf-8

import re
import os

class FormatJavaFile:

    # 匹配缩进，属性类型，属性名称
    propertyPattern = '(?P<indent>\s+)(private\s+){0,1}(?P<protype>\w+)\s+(?P<proname>\w+);'

    def __init__(self, filepath):

        if not os.path.exists(filepath):
            raise Exception('format file is not exist!')
        self.filepath = filepath

    def format(self):
        with open(self.filepath, 'r+') as f:
            filecontent = f.read()
            formatcontent = self._format(filecontent)
        with open(self.filepath, 'w') as f:
            f.write(formatcontent)

    def _format(self, filecontent):
        regex_property = re.compile(FormatJavaFile.propertyPattern)
        matches = regex_property.finditer(filecontent)
        if matches:
            for matcho in matches:
                pro = matcho.group()
                proname = matcho.group('proname')
                protype = matcho.group('protype')
                indent = matcho.group('indent').strip('\n')
                proget = self.generatepropertyget(proname, protype, indent)
                proset = self.generatepropertyset(proname, protype, indent)
                filecontent = filecontent.replace(pro, pro + proget + proset)
                print(len(indent))
        return filecontent

    def generatepropertyset(self, name, type, indent='    '):
        result = '\n{}public {} {}({} value)'.format(indent, type, 'set' + name.capitalize(), type)
        result += '\n{}{{'.format(indent)
        result += '\n{}{} = value;'.format(indent + indent, name)
        result += '\n{}}}\n'.format(indent)
        return result

    def generatepropertyget(self, name, type, indent='    '):
        result = '\n{}public {} {}()'.format(indent, type, 'get' + name.capitalize())
        result += '\n{}{{'.format(indent)
        result += '\n{}return {};'.format(indent + indent, name)
        result += '\n{}}}\n'.format(indent)
        return result

fo = FormatJavaFile('pojo.java')

fo.format()


