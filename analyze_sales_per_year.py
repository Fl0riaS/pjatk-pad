import plotly.graph_objects as go


def analyze_sales_per_year(video_game_sales):
    """
    Analyzes video game sales per year and generates a plotly figure showing the global sales and a 3-year moving average.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    plotly.graph_objs._figure.Figure: A plotly figure object containing the sales data and moving average plot.
    """
    # Grupowanie danych według roku i sumowanie globalnej sprzedaży
    sales_per_year = (
        video_game_sales.groupby("Year_of_Release")["Global_Sales"].sum().reset_index()
    )

    # Obliczenie średniej kroczącej z oknem 3 lat
    sales_per_year["Moving_Average"] = (
        sales_per_year["Global_Sales"].rolling(window=3).mean()
    )

    # Rysowanie wykresu
    figure = go.Figure(
        layout=go.Layout(
            title="Globalna sprzedaż gier na przestrzeni lat",
            xaxis_title="Rok",
            yaxis_title="Sprzedaż (mln szt.)",
        )
    )
    figure.add_trace(
        go.Scatter(
            x=sales_per_year["Year_of_Release"],
            y=sales_per_year["Moving_Average"],
            mode="lines",
            name="Średnia krocząca",
        )
    )
    figure.add_trace(
        go.Scatter(
            x=sales_per_year["Year_of_Release"],
            y=sales_per_year["Global_Sales"],
            mode="lines+markers",
            name="Globalna sprzedaż",
        )
    )

    return figure
