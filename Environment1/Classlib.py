# Other Imports
import time
from dataclasses import dataclass

# selenium imports
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common import exceptions

from Groupmelib import Groupme

Work_orders = []


def select_element(method, flag):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((method, flag)))


# Define a workorder
driver = webdriver.Chrome()


@dataclass
class Workorder:
    customer_name: str
    WO_number: str


class Lightspeed:
    def Login(username, password):

        driver.get('https://cloud.lightspeedapp.com/login.html')

        usrname = select_element(By.CSS_SELECTOR, "input[name = 'login']")
        passwrd = select_element(By.CSS_SELECTOR, "input[name = 'password']")

        usrname.clear()
        passwrd.clear()

        usrname.send_keys(username)
        passwrd.send_keys(password)

        login_button = select_element(By.CSS_SELECTOR, "button[type = 'submit']")
        login_button.click()

    # Clock an employee in to work
    def clock_in(name, pin):
        menu = select_element(By.CSS_SELECTOR, "a[class = 'cr-topbar__toggler-link']")
        time_clock = select_element(By.CSS_SELECTOR, "a[title = 'Time clock']")
        try:
            time_clock.click()
        except:
            menu.click()
            time_clock.click()

        time.sleep(2)

        is_clocked_in = False

        employees_clocked_in = driver.find_elements_by_xpath('/html/body/div[3]/nav/div/div/article/div[1]/ul/li')
        # check if the employee is clocked in or not
        for employee in employees_clocked_in:
            if name == employee.text:
                is_clocked_in = True
            else:
                pass

        if not is_clocked_in:
            print('Welcome back, ', name, '! Clocking you in now...')
            # Enter the employee pin number
            clock_pin_input = select_element(By.CSS_SELECTOR, "input[id = 'clock_access_pin']")
            clock_pin_input.clear()
            clock_pin_input.send_keys(pin)
            clock_submit_button = select_element(By.CSS_SELECTOR, "input[id = 'clock-in-out-submit']")
            clock_submit_button.click()
            time.sleep(2)
            # Check if you are now clocked in
            for employee in employees_clocked_in:
                if name == employee.text:
                    print(name, ', you are now clocked in')
                    is_clocked_in = True
                else:
                    pass
            if not is_clocked_in:
                print('Something may have gone wrong with clocking in, try clocking in manually')
            else:
                pass

        # don't do anything if they were already clocked in
        else:
            print(
                'You were already clocked in! If you were trying to clock in, please inform your manager about the mistake.')

    # Access the Service Menu
    def Service():
        '''
        Accesses the Service Menu
        :return:
        '''
        # first, see if the main menu is present
        time.sleep(3)
        service_menu = driver.find_element(By.CSS_SELECTOR, "a[title = 'Service']")
        if service_menu.is_displayed():
            service_menu.click()
        # if It's not, then click the main menu button to make it come up
        else:
            main_menu = driver.find_element(By.CSS_SELECTOR, "a[class = 'cr-topbar__toggler-link']")
            main_menu.click()
            service_menu.click()
        # either way, click the service button

    def create_workorder():
        time.sleep(2)
        # find the customer's name
        customer_name = driver.find_element_by_xpath('//*[@id="view"]/div/div[2]/div/div/div[1]/hgroup/h2').text
        # find the workorder number
        wo_number = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[5]/span/var').text
        # add it to the list
        new_wo = Workorder(customer_name, wo_number)
        Work_orders.append(new_wo)
        print('Added ', new_wo.customer_name, '\'s Work Order to the list')
        print('Number ', new_wo.WO_number)
        line_items = driver.find_elements_by_css_selector("tr[data-automation = 'wolineItem']")
        print('With ', len(line_items), ' line items')

    def search_workorder_by_id(wo_number):

        # Access the service menu
        Lightspeed.Service()

        # Access the workorders and look for the WO number
        work_orders_button = select_element(By.CSS_SELECTOR, "button[id = 'workOrdersButton']")
        work_orders_button.click()
        try:
            id_search = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "name = ['id_search']")))
            id_search.clear()
            id_search.send_keys(wo_number)
        except selenium.common.exceptions.TimeoutException:
            driver.find_element_by_xpath('//*[@id="listing_id_search"]').clear()
            driver.find_element_by_xpath('//*[@id="listing_id_search"]').send_keys(wo_number)
            driver.find_element_by_xpath('//*[@id="listing_id_search"]').send_keys(Keys.ENTER)
            time.sleep(1)
            order = select_element(By.XPATH, "/html/body/div[3]/div[6]/div/div/div/div/table/tbody/tr/td[1]/a")
            order.click()
            order.click()
        Lightspeed.create_workorder()

    def finish_workorder(wo_number, contact_result):

        # Search the workorder in question
        Lightspeed.search_workorder_by_id(wo_number=wo_number)

        # Set the Status to finished
        status_bar = select_element(By.ID, 'workorder_edit_status_field')
        order_status = Select(status_bar)
        order_status.select_by_visible_text('Finished')
        all_available_options = order_status.options
        print(all_available_options)

        # Note the Hook Out
        hook_out = select_element(By.ID, 'hookOutInputField')
        hook_out.clear()
        hook_out.send_keys('RPS Ready for Pickup')

        # Check all the "Finished" Checkboxes
        finished_checkboxes = driver.find_elements_by_xpath(
            "/html/body/div[3]/div[7]/div/div[2]/div/div/div[2]/div/table[1]/tbody/tr/td[4]/label/input")
        print('Found ', len(finished_checkboxes), ' finished checkboxes')
        for checkbox in finished_checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
            else:
                print('Line item has already been marked finished')
                pass

        # Write in the notes how the customer was contacted with a timestamp
        add_time = select_element(By.XPATH, '//*[@id="workorder_status_wrapper"]/div[3]/div[2]/label/a')
        add_time.click()

        # write the contact result into the notes
        notes = select_element(By.XPATH, '//*[@id="internal_note"]')
        try:
            if contact_result == 'Spoke':
                notes.send_keys(
                    'Spoke with customer(s) and advised them that their piece(s) is(are) ready to be picked up')
            elif contact_result == 'Message':
                notes.send_keys('Left voicemail advising customer(s) that their piece(s) is(are) ready to be picked up')
            else:
                notes.send_keys('Unable to contact customer(s) or leave message because ',
                                input('Please describe reason no message could be left: '))
        except TypeError:
            print("it looks like you haven't called this customer yet, call and enter a contact result")