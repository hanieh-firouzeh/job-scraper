# Job Scraper

A small Python script that collects job listings from a practice job board, keeps only the ones with "python" in the title, and saves them to a CSV file.

The practice site is [Fake Python Jobs](https://realpython.github.io/fake-jobs/), made by Real Python for learning web scraping.

## How it works

1. Downloads the page with `requests`.
2. Parses the HTML with `BeautifulSoup`.
3. Finds the job title, company, location, and the "Apply" link of each listing.
4. Keeps only the listings with "python" in the title (not case-sensitive).
5. Saves the results to `jobs.csv`.

## Output

`jobs.csv` has four columns: `Title`, `Company`, `Location`, and `Link`.

## How to run

Install the libraries:

```
pip install requests beautifulsoup4
```

Run the script:

```
python jobs.py
```

## Notes

- Close `jobs.csv` in Excel before running the script, or you will get a `PermissionError`.
- The file is saved with `utf-8-sig` encoding so Excel shows special characters correctly.
