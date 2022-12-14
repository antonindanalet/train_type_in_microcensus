from utils_mtmc.get_mtmc_files import *
from pathlib import Path
import pandas as pd


def run_train_type_in_microcensus():
    df_etappen = get_etappen(2021, selected_columns=['hhnr', 'etnr', 'f51300', 'HAF_FID'])
    ''' Since there are data collected after the change of timetable in December 2021, also get the 2022 timetable '''
    for year in [2021, 2022]:
        df_trips = read_gtfs_trips(year)  # get trips id & route id
        df_routes = read_gtfs_routes(year)  # get route id and route description
        df_trips = pd.merge(df_trips, df_routes, on='route_id', how='left')  # get trips id with route description
        df_trips = add_type_abbreviation(df_trips)  # aggregate route description in 5 categories compatible with 2015
        df_etappen = pd.merge(df_etappen, df_trips, left_on='HAF_FID', right_on='trip_id', how='left')
        df_etappen.rename({'route_id': 'route_id_' + str(year),
                           'trip_id': 'trip_id_' + str(year),
                           'route_desc': 'route_desc_' + str(year),
                           'zugtyp': 'zugtyp_' + str(year)}, axis=1, inplace=True)
    ''' Merge both years '''
    condition_2021 = ~df_etappen['route_id_2021'].isna()
    df_etappen.loc[condition_2021, 'route_id'] = df_etappen['route_id_2021']
    df_etappen.loc[condition_2021, 'trip_id'] = df_etappen['trip_id_2021']
    df_etappen.loc[condition_2021, 'route_desc'] = df_etappen['route_desc_2021']
    df_etappen.loc[condition_2021, 'zugtyp'] = df_etappen['zugtyp_2021']
    del df_etappen['route_id_2021']
    del df_etappen['trip_id_2021']
    del df_etappen['route_desc_2021']
    del df_etappen['zugtyp_2021']
    condition_2022 = ~df_etappen['route_id_2022'].isna()
    df_etappen.loc[condition_2022, 'route_id'] = df_etappen['route_id_2022']
    df_etappen.loc[condition_2022, 'trip_id'] = df_etappen['trip_id_2022']
    df_etappen.loc[condition_2022, 'route_desc'] = df_etappen['route_desc_2022']
    df_etappen.loc[condition_2022, 'zugtyp'] = df_etappen['zugtyp_2022']
    del df_etappen['route_id_2022']
    del df_etappen['trip_id_2022']
    del df_etappen['route_desc_2022']
    del df_etappen['zugtyp_2022']
    ''' Code the route description as numerical codes '''
    df_etappen = recode_route_desc(df_etappen)
    df_etappen.to_csv('../data/output/2021/etappen_with_train_type.csv', index=False)


def add_type_abbreviation(df_trips):
    """ Categories:
    0 ICE/EN/CNL/CIS/ES/MET/NZ/PEN/TGV/THA/X2
    1 EuroCity/InterCity/ICN/InterCityNight/SuperCity
    2 InterRegio
    3 Fast train/RegioExpress
    5 Urban railway/StadtExpress/Semi fast train/Omnibus train """
    dict_abbreviation = {'Tram': -99,  # 2021 codes
                         'S-Bahn': 5,  # 2021 codes
                         'RegioExpress': 3,  # 2021 codes
                         'Regio': 5,  # 2021 codes
                         'Regionalbahn': 3,  # 2021 codes
                         'InterRegio': 2,  # 2021 codes
                         'Train Express Regional': 5,  # 2021 codes
                         'Expressbus': -99,  # 2021 codes
                         'Train ??? grande vit.': 0,  # 2021 codes
                         'InterCity': 1,  # 2021 codes
                         'InterCityExpress': 2,  # 2021 codes
                         'EuroCity': 1,  # 2021 codes
                         'PanoramaExpress': 2,  # 2021 codes
                         'Extrazug': -99,  # 2021 codes
                         'Interregio-Express': 3,  # 2021 codes
                         'railjet xpress': 0,  # 2021 codes
                         'Nacht-S-Bahn': 5,  # 2021 codes
                         'nightjet': 0,  # 2021 codes
                         'Metro': -99,  # 2021 codes
                         'Bus': -99,  # 2021 codes
                         'Taxi': -99,  # 2021 codes
                         'Rufbus': -99,  # 2021 codes
                         'Kleinbus': -99,  # 2021 codes
                         'Nachtbus': -99,  # 2021 codes
                         'PanoramaBus': -99,  # 2021 codes
                         'Fernbus national': -99,  # 2021 codes
                         'Gondelbahn': -99,  # 2021 codes
                         'Sesselbahn': -99,  # 2021 codes
                         'Pendelbahn': -99,  # 2021 codes
                         'Standseilbahn': -99,  # 2021 codes
                         'Aufzug': -99,  # 2021 codes
                         'Zahnradbahn': -99,  # 2021 codes
                         'Schiff': -99,  # 2021 codes
                         'F???hre': -99,  # 2021 codes
                         'T': -99,  # Tram (2022 codes)
                         'S': 5,  # S-Bahn (2022 codes)
                         'SN': 5,  # Nacht-S-Bahn (2022 codes)
                         'RE': 3,  # RegioExpress (2022 codes)
                         'RB': 3,  # Regionalbahn / regional train (2022 codes)
                         'R': 5,  # Regio (2022 codes)
                         'IR': 2,  # InterRegio (2022 codes)
                         'IC': 1,  # InterCity (2022 codes)
                         'TER': 5,  # Train Expresse Regional (2022 codes)
                         'ICE': 0,  # InterCityExpress (2022 codes)
                         'EC': 1,  # EuroCity (2022 codes)
                         'PE': 2,  # PanoramaExpress (2022 codes)
                         'RJX': 0,  # railjet xpress (2022 codes)
                         'TGV': 0,
                         'IRE': 3,  # Interregio-Express (2022 codes)
                         'NJ': 0,  # nightjet (2022 codes)
                         'EXT': -99,  # Extrazug / special train (2022 codes)
                         'MAT': -99,  # LeermaterialZ (Reisezugswagen) / empty material train (passenger carriage)
                         'AG': -97,  # Agenturzug (2022 codes)
                         'M': -99,  # Metro (2022 codes)
                         'TX': -99,  # Taxi (2022 codes)
                         'B': -99,  # Bus (2022 codes)
                         'EXB': -99,  # Expressbus (2022 codes)
                         'RUB': -99,  # Rufbus / on-call bus (2022 codes)
                         'BN': -99,  # Nachtbus / night-bus (2022 codes)
                         'CAR': -99,  # Fernbus national / international long-distance bus (2022 codes)
                         'BP': -99,  # PanoramaBus (2022 codes)
                         'SL': -99,  # Sesselbahn / charlift (2022 codes)
                         'GB': -99,  # Gondelbahn / gondola lift (2022 codes)
                         'PB': -99,  # Pendelbahn / aerial tramway (2022 codes)
                         'FUN': -99,  # Standseilbahn / funicular (2022 codes)
                         'ASC': -99,  # Aufzug / lift (2022 codes)
                         'CC': -99,  # Zahnradbahn / rack-railroad (2022 codes)
                         'BAT': -99,  # Schiff / ship (2022 codes)
                         'FAE': -99}  # Faehre / ferry-boat (2022 codes)
    df_trips['zugtyp'] = df_trips['route_desc'].map(dict_abbreviation)
    return df_trips


