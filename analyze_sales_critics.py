import plotly.graph_objects as go
from scipy import stats
from sklearn.linear_model import LinearRegression


def analyze_sales_critics(video_game_sales):
    """
    Analyzes the relationship between video game sales and critic scores using linear regression.
    This function performs the following steps:
    1. Removes rows with missing values in the 'Critic_Score' and 'Global_Sales' columns.
    2. Calculates the Pearson correlation coefficient and p-value between critic scores and global sales.
    3. Fits a linear regression model to predict global sales based on critic scores.
    4. Generates a scatter plot with the data points and the regression line.
    5. Calculates the coefficient of determination (R^2) for the regression model.

    Parameters:
    video_game_sales (pd.DataFrame): A DataFrame containing video game sales.

    Returns:
    tuple: A tuple containing:
      - figure (plotly.graph_objs._figure.Figure): A Plotly figure object with the scatter plot and regression line.
      - corr (float): The Pearson correlation coefficient between critic scores and global sales.
      - p_value (float): The p-value associated with the Pearson correlation coefficient.
      - r_squared (float): The coefficient of determination (R^2) for the regression model.
    """
    # Nie wszystkie gry w datasecie zawierają ocenę krytyków.
    # Usunięcie wierszy z brakującymi wartościami
    cleaned_video_game_sales = video_game_sales.dropna(
        subset=["Critic_Score", "Global_Sales"]
    )

    # Obliczenie korelacji
    corr, p_value = stats.pearsonr(
        cleaned_video_game_sales["Critic_Score"],
        cleaned_video_game_sales["Global_Sales"],
    )

    model = LinearRegression()
    model.fit(
        X=cleaned_video_game_sales["Critic_Score"].values.reshape(-1, 1),
        y=cleaned_video_game_sales["Global_Sales"].values,
    )
    y_pred = model.predict(
        cleaned_video_game_sales["Critic_Score"].values.reshape(-1, 1)
    )

    # Współczynnik determinacji R^2
    r_squared = model.score(
        X=cleaned_video_game_sales["Critic_Score"].values.reshape(-1, 1),
        y=cleaned_video_game_sales["Global_Sales"].values,
    )

    # Tworzenie wykresu
    figure = go.Figure(
        layout=go.Layout(
            title="Regresja liniowa: Sprzedaż globalna a oceny krytyków(metacritic)",
            xaxis_title="Ocena krytyków",
            yaxis_title="Sprzedaż globalna (mln szt.)",
        )
    )

    # Dodanie punktów danych
    figure.add_trace(
        go.Scatter(
            x=cleaned_video_game_sales["Critic_Score"],
            y=cleaned_video_game_sales["Global_Sales"],
            mode="markers",
            name="Dane",
        )
    )

    # Dodanie linii regresji
    figure.add_trace(
        go.Scatter(
            x=cleaned_video_game_sales["Critic_Score"],
            y=y_pred,
            mode="lines",
            name="Linia regresji",
        )
    )

    return figure, corr, p_value, r_squared
