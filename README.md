# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

## Estrutura

```
index.html            todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (cores, tipografia, layout, animações)
assets/js/main.js      menu mobile, scroll reveal, botão flutuante, links de WhatsApp,
                        setas prev/next do carrossel de testemunhos (#resultados)
```

## Sistema de design

Fonte de verdade: o comentário no topo de `assets/css/style.css` e os tokens
em `:root`. Nunca acrescentar uma cor ou um tamanho de heading novo diretamente
numa regra de componente — declarar/reutilizar um token primeiro.

**Cor.** Exatamente três cores em todo o projeto:

| Token | Hex | Uso |
|---|---|---|
| `--color-white` | `#FFFFFF` | fundo de página por defeito |
| `--color-cream` | `#F0EDE7` | a *outra* superfície — substitui todos os fundos fortes/escuros de antes (hero, footer, cartão de preço em destaque) e a alternância entre secções |
| `--color-teal` | `#1C3C3D` | o único acento — botões, links, ícones, badges e elementos selecionados/alta ênfase. Nunca usado como fundo de secção inteira |

Não existe uma terceira superfície nem uma escala de cinzentos à parte: texto
(`--ink`, `--ink-soft`, `--ink-faint`), contornos (`--line`/`--hairline`) e
sombras (`--shadow`) são todos tons/opacidades derivados do teal. `--on-accent`
(branco) é a única exceção — texto/ícone sobre um preenchimento sólido de teal
(botões, badge, botão flutuante). O placeholder de foto que resta
(`.ph-photo`, em Sobre) usa `color-mix()` para gerar o gradiente só a partir
de teal/creme/branco — nunca um cinzento à parte.

O verde do WhatsApp foi **removido** nesta revisão: os CTAs de WhatsApp usam
agora `--accent` (teal), por regra explícita do sistema de cores ("não
introduzir verdes, castanhos ou dourados não relacionados"). Se no futuro se
quiser reverter isto para o verde de marca do WhatsApp como exceção funcional,
é uma decisão a confirmar com o Isaías — não fazer sem validar.

Existe uma segunda exceção, também por pedido explícito: `--star` (`#76DB5D`)
é usado **só** nos ícones de classificação por estrelas (`.testimonial__stars`,
`.resultados__rating-stars`) — nunca noutro sítio. Não reutilizar este verde
para mais nada; se precisar de outro elemento "success/positivo" no futuro,
confirmar com o Isaías se deve ser este mesmo verde ou o teal do sistema.

**Tipografia.** Uma família geométrica sans-serif (Plus Jakarta Sans) em vários
pesos. Duas escalas de heading apenas:

- `--text-hero-size` — só o `<h1>` do hero. É o único heading intencionalmente maior.
- `--text-section-title-size` (aplicado via a classe `.section-title`) — todos
  os outros headings principais de secção (Sobre, Objetivos, Resultados,
  Localização, FAQ, Contacto), sem exceção. Qualquer h2 de
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
"Isaías Rocha — Briefing" — cópia sincronizada em
[`docs/business-requirements.md`](docs/business-requirements.md), com o link
para o Google Doc original. Qualquer novo facto, preço ou afirmação deve ser
confirmado com o Isaías antes de entrar no site.

Sistema de design, requisitos de negócio e material de marca estão organizados
em `docs/` — ver `docs/design-system.md` e `docs/business-requirements.md`.

**Secções removidas a pedido do cliente:** o site já não tem uma secção de
Método (o processo em 3 passos: "Falamos sobre ti" / "Avaliamos o ponto de
partida" / "Construímos e acompanhamos o teu treino") nem de Serviços
(cartões de preços: Avaliação, Personal Training 1:1 e a Dois). O briefing
continua a ter esse conteúdo — não foi apagado da fonte, só retirado do
site — por isso é normal reencontrá-lo lá se se voltar a consultar o
documento. Não repor estas secções sem confirmar com o Isaías.

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
3. **Fotografia** — dois tipos de placeholder ainda em uso, por substituir antes de publicar:
   - `.sobre__media .ph-photo` é um gradiente derivado de teal/creme via `color-mix()` (ver
     `assets/css/style.css`) — trocar o `<div class="ph-photo">` por `<img>`, mantendo o cartão
     `.sobre__caption` sobreposto no canto inferior da foto.
   - Os 3 cartões de `.loc-grid` (VivaGym / Ao domicílio / Outdoor) e a foto de `.contacto__media`
     já usam `<img>` reais, mas `assets/img/loc-vivagym.jpg`, `loc-domicilio.jpg`,
     `loc-outdoor.jpg` e `contacto-desafio.jpg` são **fotos de stock genéricas** — não são o
     Isaías nem os seus clientes reais. Servem só para pré-visualizar as secções; substituir
     pelos ficheiros reais (mesmos nomes, para não precisar de tocar no HTML) antes de publicar.

   A foto do hero já é real (`assets/img/isaias-hero.webp`).
4. **Localização** — o botão "Ver localização no Google Maps" no cartão da VivaGym já aponta
   para uma pesquisa real da VivaGym Almirante Reis. Não há mapa incorporado nesta secção
   (substituído por 3 cartões com foto); adicionar um embed (iframe) só se o Isaías preferir
   ter o mapa visível diretamente na página.
5. **Contacto** — o briefing só menciona WhatsApp como canal de marcação; não há e-mail nem
   Instagram confirmados, por isso não aparecem no site. Adicionar em `#contacto` (e no
   JSON-LD no `<head>`) se o Isaías quiser divulgá-los.

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
