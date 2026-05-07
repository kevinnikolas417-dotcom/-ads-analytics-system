# 🚀 Guia Rápido de Instalação

## Pré-requisitos

- Python 3.9+
- Pip (gerenciador de pacotes Python)
- Conta Meta com acesso a Ads Manager
- Access Token da Meta Marketing API

## Passo 1: Obter Access Token da Meta

1. Vá para https://developers.facebook.com/
2. Faça login com sua conta Meta
3. Clique em "Minhas Aplicações" → "Criar Aplicação"
4. Tipo: Gerenciamento de Negócios
5. Nome: "Ads Analytics System"
6. Vá para Ferramentas → Explorador de Gráficos
7. Selecione sua aplicação e clique em "Obter Token de Usuário"
8. Solicite as permissões:
   - `ads_read`
   - `business_management`
   - `insights_read`

## Passo 2: Configuração do Projeto

```bash
# Crie uma pasta para o projeto
mkdir C:\projetos\ads-analytics-system
cd C:\projetos\ads-analytics-system

# Crie um arquivo .env
copy .env.example .env
```

## Passo 3: Preencha as Variáveis de Ambiente

Edite o arquivo `.env`:

```env
FACEBOOK_ACCESS_TOKEN=seu_access_token_aqui
FACEBOOK_APP_ID=seu_app_id
FACEBOOK_APP_SECRET=seu_app_secret
FACEBOOK_BUSINESS_ACCOUNT_ID=seu_business_account_id
DATABASE_URL=sqlite:///./ads_db.db
DEBUG=True
PORT=8000
```

## Passo 4: Instalar Dependências

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## Passo 5: Executar o Servidor

```bash
# Inicie o servidor FastAPI
python main.py
```

Você deverá ver:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## Passo 6: Acessar o Dashboard

Abra seu navegador e acesse: **http://localhost:8000**

Você verá o dashboard interativo com:
- 📊 Resumo de campanhas
- 📈 Gráficos de ROI, ROAS, CTR
- 💡 Recomendações automáticas
- 📋 Tabela detalhada de campanhas

## Endpoints da API

- `GET /health` - Verifica saúde da aplicação
- `GET /api/campaigns` - Lista todas as campanhas
- `GET /api/analysis/health-scores` - Calcula health scores
- `POST /api/sync/campaigns` - Sincroniza com Meta API
- `GET /api/export/metrics` - Exporta dados em JSON

## Solução de Problemas

### ❌ "Access Token Inválido"
- Verifique se o token foi copiado corretamente
- Tokens expiram em 60 dias, gere um novo se necessário

### ❌ "Nenhuma campanha encontrada"
- Verifique se sua conta Meta tem campanhas ativas
- Confirme que o Business Account ID está correto

### ❌ Porta 8000 já está em uso
- Use outra porta: `python main.py --port 8001`

## Próximos Passos

1. Configurar sincronização automática
2. Integrar com Slack para notificações
3. Adicionar mais plataformas (Google Ads, TikTok)
4. Exportar relatórios em PDF

---

**Bom uso! 🚀**
