from scipy import stats

regions = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]


def analyze_sales_per_genre(video_game_sales):
    """
    Analyzes video game sales per genre for different regions.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales
    
    Returns:
      dict: A dictionary where keys are region names and values are the results of the hypothesis test
          for that region.
    """
    result_dictionary = {}

    for region in regions:
        result_dictionary[region] = test_hypothesis(video_game_sales, region)

    return result_dictionary


def test_hypothesis(video_game_sales, region):
    # Lista unikalnych gatunków
    genres = video_game_sales["Genre"].unique()

    # Pusty słownik do przechowywania danych sprzedaży dla każdego gatunku w regionie
    sales_data = {}

    # Zebranie danych sprzedaży dla każdego gatunku
    for genre in genres:
        # Sprzedaż dla danego gatunku
        sales = video_game_sales[video_game_sales["Genre"] == genre][region]
        sales_array = sales.values
        # Zapisanie danych do słownika
        sales_data[genre] = sales_array

    # Przeprowadzenie testu ANOVA
    _, pvalue = stats.f_oneway(
        sales_data["Sports"],
        sales_data["Platform"],
        sales_data["Racing"],
        sales_data["Role-Playing"],
        sales_data["Puzzle"],
        sales_data["Misc"],
        sales_data["Shooter"],
        sales_data["Simulation"],
        sales_data["Action"],
        sales_data["Fighting"],
        sales_data["Adventure"],
        sales_data["Strategy"],
        nan_policy="omit",
    )

    # Interpretacja
    if pvalue < 0.05:
        return True
    else:
        return False
