# Design system — Isaías Rocha

Fonte de verdade real: o comentário no topo de `assets/css/style.css` e os
tokens em `:root`. Este ficheiro é um resumo de referência rápida — se
algo aqui contradisser o CSS, o CSS ganha.

**Referência visual:** [claude.ai/code/artifact/9bb04b2c-c9c0-41e9-891a-9d2990008e3f](https://claude.ai/code/artifact/9bb04b2c-c9c0-41e9-891a-9d2990008e3f)
(gerada diretamente a partir do CSS — pedir para regenerar sempre que o
sistema mudar).

## Cor

Exatamente três cores em todo o projeto:

| Token | Hex | Uso |
|---|---|---|
| `--color-white` | `#FFFFFF` | fundo de página por defeito |
| `--color-cream` | `#F0EDE7` | a outra superfície — hero, footer, alternância entre secções |
| `--color-teal` | `#1C3C3D` | único acento — botões, links, ícones, badges |

Tudo o resto (texto, contornos, sombras) é um tom/opacidade derivado do
teal via `--ink`, `--ink-soft`, `--ink-faint`, `--line`, `--shadow`.
`--on-accent` (branco) é texto sobre teal sólido. `--star` (`#76DB5D`) é
uma exceção isolada, só para os ícones de classificação por estrelas.

## Tipografia

Duas famílias:

- **Plus Jakarta Sans** — tudo o que é funcional: nav, corpo de texto,
  botões, labels, eyebrows, headlines de testemunhos.
- **Newsreader** (`--font-serif`) — reservada exclusivamente aos títulos
  principais: `.hero__title` e todos os `.section-title`. Ambos partilham
  a mesma família, peso (500) e tracking (-0.01em); só o tamanho difere
  (`--text-hero-size` vs. `--text-section-title-size`). Nenhum outro
  heading deve usar esta serif — é o contraste com o resto do texto que
  faz o título "ler-se" como título.

## Layout

- Cantos: `--radius-btn` (14px, botões/linhas), `--radius-card` (36px,
  cartões/fotos), `--radius-pill` (9999px, badges/chips).
- Contornos finos de 1px (`--hairline`) em vez de sombras, como
  ferramenta principal de elevação.
- Container: `--container` (1320px máx.).

## Regra ao adicionar algo novo

Nunca introduzir uma cor, tamanho de heading ou família tipográfica nova
diretamente numa regra de componente — declarar/reutilizar um token no
`:root` primeiro. Qualquer heading de secção novo leva `.section-title`;
qualquer novo título ao nível de página segue o mesmo tratamento do
`.hero__title`.
