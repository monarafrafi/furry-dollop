import pathlib
import bs4
import datetime


content = pathlib.Path('/tmp/example.html').read_text()
soup = bs4.BeautifulSoup(content, 'html.parser')


class Page:
    def __init__(self, soup):
        self.soup = soup


class Field:
    def __init__(self, css_selector):
        self.css_selector = css_selector


class TextInput(Field):
    def __get__(self, instance, owner ):
        element = instance.soup.select_one(self.css_selector)
        return element.text.strip()


class DateInput(TextInput):
    def __get__(self, instance, owner):
        value = super().__get__(instance, owner)
        return datetime.datetime.strptime(value, "%d%m").date()


class BasolPage(Page):

    region = TextInput("span:nth-of-type(1)")
    department = TextInput("span:nth-of-type(2)")
    number = TextInput("span:nth-of-type(3)")
    date = DateInput("span:nth-of-type(6)")
    author = TextInput("span:nth-of-type(7)")
    usual_name = TextInput("span:nth-of-type(9)")


page = BasolPage(soup)
print(page.region)

# result = soup.select_one('span:nth-of-type(1)')
# print(result.text)
# result = soup.select_one('span:nth-of-type(2)')
# print(result.text)
# result = soup.select_one('span:nth-of-type(3)')
# print(result.text.strip())
# result = soup.select_one('span:nth-of-type(6)')
# result = soup.select_one('span:nth-of-type(7)')
# result = soup.select_one('span:nth-of-type(9)')
# print(result.text)
