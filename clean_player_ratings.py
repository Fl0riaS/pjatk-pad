def clean_player_ratings(video_game_sales):
    """
    Cleans the video game sales dataset by removing rows with missing or invalid user scores,
    and converts the user scores to match the scale of critic scores.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    pandas.DataFrame: The cleaned dataset with user scores converted to integers on a scale of 0 to 100.
    """
    # Nie wszystkie gry w datasecie zawierają ocenę graczy.
    # Usunięcie wierszy z brakującymi wartościami oraz wartości "tbd"
    cleaned_video_game_sales = video_game_sales.dropna(
        subset=["User_Score", "Global_Sales"]
    )
    cleaned_video_game_sales = cleaned_video_game_sales[
        cleaned_video_game_sales["User_Score"] != "tbd"
    ]

    # Konwersja kolumny User_Score na typ float
    cleaned_video_game_sales["User_Score"] = cleaned_video_game_sales[
        "User_Score"
    ].astype(float)

    # Mnożenie wartości w kolumnie User_Score przez 10 i konwersja do typu int, tak aby dopasować wartości do kolumny Critic_Score
    cleaned_video_game_sales["User_Score"] = cleaned_video_game_sales["User_Score"] * 10

    return cleaned_video_game_sales
