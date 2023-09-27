tide-provider
===

## Germany

Parses tide information retrieved from the [Federal Maritime and Hydrographic Agency of Germany
(Bundesamt für Seeschifffahrt und Hydrographie)][bsh] and provides information to the
[woog-life API][woog-api].

Files are downloaded as `txt-Datei (HW/NW)` with the respective location/year.

See [format_description.txt](format_description.txt) for details on the format. We're not following
that description exactly since we've seen discrepancies in the actual data (see code comments).

## Canada

Parses info from [Government of Canada](https://www.tides.gc.ca/en/stations/07735/predictions/annual) and provides information to the [woog-life API][woog-api].

For this there is no official format description since it's simply a CSV with the following headers `Date and time (PDT),Metres`

[bsh]: https://www.bsh.de/DE/DATEN/Vorhersagen/Gezeiten/gezeiten_node.html
[woog-api]: https://api.woog.life
