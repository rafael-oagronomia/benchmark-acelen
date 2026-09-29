# OagronomIA — Design System (referência para o Claude Code)

> **"O Agro no Mundo da IA"** — o mundo do agro, através da IA.
> Marca de IA aplicada à agronomia e engenharia rural. Público: **agrônomos e engenheiros agrícolas** que trabalham no campo todo dia.
> Posicionamento: **tecnologia + inovação + inteligência artificial aplicada ao solo**.

Este arquivo é a fonte única de verdade visual. Toda tela, deck, página ou protótipo deve sair daqui. **Não invente** cores, tipos, espaçamentos ou componentes que não estejam aqui.

Estética-guia: **terminal agronômico** — superfícies escuras, um verde-neon de destaque, display em itálico futurista, cantos retos, movimento contido. Pense num *Bloomberg terminal para o campo*.

---

## 1. Fundamentos de conteúdo

A marca é **português do Brasil, primeiro**. O público domina vocabulário técnico agronômico, mas quer ferramentas que pareçam modernas e nativas de IA — não institucionais/empoeiradas.

### Tom de voz
- **Confiante, técnico, direto.** "Identifique pragas em segundos" — nunca "Talvez possamos te ajudar a identificar pragas."
- **Credível no campo.** Use os termos certos: *talhão, lavoura, NDVI, plantio, manejo integrado de pragas (MIP), pulverização, dose, hectare (ha), kg/ha*. Nunca aguar.
- **Aspiracional em tech.** Fale de agentes, análises, modelos, sensores — não de "features" e "dashboards".
- **"você"**, nunca "tu". Tratamento direto.
- **Sem emoji** nas superfícies de produto. O único floreio visual é o verde da marca.

### Caixa (casing)
- **Sentence case** em todo o chrome do produto: botões, itens de menu, títulos. ("Novo talhão", não "NOVO TALHÃO".)
- **CAIXA ALTA COM TRACKING LARGO** (`letter-spacing: 0.18em`) é reservada ao tratamento de eyebrow/tagline — como no "O AGRO NO MUNDO DA IA". Use com parcimônia: rótulos de seção acima de títulos, chips de status, labels de telemetria.
- **Títulos de display são itálicos** (espelham o wordmark). Corpo e UI ficam em pé (upright).

### Voz — exemplos
| Não                                                | Sim                                                       |
| -------------------------------------------------- | --------------------------------------------------------- |
| "Bem-vindo! Vamos começar sua jornada agrícola 🌱" | "Olá. Pronto para abrir o talhão de hoje?"                |
| "Nossa IA poderosa analisa suas plantações"        | "O modelo identifica a praga em 1,2 s. Confiança: 94 %."  |
| "Adicione uma nova fazenda"                        | "Novo talhão"                                             |
| "Você não tem permissão"                           | "Acesso bloqueado pelo administrador da conta."           |
| "Carregando..."                                    | "Analisando 12 ha…"                                       |

### Números e unidades
- Formatação BR: vírgula decimal, ponto de milhar → `1.450,8 kg/ha`.
- **Sempre com unidade.** Número pelado parece dado de demo.
- **Figuras tabulares** (`font-variant-numeric: tabular-nums`) em todo readout.
- Unicode ok para matemática/unidades (`° °C ± × ÷ µ ≥ ≤ ≈`), em mono.

---

## 2. Tokens de cor

```css
/* Marca — o verde-neon da tagline do wordmark */
--brand-green:        #52C937;   /* destaque principal */
--brand-green-bright: #6FE34F;   /* hover / glow / foco */
--brand-green-deep:   #2F8B1F;   /* pressionado / sobre claro */
--brand-green-mute:   #3A7A2A;   /* estados dim, dataviz */

/* Superfícies — escuras, terminal; a marca vive à noite */
--bg-0:  #050805;   /* página (quase-preto, leve tom verde) */
--bg-1:  #0B100B;   /* superfície base */
--bg-2:  #131A13;   /* card / painel */
--bg-3:  #1C241B;   /* card elevado */
--bg-4:  #252E24;   /* superfície de hover */
--line:  #2A3328;   /* divisor hairline */
--line-strong: #3A4537;

/* Modo claro (uso raro — impressão, exports, docs legais) */
--paper-0: #F4F1EA;  /* off-white quente do fundo do logo claro */
--paper-1: #EAE6DA;
--paper-2: #DCD7C7;

/* Texto sobre escuro */
--fg-1: #F2F4EE;   /* texto primário */
--fg-2: #B8BFB1;   /* secundário */
--fg-3: #7C8678;   /* terciário / labels */
--fg-4: #4D5749;   /* desabilitado / placeholder */
--fg-inv: #0B100B; /* sobre verde / sobre paper */

/* Terra — fundos de contexto "campo"/solo e dataviz (nunca chrome) */
--soil-1: #6B5A40;  --soil-2: #8A7556;
--sky-1:  #4FB7C9;  --sun-1:  #E8B33B;  --clay-1: #C26A3D;

/* Semântico */
--success: var(--brand-green);  --success-bg: rgba(82,201,55,0.12);
--warning: #E8B33B;             --warning-bg: rgba(232,179,59,0.12);
--danger:  #E5524A;             --danger-bg:  rgba(229,82,74,0.12);
--info:    #4FB7C9;             --info-bg:    rgba(79,183,201,0.12);

/* Dataviz — rampa agro: solo nu → muda → dossel */
--dv-1: #2F8B1F;  --dv-2: #52C937;  --dv-3: #9BE05F;  --dv-4: #E8B33B;
--dv-5: #C26A3D;  --dv-6: #4FB7C9;  --dv-7: #8A7556;
```

