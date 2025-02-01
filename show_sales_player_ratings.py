import plotly.express as px
from clean_player_ratings import clean_player_ratings


def show_sales_player_ratings(video_game_sales):
    """
    Generates a scatter plot showing the relationship between user scores and global sales of video games.
    
    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.
    
    Returns:
    plotly.graph_objs._figure.Figure: A Plotly figure object representing the scatter plot.
    """
    cleaned_video_game_sales = clean_player_ratings(video_game_sales)

    figure = px.scatter(
        cleaned_video_game_sales,
        x="User_Score",
        y="Global_Sales",
        title="Sprzedaż globalna a oceny graczy(metacritic)",
        labels={
            "User_Score": "Ocena graczy",
            "Global_Sales": "Sprzedaż globalna (mln szt.)",
        },
    )

    return figure
