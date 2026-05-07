# 🐙 Configuração do GitHub

## Passo 1: Criar um Repositório no GitHub

1. Vá para https://github.com/new
2. Faça login com sua conta GitHub
3. Preencha os dados:
   - **Repository name**: `ads-analytics-system`
   - **Description**: Sistema de análise e otimização de campanhas Facebook/Instagram Ads
   - **Public/Private**: Escolha sua preferência
   - Clique em **Create repository**

## Passo 2: Inicializar Git Localmente

Abra o Command Prompt na pasta do projeto:

```bash
cd C:\projetos\ads-analytics-system

# Inicialize o git
git init

# Configure seu usuário
git config user.name "Seu Nome"
git config user.email "seu.email@example.com"

# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "Initial commit: Ad Analytics System"

# Adicione o repositório remoto (substitua seu-usuario)
git remote add origin https://github.com/seu-usuario/ads-analytics-system.git

# Envie para o GitHub
git branch -M main
git push -u origin main
```

## Passo 3: Criar .gitignore

Crie um arquivo `.gitignore` na raiz do projeto:

```
# Ambiente virtual
venv/
env/
*.pyc
__pycache__/

# Variáveis de ambiente
.env
.env.local

# Banco de dados
*.db
*.sqlite
*.sqlite3

# IDE
.vscode/
.idea/
*.swp

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db
```

## Passo 4: Colaboração

Para adicionar colaboradores:
1. Vá para **Settings** → **Collaborators**
2. Clique em **Add people**
3. Digite o username do colaborador

## Passo 5: Criar Branches

```bash
# Criar branch de desenvolvimento
git checkout -b develop

# Criar branch para feature
git checkout -b feature/nova-funcionalidade

# Faça suas alterações e commit
git commit -m "Add nova funcionalidade"

# Envie para GitHub
git push origin feature/nova-funcionalidade

# Crie um Pull Request no GitHub
```

## Passo 6: Versionamento

Use Semantic Versioning (MAJOR.MINOR.PATCH):

```bash
# Criar tag e release
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0

# No GitHub: vá para Releases e crie uma release
```

## Comandos Úteis

```bash
# Ver status
git status

# Ver histórico
git log --oneline

# Ver branches
git branch -a

# Atualizar branch local
git pull origin main

# Mudar URL do remote
git remote set-url origin https://github.com/novo-usuario/repo.git
```

---

**Repositório criado com sucesso! 🚀**
