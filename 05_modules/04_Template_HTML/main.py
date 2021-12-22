from string import Template
from datetime import datetime

with open('/dev/python/utilities_python/05_python_modules/09_Template_HTML/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%Y-%m-%d')
    corpo_msg = template.substitute(nome="Raul Moraes", data=data_atual)
    # corpo_msg = template.safe_substitute(nome="Raul Moraes", data=data_atual)

print(corpo_msg)