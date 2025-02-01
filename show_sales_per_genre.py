import plotly.express as px

def show_sales_per_genre(video_game_sales):
  """
  Generates a bar chart showing video game sales per genre across different regions.
  Parameters:
  video_game_sales (DataFrame): A pandas DataFrame containing video game sales data with columns 
                  'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', and 'Other_Sales'.
  Returns:
  plotly.graph_objs._figure.Figure: A Plotly bar chart figure object representing the sales data.
  """
  # Grupowanie sprzedaży gier według regionów
  genre_by_region_sales = (
      video_game_sales.groupby("Genre")[
          ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
      ]
      .sum()
      .reset_index()
  )

  # Przekształcenie danych, tak aby móc je odpowiednio wyświetlić na wykresie
  genre_by_region_sales = genre_by_region_sales.melt(
      id_vars="Genre", var_name="Region", value_name="Sales"
  )

  # Przekształcenie nazw regionów na bardziej czytelne
  genre_by_region_sales["Region"] = genre_by_region_sales["Region"].map(
      {
          "NA_Sales": "Sprzedaż w Północnej Ameryce",
          "EU_Sales": "Sprzedaż w Europie",
          "JP_Sales": "Sprzedaż w Japonii",
          "Other_Sales": "Sprzedaż w Pozostałych Regionach",
      }
  )

  # Tworzenie wykresu słupkowego
  figure = px.bar(
      genre_by_region_sales,
      x="Region",
      y="Sales",
      color="Genre",
      barmode="group",
      title="Sprzedaż gier w różnych regionach dla poszczególnych gatunków",
      labels={"Region": "Region", "Sales": "Sprzedaż (mln szt.)", "Genre": "Gatunek"},
  )

  return figure