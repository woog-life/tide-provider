tide-provider
===

parses tide information retrieved from [Federal Maritime and Hydrographic Agency of Germany (Bundesamt für Seeschifffahrt und Hydrographie)](https://www.bsh.de/DE/DATEN/Vorhersagen/Gezeiten/gezeiten_node.html) and provides information to the [woog-life api](https://api.woog.life).

Files are downloaded as `txt-Datei (HW/NW)` with the respective location/year.

See [format_description.md](format_description.md) for details on the format, we're not following these information exactly since we've seen discrepencies in the actual data (see code comments).
