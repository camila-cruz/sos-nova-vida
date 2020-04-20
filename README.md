# sos-nova-vida
Sistema integrado com website para a SOS Nova Vida

## O que é?

É um sistema de controle para os acolhidos da instituição beneficente SOS Nova Vida, localizada em Suzano. A aplicação é integrada ao site oficial da entidade!

## Instalando as dependências

Atualmente, o projeto precisa desses pacotes para funcionar:
* Django 2.2.10
* Django Widget Tweaks 1.4.5
* Django Local Flavor 2.2
* Pillow

Para instalar as dependências, digite o comando:
~~~python
pip install -r requirements.txt
~~~

## Como acessar?

Primeiro, é necessário subir o servidor:
~~~python
python manage.py runserver
~~~

Depois, por um navegador, deve-se acessar a url:
~~~
http://localhost:8000/
~~~
