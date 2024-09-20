from selenium.webdriver.edge.options import Options
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv


# aria-label="Next"
def main_job():
        chrome_options = Options()
        chrome_driver = "/Users/vishal04/Desktop/Image_geo_location_gmap/chromedriver" # chromedrive software location
        driver = webdriver.Chrome(service=Service(chrome_driver), options=chrome_options)
        wait = WebDriverWait(driver, 30)

        # open url
        in_URL = 'https://www.google.com/maps/contrib/105321065996895293288/photos/@6.5761012,3.389797,3a,75y,90t/data=!3m7!1e2!3m5!1sAF1QipPMCYrug0dvTCFaHfX0Aml26P-x4F2Rhz7eZfo-!2e10!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPMCYrug0dvTCFaHfX0Aml26P-x4F2Rhz7eZfo-%3Dw365-h486-k-no!7i1932!8i2576!4m3!8m2!3m1!1e1?entry=ttu'
    
        wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(@aria-label, 'Next')]")))
        while True:
               sleep(0.3)
               driver.find_element(By.XPATH,
                                    "//button[contains(@aria-label, 'Next')]").click()
               currenturl = driver.current_url
               try:
                link = currenturl.split('!1s')[-1].split('!')[0]
                gps = currenturl.split('@')[-1].split(',')[0]+','+currenturl.split('@')[-1].split(',')[1]
                row = [link,gps]

                with open('example.csv', 'a',newline='') as csvfile:
                # creating a csv writer object 
                        csvwriter = csv.writer(csvfile) 
                                
                        # writing the fields 
                        csvwriter.writerow(row) 
               except:
                pass
  
main_job()