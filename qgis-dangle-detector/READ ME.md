# Identificador de Dangles em Redes Lineares (QGIS)

Este projeto contém um script em Python desenvolvido para o QGIS que identifica "dangles" — ou seja, extremidades soltas — em redes espaciais formadas por linhas (como ruas ou trilhas). É útil para detectar erros topológicos em redes viárias antes da simulação ou análise.

## Funcionalidades

- Identifica automaticamente os pontos finais desconectados (dangles).
- Cria uma nova camada de pontos com os dangles detectados.
- Interface amigável via QGIS (seleção da camada e barra de progresso).
- Identifica automaticamente os pontos finais desconectados, mesmo que sobrepostos (false positive dangles) -- Solicitação Pendente de implementação !!

## Requisitos

- **QGIS**: 3.28 ou superior (recomendado)
- **Python**: Versão utilizada pelo QGIS (geralmente Python 3.9+)
- Bibliotecas internas: `qgis.core`, `qgis.PyQt.QtWidgets`

## Como usar

1. Abra o QGIS.
2. Carregue sua camada linear (ex: ruas).
3. Execute o script pelo console Python ou crie um script dentro do Processamento.
4. Selecione a camada quando solicitado.
5. Os dangles serão adicionados como uma nova camada chamada `Dangles`.

---

# Dangle Identifier in Line Networks (QGIS)

This project contains a Python script for QGIS to identify "dangles" — loose ends — in spatial line networks (e.g., roads or trails). It's useful for detecting topological errors in road networks before simulations or analysis.

## Features

- Automatically detects disconnected endpoints (dangles).
- Creates a new point layer marking the dangles.
- User-friendly interaction via QGIS (layer selection and progress bar).

## Requirements

- **QGIS**: 3.28 or higher (recommended)
- **Python**: The version embedded in QGIS (typically Python 3.9+)
- Built-in libraries: `qgis.core`, `qgis.PyQt.QtWidgets`

## How to use

1. Open QGIS.
2. Load your line layer (e.g., streets).
3. Run the script via the Python console or as a Processing script.
4. Select the layer when prompted.
5. Dangles will appear in a new layer named `Dangles`.
