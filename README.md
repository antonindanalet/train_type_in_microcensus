# Train type in the Mobility and Transport Microcensus (MTMC) 2021

This code describes how the variable about the type of train has been generated in the MTMC dataset 2021.

The original variables in the trip leg file (etappen.csv) are:

| Variable | Label (EN)                          | Label (DE)               |
| -------- | ----------------------------------- | ------------------------ |
| hhnr   	| Household ID number                  | Haushaltnummer           |
| etnr	  | Trip leg ID number                   | Etappennummer            |
| HAF_FID	| Old (2015) name of the variable      |                          |
| f51300	| Transport mode used for the trip leg | Benutztes Verkehrsmittel |

The variables that are added by this code are:

| Variable   | Label (EN)                                                    | Label (DE)                                                 |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| route_id	 | Route ID in GTFS timetable                                    | Routennummer im GTFS-Fahrplan                              |
| trip_id	   | Trip ID in GTFS timetable (new name for HAF_ID, same content) | Reisenummer im GTFS-Fahrplan (neue Name für HAF_ID)        |
| route_desc | Transport mode in GTFS timetable (from file routes.txt)       | Verkehrsmittel im GTFS-Fahrplan (aus der Datei routes.txt) |
| zugtyp     | Type of train according to HRDF file 'ZUGART'                 | Zugtyp                                                     |

The route_desc variable is coded as follows:

| Value | Label (DE)                                                  | Label (FR)                                  | Label (IT)                          | Label (EN)                                |
|-------|-------------------------------------------------------------|---------------------------------------------|-------------------------------------|-------------------------------------------|
| 1     | Aufzug (Kodierung GTFS 2022: "ASC")                         | Ascenseur                                   | Ascensore                           | Lift                                      |
| 2     | Bus (Kodierung GTFS 2022: "B")                              | Bus                                         | Bus                                 | Bus                                       |
| 3     | Schiff (Kodierung GTFS 2022: "BAT")                         | Bateau                                      | Battello                            | Ship                                      |
| 4     | Nachtbus (Kodierung GTFS 2022: "BN")                        | Bus ligne de nuit                           | Bus notturno                        | Nightbus                                  |
| 5     | PanoramaBus (Kodierung GTFS 2022: "BP")                     | PanoramaBus                                 | Bus panoramico                      | Panorama bus                              |
| 7     | Fernbus national (Kodierung GTFS 2022: "CAR")               | Bus longues distances national              | Bus nazionale a lunga percorrenza   | National long-distance bus                |
| 8     | Zahnradbahn (Kodierung GTFS 2022: "CC")                     | Chemin de fer à crémaillère                 | Cremagliera                         | Rack-railroad                             |
| 9     | EuroCity (Kodierung GTFS 2022: "EC")                        | EuroCity                                    | EuroCity                            | EuroCity                                  |
| 10    | Expressbus (Kodierung GTFS 2022: "EXB")                     | Bus express                                 | Bus espresso                        | Express bus                               |
| 11    | Extrazug (Kodierung GTFS 2022: "EXT")                       | Train spécial                               | Treno speciale                      | Special train                             |
| 12    | Fähre (Kodierung GTFS 2022: "FAE")                          | Bac                                         | Traghetto                           | Ferry-boat                                |
| 13    | Standseilbahn (Kodierung 2022: "FUN")                       | Funiculaire                                 | Funicolare                          | Funicular                                 |
| 14    | Gondelbahn (Kodierung GTFS 2022: "GB")                      | Télécabine                                  | Cabinovia                           | Gondola lift                              |
| 15    | InterCity (Kodierung GTFS 2022: "IC")                       | InterCity                                   | InterCity                           | InterCity                                 |
| 16    | InterCityExpress (Kodierung GTFS 2022: "ICE")               | InterCityExpress                            | InterCityExpress                    | InterCityExpress                          |
| 17    | InterRegio (Kodierung GTFS 2022: "IR")                      | InterRegio                                  | InterRegio                          | InterRegio                                |
| 18    | Interregio-Express (Kodierung GTFS 2022: "IRE")             | Interregio-Express                          | Interregio-Express                  | Interregio-Express                        |
| 19    | Kleinbus                                                    | Minibus                                     | Minibus                             | Minibus                                   |
| 20    | Metro (Kodierung GTFS 2022: "M")                            | Métro                                       | Metropolitana                       | Underground                               |
| 21    | LeermaterialZ (Reisezugswagen) (Kodierung GTFS 2022: "MAT") | Train de matériel vide (voitures voyageurs) | Materiale vuoto (treno viaggiatori) | Empty material train (passenger carriage) |
| 22    | nightjet (Kodierung GTFS 2022: "NJ")                        | nightjet                                    | nightjet                            | nightjet                                  |
| 23    | Pendelbahn (Kodierung GTFS 2022: "PB")                      | Téléphérique à va-et-vient                  | funivia a va e vieni                | aerial tramway                            |
| 24    | PanoramaExpress (Kodierung GTFS 2022: "PE")                 | PanoramaExpress                             | PanoramaExpress                     | PanoramaExpress                           |
| 25    | Regio (Kodierung GTFS 2022: "R")                            | Regio                                       | Regio                               | Regio                                     |
| 26    | Regionalbahn (Kodierung GTFS 2022: "RB")                    | Train régional                              | Ferrovia regionale                  | Regional train                            |
| 27    | RegioExpress (Kodierung GTFS 2022: "RE")                    | RegioExpress                                | RegioExpress                        | RegioExpress                              |
| 28    | railjet xpress (Kodierung GTFS 2022: "RJX")                 | railjet xpress                              | railjet xpress                      | railjet xpress                            |
| 29    | Rufbus (Kodierung GTFS 2022: "RUB")                         | Bus sur appel                               | bus a chiamata                      | On-call bus                               |
| 30    | S-Bahn (Kodierung GTFS 2022: "S")                           | RER                                         | Rete celere                         | Urban train                               |
| 31    | Sesselbahn (Kodierung GTFS 2022: "SL")                      | Télésiège                                   | Seggiovia                           | Chairlift                                 |
| 32    | Nacht-S-Bahn (Kodierung GTFS 2022: "SN")                    | RER-nuit                                    | Rete celere notte                   | Night-urban train                         |
| 33    | Tram (Kodierung GTFS 2022: "T")                             | Tram                                        | Tram                                | Tramway                                   |
| 34    | Train Express Regional (Kodierung GTFS 2022: "TER")         | Train Express Regional                      | Train Express Regional              | Train Express Regional                    |
| 35    | Train à grande vitesse (codage GTFS 2022: "TGV")            | Train à grande vitesse                      | Train à grande vitesse              | Train à grande vitesse                    |
| 36    | Taxi (Kodierung GTFS 2022: "TX")                            | Taxi                                        | Taxi                                | Taxi                                      |
| 37    | Agenturzug (Kodierung GTFS 2022: "AG")                      | Train d'agence                              | Treno d'agenzia                     | Agencytrain                               |

