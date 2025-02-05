from dash import Dash, html, dcc, dash_table
from analyze_sales_per_year import analyze_sales_per_year
from load_data import load_data
from show_sales_per_genre import show_sales_per_genre
from analyze_sales_per_genre import analyze_sales_per_genre
from show_sales_critics import show_sales_critics
from analyze_sales_critics import analyze_sales_critics
from show_sales_player_ratings import show_sales_player_ratings
from analyze_sales_player_ratings import analyze_sales_player_ratings
from show_publisher_sales import show_publisher_sales
from analyze_publisher_sales import analyze_publisher_sales

# region CONSTANTS
regions = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
translated_regions = {
    "NA_Sales": "Północna Ameryka",
    "EU_Sales": "Europa",
    "JP_Sales": "Japonia",
    "Other_Sales": "Pozostałe Regiony",
}
# endregion

# region DATA
video_game_sales = load_data()

# Wykonanie funkcji pokazujących dane do analizy
show_publisher_sales_results = show_publisher_sales(video_game_sales)

# Wykonanie funkcji analizujących dane
analyze_sales_per_genre_results = analyze_sales_per_genre(video_game_sales)
analyze_sales_critics_results = analyze_sales_critics(video_game_sales)
analyze_sales_player_ratings_results = analyze_sales_player_ratings(video_game_sales)
# endregion

# region DASHBOARD
# Inicjalizacja aplikacji Dash
app = Dash()

