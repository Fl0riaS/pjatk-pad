from scipy import stats


def analyze_publisher_sales(video_game_sales):
    """
    Analyzes video game sales data using ANOVA to determine if there is a statistically significant difference
    in global sales among publishers who have released at least 20 games.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    bool: True if there is a statistically significant difference in global sales among the publishers,
        False otherwise.
    """
    cleared_video_game_sales = video_game_sales.dropna(
        subset=["Publisher", "Global_Sales"]
    )

    # Zliczenie liczby gier wydanych przez każdego wydawcę
    publisher_sales = (
        cleared_video_game_sales.groupby("Publisher")["Global_Sales"]
        .agg(["count"])
        .reset_index()
    )

    # Analizie zostaną poddani tylko wydawcy, którzy wydali co najmniej 20 gier
    sales_data_for_publishers = []
    for publisher in publisher_sales[publisher_sales["count"] >= 20]["Publisher"]:
        sales_data_for_publishers.append(
            cleared_video_game_sales[
                cleared_video_game_sales["Publisher"] == publisher
            ]["Global_Sales"]
        )

    # Przeprowadzenie testu ANOVA
    _, pvalue = stats.f_oneway(*sales_data_for_publishers)

    return pvalue < 0.05