The zugtyp variable / type of train is coded as follows:

| Value | Label (EN)                                               | Label (DE)                                      |
|-------|----------------------------------------------------------|-------------------------------------------------|
| -99   | Transport mode is not train                              | f51300 ungleich 9                               |
| -97   | No matching found                                        | Zugtyp konnte nicht zugewiesen werden           |
| 0     | ICE/EN/CNL/CIS/ES/MET/NZ/PEN/TGV/THA/X2                  | ICE/EN/CNL/CIS/ES/MET/NZ/PEN/TGV/THA/X2         |
| 1     | EuroCity/InterCity/ICN/InterCityNight/SuperCity          | EuroCity/InterCity/ICN/InterCityNight/SuperCity |
| 2     | InterRegio                                               | InterRegio                                      |
| 3     | Fast train/RegioExpress                                  | Schnellzug/RegioExpress                         |
| 5     | Urban railway/StadtExpress/Semi fast train/Omnibus train | S-Bahn/StadtExpress/Eilzug/Regionalzug          |

The aggregation key can be found <a href="https://github.com/antonindanalet/train_type_in_microcensus/blob/master/src/run_train_type_in_microcensus.py#L50">in the code</a> or in the <a href="https://github.com/antonindanalet/train_type_in_microcensus/blob/master/data/input/hrdf/ZUGART">ZUGART file</a> from the HRDF timetable.
