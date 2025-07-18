# Wisielec / Hangman

## Polski

### Opis projektu
**Wisielec** to klasyczna gra słowna zaimplementowana w języku Python z użyciem biblioteki Tkinter. Gra posiada interfejs graficzny (GUI) i została zaprojektowana z myślą o języku polskim, obsługując polskie znaki (np. ą, ć, ł, ź). Celem gracza jest odgadnięcie losowo wybranego słowa, podając pojedyncze litery, przy ograniczonym limicie prób. Projekt demonstruje umiejętności programistyczne w zakresie tworzenia aplikacji z interfejsem graficznym i obsługi plików.

### Funkcjonalności
- Losowanie słów z pliku `words.txt`.
- Obsługa polskich znaków.
- Prosty interfejs graficzny oparty na Tkinter.
- Wyświetlanie użytych liter i licznik prób.
- Możliwość zakończenia gry i restartu.

### Wymagania
- Python 3.6 lub nowszy
- Biblioteka Tkinter (zazwyczaj wbudowana w Pythona)
- Plik `words.txt` z listą słów (jedno słowo na linii)

### Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Entariel/Hangman_game.git
   ```
2. Przejdź do katalogu projektu:
   ```bash
   cd Hangman_game
   ```
3. Upewnij się, że masz zainstalowanego Pythona.
4. Przygotuj plik `words.txt` w katalogu projektu z listą słów (np. `kot`, `pies`).

### Użycie
1. Uruchom grę, wykonując:
   ```bash
   python hangman.py
   ```
2. Wpisz literę w polu tekstowym i naciśnij Enter lub kliknij "Zgadnij".
3. Gra pokaże, czy litera jest w słowie, i zaktualizuje stan gry.
4. Po wygranej lub przegranej możesz zakończyć lub zrestartować grę.

### Struktura projektu
```
Hangman_game/
├── hangman.py       # Główny kod gry
├── words.txt       # Plik z listą słów
├── .gitignore      # Plik ignorujący określone pliki dla Git
├── .idea/          # Katalog ustawień IDE (np. PyCharm)
├── README.md       # Ten plik
```

### Przykład pliku `words.txt`
```
kot
pies
drzewo
słońce
```

---

## English

### Project Description
**Hangman** is a classic word-guessing game implemented in Python using the Tkinter library. The game features a graphical user interface (GUI) and is designed with Polish language support, including Polish characters (e.g., ą, ć, ł, ź). The player's goal is to guess a randomly selected word by entering individual letters within a limited number of attempts. This project showcases skills in developing GUI applications and file handling in Python.

### Features
- Random word selection from the `words.txt` file.
- Support for Polish characters.
- Simple GUI built with Tkinter.
- Display of used letters and attempt counter.
- Option to end or restart the game.

### Requirements
- Python 3.6 or higher
- Tkinter library (usually included with Python)
- A `words.txt` file with a list of words (one word per line)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Entariel/Hangman_game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Hangman_game
   ```
3. Ensure Python is installed.
4. Prepare a `words.txt` file in the project directory with a list of words (e.g., `cat`, `dog`).

### Usage
1. Run the game by executing:
   ```bash
   python hangman.py
   ```
2. Enter a letter in the text field and press Enter or click "Guess".
3. The game will indicate if the letter is in the word and update the game state.
4. After winning or losing, you can end or restart the game.

### Project Structure
```
Hangman_game/
├── hangman.py       # Main game script
├── words.txt       # File with the list of words
├── .gitignore      # File ignoring specific files for Git
├── .idea/          # IDE settings directory (e.g., PyCharm)
├── README.md       # This file
```

### Example `words.txt` File
```
cat
dog
tree
sun
```