def recode_route_desc(df_etappen):
    # The coding is based on the coding in the ZUGART file
    dict_codes = {'Aufzug': 1,
                  'ASC': 1,  # Aufzug / lift
                  'Bus': 2,
                  'B': 2,  # Bus
                  'Schiff': 3,
                  'BAT': 3,  # Schiff / ship
                  'Nachtbus': 4,
                  'BN': 4,  # Nachtbus / night-bus
                  'PanoramaBus': 5,
                  'BP': 5,  # PanoramaBus
                  'Fernbus national': 7,
                  'CAR': 7,  # Fernbus national / international long-distance bus
                  'Zahnradbahn': 8,
                  'CC': 8,  # Zahnradbahn / rack-railroad
                  'EuroCity': 9,
                  'EC': 9,  # EuroCity
                  'Expressbus': 10,
                  'EXB': 10,  # Expressbus
                  'Extrazug': 11,
                  'EXT': 11,  # Extrazug / special train
                  'F???hre': 12,
                  'FAE': 12,  # Faehre / ferry-boat
                  'Standseilbahn': 13,
                  'FUN': 13,  # Standseilbahn / funicular
                  'Gondelbahn': 14,
                  'GB': 14,  # Gondelbahn / gondola lift
                  'InterCity': 15,
                  'IC': 15,  # InterCity
                  'InterCityExpress': 16,
                  'ICE': 16,  # InterCityExpress
                  'InterRegio': 17,
                  'IR': 17,  # InterRegio
                  'Interregio-Express': 18,
                  'IRE': 18,  # Interregio-Express
                  'Kleinbus': 19,
                  'Metro': 20,
                  'M': 20,  # Metro
                  'MAT': 21,  # LeermaterialZ (Reisezugswagen) / empty material train (passenger carriage)
                  'nightjet': 22,
                  'NJ': 22,  # nightjet
                  'Pendelbahn': 23,
                  'PB': 23,  # Pendelbahn / aerial tramway
                  'PanoramaExpress': 24,
                  'PE': 24,  # PanoramaExpress
                  'Regio': 25,
                  'R': 25,  # Regio
                  'Regionalbahn': 26,
                  'RB': 26,  # Regionalbahn / regional train
                  'RegioExpress': 27,
                  'RE': 27,  # RegioExpress
                  'railjet xpress': 28,
                  'RJX': 28,  # railjet xpress
                  'Rufbus': 29,
                  'RUB': 29,  # Rufbus / on-call bus
                  'S-Bahn': 30,
                  'S': 30,  # S-Bahn
                  'Sesselbahn': 31,
                  'SL': 31,  # Sesselbahn / charlift
                  'Nacht-S-Bahn': 32,
                  'SN': 32,  # Nacht-S-Bahn
                  'Tram': 33,
                  'T': 33,  # Tram
                  'Train Express Regional': 34,
                  'TER': 34,  # Train Expresse Regional
                  'Train ??? grande vit.': 35,
                  'TGV': 35,
                  'Taxi': 36,
                  'TX': 36,  # Taxi
                  'AG': 37}  # Agenturzug
    df_etappen['route_desc'] = df_etappen['route_desc'].map(dict_codes)
    return df_etappen


def read_gtfs_routes(year):
    path_to_routes_file = Path('../data/input/gtfs/' + str(year) + '/routes.txt')
    # Get route_id & route_type
    with open(path_to_routes_file, 'r') as trip_file:
        df_routes = pd.read_csv(trip_file, sep=',', usecols=['route_id', 'route_desc'])
    return df_routes


def read_gtfs_trips(year):
    path_to_trips_file = Path('../data/input/gtfs/' + str(year) + '/trips.txt')
    # Get route_id & trip_id
    with open(path_to_trips_file, 'r') as trip_file:
        df_trips = pd.read_csv(trip_file, sep=',', usecols=['trip_id', 'route_id'])
    return df_trips


if __name__ == '__main__':
    run_train_type_in_microcensus()
