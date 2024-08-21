# 🕹️ Board Game Catalog API

Bem-vindo à **Board Game Catalog API**! Esta API permite que você gerencie um catálogo de jogos de tabuleiro, bem como o histórico de partidas jogadas, incluindo jogadores e pontuações.

## 📝 Funcionalidades

- **Jogos de Tabuleiro**: Gerencie um catálogo de jogos de tabuleiro, incluindo título, descrição, fotos, número de jogadores e avaliações.
- **Jogadores**: Adicione e gerencie jogadores.
- **Partidas**: Registre partidas jogadas, incluindo os jogos, jogadores e suas respectivas pontuações.

## 🚀 Começando

### Requisitos

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/board-game-catalog.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd board-game-catalog
    ```

3. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

### 🛠️ Como Usar

1. Configure as variáveis de ambiente, se necessário (por exemplo, banco de dados).

2. Inicie o servidor:

    ```bash
    python app.py
    ```

3. Acesse a API em `http://localhost:5000`.

### 📖 Documentação da API

A API foi documentada utilizando o [OpenAPI 3.0](https://swagger.io/specification/) e pode ser encontrada na pasta swagger. Abaixo, estão alguns dos principais endpoints:

#### 🎮 Jogos de Tabuleiro

- **GET /games**: Lista todos os jogos de tabuleiro.
- **POST /games**: Adiciona um novo jogo de tabuleiro.
- **GET /games/{gameId}**: Obtém detalhes de um jogo específico.
- **PUT /games/{gameId}**: Atualiza um jogo existente.
- **DELETE /games/{gameId}**: Exclui um jogo.

#### 🧑‍🤝‍🧑 Jogadores

- **GET /players**: Lista todos os jogadores.
- **POST /players**: Adiciona um novo jogador.
- **GET /players/{playerId}**: Obtém detalhes de um jogador específico.
- **PUT /players/{playerId}**: Atualiza um jogador existente.
- **DELETE /players/{playerId}**: Exclui um jogador.

#### 🏆 Partidas

- **GET /matches**: Lista todas as partidas.
- **POST /matches**: Registra uma nova partida.
- **GET /matches/{matchId}**: Obtém detalhes de uma partida específica.

### 🧪 Testes

Para rodar os testes, use o comando:

```bash
pytest