**Regras de cor**
- O verde é o **único** saturado do sistema. Use como ponteiro laser, não como fundo genérico.
- Superfícies padrão são **planas e escuras**. Sem texturas, sem gradientes decorativos.
- Cores de terra/dataviz **só** em gráficos e mapas — nunca no chrome.
- Não invente cores novas; se precisar de tonalidade harmônica, derive das existentes em oklch.

---

## 3. Tipografia

```css
--font-display: 'Chakra Petch', 'Eurostile', 'Bahnschrift', system-ui, sans-serif;
--font-body:    'Manrope', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif;
--font-mono:    'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
```

Carregar via Google Fonts:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Manrope:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

| Papel   | Família         | Uso                                                                 |
| ------- | --------------- | ------------------------------------------------------------------- |
| Display | **Chakra Petch** | Itálico 500/600/700 para H1/H2, eyebrows, números de KPI            |
| Corpo   | **Manrope**      | 400/500/600/700. UI e texto corrido                                 |
| Mono    | **JetBrains Mono** | Readouts de sensor, valores, IDs, código. Tabular figures         |

**Escala** (minor third 1.25): `--fs-12 … --fs-96` → 12,13,14,15,16,18,20,24,32,40,56,72,96px.
**Line-height:** `--lh-tight:1.04` · `--lh-snug:1.18` · `--lh-base:1.5` · `--lh-loose:1.72`.
**Tracking:** `--tr-display:-0.01em` · `--tr-body:0` · `--tr-eyebrow:0.18em` · `--tr-label:0.08em`.

### Estilos semânticos (aplicáveis direto)
```css
h1        /* Chakra Petch, italic 700, 56px, lh-tight, tracking display */
h2        /* Chakra Petch, italic 600, 40px, lh-snug */
h3        /* Chakra Petch, 600, 24px (NÃO itálico) */
h4        /* Manrope, 700, 18px */
.display  /* Chakra Petch, italic 700, 72px — hero */
.eyebrow  /* Chakra Petch, 500, 13px, UPPERCASE, tracking 0.18em, cor verde */
.label    /* Chakra Petch, 500, 12px, UPPERCASE, tracking 0.08em, cor fg-3 */
.body / p /* Manrope 16px, lh-base */
.body-lg  /* 18px */   .body-sm /* 14px, cor fg-2 */
.readout  /* JetBrains Mono, 500, tabular-nums — valores de métrica */
code/.mono/kbd /* JetBrains Mono 0.92em */
```

Hierarquia vem de **itálico-display vs corpo-upright**, não de muitos tamanhos. Mantém o visual terminal-clean.

> O **wordmark** é tratado como arte, não texto: use o PNG `assets/logo-transparent-cropped.png` sempre que a marca precisar aparecer.

---

## 4. Espaçamento, raio, elevação, motion

```css
/* Espaçamento — base 4px */
--s-1:4  --s-2:8  --s-3:12  --s-4:16  --s-5:20  --s-6:24
--s-8:32 --s-10:40 --s-12:48 --s-16:64 --s-20:80 --s-24:96
/* Mais comuns: 12 / 16 / 24. Grid de 8px. */

/* Raio — contido; retos/tech */
--r-0:0  --r-1:2  --r-2:4  --r-3:8  --r-4:12  --r-pill:999px
/* NUNCA cantos bolha 16px+ (lê consumer). Pill só em filtros, chips de status, avatares. */

/* Elevação — sutil no escuro; apoie em bordas + glow */
--sh-1: 0 1px 0 rgba(255,255,255,0.03), 0 1px 2px rgba(0,0,0,0.4);
--sh-2: 0 2px 8px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.03) inset;
--sh-3: 0 8px 24px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,255,255,0.04) inset;
--sh-glow:      0 0 0 1px rgba(82,201,55,0.5), 0 0 24px -4px rgba(82,201,55,0.4);
--sh-glow-soft: 0 0 32px -8px rgba(82,201,55,0.35);

/* Motion — snappy, nunca bouncy. Sem spring/overshoot. É instrumento, não brinquedo. */
--ease-out:  cubic-bezier(0.2, 0.7, 0.2, 1);
--ease-snap: cubic-bezier(0.4, 0, 0.1, 1);
--t-fast: 120ms;  /* hovers, mudança de cor */
--t-base: 200ms;  /* shifts de layout */
--t-slow: 360ms;  /* entradas */
```

