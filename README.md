# 📊 Sistema de Análise de Campanhas Facebook/Instagram Ads

Um sistema completo para coletar, analisar e otimizar suas campanhas de publicidade no Facebook e Instagram.

## ✨ Funcionalidades

- 🔗 **Integração com Meta Marketing API** - Conecta automaticamente com suas contas
- 📈 **Coleta de Dados** - Puxa informações em tempo real das campanhas
- 📊 **Análise Automática** - Calcula métricas importantes (ROI, ROAS, CPC, CTR)
- 🎯 **Recomendações** - Sugere otimizações baseadas em performance
- 📱 **Dashboard Interativo** - Interface HTML com gráficos dinâmicos
- 💾 **Armazenamento Seguro** - Banco de dados com histórico completo

## 🚀 Como Começar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/ads-analytics-system.git
cd ads-analytics-system
```

### 2. Configure o ambiente
```bash
cp .env.example .env
pip install -r requirements.txt
```

### 3. Conecte com Meta
- Acesse https://developers.facebook.com/
- Crie uma aplicação e obtenha o Access Token
- Adicione o token no arquivo `.env`

### 4. Inicie o servidor
```bash
python main.py
```

### 5. Abra o dashboard
- Acesse `http://localhost:8000`

## 📋 Requisitos

- Python 3.9+
- Conta Meta (Facebook/Instagram Ads)
- Access Token da Meta Marketing API

## 🔧 Configuração

Edite o arquivo `.env`:

```env
FACEBOOK_ACCESS_TOKEN=seu_token_aqui
FACEBOOK_APP_ID=seu_app_id
FACEBOOK_APP_SECRET=seu_app_secret
FACEBOOK_BUSINESS_ACCOUNT_ID=seu_business_account_id
DEBUG=True
PORT=8000
```

## 📚 Documentação

- [Meta Marketing API](https://developers.facebook.com/docs/marketing-api)
- [FastAPI](https://fastapi.tiangolo.com/)
- Veja QUICK_START.md para guia de instalação detalhado

## 📄 Licença

MIT License

---

**Desenvolvido para otimizar suas campanhas de publicidade**
