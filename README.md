# The official freedom L10n server (Called it LTenn-Server)

Get/Update/Upgrade/Push/Pull applications l10n files. A freedom TMS. With this
server you can create applications, manage, pull and push changes, remove,
update and make igrations to other languages in your l10n Applications.

## Models and Schema

You can see l10n class-diagram model schemas powered on plantuml by
[this](./docs/l10n_model.png) directed link

## Access and Development (Api/Server/DB)

```bash
docker exec -it l10n_psql psql -U root -W l10n
# password: root
```