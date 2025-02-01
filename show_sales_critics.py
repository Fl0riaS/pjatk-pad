import plotly.express as px


def show_sales_critics(video_game_sales):
    """
    Generates a scatter plot showing the relationship between critic scores and global sales of video games.
    This function takes a DataFrame containing video game sales data, removes rows with missing values in the
    'Critic_Score' and 'Global_Sales' columns, and creates a scatter plot using Plotly Express. The x-axis
    represents the critic scores, and the y-axis represents the global sales in millions of units.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    plotly.graph_objs._figure.Figure: A Plotly Figure object representing the scatter plot.
    """
    # Nie wszystkie gry w datasecie zawierają ocenę krytyków.
    # Usunięcie wierszy z brakującymi wartościami
    cleaned_video_game_sales = video_game_sales.dropna(
        subset=["Critic_Score", "Global_Sales"]
    )

    figure = px.scatter(
        cleaned_video_game_sales,
        x="Critic_Score",
        y="Global_Sales",
        title="Sprzedaż globalna a oceny krytyków(metacritic)",
        labels={
            "Critic_Score": "Ocena krytyków",
            "Global_Sales": "Sprzedaż globalna (mln szt.)",
        },
    )

    return figure