- **Cards:** fill `--bg-2`, `1px solid var(--line)`, raio `--r-3` (8px). A hairline é lei — nunca separe card do fundo só com sombra. Card ativo/elevado sobe pra `--bg-3` + `--sh-2`.
- **Foco em input:** contorno **sempre verde** (`--sh-glow`), borda vira `--brand-green`. Nunca azul.
- **Loading:** permitido um *scanline/sweep* verde cruzando o topo do card (metáfora "sistema lendo o campo").
- **Reduce-motion:** respeitar sempre; trocar sweep por estado dim estático.
- **Densidade ALTA.** Agrônomos querem muito dado tabular na tela. Altura de linha padrão **40px**, não 56.

---

## 5. Iconografia

Sistema: **[Lucide](https://lucide.dev/)**, stroke, peso **1.5px** (no kit usa-se 1.75px em SVG inline), tamanho padrão 20px.

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<i data-lucide="sprout" style="width:20px;height:20px;stroke:var(--fg-2)"></i>
<script>lucide.createIcons();</script>
```

Glyphs agro úteis: `sprout, tractor, leaf, wheat, cloud-sun, droplets, bug, flask-conical, map, satellite, radar`.

**Regras**
- Um único peso de stroke. Não misture outline e filled.
- Ícone ativo/selecionado: `stroke: var(--brand-green)`, sem mudar fill.
- Em botão, ícone fica à **esquerda** do label, 8px de gap.
- Nunca troque ícone por emoji. Emoji só em conteúdo gerado por usuário real (ex.: chat).

---

## 6. Componentes (CSS de referência do UI kit)

Layout do app: topbar fixa **56px**, sidebar **220px**, painel inspector **360px** onde houver. Grid `220px 1fr` / `56px 1fr`; main interno `300px 1fr 360px` (lista · mapa · inspector).

### Botões
```css
.btn { display:inline-flex; align-items:center; gap:8px; font:600 13px var(--font-body);
       padding:8px 14px; border-radius:6px; border:none; cursor:pointer;
       transition: background var(--t-fast) var(--ease-out); }
.btn--primary        { background:var(--brand-green); color:#0B100B; }
.btn--primary:hover  { background:var(--brand-green-bright); }
/* pressionado: --brand-green-deep + translateY(1px). Sem scale. */
.btn--ghost          { background:transparent; color:var(--fg-1); border:1px solid var(--line-strong); }
.btn--ghost:hover    { background:rgba(82,201,55,0.08); color:var(--brand-green); border-color:var(--brand-green); }
.btn svg { width:14px; height:14px; stroke:currentColor; fill:none; stroke-width:1.75; }
```

### Inputs
```css
input { height:34px; background:var(--bg-2); border:1px solid var(--line);
        color:var(--fg-1); border-radius:6px; padding:0 12px; font:13px var(--font-body); outline:none; }
input:focus { border-color:var(--brand-green); box-shadow:0 0 0 1px rgba(82,201,55,0.4); }
```

### Chips (filtro)
```css
.chip { padding:4px 10px; border-radius:999px; font:500 11px var(--font-display);
        letter-spacing:0.06em; text-transform:uppercase; background:var(--bg-3);
        color:var(--fg-2); border:1px solid var(--line); cursor:pointer; }
.chip--on { border-color:var(--brand-green); color:var(--brand-green); background:rgba(82,201,55,0.08); }
```

### Status (pill com dot)
```css
.status { display:inline-flex; align-items:center; gap:6px; padding:3px 8px; border-radius:999px;
          font:600 9px var(--font-display); letter-spacing:0.08em; text-transform:uppercase; }
.status .dot { width:6px; height:6px; border-radius:50%; }
.status--ok    { background:rgba(82,201,55,0.12);  color:#6FE34F; }  /* dot #52C937 */
.status--warn  { background:rgba(232,179,59,0.12); color:#E8B33B; }  /* dot #E8B33B */
.status--alert { background:rgba(229,82,74,0.12);  color:#E5524A; }  /* dot #E5524A */
.status--info  { background:rgba(79,183,201,0.12); color:#4FB7C9; }  /* dot #4FB7C9 */
```

### Card de métrica
```css
.metric      { background:var(--bg-2); border:1px solid var(--line); border-radius:6px; padding:12px 14px; }
.metric__lbl { font:500 10px var(--font-display); letter-spacing:0.12em; text-transform:uppercase; color:var(--fg-3); }
.metric__val { font:500 26px/1 var(--font-mono); font-variant-numeric:tabular-nums; color:var(--fg-1); margin-top:6px; }
.metric__val .u     { font-size:13px; color:var(--fg-3); margin-left:4px; }   /* unidade */
.metric__delta      { font:500 11px var(--font-mono); color:var(--brand-green); margin-top:6px; }
```

### Alerta (inline)
```css
.alert       { display:flex; gap:10px; padding:10px 12px; border-radius:6px; border:1px solid; align-items:flex-start; }
.alert--warn { background:rgba(232,179,59,0.08); border-color:rgba(232,179,59,0.35); color:#E8B33B; }
.alert--ok   { background:rgba(82,201,55,0.08);  border-color:rgba(82,201,55,0.35);  color:#9BE05F; }
.alert__ttl  { font:600 11px var(--font-display); letter-spacing:0.08em; text-transform:uppercase; }
.alert__msg  { color:var(--fg-1); font-size:12px; line-height:1.5; margin-top:2px; }
```

### Linha de lista (talhão) e nav
```css
/* item de sidebar ativo: cor verde, bg rgba(82,201,55,0.06), border-left 2px verde */
/* hover em card/row: bg --bg-2 → --bg-3, barra verde 2px desliza de translateX(-4px) para 0 */
/* row de lista ativa: ::before barra verde 2px na borda esquerda */
```

---

## 7. Fundos e imagens

- Superfícies padrão: **plano escuro**. Sem textura.
- **Hero/login/marketing apenas:** foto aérea de campo dessaturada quase-monocromática (sépia quente ou verde frio) com gradiente preto de cima pra baixo. Imagem **nunca é decorativa** — sempre campos reais, drone, raster NDVI ou hardware em campo. Nada de foto de escritório, gradiente abstrato ou "fazenda gerada por IA".
- Fundos de dados (gráficos/mapas): `--bg-2`. Mapas: basemap escuro (ex.: dark Carto) com polígonos em verde da marca.
- Vidro/blur **raro**: scrim de modal `rgba(5,8,5,0.7)` + `backdrop-filter:blur(8px)`; sidebar sobre mapa `rgba(11,16,11,0.85)` + blur. Só isso.

---

## 8. Checklist rápido (antes de entregar)

- [ ] Fundo escuro `--bg-0`, cards `--bg-2` com hairline `--line`.
- [ ] Verde usado como destaque pontual, não como preenchimento genérico.
- [ ] Títulos em Chakra Petch itálico; corpo em Manrope; readouts em JetBrains Mono tabular.
- [ ] Eyebrow em CAIXA ALTA verde com tracking 0.18em; resto em sentence case.
- [ ] Cantos ≤ 12px (pill só em chip/filtro/avatar). Sem cantos bolha.
- [ ] Números em PT-BR com unidade e tabular-nums.
- [ ] Foco de input verde, nunca azul. Motion snappy, sem overshoot.
- [ ] Sem emoji no chrome. Ícones Lucide, um único peso de stroke.
- [ ] Copy em PT-BR, técnica e direta, termo agronômico correto.

---

## 9. Mascote — ClaudIA

**ClaudIA** é a assistente de IA da comunidade, de ponta a ponta: conduz o cadastro conversacional e é a face de todo assistente do produto (chat RAG, recomendações, notificações de IA).

- **Visual:** foto oficial — moça de boné verde-escuro com o broto neon da marca, fundo escuro (asset canônico: `public/claudia-avatar.png`, derivado do original `avatar claudIA.png`). Exibida sempre em recorte circular com borda `--line-strong`.
- **Componente canônico:** `components/brand/claudia-avatar.tsx` (`<ClaudiaAvatar size={n} />`). Não usar emoji, outra foto ou ilustração para representar a IA.
- **Voz:** a mesma do DS (§1) — direta, técnica, calorosa na medida; PT-BR; sem emoji nas falas dela (emoji só em conteúdo do usuário).
- **Uso:** toda superfície onde a IA "fala" mostra o avatar da ClaudIA + nome. Onde a IA apenas processa (badge de loading, telemetria), usar apenas o nó verde pulsante.

---

*Fonte: OagronomIA Design System. As telas do UI kit são inferências plausíveis e consistentes com a marca — quando houver codebase/Figma real, rederive os componentes de tela a partir da fonte.*
