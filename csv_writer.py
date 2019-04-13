"""
    Simple script to scrape cat quotes from a website and store in a CSV file
    csv_writer.py
    
    Andrew Tandy 2019
"""

import csv
from site_scraper import scrape_site

def compile_csv(name):
    """ using csv module to write records to named csv file """
    csv_file  = open(name+'.csv', 'w')
    csv_writer = csv.writer(csv_file)

    # Write the first row as headers for the file, Quote & Author respectively
    csv_writer.writerow([
        'Quote',
        'Author'
    ])

    # Run the function from scrape and store results
    scrape_quotes = scrape_site()

    for i in range(len(scrape_quotes)):
        """ for loop to pull from scrape_quotes object """

        # Create quote and author and pull from scrape_quotes object
        quote = scrape_quotes[i][0]
        author = scrape_quotes[i][1]

        # Write a new row into csv
        csv_writer.writerow([
            quote,
            author
        ])
        
        # Show the process completed in terminal
        print(f'{quote} - {author} written to {name}.csv')

    # Ensure csv file is closed at the end
    csv_file.close()
