# The official freedom L10n server (Called it LTenn-Server)

Get/Update/Upgrade/Push/Pull applications l10n files. A freedom TMS. With this
server you can create applications, manage, pull and push changes, remove,
update and make igrations to other languages in your l10n Applications.

## Models and Schema

You can see l10n class-diagram model schemas powered on **plantuml** by
[this](./docs/l10n_model.png) directed link.

## Access and Development (Api/Server/DB)

```bash
docker exec -it l10n_psql psql -U root -W l10n
# password: root
```

## TODO

- [ ] Make locale.json field to relational field
- [ ] Make Repo CRUD Apis
    - [ ] Create App [POST]
    - [ ] Get all Apps [GET]
    - [ ] Update App by id [PUT]
    - [ ] Delete App by id [DELETE]
- [ ] Make Locale Apis
    - [ ] Get all Locales [GET]
    - [ ] Create Locale [POST]
    - [ ] Update Locale by id [PUT]
    - [ ] Delete Locale by id [DELETE]
- [x] Create Authentications
    - [x] Generate JWT {access, refresh}
    - [x] Users
        - [x] Sign-up
        - [x] Sign-in
    - [ ] Validate user from header
- [x] Add CORS middleware

## To know: How it happened

- [ ] is require field detection in model?
- [ ] is data duplicate?