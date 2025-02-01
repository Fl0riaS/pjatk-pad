import plotly.express as px


def show_publisher_sales(video_game_sales):
    """
    Generates bar charts showing the total and average global sales of video games by publisher.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    tuple: A tuple containing two plotly.graph_objects.Figure objects:
      - figure_total: Bar chart of the total global sales by publisher for the top 10 publishers.
      - figure_average: Bar chart of the average global sales by publisher for the top 10 publishers.
    """
    cleared_video_game_sales = video_game_sales.dropna(
        subset=["Publisher", "Global_Sales"]
    )

    # Grupowanie danych według wydawców, sumowanie, uśrednianie dla sprzedaży globalnej i reset indeksu
    publisher_sales = (
        cleared_video_game_sales.groupby("Publisher")["Global_Sales"]
        .agg(["count", "sum", "mean"])
        .reset_index()
    )
    publisher_sales.columns = [
        "Publisher",
        "Number_of_Games",
        "Total_Global_Sales",
        "Average_Global_Sales",
    ]

    # Sortowanie danych według sprzedaży globalnej, tak aby pokazać 10 wydawców z największą sprzedażą
    top_publishers = publisher_sales.sort_values(
        by="Total_Global_Sales", ascending=False
    ).head(10)

    figure_total = px.bar(
        top_publishers,
        x="Publisher",
        y="Total_Global_Sales",
        title="Sprzedaż globalna gier(całkowita) w zależności od wydawcy - 10 największych wydawców",
        labels={"Total_Global_Sales": "Sprzedaż globalna (mln szt.)"},
    )

    figure_average = px.bar(
        top_publishers,
        x="Publisher",
        y="Average_Global_Sales",
        title="Sprzedaż globalna gier(średnia) w zależności od wydawcy - 10 największych wydawców",
        labels={"Average_Global_Sales": "Średnia sprzedaż globalna (mln szt.)"},
    )

    return figure_total, figure_average
