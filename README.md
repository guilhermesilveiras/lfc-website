# Learning from Commits

[![Jekyll Build and Deploy](https://github.com/SEU_USUARIO/lfc-website/actions/workflows/jekyll.yml/badge.svg)](https://github.com/SEU_USUARIO/lfc-website/actions/workflows/jekyll.yml)

Melhorar a qualidade e a agilidade do desenvolvimento de software através de métodos inteligentes e ciência de dados.

## 🎯 Sobre o Projeto

O **Learning from Commits (LFC)** é uma iniciativa de pesquisa que utiliza inteligência artificial e análise de histórico de commits para prever e prevenir defeitos em software.

### Características Principais

- 🔍 **Detecção Antecipada**: Identifica mudanças arriscadas antes da produção
- 🎯 **Revisões Focadas**: Prioriza revisões de código baseadas em risco
- 💸 **Redução de Custos**: Diminui retrabalhos com ações preventivas
- 🤖 **IA Integrada**: Utiliza machine learning e o algoritmo SZZ

## 🚀 Tecnologias

- **Frontend**: Jekyll + GitHub Pages
- **Styling**: CSS3 com design neubrutalista
- **Fonts**: Fira Code (monospace)
- **Deploy**: GitHub Actions
- **Analytics**: Baseado em dados de commits

## 📊 Impacto Esperado

- **$381B**: Custo anual mundial com correções de software
- **60%**: Do tempo de desenvolvimento gasto em debugging  
- **85%**: Dos bugs introduzidos durante desenvolvimento

## 🛠️ Desenvolvimento Local

### Pré-requisitos

- Ruby 3.1+
- Bundler
- Git

### Instalação

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/lfc-website.git
cd lfc-website

# Instale as dependências
bundle install

# Execute localmente
bundle exec jekyll serve

# Acesse http://localhost:4000
```

### Estrutura do Projeto

```
├── _config.yml          # Configuração Jekyll
├── _layouts/            # Templates de página
├── _posts/              # Posts do blog
├── assets/              # CSS, JS, imagens
├── blog/                # Página do blog
├── about/               # Página sobre
├── index.html           # Homepage
└── .github/workflows/   # CI/CD
```

## 📝 Criando Conteúdo

### Novo Post

Crie um arquivo em `_posts/` seguindo o padrão:

```markdown
---
layout: post
title: "Título do Post"
date: 2024-MM-DD
author: "Seu Nome"
tags: [tag1, tag2]
excerpt: "Breve descrição do post"
---

Conteúdo do post em Markdown...
```

### Nova Página

Crie um diretório com `index.html`:

```markdown
---
layout: default
title: "Título da Página"
---

Conteúdo da página...
```

## 🎨 Design System

### Cores

- **Accent**: `#f59e0b` (Amarelo dourado)
- **Dark**: `#0f172a` (Azul escuro)
- **Muted**: `#374151` (Cinza)
- **Terminal**: `#00ff41` (Verde terminal)

### Tipografia

- **Títulos**: Fira Code (monospace)
- **Corpo**: System fonts
- **Código**: Fira Code

### Componentes

- Cards com bordas grossas
- Botões neubrutalistas
- Efeitos de sombra
- Design responsivo

## 🚀 Deploy

O site é automaticamente implantado no GitHub Pages através de GitHub Actions:

1. Push para `main` branch
2. GitHub Actions executa Jekyll build
3. Deploy automático para `gh-pages`
4. Site disponível em `https://SEU_USUARIO.github.io/lfc-website`

### Configuração do GitHub Pages

1. Vá em Settings > Pages
2. Source: Deploy from a branch
3. Branch: `gh-pages`
4. Folder: `/ (root)`

## 👥 Equipe

- **Cleviton Monteiro** - Doutor em engenharia de software
- **Rodrigo G F Soares** - Doutor em ciência da computação
- **João Victor Vieira** - Desenvolvedor Full stack
- **Douglas Vidal** - Pesquisador
- **Aline Costa** - Bacharela em Ciência da Computação
- **Igor de Castro** - Engenheiro de Software
- **Guilherme Salgueiro** - Pesquisador
- **Italo Santos** - Pesquisador

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Contato

- Website: [https://learningfromcommits.com](https://learningfromcommits.com)
- Email: contato@learningfromcommits.com
- GitHub: [@lfc-team](https://github.com/lfc-team)

---

*Desenvolvido com ❤️ pela equipe Learning from Commits*