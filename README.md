# 🤖 Bot Rochinha Pé Duro – v1.2

O **Rochinha Pé Duro** é um bot de apostas esportivas com inteligência artificial de múltiplos modos,
desenvolvido para analisar jogos de futebol e emitir **sinais altamente confiáveis e lucrativos**.

---

## ⚙️ Modos de IA Ativos

### ✅ Ultra Conservador Ajustado
- Odds ≥ 1.65 (ou ≥ 1.56 com confiança > 87%)
- Stake variável (1.5% a 2%)
- Foco em mercados com ROI comprovado

### ✅ Modo Omega
- Validação cruzada tripla (3 IAs)
- Fair odds + value bet detection
- Envio apenas com consenso total

### ✅ Modo Zenith
- Memória de padrões vencedores
- Contrarian edge (apostas contra o público)
- Detecção de armadilhas

### ✅ Modo Moscou
- IA adaptativa com leitura de linha
- Cálculo de valor justo
- Foco em ROI por time, técnico e contexto

### ✅ Modo Ares
- IA ofensiva (resultado, BTTS, over/under, jogador para finalizar)
- Permite combinação de mercados
- Stake variável de 1.5% a 2.5%

### ✅ Modo RIO v1.2 (NOVO!)
- Validação cruzada 2x1 (IA principal obrigatória)
- Fair odds estendida (Tier 2: 1.56 a 1.64 com confiança > 90%)
- Novos mercados lucrativos (time marca no 2º tempo, under 3.5)
- Camada sombra com stake reduzida
- Hot Player Detector + sharp money detection

---

## 🚀 Como rodar o bot

```bash
python main.py
```

---

## 📂 Estrutura

```
main.py
/modos/
    ultra.py
    omega.py
    zenith.py
    moscou.py
    modo_rio_v12.py
/utils/
    filtros.py
    calculos.py
```

---

## 📤 Canais de envio

- Telegram (via bot API)
- E-mail (SMTP configurável)
- Painel (opcional)

---

## 🧠 Requisitos

- Python 3.10+
- Bibliotecas: requests, pandas, numpy, etc.
- API de dados (ex: API-Football) integrada

---

Criado com 💙 para ser uma **máquina de green**.
