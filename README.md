# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

## Estrutura

```
index.html            todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (cores, tipografia, layout, animações)
assets/js/main.js      menu mobile, scroll reveal, botão flutuante, links de WhatsApp
```

## Antes de publicar

1. **Número de WhatsApp** — editar `WHATSAPP_NUMBER` em `assets/js/main.js` (linha ~10).
   Todos os botões "WhatsApp" / "Marcar avaliação gratuita" leem deste único sítio.
2. **Fotografia (Sobre)** — `.sobre__media .ph-photo` em `assets/css/style.css` é um gradiente
   dourado/castanho placeholder. Substituir por uma foto real do Isaías (`background-image`
   ou trocar por `<img>`), mantendo o cartão `.sobre__caption` sobreposto no canto inferior.
3. **Mapa (Localização)** — `.loc-map` é uma grelha CSS com um pin decorativo. Substituir por
   um embed do Google Maps (iframe) apontado à morada/zona real, dentro do mesmo `.loc-card`.
4. **Contactos** — atualizar e-mail e Instagram na secção `#contacto`.
5. **Textos e preços** — reviews, credenciais, estatísticas e os 3 planos em `#servicos`
   (Sessão Avulsa 45€, Acompanhamento Mensal 320€, Transformação 12 Semanas 850€) são
   exemplos de referência — confirmar valores e nomes reais antes de publicar.

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
