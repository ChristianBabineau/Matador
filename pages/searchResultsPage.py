from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class SearchResultsPage:
    def __init__ (self, driver):
        self.driver = driver
        
    #XPATHS
    IMAGE_THUMBNAILS = (By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div/div/div/section[1]/ol/li[1]/div/div/div[2]")
    RESULTS = (By.XPATH,"/html/body/div[2]/div[6]/div[4]/div/div/div/div/section[1]/ol")

    def getImageURLs(self):
        thumbnails = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.IMAGE_THUMBNAILS)
        )
        images = thumbnails.find_elements(By.CLASS_NAME, 'module--images__thumbnails__link')
        imageURLS = [image.get_attribute('href') for image in images]
        urlList=[]
        pattern = r'(?:\=http).*'
        for url in imageURLS:
            urlList.append(re.findall(pattern,url)[0].strip('='))
        return urlList
    
    def getTitles(self):

        results = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.RESULTS)
        )
        titleList=[]
        for i in range(10):
            titleList.append(results.find_element(By.XPATH, '//*[@id="r1-'+str(i)+'"]/div[2]/h2/a/span').text)

        return titleList