# Layout aplikacji
app.layout = [
    html.H1(children="Analiza danych sprzedaży gier"),
    html.H2(children="Jakub Znyk"),
    html.A(
        children="Zbiór danych wykorzystany do analizy(źródło)",
        href="https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings",
    ),
    dash_table.DataTable(data=video_game_sales.to_dict("records"), page_size=10),
    html.H2(
        children="Trendy sprzedaży gier na przestrzeni lat",
    ),
    html.P(children="Analiza została wykonana za pomocą średniej kroczącej"),
    dcc.Graph(figure=analyze_sales_per_year(video_game_sales)),
    html.P(
        children="Z pomocą wykorzystania średniej kroczącej, możemy zauważyć wyraźny trend wzrostowy trwający od 1980 do 2009 roku. Potem rozpoczął się trend spadkowy, który trwa aż do końca okresu zebranych danych, tj. do roku 2016."
    ),
    html.H2(children="Związek między gatunkiem gry a sprzedażą w danych regionach"),
    dcc.Graph(figure=show_sales_per_genre(video_game_sales)),
    html.P(
        children="Na wykresach możemy zauważyć różnice między ilością sprzedanych gier danego gatunku. Za pomocą testu ANOVA(testujemy wpływ gatunku - zmiennej kategorycznej na sprzedaż - zmiennej ciągłej) sprawdzimy, czy istnieje istotny statystycznie związek między gatunkiem gry a wysoką sprzedażą w danym regionie. "
    ),
    html.P(children="Hipoteza zerowa:"),
    html.P(
        children="• Nie stwierdzono istotnego statystycznie związku między gatunkiem gry a wysoką sprzedażą.",
        className="indent-text",
    ),
    html.P(children="Hipoteza alternatywna:"),
    html.P(
        children="• Istnieje istotny statystycznie związek między gatunkiem gry a wysoką sprzedażą w danym regionie.",
        className="indent-text",
    ),
    html.P(children="Wyniki testu hipotez dla poszczególnych regionów:"),
    html.Div(
        children=[
            html.P(
                children=f"• {translated_regions[region]}: {'Istnieje istotny związek' if result else 'Nie stwierdzono istotnego związku'}",
                className="indent-text",
            )
            for region, result in analyze_sales_per_genre_results.items()
        ]
    ),
    html.P(
        children="Dla każdego z regionów możemy odrzucić hipotezę zerową i przyjąć hipotezę alternatywną, która mówi, że Istnieje istotny statystycznie związek między gatunkiem gry a wysoką sprzedażą w danym regionie."
    ),
    html.H2(children="Zależność pomiędzy ocenami krytyków a sprzedażą gry"),
    dcc.Graph(figure=show_sales_critics(video_game_sales)),
    html.P(
        children="Na wykresie możemy dostrzec, że więcej punktów na górze wykresu - sprzedaż(nieco zaburzone przez 'Wii Sports') znajduje się przy jego prawej stronie - większa ocena krytyków. Za pomocą regresji liniowej sprawdzimy, czy oceny krytyków mają rzeczywisty wpływ na sprzedaż gier. Oceny krytyków zbierane i podsumowywane są przez portal Metacritic, który zbiera recenzje wystawione przez niezależne redakcje."
    ),
    dcc.Graph(figure=analyze_sales_critics_results[0]),
    html.P(children="Wyniki analizy:"),
    html.P(
        children=f"• Współczynnik korelacji Pearsona: {analyze_sales_critics_results[1]:.2f}",
        className="indent-text",
    ),
    html.P(
        children=f"• Wartość p: {analyze_sales_critics_results[2]:.2f}",
        className="indent-text",
    ),
    html.P(
        children=f"• Współczynnik determinacji R^2: {analyze_sales_critics_results[3]:.2f}",
        className="indent-text",
    ),
    html.P(children="Podsumowanie analizy:"),
    html.P(
        children="Wartość 0.25 współczynnika korelacji sugeruje słabą dodatnią korelację. Istnieje pewna pozytywna zależność, ale jest ona stosunkowo słaba.",
        className="indent-text",
    ),
    html.P(
        children="Wartość p na poziomie 0.00 oznacza, że wyniki są wysoce istotne statystycznie.",
        className="indent-text",
    ),
    html.P(
        children="Wartość 0.06 współczynnika determinacji R^2 sugeruje, że około 6% zmienności sprzedaży gier jest wyjaśnione przez oceny krytyków.",
        className="indent-text",
    ),
    html.H2(children="Zależność pomiędzy ocenami graczy a sprzedażą gry"),
    dcc.Graph(figure=show_sales_player_ratings(video_game_sales)),
    html.P(
        children="Naturalnym następstwem poprzedniego testu jest sprawdzenie, czy oceny graczy mają wpływ na sprzedaż gier. Oceny graczy również zbierane przez portal Metacritic. Do analizy przekazane zostały gry z ilością ocen większą niż 3 - tylko wtedy portal podaje ocenę liczbową. Dodatkowo, ocena graczy mieści się w przedziale od 0 do 10 - ale na potrzeby zobrazowania podobieństw i różnic w ocenach graczy i krytyków, dane te zostały przekonwertowane na skalę 0-100. Przy ocenach graczy, również możemy zaobserwować zależność, w którym lepiej sprzedające się gry mają tendencję do znajdowania się w prawej części wykresu. Analogicznie do poprzedniego testu, sprawdzimy, czy oceny graczy mają rzeczywisty wpływ na sprzedaż gier.",
    ),
    dcc.Graph(figure=analyze_sales_player_ratings_results[0]),
    html.P(children="Wyniki analizy:"),
    html.P(
        children=f"• Współczynnik korelacji Pearsona: {analyze_sales_player_ratings_results[1]:.2f}",
        className="indent-text",
    ),
    html.P(
        children=f"• Wartość p: {analyze_sales_player_ratings_results[2]:.2f}",
        className="indent-text",
    ),
    html.P(
        children=f"• Współczynnik determinacji R^2: {analyze_sales_player_ratings_results[3]:.2f}",
        className="indent-text",
    ),
    html.P(children="Podsumowanie analizy:"),
    html.P(
        children="Wartość 0.09 współczynnika korelacji sugeruje bardzo słabą dodatnią korelację.",
        className="indent-text",
    ),
    html.P(
        children="Wartość p na poziomie 0.00 oznacza, że wyniki są wysoce istotne statystycznie.",
        className="indent-text",
    ),
    html.P(
        children="Wartość 0.01 współczynnika determinacji R^2 sugeruje, że około 1% zmienności sprzedaży gier jest wyjaśnione przez oceny graczy.",
        className="indent-text",
    ),
    html.P(
        children="Co za tym idzie, możemy stwierdzić, że oceny krytyków w większym stopniu wpływają na sprzedaż gry niż oceny graczy."
    ),
    html.H2(children="Wpływ wydawcy na sprzedaż gry"),
    dcc.Graph(figure=show_publisher_sales_results[0]),
    dcc.Graph(figure=show_publisher_sales_results[1]),
    html.P(
        children="Na wykresie możemy zauważyć, że niektórzy wydawcy mają znacznie większą sprzedaż niż inni. Różnice możemy zauważyć nie tylko w całkowitej sprzedaży, na którą wpływa ilość wydanych gier przez danego wydawcę, ale również w średniej sprzedaży. Za pomocą testu ANOVA(testujemy wpływ wydawcy - zmiennej kategorycznej na sprzedaż - zmiennej ciągłej), sprawdzimy, czy istnieje istotny statystycznie związek między wydawcą gry a wysoką sprzedażą. Analizie zostaną poddani tylko ci wydawcy, którzy wydali przynajmniej 20 gier.",
    ),
    html.P(children="Hipoteza zerowa:"),
    html.P(
        children="• Nie stwierdzono istotnego statystycznie związku między wydawcą gry a wysoką sprzedażą.",
        className="indent-text",
    ),
    html.P(children="Hipoteza alternatywna:"),
    html.P(
        children="• Istnieje istotny statystycznie związek między wydawcą gry a wysoką sprzedażą.",
        className="indent-text",
    ),
    html.P(children="Wynik testu ANOVA:"),
    html.P(
        children=f"• {'Istnieje istotny związek' if analyze_publisher_sales(video_game_sales) else 'Nie stwierdzono istotnego związku'}",
        className="indent-text",
    ),
]
# endregion

if __name__ == "__main__":
    app.run(debug=True)
