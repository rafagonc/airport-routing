# Dependências #

Projeto testado com **Python 3.6.4**

Para instalar as dependências:

- `pip install -r requirements.txt`

# Testes #

Localizados em triṕ/routes/tests.py

Para rodar os testes na sua máquina:

- `py.test trip`

Para rodar testes com docker:

- `docker run -ti rafagonc/airport-routing py.test`

# Como Executar #

Na pasta root do projeto

- Sem Docker
    - CLI
        - `python manage.py cli input-file.csv`

    - REST
        - `python manage.py rest input-file.csv`
        - Documentação disponível em `0.0.0.0:8000/docs/`

- Com Docker
    - CLI
        - `docker run -ti rafagonc/airport-routing python manage.py cli input-file.csv`
        - **Trocando input** `docker run -v {path_para_seu_input_file}:/app/input-file.csv -it rafagonc/airport-routing python manage.py cli input-file.csv`

    - REST
        - `docker run -ti -p 8000:8000 rafagonc/airport-routing python manage.py rest input-file.csv`
        - Documentação disponível em `0.0.0.0:8000/docs/`
        - **Trocando input** `docker run -v {path_para_seu_input_file}:/app/input-file.csv -it rafagonc/airport-routing python manage.py rest input-file.csv`

  

**Estrutura de arquivos e pacotes.**

A estrutura segue a arquitetura do Django de apps separados em módulos. A intenção é deixar o mais simples e intuitivo possível para que o próximo desenvolvedor não tenha dificuldade em se localizar e fazer manutenção.

**Explique as decisões de design adotadas para a solução.**

Decisões tomadas no projeto:

- Utilização do algoritmo de dijkstra pronto para não reinventar a roda.
- Arquitetura REST utilizando todos os status_codes e métodos (GET, POST, PUT, PATCH, DELETE)
- Uso do Docker para facilitar o teste em qualquer máquina e facilitar a utilização do mesmo em orquestradores como Kubernetes.

**Descreva sua APÌ Rest de forma simplificada.**

- Path: /routes/
  - POST - Criar nova rota
    - Params - {"source": "GRU", "destination": "CDG", "cost": 3}
    - Response 200 - {"message": "New route successfully registered"}
    - Response 400 - {"error": "Airports should have only 3 letters!"}
    - Response 400 - {"error": "Invalid cost for route"}
    - Response 400 - {"error": "There is already a cost for this route"}
  - GET - Find Best Route
    - Params - ?source=GRU&destination=CDG
    - Response 200 - {"route":["GRU","BRC","SCL","ORL","CDG"],"cost":40}
    - Response 400 - {"error": "There is no possible route between these airports"}}

----------------------------------------------------------------------------------------

# Rota de Viagem #

Um turista deseja viajar pelo mundo pagando o menor preço possível independentemente do número de conexões necessárias.
Vamos construir um programa que facilite ao nosso turista, escolher a melhor rota para sua viagem.

Para isso precisamos inserir as rotas através de um arquivo de entrada.

## Input Example ##
```csv
GRU,BRC,10
BRC,SCL,5
GRU,CDG,75
GRU,SCL,20
GRU,ORL,56
ORL,CDG,5
SCL,ORL,20
```

## Explicando ## 
Caso desejemos viajar de **GRU** para **CDG** existem as seguintes rotas:

1. GRU - BRC - SCL - ORL - CDG ao custo de **$40**
2. GRU - ORL - CGD ao custo de **$64**
3. GRU - CDG ao custo de **$75**
4. GRU - SCL - ORL - CDG ao custo de **$48**
5. GRU - BRC - CDG ao custo de **$45**

O melhor preço é da rota **4** logo, o output da consulta deve ser **CDG - SCL - ORL - CDG**.

### Execução do programa ###
A inicializacao do teste se dará por linha de comando onde o primeiro argumento é o arquivo com a lista de rotas inicial.

```shell
$ mysolution input-routes.csv
```

Duas interfaces de consulta devem ser implementadas:
- Interface de console deverá receber um input com a rota no formato "DE-PARA" e imprimir a melhor rota e seu respectivo valor.
  Exemplo:
  ```shell
  please enter the route: GRU-CGD
  best route: GRU - BRC - SCL - ORL - CDG > $40
  please enter the route: BRC-CDG
  best route: BRC - ORL > $30
  ```

- Interface Rest
    A interface Rest deverá suportar:
    - Registro de novas rotas. Essas novas rotas devem ser persistidas no arquivo csv utilizado como input(input-routes.csv),
    - Consulta de melhor rota entre dois pontos.

Também será necessária a implementação de 2 endpoints Rest, um para registro de rotas e outro para consula de melhor rota.

## Recomendações ##
Para uma melhor fluides da nossa conversa, atente-se aos seguintes pontos:

* Envie apenas o código fonte,
* Estruture sua aplicação seguindo as boas práticas de desenvolvimento,
* Evite o uso de frameworks ou bibliotecas externas à linguagem. Utilize apenas o que for necessário para a exposição do serviço,
* Implemente testes unitários seguindo as boas praticas de mercado,
* Documentação
  Em um arquivo Texto ou Markdown descreva:
  * Como executar a aplicação,
  * Estrutura dos arquivos/pacotes,
  * Explique as decisões de design adotadas para a solução,
  * Descreva sua APÌ Rest de forma simplificada.

