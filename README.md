# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

## Estrutura

```
index.html            todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (cores, tipografia, layout, animações)
assets/js/main.js      menu mobile, scroll reveal, botão flutuante, links de WhatsApp
```

## Fonte de verdade do conteúdo

Todo o texto (bio, certificações, método, preços, localização) vem do documento
"Isaías Rocha — Briefing". Não há reviews de clientes reais nesse documento, por
isso a secção `#resultados` foi escrita como conteúdo motivacional/aspiracional
em vez de testemunhos inventados — ver nota no próprio `index.html`. Qualquer
novo facto, preço ou afirmação deve ser confirmado com o Isaías antes de entrar
no site.

## Antes de publicar

1. **Número de WhatsApp** — editar `WHATSAPP_NUMBER` em `assets/js/main.js` (linha ~10).
   Todos os botões "WhatsApp" / "Falar comigo no WhatsApp" leem deste único sítio.
   O briefing não indica um número — está por confirmar.
2. **Fotografia (Sobre)** — `.sobre__media .ph-photo` em `assets/css/style.css` é um gradiente
   dourado/castanho placeholder. Substituir por uma foto real do Isaías (`background-image`
   ou trocar por `<img>`), mantendo o cartão `.sobre__caption` sobreposto no canto inferior.
3. **Mapa (Localização)** — `.loc-map` é uma grelha CSS com um pin decorativo. O botão "Ver
   localização no Google Maps" já aponta para uma pesquisa real da VivaGym Almirante Reis;
   pode ser substituído por um embed (iframe) se preferires um mapa incorporado.
4. **Contacto** — o briefing só menciona WhatsApp como canal de marcação; não há e-mail nem
   Instagram confirmados, por isso não aparecem no site. Adicionar em `#contacto` (e no
   JSON-LD no `<head>`) se o Isaías quiser divulgá-los.
5. **Preços e serviços** — confirmar que os valores em `#servicos` (Avaliação 50€, Personal
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
