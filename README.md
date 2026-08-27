# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

## Estrutura

```
index.html            todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (cores, tipografia, layout, animações)
assets/js/main.js      menu mobile, scroll reveal, botão flutuante, links de WhatsApp
```

## Sistema de design

Fonte de verdade: o comentário no topo de `assets/css/style.css` e os tokens
em `:root`. Nunca acrescentar uma cor ou um tamanho de heading novo diretamente
numa regra de componente — declarar/reutilizar um token primeiro.

**Cor.** Exatamente três cores em todo o projeto:

| Token | Hex | Uso |
|---|---|---|
| `--color-white` | `#FFFFFF` | fundo de página por defeito |
| `--color-cream` | `#F0EDE7` | a *outra* superfície — substitui todos os fundos fortes/escuros de antes (hero, footer, cartão de preço em destaque, banner "Mostra", avatares) e a alternância entre secções |
| `--color-teal` | `#1C3C3D` | o único acento — botões, links, ícones, badges e elementos selecionados/alta ênfase. Nunca usado como fundo de secção inteira |

Não existe uma terceira superfície nem uma escala de cinzentos à parte: texto
(`--ink`, `--ink-soft`, `--ink-faint`), contornos (`--line`/`--hairline`) e
sombras (`--shadow`) são todos tons/opacidades derivados do teal. `--on-accent`
(branco) é a única exceção — texto/ícone sobre um preenchimento sólido de teal
(botões, badge, botão flutuante). Os placeholders de foto (`.ph-photo`, em
Sobre e Mostra) usam `color-mix()` para gerar o gradiente só a partir de
teal/creme/branco — nunca um cinzento à parte.

O verde do WhatsApp foi **removido** nesta revisão: os CTAs de WhatsApp usam
agora `--accent` (teal), por regra explícita do sistema de cores ("não
introduzir verdes, castanhos ou dourados não relacionados"). Se no futuro se
quiser reverter isto para o verde de marca do WhatsApp como exceção funcional,
é uma decisão a confirmar com o Isaías — não fazer sem validar.

**Tipografia.** Uma família geométrica sans-serif (Plus Jakarta Sans) em vários
pesos. Duas escalas de heading apenas:

- `--text-hero-size` — só o `<h1>` do hero. É o único heading intencionalmente maior.
- `--text-section-title-size` (aplicado via a classe `.section-title`) — todos
  os outros headings principais de secção (Sobre, Objetivos, Método, Serviços,
  Resultados, Mostra, Localização, FAQ, Contacto), sem exceção. Qualquer h2 de
  secção novo tem de levar a classe `.section-title`; ajustar só `max-width`
  por secção se for preciso controlar a quebra de linha, nunca o `font-size`.

Eyebrows/labels de secção partilham um único conjunto de tokens (`--eyebrow-size`
/ `--eyebrow-weight` / `--eyebrow-tracking`) via a classe `.eyebrow`, já
aplicada de forma consistente em todas as secções.

**Layout.** Cantos bem arredondados (36px em cartões via `--radius-card`, 14px
em botões via `--radius-btn`, pill em badges/chips via `--radius-pill`) e
contornos finos de 1px (`--hairline`) a substituir sombras como principal
ferramenta de elevação — inalterado desde a base original (referência Awesomic,
styles.refero.design).

## Fonte de verdade do conteúdo

Todo o texto (bio, certificações, método, preços, localização) vem do documento
"Isaías Rocha — Briefing". Qualquer novo facto, preço ou afirmação deve ser
confirmado com o Isaías antes de entrar no site.

**Exceção conhecida — `#resultados`:** o briefing não tem testemunhos de
clientes reais (sem nomes, fotos ou classificações). Os 3 cartões de
testemunho nessa secção usam nomes, avatares (iniciais sobre gradiente,
não fotos reais de ninguém) e classificações de 5 estrelas **fictícios**,
a pedido explícito, só para pré-visualizar o layout. Isto está marcado com
um comentário HTML antes da secção em `index.html`. **Substituir por
testemunhos reais (idealmente com consentimento explícito para usar nome
e foto) antes de publicar** — os textos completos podem ficar como ponto
de partida se um cliente real disser algo semelhante.

## Antes de publicar

1. **Número de WhatsApp** — editar `WHATSAPP_NUMBER` em `assets/js/main.js` (linha ~10).
   Todos os botões "WhatsApp" / "Falar comigo no WhatsApp" leem deste único sítio.
   O briefing não indica um número — está por confirmar.
2. **Testemunhos (`#resultados`)** — nomes, avatares e classificações são fictícios
   (ver acima). Substituir pelos 3 testemunhos reais antes de publicar.
3. **Fotografia (Sobre + Mostra + Contacto)** — `.sobre__media .ph-photo`, os dois `.ph-photo` da
   secção `.mostra` (entre Resultados e Localização) e o `.ph-photo` de `.contacto__media` em
   `assets/css/style.css` são gradientes placeholder derivados de teal/creme (a foto do hero já
   é real — `assets/img/isaias-hero.webp`). Substituir os quatro por fotos reais (do Isaías e de
   sessões de treino) antes de publicar — trocar o `<div class="ph-photo">` por `<img>`, mantendo
   o cartão `.sobre__caption` sobreposto no canto inferior da foto do Sobre.
4. **Mapa (Localização)** — `.loc-map` é uma grelha CSS com um pin decorativo. O botão "Ver
   localização no Google Maps" já aponta para uma pesquisa real da VivaGym Almirante Reis;
   pode ser substituído por um embed (iframe) se preferires um mapa incorporado.
5. **Contacto** — o briefing só menciona WhatsApp como canal de marcação; não há e-mail nem
   Instagram confirmados, por isso não aparecem no site. Adicionar em `#contacto` (e no
   JSON-LD no `<head>`) se o Isaías quiser divulgá-los.
6. **Preços e serviços** — confirmar que os valores em `#servicos` (Avaliação 50€, Personal
   Training 1:1 e a Dois) continuam atualizados antes de publicar; são os do briefing mas
   podem mudar com o tempo.

## Adicionar versão em inglês

O conteúdo está isolado do layout (nenhum texto está "cozido" em CSS/imagens), pelo que basta:

1. Duplicar `index.html` como `en.html`.
2. Traduzir apenas os nós de texto — manter classes, ids e estrutura intactos.
3. Adicionar um seletor de idioma na nav (`.nav__links`) a apontar `index.html` ⇄ `en.html`.

## Correr localmente

Qualquer servidor estático funciona, por exemplo:

```
python3 -m http.server 8000
```

depois abrir `http://localhost:8000`.
