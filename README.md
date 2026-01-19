# API Flask — Regiões e Pokémons

API simples em Flask para cadastrar e gerenciar **regiões** e **pokémons** via HTTP.

> Observação importante: os dados ficam em memória (dicionários Python em `db.py`). Ao reiniciar o servidor, tudo é perdido.

## Requisitos
- Python 3.x

## Instalação
No diretório do projeto:

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python app.py
```

Por padrão o Flask sobe em: `http://localhost:5000`

## Funcionamento

A API aceita JSON no corpo das requisições e salva o conteúdo "como vier", adicionando um campo `id` gerado automaticamente usando UUID.

- **Região**: recebe um JSON (ex.: `{ "nome": "Kanto" }`) e adiciona `id`.
- **Pokémon**: recebe um JSON (ex.: `{ "nome": "Pikachu", "tipo": "Elétrico" }`) e adiciona `id`.

## Endpoints

### Regiões

- `GET /regioes` — lista todas as regiões
- `GET /regiao/<id_regiao>` — busca região por id
- `GET /regiao?nome=XPTO` — busca região por nome (querystring obrigatória `nome`)
- `POST /regiao` — cria região
- `PUT /regiao/<id_regiao>` — atualiza região por id
- `DELETE /regiao/<id_regiao>` — remove região por id

### Pokémons

- `GET /pokemons` — lista todos os pokémons
- `GET /pokemon/<id_pokemon>` — busca pokémon por id
- `GET /pokemon?nome=XPTO` — busca pokémon por nome (querystring obrigatória `nome`)
- `POST /pokemon` — cria pokémon
- `PUT /pokemon/<id_pokemon>` — atualiza pokémon por id
- `DELETE /pokemon/<id_pokemon>` — remove pokémon por id

## Exemplos de uso

### Criar uma região

```bash
curl -X POST http://localhost:5000/regiao \
  -H "Content-Type: application/json" \
  -d '{"nome": "Kanto", "geração": 1}'
```

Resposta:
```json
{
  "id": "abc123...",
  "nome": "Kanto",
  "geração": 1
}
```

### Criar um pokémon

```bash
curl -X POST http://localhost:5000/pokemon \
  -H "Content-Type: application/json" \
  -d '{"nome": "Pikachu", "tipo": "Elétrico", "nível": 25}'
```

Resposta:
```json
{
  "id": "def456...",
  "nome": "Pikachu",
  "tipo": "Elétrico",
  "nível": 25
}
```

### Buscar todas as regiões

```bash
curl http://localhost:5000/regioes
```

Resposta:
```json
{
  "Regiões": [
    {
      "id": "abc123...",
      "nome": "Kanto",
      "geração": 1
    }
  ]
}
```

### Buscar região por id

```bash
curl http://localhost:5000/regiao/abc123...
```

### Buscar região por nome

```bash
curl "http://localhost:5000/regiao?nome=Kanto"
```

### Atualizar uma região

```bash
curl -X PUT http://localhost:5000/regiao/abc123... \
  -H "Content-Type: application/json" \
  -d '{"geração": 1, "nome": "Kanto"}'
```

### Deletar uma região

```bash
curl -X DELETE http://localhost:5000/regiao/abc123...
```

### Listar todos os pokémons

```bash
curl http://localhost:5000/pokemons
```

### Buscar pokémon por id

```bash
curl http://localhost:5000/pokemon/def456...
```

### Buscar pokémon por nome

```bash
curl "http://localhost:5000/pokemon?nome=Pikachu"
```

### Atualizar um pokémon

```bash
curl -X PUT http://localhost:5000/pokemon/def456... \
  -H "Content-Type: application/json" \
  -d '{"nível": 30}'
```

### Deletar um pokémon

```bash
curl -X DELETE http://localhost:5000/pokemon/def456...
```

## Notas importantes

- Os IDs são gerados automaticamente usando UUID
- Como não há validação de schema, você pode adicionar quaisquer campos no JSON; eles serão armazenados e retornados
- Os dados são armazenados em dicionários em memória, não em um banco de dados persistente
