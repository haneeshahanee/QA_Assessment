from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AmazonAutomation:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def navigate_to_homepage(self):
        # Navigating to Amazon's homepage
        self.driver.get("https://www.amazon.com")
        time.sleep(2)
        print(" Navigated to Amazon")

    def search_product(self, product_name):
        # Finding the search box, type the product name and press Enter
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys(product_name, Keys.RETURN)
        time.sleep(2)
        print(f" Searched for: {product_name}")

    def click_first_result(self):
      
        time.sleep(3)  # wait for Amazon to load

        # Finding any product link with /dp/ in URL
        all_links = self.driver.find_elements(By.TAG_NAME, "a")

        for link in all_links:
            href = link.get_attribute("href")
            if href and "/dp/" in href and link.is_displayed():
                try:
                    # Scroll to the link and click it (using JS for better reliability)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
                    time.sleep(1)
                    self.driver.execute_script("arguments[0].click();", link)
                    time.sleep(3)
                    print(" Clicked first result")
                    return
                except:
                    #if click fails, try next link
                    continue

        raise Exception("Could not find first result")

    def validate_product_page(self):
        # Checking for Add to Cart button
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
            print(" Product page loaded - Add to Cart found")
        except:
            # Checking URL as fallback
            if "/dp/" in self.driver.current_url:
                print(" Product page loaded - URL verified")
            else:
                raise Exception("Product page not loaded")

    def take_screenshot(self, filename="product_screenshot.png"):
        #takes a screenshot of the current page
        self.driver.save_screenshot(filename)
        print(f" Screenshot saved: {filename}")

    def close(self):
        #closing the browser
        self.driver.quit()


def main():
    print("Starting automation...")

    bot = AmazonAutomation()

    try:
        #navigation and actions
        bot.navigate_to_homepage()
        bot.search_product("laptop")
        bot.click_first_result()
        bot.validate_product_page()
        bot.take_screenshot()

        print("\n SUCCESS - All steps completed!")
        time.sleep(3)

    except Exception as e:
        print(f"\n ERROR: {e}")
        bot.take_screenshot("error.png")

    finally:
        bot.close()


if __name__ == "__main__":
    main()