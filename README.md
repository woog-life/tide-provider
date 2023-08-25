tide-provider
===

Parses tide information retrieved from the [Federal Maritime and Hydrographic Agency of Germany
(Bundesamt für Seeschifffahrt und Hydrographie)][bsh] and provides information to the
[woog-life API][woog-api].

Files are downloaded as `txt-Datei (HW/NW)` with the respective location/year.

See [format_description.txt](format_description.txt) for details on the format. We're not following
that description exactly since we've seen discrepancies in the actual data (see code comments).

[bsh]: https://www.bsh.de/DE/DATEN/Vorhersagen/Gezeiten/gezeiten_node.html
[woog-api]: https://api.woog.life
