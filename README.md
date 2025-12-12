# Amazon Product Search Automation

Automation project for the QA Skill Assessment. I've built a Selenium script that automates the product search workflow on Amazon.com.

## What I've Automated

I created this script to automatically:
1. Open Amazon's homepage
2. Search for a product (I used "laptop" as an example)
3. Click on the first product from the search results
4. Check if the product page loaded correctly
5. Save a screenshot of the product page

The whole thing runs automatically once you start it

## Why I Built It This Way

### Handling Dynamic Elements
Amazon's website loads elements dynamically, so I used `WebDriverWait` throughout my code. This makes sure the script waits for elements to appear before trying to interact with them. I set a 20-second timeout which works well for most internet speeds.

### Reusable Methods
I organized everything into separate methods - one for each step. This makes the code easy to read and modify. If I need to change how the search works, I just update that one method.

### Validation Strategy
For validation, I check if the "Add to Cart" button exists on the product page. As a backup, I also verify the URL contains "/dp/" which is Amazon's product page pattern. This dual approach makes it more reliable.

### Screenshot Feature
I added automatic screenshots so you can see the final result. If something goes wrong, it saves an error screenshot which helps with debugging.

## Tech Stack I Used

- **Language:** Python 3
- **Framework:** Selenium WebDriver  
- **Browser:** Chrome (with ChromeDriver)
- **Key Technique:** WebDriverWait for handling dynamic content

## Getting Started

### Installing Dependencies

First, install Selenium:

```bash
pip install selenium
```

Then install ChromeDriver (this lets Selenium control Chrome):

```bash
pip install webdriver-manager
```

Or if you prefer, I've created a requirements file:

```bash
pip install -r requirements.txt
```

## Running the Script

Just run this command in your terminal:

```bash
python amazon_search.py
```

The browser will open automatically and you'll see it perform each step.

## How My Code Works

I structured everything in a class called `AmazonAutomation`. Here's what each method does:

### 1. `__init__()`
Sets up Chrome with some options to make it work smoothly. I disabled some automation flags so Amazon doesn't immediately detect it as a bot.

### 2. `navigate_to_homepage()`
Opens Amazon.com and waits for it to load. Simple but essential!

### 3. `search_product()`
Finds the search box using its ID, types in the product name, and presses Enter. I used `WebDriverWait` here to make sure the search box is ready before typing.

### 4. `click_first_result()`
This was the trickiest part. Amazon's search results can have different structures, so I made it find ANY link with "/dp/" in the URL (that's how Amazon structures product links). Once it finds one, it scrolls to it and clicks using JavaScript - which is more reliable than regular clicks.

### 5. `validate_product_page()`
Checks if we're actually on a product page by looking for the "Add to Cart" button. If that's not found, it checks the URL as a backup. This way, validation still works even if Amazon changes their button layout.

### 6. `take_screenshot()`
Saves a picture of whatever's on screen. Gets saved as "product_screenshot.png" in the same folder.

### 7. `close()`
Closes the browser cleanly.

## What You'll See When It Runs

If everything works correctly:

```
Starting automation...
✓ Navigated to Amazon
✓ Searched for: laptop
✓ Clicked first result
✓ Product page loaded - Add to Cart found
✓ Screenshot saved: product_screenshot.png

✓ SUCCESS - All steps completed!
```

If there's an issue:

```
Starting automation...
✓ Navigated to Amazon
✓ Searched for: laptop
✗ ERROR: Could not find first result
✓ Screenshot saved: error.png
```

## Common Issues and How I Handle Them

### Amazon Shows a CAPTCHA

Sometimes Amazon asks to verify you're not a robot. If this happens, check the `error.png` file - you'll see the CAPTCHA there.

**Quick fix:** Add this line to allow manual CAPTCHA solving:

```python
def navigate_to_homepage(self):
    self.driver.get("https://www.amazon.com")
    input("If you see a CAPTCHA, solve it and press Enter...")
    time.sleep(2)
    print("Navigated to Amazon")
```

### Elements Not Found

If the script can't find elements, it might be loading too slowly. I've added wait times, but you can increase them:

```python
time.sleep(5)  # Change any time.sleep(2) to this
```

### ChromeDriver Issues

Make sure your ChromeDriver version matches your Chrome browser version. Using `webdriver-manager` (like I did in the install steps) handles this automatically.

## Customizing the Search

Want to search for something other than laptops? Just change line 66:

```python
bot.search_product("wireless mouse")
```

You can search for anything Amazon sells!

## Project Structure

```
amazon-automation/
│
├── amazon_search.py          # My main script
├── requirements.txt          # Dependencies
├── product_screenshot.png    # Generated when successful
README.md          

```

## Requirements File

Here's what's in my `requirements.txt`:

```
selenium>=4.15.0
```

## Assignment Requirements - How I Met Them

✅ **Navigate to homepage** - Done in `navigate_to_homepage()` method  
✅ **Search for product** - Done in `search_product()` method  
✅ **Click first result** - Done in `click_first_result()` method  
✅ **Validate page loaded** - Done in `validate_product_page()` method (checks Add to Cart button)  
✅ **Handle dynamic elements** - Used WebDriverWait throughout  
✅ **Reusable methods** - Each step is a separate, clear method  
✅ **Take screenshot** - Done in `take_screenshot()` method  
✅ **Clean code** - Organized in a class with descriptive names  


## Testing Notes

I tested this script multiple times and it works reliably on my machine. However, Amazon sometimes shows CAPTCHAs or changes their layout, so if you run into issues, check the error screenshot first - it usually shows what went wrong
---
