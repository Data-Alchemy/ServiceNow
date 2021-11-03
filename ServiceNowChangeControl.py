# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time

wndw_email = open('').read()
wndw_pwd = open('').read()

email=wndw_email
password=wndw_pwd

cc_days_out = 3
window = 30
config_item = "IICS IPaaS"
#"TRICKLEF1AS1WP"
#Azure Analysis Services
#"IICS IPaaS"
#'Control-M Jobs'
short_desc = 'tf_C009_SALES_DW_to_PMM is failing due to pre processing shell script not working'
chang_desc = 'Change job in ipaas production  to stop future errors from occuring. Job ID: DWIP0022D ' \
             'Job Name: Import NMH to DW , Reason: This job is failing because of a bad command setup. '
why_this_time = 'This process is high visibility and leadership team has asked the problems be resolved'
communicate = 'BI Team , Data Services Team , DnA Team'
worse_case = 'Job will fail and process will not be available until rollback'
impacts_who = 'BI Team, DnA Team'
pre_imp = 'Verify that job is working'
imp = 'Verify that implementation completed successfully'
ver = 'Verify the new job completes successfully'
bck = 'Rollback change'
work_notes = "change is required to fix issues with Informatica PMM job"
assign_to = 'Sebastian Hansen'
assign_group = "Data Engineering - Data Services"

