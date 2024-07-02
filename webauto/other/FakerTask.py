
from faker import Faker
import openpyxl

# 定义不同国家的 locale
locales = ['en_US', 'fr_FR', 'de_DE', 'ja_JP', 'zh_CN', 'it_IT', 'es_ES']
#美国、法国、德国、日本、中国、意大利和西班牙,'zh_TW'台湾


fakers = Faker(locales)    #列表形式
# fakers = {locale: Faker(locale) for locale in locales}   字典形式

#1、创建excel
excel = openpyxl.Workbook()
#2、创建sheet页和名字
sheet = excel.active
sheet.title = 'data1'
#3、往对应sheet页添加一行信息，充当表头
sheet.append(['Name', 'Site', 'Email', 'PhoneNumber'])
#4、save Excel



for _ in range(100):
    # locale = locales[_ % len(locales)]  取模按顺序拿locales里的值
    locale = random.choice(locales)  #利用random.choice随机拿列表里的元素
    fake = fakers[locale]

    name = fake.name()
    site = fake.address()
    email = fake.user_name() + '@git.cn'
    phone_number = fake.phone_number()

    sheet.append([name, site, email, phone_number])
sheet.save('UserData.xlsx')