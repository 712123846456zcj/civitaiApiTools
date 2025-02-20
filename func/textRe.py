import re

from html.parser import HTMLParser

isReTXT = True

# class TextExtractor(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.text = ""
#
#     def handle_data(self, data):
#         data = re.sub(r'(<\/p>|<\/a>|<\/[^>]*>)', '', data)
#         if "\n" in data:
#             self.text += "\n" + data + "\n"
#         else:
#             self.text += data + "\n"
#
#     def get_extracted_text(self):
#         return self.text.strip()
#
# def extract_text_from_html(html_content):
#     if isReTXT:
#         parser = TextExtractor()
#         parser.feed(html_content)
#         text = parser.get_extracted_text()
#         return str(text)
#     else:
#         return html_content

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.is_link = False
        self.current_link = ""

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.is_link = True
            for attr in attrs:
                if attr[0] == "href":
                    self.current_link = attr[1]

    def handle_endtag(self, tag):
        if tag == "a":
            if self.is_link and self.current_link:
                self.text += f" ({self.current_link})"
            self.is_link = False
            self.current_link = ""

    def handle_data(self, data):
        if self.is_link:
            # Append the link text
            self.text += data
        else:
            # Handle regular text
            data = re.sub(r'(<\/p>|<\/[^>]*>)', '', data)
            if "\n" in data:
                self.text += "\n" + data + "\n"
            else:
                self.text += data + "\n\n"

    def get_extracted_text(self):
        return self.text.strip()

def extract_text_from_html(html_content, isReTXT=True):
    if isReTXT:
        parser = TextExtractor()
        parser.feed(html_content)
        text = parser.get_extracted_text()
        return text
    else:
        return html_content



def text_clean(cleaned_filename):
    # one edit step
    cleaned_filename = str(cleaned_filename).rstrip()
    # if '/' in cleaned_filename:
    #     cleaned_filename = cleaned_filename.replace('/','')
    if ' ' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace(' ','_')
    if '\\' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace('\\','')
    if ':' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace(':','-')
    if '|' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace('|','-')
    if '\n' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace('\n','_')
    if '&' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace('&','-')
    if '\t' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace('\t','_')
    
    if r'/' in cleaned_filename:
        cleaned_filename = cleaned_filename.replace(r'/','')
        # 定义特殊字符的替换规则
        # 此处定义为：将非法特殊字符替换为'-'，其他无效字符替换为'_'
        # 字符类 [^\*"/:?\\|<>，换行，空格，制表符] 表示所有非法字符，将其替换为 '-'
        cleaned_filename = re.sub(r'[^\w\s./\\\-]', '-', cleaned_filename)

        # 替换非字符类 [^\w\s./\\\-] 表示除字母、数字、空白字符（包括空格和制表符）和合法标点符号以外的字符，将其替换为 '_'
        cleaned_filename = re.sub(r'[^\w\s./\\\-]', '_', cleaned_filename)
    else:
        # 定义特殊字符的替换规则
        # 此处定义为：将非法特殊字符替换为'-'，其他无效字符替换为'_'
        # 字符类 [^\*"/:?\\|<>，换行，空格，制表符] 表示所有非法字符，将其替换为 '-'
        cleaned_filename = re.sub(r'[^\w\s./\\\-]', '-', cleaned_filename)

        # 替换非字符类 [^\w\s./\\\-] 表示除字母、数字、空白字符（包括空格和制表符）和合法标点符号以外的字符，将其替换为 '_'
        cleaned_filename = re.sub(r'[^\w\s./\\\-]', '_', cleaned_filename)
    return cleaned_filename


