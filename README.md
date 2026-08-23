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
   Todos os botões "Falar no WhatsApp" / "Marcar sessão" leem deste único sítio.
2. **Fotografias** — as imagens atuais são placeholders do Unsplash (a preto e branco/duotone
   via CSS). Substituir os `src` das `<img>` em Hero, Sobre e Serviços por fotografia real
   do Isaías (idealmente still shots de treino, retrato editorial, mesma paleta tonal).
3. **Contactos** — atualizar e-mail e Instagram na secção `#contacto`.
4. **Mapa** — o iframe do Google Maps na secção `#localizacao` mostra Lisboa de forma genérica;
   pode ser substituído por um embed apontado à morada exata do estúdio.
5. **Textos** — reviews, credenciais e estatísticas (anos de experiência, nº clientes) são
   exemplos de referência — confirmar valores reais.

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
