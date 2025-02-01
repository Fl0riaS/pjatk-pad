# PAD - projekt finalny

## Opis struktury projektu

Poza opisem, w każdym pliku został zawarty stosowny komentarz opisujący działanie danej funkcji

### Katalog *assets*

- Zawiera [dataset](https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings) na którym została wykonana analiza oraz plik css odpowiadający za style dashboardu

### Plik *main.py*

- Główny funkcja projektu, zawierająca w sobie dashboard zbierający wyniki analizy.

### Plik *load_data.py*

- Funkcja wczytująca dataset do dataframe oraz dokonujący wstępnej obróbki danych.

### Pliki z przedrostkiem *analyze*

- Funkcje dokonujące analizy danych(po uprzednim dostosowaniu danych), zwracające dane pozwalające na ukazanie wyników analizy w dashboardzie.

### Pliki z przedrostkiem *clean*

- Pliki odpowiadające za czyszczenie i przetwarzanie danych specyficzne dla danego analizowanego przypadku.

### Pliki z przedrostkiem *show*

- Funkcja zwracające wykresy danych, pozwalające na przegląd danego analizowanego przypadku przed wykonaniem analizy.

## Wymagania

- Python 3.12.0
- dash 2.18.2
- pandas 2.2.3
- scipy 1.14.1
- plotly 5.24.1
- scikit-learn 1.5.2

## Uruchomienie projektu

```bash
python .\main.py
```
