import plotly.graph_objects as go
from scipy import stats
from sklearn.linear_model import LinearRegression
from clean_player_ratings import clean_player_ratings


def analyze_sales_player_ratings(video_game_sales):
    """
    Analyzes the relationship between video game sales and player ratings using linear regression.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    tuple: A tuple containing:
      - figure (plotly.graph_objs._figure.Figure): A Plotly figure object with the scatter plot and regression line.
      - corr (float): Pearson correlation coefficient between user scores and global sales.
      - p_value (float): P-value of the Pearson correlation.
      - r_squared (float): Coefficient of determination (R^2) of the linear regression model.
    """
    cleaned_video_game_sales = clean_player_ratings(video_game_sales)

    # Obliczenie korelacji
    corr, p_value = stats.pearsonr(
        cleaned_video_game_sales["User_Score"],
        cleaned_video_game_sales["Global_Sales"],
    )

    model = LinearRegression()
    model.fit(
        X=cleaned_video_game_sales["User_Score"].values.reshape(-1, 1),
        y=cleaned_video_game_sales["Global_Sales"].values,
    )
    y_pred = model.predict(cleaned_video_game_sales["User_Score"].values.reshape(-1, 1))

    # Współczynnik determinacji R^2
    r_squared = model.score(
        X=cleaned_video_game_sales["User_Score"].values.reshape(-1, 1),
        y=cleaned_video_game_sales["Global_Sales"].values,
    )

    figure = go.Figure(
        layout=go.Layout(
            title="Regresja liniowa: Sprzedaż globalna a oceny graczy(metacritic)",
            xaxis_title="Ocena graczy",
            yaxis_title="Sprzedaż globalna (mln szt.)",
        )
    )

    # Dodanie punktów danych
    figure.add_trace(
        go.Scatter(
            x=cleaned_video_game_sales["User_Score"],
            y=cleaned_video_game_sales["Global_Sales"],
            mode="markers",
            name="Dane",
        )
    )

    # Dodanie linii regresji
    figure.add_trace(
        go.Scatter(
            x=cleaned_video_game_sales["User_Score"],
            y=y_pred,
            mode="lines",
            name="Linia regresji",
        )
    )

    return figure, corr, p_value, r_squared
