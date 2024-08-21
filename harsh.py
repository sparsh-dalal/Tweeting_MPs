from selenium import webdriver
from time import sleep

# Replace this path with the actual path to your Chrome WebDriver executable
webdriver_path = 'C:\Program Files\Drivers\chromedriver-win64\chromedriver.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)
tweet = {'917791044158185473', '917791130590183424', '917791291823591425'}
# Open the Google homepage
for x in tweet:

    driver.get(f'https://twitter.com/WMTWTV/status/{x}')
    sleep(10)

# You can perform additional actions here, such as searching on Google or interacting with elements on the page

# Close the browser window
driver.quit()