def business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date.strftime("%Y-%m-%d %H:%M:%S")
current_date = datetime.datetime.now() -datetime.timedelta(hours=datetime.datetime.now().hour+12,minutes=datetime.datetime.now().minute,seconds= datetime.datetime.now().second )
start_window = current_date
end_window = current_date +datetime.timedelta(minutes=window)
start_date= business_days(start_window,cc_days_out)
end_date= business_days(end_window,cc_days_out)
print(start_date)
print(end_date)

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        self.driver.delete_all_cookies()
        self.email = email
        self.password = password
        driver.get(f'{url}')
        driver.maximize_window()
        email_element = driver.find_element_by_name('IDToken1')
        email_element.send_keys(self.email)  # Give keyboard input
        # send password#
        password_element = driver.find_element_by_name('IDToken2')
        password_element.send_keys(self.password)  # Give password as input too
        login_button2 = driver.find_element_by_xpath('//*[@id="loginContent"]/form/fieldset/div/input')
        login_button2.click()
        driver.switch_to.frame(0)
        driver.find_element_by_id("sys_display.change_request.cmdb_ci").send_keys(config_item)
        driver.find_element_by_id("sys_display.change_request.cmdb_ci").send_keys(Keys.ENTER)
        driver.find_element_by_id("change_request.start_date").send_keys(start_date)
        driver.find_element_by_id("change_request.end_date").send_keys(end_date)
        driver.find_element_by_id("change_request.short_description").send_keys(short_desc)
        driver.find_element_by_id("change_request.description").send_keys(chang_desc)
        driver.implicitly_wait(2)
        driver.find_element_by_id("change_request.u_date_time_reason").send_keys(why_this_time)
        driver.find_element_by_id("change_request.u_date_time_reason").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.u_business_change_plan").send_keys(short_desc)#communicate how and what
        driver.find_element_by_id("change_request.u_business_change_plan").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.u_communicated").send_keys(communicate)#"communicate to who"
        driver.find_element_by_id("change_request.u_communicated").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.u_worst_case_impact").send_keys(worse_case)#"worse case impact"
        driver.find_element_by_id("change_request.u_worst_case_impact").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.u_worst_case_to").send_keys(impacts_who)#"worse case impacts who"
        driver.find_element_by_id("change_request.u_worst_case_to").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.test_plan").send_keys(pre_imp)#"pre-implementation testing"
        driver.find_element_by_id("change_request.test_plan").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.implementation_plan").send_keys(imp)#"Implementation Plan"
        driver.find_element_by_id("change_request.implementation_plan").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.u_verified_to").send_keys(ver)
        driver.find_element_by_id("change_request.u_verified_to").send_keys(Keys.RETURN)
        driver.find_element_by_id("change_request.backout_plan").send_keys(bck )#"backout plan"
        driver.find_element_by_id("change_request.backout_plan").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath('//button[@id="sysverb_insert_bottom"]'))
        driver.find_element_by_xpath('//button[@id="sysverb_insert_bottom"]').click()
        driver.implicitly_wait(1)
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_id("fill_out_risk_assessment_bottom"))
        driver.find_element_by_id("fill_out_risk_assessment_bottom").click()
        time.sleep(2)
        driver.implicitly_wait(1)
        driver.switch_to.frame(1)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='QUESTION:e91eea3a2bb5790089a181afe8da159d']/div[2]/div/span[2]/div/span/label").click()
        driver.find_element_by_xpath("//div[@id='QUESTION:b1ddae3a2bb5790089a181afe8da1589']/div[2]/div/span[2]/div/span/label").click()
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath("//div[@id='QUESTION:b1ddae3a2bb5790089a181afe8da1589']/div[2]/div/span[2]/div/span/label"))
        driver.find_element_by_xpath("//div[@id='QUESTION:b1ddae3a2bb5790089a181afe8da1589']/div[2]/div/span[2]/div/span/label").click()
        driver.find_element_by_id("post_survey").click()
        driver.switch_to.parent_frame()
        driver.find_element_by_id("928001540a0a2c764eaf70d16624a94a_bottom").click()
        driver.find_element_by_id("change_request.scope").click()
        Select(driver.find_element_by_id("change_request.scope")).select_by_visible_text("A few clients, less than 1 department")
        driver.find_element_by_id("change_request.scope").click()
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_id("928001540a0a2c764eaf70d16624a94a_bottom"))
        driver.find_element_by_id("928001540a0a2c764eaf70d16624a94a_bottom").click()
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_id("create_change_task_bottom"))
        driver.find_element_by_id("create_change_task_bottom").click()
        driver.find_element_by_id("change_task.u_deployment_type").click()
        Select(driver.find_element_by_id("change_task.u_deployment_type")).select_by_visible_text("No Tool")
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_id("change_task.u_deployment_type"))
        driver.find_element_by_id("change_task.u_deployment_type").click()
        driver.find_element_by_id("change_task.short_description").click()
        driver.find_element_by_id("change_task.short_description").click()
        driver.find_element_by_id("change_task.short_description").clear()
        driver.find_element_by_id("change_task.short_description").send_keys("make requested change")
        driver.find_element_by_id("change_task.description").click()
        driver.find_element_by_xpath("//div[@id='element.change_task.description']/div[2]").click()
        driver.find_element_by_id("change_task.description").clear()
        driver.find_element_by_id("change_task.description").send_keys("change is required to support production process")
        driver.find_element_by_id("activity-stream-work_notes-textarea").click()
        driver.find_element_by_id("activity-stream-work_notes-textarea").click()
        driver.find_element_by_id("activity-stream-work_notes-textarea").clear()
        driver.find_element_by_id("activity-stream-work_notes-textarea").send_keys(work_notes)
        driver.find_element_by_id("sys_display.change_task.assigned_to").click()
        driver.find_element_by_id("sys_display.change_task.assignment_group").send_keys(assign_group)
        driver.find_element_by_id("sys_display.change_task.assigned_to").send_keys(assign_to)
        driver.find_element_by_id("sys_display.change_task.assigned_to").click()
        driver.find_element_by_id("activity-stream-work_notes-textarea").click()
        driver.find_element_by_id("sys_display.change_task.assigned_to").click()
        driver.find_element_by_id("element.change_task.assigned_to").click()
        driver.find_element_by_id("sys_display.change_task.assignment_group").click()
        driver.find_element_by_id("change_task.u_timing").click()
        Select(driver.find_element_by_id("change_task.u_timing")).select_by_visible_text("Between")
        driver.find_element_by_id("change_task.u_timing").click()
        #driver.find_element_by_id("accept_change_task").click()
        driver.find_element_by_xpath("//body").click()
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_id("request_accept_change_task_bottom"))
        driver.find_element_by_id("request_accept_change_task_bottom").click()
        time.sleep(2)
        driver.implicitly_wait(1)
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath('//*[@id="accept_change_task"]'))
        driver.find_element_by_xpath('//*[@id="accept_change_task"]').click
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_id("accept_change_task"))
        driver.find_element_by_id("accept_change_task").click()
        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_id("request_change_approval_bottom"))
        driver.find_element_by_id("request_change_approval_bottom").click()
        time.sleep(2)
#        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_id("request_change_approval"))
#        driver.find_element_by_id("request_change_approval").click()
        print('Change Control Submitted for approval')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
