import pandas as pd

def load_data():
    """
    Loads and preprocesses video game sales data from a CSV file.
    The function performs the following steps:
    1. Reads the video game sales data from 'assets/vgsales.csv'.
    2. Drops rows with NaN values in the 'Year_of_Release' column.
    3. Converts the 'Year_of_Release' column to integer type.
    4. Filters out rows where the 'Year_of_Release' is greater than 2016.
    Returns:
      pd.DataFrame: A DataFrame containing the preprocessed video game sales data.
    """
    # Wczytanie danych
    video_game_sales = pd.read_csv("assets/vgsales.csv")

    # Konwersja kolumny 'Year' na typ 'int'
    # Czyszczenie danych z wartości NaN, poprzez usunięcie ich z datasetu
    video_game_sales = video_game_sales.dropna(subset=["Year_of_Release"])
    video_game_sales["Year_of_Release"] = video_game_sales["Year_of_Release"].astype(
        int
    )

    # Dataset zawiera dane do 2016 roku, jednak zawiera również dane przedsprzedaży gier, które jeszcze wtedy nie wyszły.
    # Analiza będzie opierać się o gry, które miały już swoją premierę, zatem usunięte zostaną wszystkie pozycje z datą wydania ustawioną na 2017 rok i później
    video_game_sales = video_game_sales[video_game_sales["Year_of_Release"] <= 2016]

    return video_game_sales