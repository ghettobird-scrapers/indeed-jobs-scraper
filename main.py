# Based on:
# https://github.com/UmaisZahid/Indeed-Job-Scraper/blob/master/scrape.py

from ghettobird import fly
from selenium import webdriver

chromedriver_location = 'c:/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver_location)

bird = {
    "url": "https://www.indeed.com/l-St.-Louis,-MO-jobs.html",
    "flightpath": {
        "jobs": [{
            "@iterate": "//div[@data-tn-component='organicJob']",
            "title": ".//a[@data-tn-element='jobTitle']",
            "company": ".//*[@data-tn-element='companyName']",
            "rating": ".//span[@class='ratingsContent']",
            "location": ".//span[@class='location accessible-contrast-color-location']",
            "description": ".//div[@class='summary']//ul//li",
            "salary": ".//span[@class='salaryText']",
            "date_posted": ".//span[@class='date ']"
        }]
    }, "options": {
        "browser": browser
    }
}

scraped = fly(bird)
print(scraped['results'])
