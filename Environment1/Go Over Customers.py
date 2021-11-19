import time

from Classlib import select_element
from Classlib import Lightspeed as ls
from Classlib import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

ls.Login('marpab96@gmail.com','Il0veSad!e2020')
ls.Service()

# Access the workorders
Workorders_button = select_element(By.CSS_SELECTOR, "button[id = 'workOrdersButton']")
Workorders_button.click()

# Filter by workorders for me
Employee_filter = Select(select_element(By.CSS_SELECTOR, "select[id = 'listing_employee_id']"))
Employee_filter.select_by_visible_text('Pablo Martinez')

search_button = select_element(By.CSS_SELECTOR, "button[id = 'searchButton']")
search_button.click()

time.sleep(2)
workorders = driver.find_elements(By.CSS_SELECTOR, "tr[data-automation = 'rowWorkorders']")
WO_count = len(workorders)
print('Sorting through ', WO_count, ' workorders...')

# Access the notes on each workorder
for workorder in workorders:
    access = driver.find_element(By.CSS_SELECTOR, "a[title = 'Edit Record']")
    link = access.get_attribute('href')

    # replace this with a new tab, eventually
    driver.get(link)

    # Find the notes
    notes_box = select_element(By.CSS_SELECTOR, "[id = 'internal_note']")
    notes = notes_box.text

    # Extract the dates and number of events with customer

    # Find when the last contact happened

    # if it happened over a month ago, the workorder to a list

    # Close this window and go back to the main one

# Find the last date on which the customer was contacted

# if the date of last contact was more than a month ago, look at the date they last made a payment of some sort

# if any of those dates are over a month, let me know to call them'''
