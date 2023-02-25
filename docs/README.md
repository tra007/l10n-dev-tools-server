# Documents, Researches, Usages, Developments

- How I handled indexes. [Read](https://en.wikipedia.org/wiki/Database_index)


## Backup and restore database in psql

```bash
docker exec -u root l10n_psql pg_dump -Fc l10n > db.dump # Dump and backup
docker exec -i -u root l10n_psql pg_restore -C -D postgres < db.dump # Restore
```