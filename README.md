# CRUD de Receitas

![Lincença do projeto](	https://img.shields.io/github/license/robsonleal/pedroreceitas)
![Bagde status desenvolvimento](https://img.shields.io/static/v1?label=status&message=CONCLUÍDO&color=green)

## Índice

* [Título](#Título)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto

Projeto de um site para cadastro de receitas.

Neste site o usuário vai conseguir gerenciar as suas receitas favoritas, também vai conseguir fazer buscar pelo site procurando por receitas de outros usuários.

## Funcionalidades e Demonstração da Aplicação
- `Funcionalidade 1`: Fazer o cadastro de novos usuários;
- `Funcionalidade 2`: Fazer o login de usuários cadastrados;
- `Funcionalidade 3`: Cadastrar e vincular novas receitas ao usuário que as criou;
- `Funcionalidade 4`: Gerenciar(Modificar/Apagar) as receitas que foram criadas;
- `Funcionalidade 5`: O administrador pode aprovar as receitas para aparecerem na página principal do site, ficando esta disponível para todos os usuários (Até os não cadastrados);
- `Funcionalidade 6`: Fazer pesquisas no site para localizar as receitas favoritas;

Página inicial com usuário logado:
![image](https://user-images.githubusercontent.com/27708175/152462392-903d3cd1-7230-4237-a20b-228bebfa5f0f.png)

Página de cadastro de receita:
![image](https://user-images.githubusercontent.com/27708175/152462262-3c408153-33d2-4ae3-9c41-39278e9a9f87.png)

Págína de login:
![imagem da página de login](https://user-images.githubusercontent.com/27708175/152462000-e824da45-99ed-444f-878a-314a69459e4c.png)

## Acesso ao Projeto

** Deploy da aplicação http://pedroreceita.herokuapp.com/ (As imagens das receitas não estão sendo exibidas) ** <br><br>

## instruções para baixar e rodar localmente
** PRÉ-REQUISITOS: Possuir o banco de dados PostgreSQL intalado e configurado na máquina **

```console
git clone git@github.com:robsonleal/pedroreceitas.git
cd pedroreceitas
python -m venv ./venv
source /<caminho_até_o_projeto>/venv/bin/activate
pip install 'requirements.txt'
python manage.py runserver
```
- Abrir o endereço localhost:8000 no navegador de sua preferência

## Tecnologias utilizadas
`Django 4`
`Python 3`
`PostgreSQL`
