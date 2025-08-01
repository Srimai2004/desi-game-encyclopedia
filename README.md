## desi-game-encyclopedia

A Streamlit app to document and preserve traditional Indian games — their rules, regional variations, and stories contributed by users.

### Features:

- Add games with game name, region/state, rules, and variations.
- View all submitted games in an organized expandable list.
- Remove duplicate entries automatically.
- Delete individual entries.
- Data is stored locally in a CSV file (game_data.csv).

- Contributions are credited by contributor name optionally.


## Installation & Setup (Local)

1. Clone/download this repository.

2. Create a Python virtual environment (optional but recommended):


```bash
  python -m venv venv
```
3. Activate the virtual environment:

 ### Windows:   venv\Scripts\activate

 ### Mac/Linux: source venv/bin/activate

4. Install dependencies:

```bash
  pip install -r requirements.txt
```

5. Run the app locally:

```bash
 streamlit run app.py

```



### Usage

- Fill in the form to add a new game entry.

- Use the expandable sections to view game details.

- Remove duplicate entries using the "Clean Duplicate Entries" button.

- Delete entries by checking the box and confirming.

### Dependencies

- streamlit

- pandas
