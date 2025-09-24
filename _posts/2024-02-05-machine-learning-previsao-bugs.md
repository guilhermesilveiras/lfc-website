---
layout: post
title: "Machine Learning para Previsão de Bugs: Características e Modelos"
date: 2024-02-05
author: "Cleviton Monteiro"
tags: [machine-learning, previsão, características, modelos]
excerpt: "Exploramos as características extraídas de commits e os modelos de machine learning utilizados para prever a introdução de bugs em software."
---

## Características dos Commits

Para treinar nossos modelos de machine learning, extraímos diversas características dos commits que podem indicar a probabilidade de introdução de bugs.

### Métricas de Código

#### Complexidade
- **Complexidade Ciclomática**: Número de caminhos independentes no código
- **Profundidade de Aninhamento**: Níveis de estruturas de controle aninhadas
- **Linhas de Código**: Tamanho absoluto das mudanças

```python
def extract_complexity_metrics(diff):
    """
    Extrai métricas de complexidade de um diff
    """
    return {
        'cyclomatic_complexity': calculate_cyclomatic_complexity(diff),
        'nesting_depth': calculate_nesting_depth(diff),
        'lines_added': count_lines_added(diff),
        'lines_deleted': count_lines_deleted(diff)
    }
```

#### Métricas de Mudança
- **Número de arquivos modificados**
- **Número de métodos alterados**
- **Proporção de código novo vs. modificado**

### Características do Desenvolvedor

#### Experiência
- **Commits anteriores no projeto**
- **Experiência com arquivos específicos**
- **Tempo desde o último commit**

#### Padrões de Trabalho
- **Hora do commit** (commits noturnos tendem a ter mais bugs)
- **Dia da semana** (sexta-feira pode ser mais arriscada)
- **Tamanho médio dos commits do desenvolvedor**

### Características Semânticas

#### Mensagem do Commit
Utilizamos **NLP** para analisar mensagens:

```python
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_message_features(commit_message):
    """
    Extrai características da mensagem do commit
    """
    # Palavras-chave relacionadas a urgência
    urgent_keywords = ['urgent', 'quick', 'hotfix', 'asap']
    urgency_score = sum(1 for word in urgent_keywords 
                       if word in commit_message.lower())
    
    # Sentimento da mensagem
    sentiment = analyze_sentiment(commit_message)
    
    return {
        'urgency_score': urgency_score,
        'sentiment': sentiment,
        'message_length': len(commit_message),
        'has_question_mark': '?' in commit_message
    }
```

#### Código Modificado
- **Tipos de mudanças** (adição, remoção, modificação)
- **Padrões sintáticos** identificados via AST
- **Densidade de comentários**

## Modelos de Machine Learning

### Abordagens Testadas

#### 1. Random Forest
Nosso modelo baseline, robusto e interpretável:

```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
```

**Vantagens:**
- Lida bem com features categóricas e numéricas
- Fornece importância das características
- Resistente a overfitting

#### 2. Gradient Boosting (XGBoost)
Modelo de alta performance:

```python
import xgboost as xgb

xgb_model = xgb.XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6
)
```

**Vantagens:**
- Excelente performance preditiva
- Lida bem com features desbalanceadas
- Suporte nativo para missing values

#### 3. Deep Learning (Neural Networks)
Para capturar padrões complexos:

```python
import tensorflow as tf

def create_bug_prediction_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_dim=input_dim),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy', 'precision', 'recall']
    )
    
    return model
```

### Resultados Comparativos

| Modelo | Precisão | Recall | F1-Score | Tempo de Treino |
|--------|----------|---------|----------|-----------------|
| Random Forest | 0.78 | 0.72 | 0.75 | 2 min |
| XGBoost | 0.82 | 0.79 | 0.80 | 5 min |
| Neural Network | 0.85 | 0.81 | 0.83 | 15 min |

### Interpretabilidade

Um aspecto crucial é entender **por que** um commit é classificado como arriscado:

```python
import shap

# SHAP para explicar predições
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)

# Características mais importantes
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': shap_values.mean(axis=0)
}).sort_values('importance', ascending=False)
```

### Desafios e Soluções

#### 1. Desbalanceamento de Classes
Apenas 10-20% dos commits introduzem bugs.

**Solução:** Técnicas de balanceamento (SMOTE, class weights)

#### 2. Concept Drift
Padrões de bugs mudam ao longo do tempo.

**Solução:** Modelos adaptativos com janelas deslizantes

#### 3. Generalização entre Projetos
Modelos treinados em um projeto podem não funcionar em outro.

**Solução:** Transfer learning e domain adaptation

## Próximos Desenvolvimentos

Estamos trabalhando em:
- **Ensemble de modelos** para maior robustez
- **Explicações locais** para cada predição
- **Modelos específicos por linguagem** de programação

---

*A combinação de características bem engineered e modelos robustos é a chave para previsões precisas de bugs.*