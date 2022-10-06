# Train type in the Mobility and Transport Microcensus (MTMC) 2021

This code describes how the variable about the type of train has been generated in the MTMC dataset 2021.

The original variables in the trip leg file (etappen.csv) are:

| Variable | Label | 
| --- | --- | 
| hhnr	| Household ID number | 
| etnr	| Trip leg ID number | 
| HAF_FID	| Old (2015) name of the variable | 
| f51300	| Transport mode used for the trip leg | 

The variables that are added by this code are:

| Variable | Label |
| --- | --- | 
| route_id	| Route ID in GTFS timetable | 
| trip_id	| Trip ID in GTFS timetable (new name for the variable HAF_ID, same content) | 
| route_desc |	Transport mode in GTFS timetable (from file routes.txt) | 
| zugtyp | Type of train | 

The route_desc variable is coded as follows:

| Value | Label (DE)                                                  | Label (FR)                                  | Label (IT)                          | Label (EN)                                |
|-------|-------------------------------------------------------------|---------------------------------------------|-------------------------------------|-------------------------------------------|
| 1     | Tram (Kodierung GTFS 2022: "T")                             | Tram                                        | Tram                                | Tramway                                   |
| 2     | S-Bahn (Kodierung GTFS 2022: "S")                           | RER                                         | Rete celere                         | Urban train                               |
| 3     | RegioExpress (Kodierung GTFS 2022: "RE")                    | RegioExpress                                | RegioExpress                        | RegioExpress                              |
| 4     | Regio (Kodierung GTFS 2022: "R")                            | Regio                                       | Regio                               | Regio                                     |
| 5     | Regionalbahn (Kodierung GTFS 2022: "RB")                    | Train régional                              | Ferrovia regionale                  | Regional train                            |
| 6     | InterRegio (Kodierung GTFS 2022: "IR")                      | InterRegio                                  | InterRegio                          | InterRegio                                |
| 7     | Train Express Regional (Kodierung GTFS 2022: "TER")         | Train Express Regional                      | Train Express Regional              | Train Express Regional                    |
| 8     | Expressbus (Kodierung GTFS 2022: "EXB")                     | Bus express                                 | Bus espresso                        | Express bus                               |
| 9     | Train à grande vitesse (codage GTFS 2022: "TGV")            | Train à grande vitesse                      | Train à grande vitesse              | Train à grande vitesse                    |
| 10    | InterCity (Kodierung GTFS 2022: "IC")                       | InterCity                                   | InterCity                           | InterCity                                 |
| 11    | InterCityExpress (Kodierung GTFS 2022: "ICE")               | InterCityExpress                            | InterCityExpress                    | InterCityExpress                          |
| 12    | EuroCity (Kodierung GTFS 2022: "EC")                        | EuroCity                                    | EuroCity                            | EuroCity                                  |
| 13    | PanoramaExpress (Kodierung GTFS 2022: "PE")                 | PanoramaExpress                             | PanoramaExpress                     | PanoramaExpress                           |
| 14    | Extrazug (Kodierung GTFS 2022: "EXT")                       | Train spécial                               | Treno speciale                      | Special train                             |
| 15    | Interregio-Express (Kodierung GTFS 2022: "IRE")             | Interregio-Express                          | Interregio-Express                  | Interregio-Express                        |
| 16    | railjet xpress (Kodierung GTFS 2022: "RJX")                 | railjet xpress                              | railjet xpress                      | railjet xpress                            |
| 17    | Nacht-S-Bahn (Kodierung GTFS 2022: "SN")                    | RER-nuit                                    | Rete celere notte                   | Night-urban train                         |
| 18    | nightjet (Kodierung GTFS 2022: "NJ")                        | nightjet                                    | nightjet                            | nightjet                                  |
| 19    | Metro (Kodierung GTFS 2022: "M")                            | Métro                                       | Metropolitana                       | Underground                               |
| 20    | Bus (Kodierung GTFS 2022: "B")                              | Bus                                         | Bus                                 | Bus                                       |
| 21    | Taxi (Kodierung GTFS 2022: "TX")                            | Taxi                                        | Taxi                                | Taxi                                      |
| 22    | Rufbus (Kodierung GTFS 2022: "RUB")                         | Bus sur appel                               | bus a chiamata                      | On-call bus                               |
| 23    | Kleinbus                                                    | Minibus                                     | Minibus                             | Minibus                                   |
| 24    | Nachtbus (Kodierung GTFS 2022: "BN")                        | Bus ligne de nuit                           | Bus notturno                        | Nightbus                                  |
| 25    | PanoramaBus (Kodierung GTFS 2022: "BP")                     | PanoramaBus                                 | Bus panoramico                      | Panorama bus                              |
| 26    | Fernbus national (Kodierung GTFS 2022: "CAR")               | Bus longues distances national              | Bus nazionale a lunga percorrenza   | National long-distance bus                |
| 27    | Gondelbahn (Kodierung GTFS 2022: "GB")                      | Télécabine                                  | Cabinovia                           | Gondola lift                              |
| 28    | Sesselbahn (Kodierung GTFS 2022: "SL")                      | Télésiège                                   | Seggiovia                           | Chairlift                                 |
| 29    | Pendelbahn (Kodierung GTFS 2022: "PB")                      | Téléphérique à va-et-vient                  | funivia a va e vieni                | aerial tramway                            |
| 30    | Standseilbahn (Kodierung 2022: "FUN")                       | Funiculaire                                 | Funicolare                          | Funicular                                 |
| 31    | Aufzug (Kodierung GTFS 2022: "ASC")                         | Ascenseur                                   | Ascensore                           | Lift                                      |
| 32    | Zahnradbahn (Kodierung GTFS 2022: "CC")                     | Chemin de fer à crémaillère                 | Cremagliera                         | Rack-railroad                             |
| 33    | Schiff (Kodierung GTFS 2022: "BAT")                         | Bateau                                      | Battello                            | Ship                                      |
| 34    | Fähre (Kodierung GTFS 2022: "FAE")                          | Bac                                         | Traghetto                           | Ferry-boat                                |
| 35    | LeermaterialZ (Reisezugswagen) (Kodierung GTFS 2022: "MAT") | Train de matériel vide (voitures voyageurs) | Materiale vuoto (treno viaggiatori) | Empty material train (passenger carriage) |
| 36    | Agenturzug (Kodierung GTFS 2022: "AG")                      | Train d'agence                              | Treno d'agenzia                     | Agencytrain                               |

The zugtyp variable / type of train is coded as follows:

| Value | Label                                           |
|-------|-------------------------------------------------|
| -99   | Transport mode is not train                     |
| -97   | No matching found                               |
| 0     | ICE/EN/CNL/CIS/ES/MET/NZ/PEN/TGV/THA/X2         |
| 1     | EuroCity/InterCity/ICN/InterCityNight/SuperCity |
| 2     | InterRegio                                      |
| 3     | RegioExpress                                    |
| 5     | S-Bahn/StadtExpress/Eilzug/Regionalzug          |

The aggregation key can be found <a href="https://github.com/antonindanalet/train_type_in_microcensus/blob/master/src/run_train_type_in_microcensus.py#L50">in the code</a>.
