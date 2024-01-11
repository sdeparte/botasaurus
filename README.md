<p align="center">
  <img src="https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/mascot.png" alt="botasaurus" />
</p>
  <div align="center" style="margin-top: 0;">
  <h1>🤖 Botasaurus 🤖</h1>
  </div>

<h3 align="center">
  The web has evolved. Finally, web scraping has too.
</h3>

<p align="center">
  <b>The All in 1 Web Scraping Framework</b>
</p>


<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/botasaurus.svg" width="80px" height="28px" alt="View" />
</p>


<p align="center">
  <a href="https://gitpod.io/#https://github.com/omkarcloud/botasaurus-starter">
    <img alt="Run in Gitpod" src="https://gitpod.io/button/open-in-gitpod.svg" />
  </a>
</p>

## In a nutshell

Botasaurus is an all in 1 web scraping framework built for the modern web. We
address the key pain points web scrapers face when scraping the web.

Our aim it to make web scraping extremely easy and save you hours of Development Time.

## Features

Botasaurus comes fully baked, with batteries included. Here is a list of things it can do that no other web scraping framework can:

- **Most Stealthiest Framework LITERALLY**: In the entire JS and Python Universe, we are literally the most stealthy framework, even more stealthy than `undetected-chromedriver` and `puppeteer-stealth`. Our framework can easily bypass Cloudflare JS and Captcha Challenges, and your bots can easily visit websites like `https://nowsecure.nl/`. For more details, [see this FAQ.](https://github.com/omkarcloud/botasaurus/tree/master#can-you-bypass-cloudflareimperva-challenges)
- **Defeat Cloudflare with HTTP Requests:** No HTTP library, be it `httpx`, `hrequests`, or `cloudscraper`, can defeat Cloudflare, but we can 😤! [Read on to learn how.](https://github.com/omkarcloud/botasaurus/tree/master#how-to-scrape-cloudflare-protected-websites-with-simple-http-requests)
- **SSL Support for Authenticated Proxy:** We are the first and only Python Web Scraping Framework to offer SSL support for authenticated proxies. No other web scraping libraries be it cloudscraper, seleniumwire, playwright provides this unique feature, enabling you to easily bypass Cloudflare detection when using authenticated proxies.
- **Data Cleaners:** Clean data scraped from the website with ease.
- **Debuggability:** When a crash occurs due to an incorrect selector, etc., Botasaurus pauses the browser instead of closing it, facilitating painless on-the-spot debugging.
- **Caching:** Botasaurus allows you to cache web scraping results, ensuring lightning-fast performance on subsequent scrapes.
- **Easy Configuration:** Easily save time with parallelization, profile, and proxy configuration.
- **Time-Saving Selenium Shortcuts:** Botasaurus comes with numerous Selenium shortcuts to make web scraping incredibly easy.

## 🚀 Getting Started with Botasaurus

Welcome to Botasaurus! Let’s dive right in with a straightforward example to understand how it works.

In this tutorial, we will go through the steps to scrape the heading text from [https://www.omkar.cloud/](https://www.omkar.cloud/).

![Botasaurus in action](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/starter-bot-running.gif)

### Step 1: Install Botasaurus

First things first, you need to install Botasaurus. Run the following command in your terminal:

```shell
python -m pip install botasaurus
```

### Step 2: Set Up Your Botasaurus Project

Next, let’s set up the project:

1. Create a directory for your Botasaurus project and navigate into it:

```shell
mkdir my-botasaurus-project
cd my-botasaurus-project
code .  # This will open the project in VSCode if you have it installed
```

### Step 3: Write the Scraping Code

Now, create a Python script named `main.py` in your project directory and insert the following code:

```python
from botasaurus import *

@browser
def scrape_heading_task(driver: AntiDetectDriver, data):
    # Navigate to the Omkar Cloud website
    driver.get("https://www.omkar.cloud/")
    
    # Retrieve the heading element's text
    heading = driver.text("h1")

    # Save the data as a JSON file in output/scrape_heading_task.json
    return {
        "heading": heading
    }
     
if __name__ == "__main__":
    # Initiate the web scraping task
    scrape_heading_task()
```

Let’s dissect this code:

- We define a custom scraping task, `scrape_heading_task`, decorated with `@browser`:
```python
@browser
def scrape_heading_task(driver: AntiDetectDriver, data):
```  

- Botasaurus automatically provides an Anti Detection Selenium driver to our function:
```python
def scrape_heading_task(driver: AntiDetectDriver, data):
```  

- Inside the function, we:
    - Navigate to Omkar Cloud
    - Extract the heading text
    - Return the data to be automatically saved as `scrape_heading_task.json` by Botasaurus:
```python
    driver.get("https://www.omkar.cloud/")
    heading = driver.text("h1")
    return {"heading": heading}
```  

- Finally, we initiate the scraping task:
```python
if __name__ == "__main__":
    scrape_heading_task()
```  

### Step 4: Run the Scraping Task

Time to run your bot:

```shell
python main.py
```

After executing the script, it will:
- Launch Google Chrome
- Navigate to [omkar.cloud](https://www.omkar.cloud/)
- Extract the heading text
- Save it automatically as `output/scrape_heading_task.json`.

![Botasaurus in action](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/starter-bot-running.gif)

Now, let’s explore another way to scrape the heading using the `request` module. Replace the previous code in `main.py` with the following:

```python
from botasaurus import *

@request
def scrape_heading_task(request: AntiDetectRequests, data):
    # Navigate to the Omkar Cloud website
    soup = request.bs4("https://www.omkar.cloud/")
    
    # Retrieve the heading element's text
    heading = soup.find('h1').get_text()

    # Save the data as a JSON file in output/scrape_heading_task.json
    return {
        "heading": heading
    }
     
if __name__ == "__main__":
    # Initiate the web scraping task
    scrape_heading_task()
```

In this code:

- We are using the BeautifulSoup (bs4) module to parse and scrape the heading.
- The `request` object provided is not a standard Python request object but an Anti Detect request object, which also preserves cookies.

### Step 5: Run the Scraping Task (Using Anti Detect Requests)

Finally, run the bot again:

```shell
python main.py
```

This time, you will observe the same result as before, but instead of using Anti Detect Selenium, we are utilizing the Anti Detect request module.

*Note: If you don't have Python installed, then you can run Botasaurus in Gitpod, a browser-based development environment, by following [this section](https://github.com/omkarcloud/botasaurus#how-to-run-botasaurus-in-gitpod).*

## 💡 Understanding Botasaurus

Power of Bots is Immense, A Bot
   - Can apply on your behalf to Linkedin Jobs 24 Hours
   - Scrape Phone Number of Thousands of Businesses from Google Maps to sell your Products to.
   - Mass Message People on Twitter/LinkedIn/Reddit for selling your Product
   - Sign Up 100's of Accounts on MailChimp to send 50,000 (500 emails * 100) Emails all for free

Let's learn features of Botasaurus that help you unlock these super powers? 

### Could you show me an example where you defeat Cloudflare?

Sure, Run the following Python code to scrape G2.com, a website protected by Cloudflare:

```python
from botasaurus import *

@browser()
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.google_get("https://www.g2.com/products/github/reviews")
    heading = driver.text('h1')
    print(heading)
    return heading

scrape_heading_task()
```

After running this script, you'll notice that the G2 page opens successfully, and the code prints the page's heading.

![not blocked](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/botasurussuccesspage.png)

### How to Scrape Multiple Data Points/Links?

To scrape multiple data points or links, define the `data` variable and provide a list of items to be scraped:

```python
@browser(data=["https://www.omkar.cloud/", "https://www.omkar.cloud/blog/", "https://stackoverflow.com/"])
def scrape_heading_task(driver: AntiDetectDriver, data):
  # ...
```

Botasaurus will launch a new browser instance for each item in the list and merge and store the results in `scrape_heading_task.json` at the end of the scraping.

![scraped data](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/scraped-data.png)

Please note that the `data` parameter can also handle items such as dictionaries.

For instance, if you're automating the sign-up process for bot accounts on a website, you can pass dictionaries to it like so:

```python
@browser(data=[{"name": "Mahendra Singh Dhoni", ...}, {"name": "Virender Sehwag", ...}])
def scrape_heading_task(driver: AntiDetectDriver, data: dict):
    # ...
```

<!-- In this example, the `data` parameter is supplied with a list of dictionaries. Each dictionary contains details for a different bot account that you wish to sign up. -->

### How to Scrape in Parallel?

To scrape data in parallel, set the `parallel` option in the browser decorator:

```python
@browser(parallel=3, data=["https://www.omkar.cloud/", ...])
def scrape_heading_task(driver: AntiDetectDriver, data):
  # ...
```

### How to know how many scrapers to run parallely?

To determine the optimal number of parallel scrapers, pass the `bt.calc_max_parallel_browsers` function, which calculates the maximum number of browsers that can be run in parallel based on the available RAM:

```python
@browser(parallel=bt.calc_max_parallel_browsers, data=["https://www.omkar.cloud/", ...])
def scrape_heading_task(driver: AntiDetectDriver, data):
  # ...
```

*Example: If you have 5.8 GB of free RAM, `bt.calc_max_parallel_browsers` would return 10, indicating you can run up to 10 browsers in parallel.*

### How to Cache the Web Scraping Results?

To cache web scraping results and avoid re-scraping the same data, set `cache=True` in the decorator:

```python
@browser(cache=True, data=["https://www.omkar.cloud/", ...])
def scrape_heading_task(driver: AntiDetectDriver, data):
  # ...  
```


### How Botasaurus helps me in debugging?

Botasaurus enhances the debugging experience by pausing the browser instead of closing it when an error occurs. This allows you to inspect the page and understand what went wrong, which can be especially helpful in debugging and removing the hassle of reproducing edge cases.

Botasaurus also plays a beep sound to alert you when an error occurs.

![](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/error-prompt.png)

### How to Block Resources like CSS, Images, and Fonts to Save Bandwidth?

Blocking resources such as CSS, images, and fonts can significantly speed up your web scraping tasks, reduce bandwidth usage, and save money spent on proxies.

For example, a page that originally takes 4 seconds and 12 MB's to load might only take one second and 100 KB to load after css, images, etc have been blocked.

To block images, simply use the `block_resources` parameter. For example:

```python
@browser(block_resources=True) # Blocks ['.css', '.jpg', '.jpeg', '.png', '.svg', '.gif', '.woff', '.pdf', '.zip']
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.get("https://www.omkar.cloud/")
    driver.prompt()
    
scrape_heading_task()    
```

If you wish to block only images and fonts, while allowing CSS files, you can set `block_images` like this:

```python
@browser(block_images=True) # Blocks ['.jpg', '.jpeg', '.png', '.svg', '.gif', '.woff', '.pdf', '.zip']
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.get("https://www.omkar.cloud/")
    driver.prompt()

scrape_heading_task()        
```

To block a specific set of resources, such as only JavaScript, CSS, fonts, etc., specify them in the following manner:

```python
@browser(block_resources=['.js', '.css', '.jpg', '.jpeg', '.png', '.svg', '.gif', '.woff', '.pdf', '.zip'])
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.get("https://www.omkar.cloud/")
    driver.prompt()

scrape_heading_task()        
```

### How to Configure UserAgent, Proxy, Chrome Profile, Headless, etc.?

To configure various settings such as UserAgent, Proxy, Chrome Profile, and headless mode, you can specify them in the decorator as shown below:

```python
@browser(
  headless=True, 
  profile='my-profile', 
  proxy="http://your_proxy_address:your_proxy_port",
  user_agent=bt.UserAgents.user_agent_106
)
def scrape_heading_task(driver: AntiDetectDriver, data):
  # ...
```


You can also pass additional parameters when calling the scraping function, as demonstrated below:

```python
@browser()
def scrape_heading_task(driver: AntiDetectDriver, data):
    # ...

data = "https://www.omkar.cloud/"
scrape_heading_task(
  data, 
  headless=True, 
  profile='my-profile', 
  proxy="http://your_proxy_address:your_proxy_port",
  user_agent=bt.UserAgents.user_agent_106
)
```

Furthermore, it's possible to define functions that dynamically set these parameters based on the data item. For instance, to set the profile dynamically according to the data item, you can use the following approach:

```python
@browser(profile=lambda data: data["profile"], headless=True, proxy="http://your_proxy_address:your_proxy_port", user_agent=bt.UserAgents.user_agent_106)
def scrape_heading_task(driver: AntiDetectDriver, data):
    # ...

data = {"link": "https://www.omkar.cloud/", "profile": "my-profile"}
scrape_heading_task(data)
```

Additionally, if you need to pass metadata that is common across all data items, such as an API Key, you can do so by adding it as a `metadata` parameter. For example:

```python
@browser()
def scrape_heading_task(driver: AntiDetectDriver, data, metadata):
    print("metadata:", metadata)
    print("data:", data)

data = {"link": "https://www.omkar.cloud/", "profile": "my-profile"}
scrape_heading_task(
  data, 
  metadata={"api_key": "BDEC26..."}
)
```


<!-- ### How Can I Save Data With a Different Name Instead of 'all.json'?

To save the data with a different filename, pass the desired filename along with the data in a tuple as shown below:

```python
@browser(block_resources=True, cache=True)
def scrape_article_links(driver: AntiDetectDriver, data):
    # Visit the Omkar Cloud website
    driver.get("https://www.omkar.cloud/blog/")
    
    links = driver.links("h3 a")

    filename = "links"
    return filename, links
```
 -->




### Do you support SSL for Authenticated Proxies?

Yes, we are the first Python Library to support SSL for authenticated proxies. Proxy providers like BrightData, IPRoyal, and others typically provide authenticated proxies in the format "http://username:password@proxy-provider-domain:port". For example, "http://greyninja:awesomepassword@geo.iproyal.com:12321".

However, if you use an authenticated proxy with a library like seleniumwire to scrape a Cloudflare protected website like G2.com, you will surely be blocked because you are using a non-SSL connection. 

To verify this, run the following code:

First, install the necessary packages:
```bash 
python -m pip install selenium_wire chromedriver_autoinstaller
```

Then, execute this Python script:
```python
from seleniumwire import webdriver
from chromedriver_autoinstaller import install

# Define the proxy
proxy_options = {
    'proxy': {
        'http': 'http://username:password@proxy-provider-domain:port', # TODO: Replace with your own proxy
        'https': 'http://username:password@proxy-provider-domain:port', # TODO: Replace with your own proxy
    }
}

# Install and set up the driver
driver_path = install()
driver = webdriver.Chrome(driver_path, seleniumwire_options=proxy_options)

# Navigate to the desired URL
link = 'https://www.g2.com/products/github/reviews'
driver.get("https://www.google.com/")
driver.execute_script(f'window.location.href = "{link}"')

# Prompt for user input
input("Press Enter to exit...")

# Clean up
driver.quit()
```

You will definitely encounter a block by Cloudflare:

![blocked](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/seleniumwireblocked.png)

However, using proxies with Botasaurus prevents this issue. See the difference by running the following code:
```python
from botasaurus import *

@browser(proxy="http://username:password@proxy-provider-domain:port") # TODO: Replace with your own proxy 
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.google_get("https://www.g2.com/products/github/reviews")
    driver.prompt()
scrape_heading_task()    
```  

Result: 
![not blocked](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/botasurussuccesspage.png)

NOTE: To run the code above, you will need Node.js installed.

### How to Scrape Cloudflare-Protected Websites with Simple HTTP Requests?

No HTTP library, be it `httpx`, `hrequests`, or `cloudscraper`, can defeat Cloudflare. But, we can thanks to `got-scraping` library. 

All you need to do is specify the `use_stealth` option.

Sounds too good to be true? Run the following code to see it in action:

```python
from botasaurus import *

@request(use_stealth=True)
def scrape_heading_task(request: AntiDetectRequests, data):
    response = request.get('https://www.g2.com/products/github/reviews')
    print(response.status_code)
    return response.text

scrape_heading_task()
```

### Can you bypass Cloudflare/Imperva Challenges?

Yes, we can. Let's learn about various challenges and the best ways to bypass them.

*Connection Challenge*

This is the most popular challenge and requires making a browser-like connection with appropriate headers to the target website. It's commonly used to protect:
- Product Pages
- Blog Pages
- Search Result Pages

Example Page: https://www.g2.com/products/github/reviews

#### What Does Not Work?

Using `httpx`, `hrequests`, or `cloudscraper` fails because, while they send browser-like user agents and headers, they don't establish a browser-like connection, leading to detection.

#### What Works?

- Use the stealth request mode and visit via Google (default behavior). [Recommended]
```python
from botasaurus import *

@request(use_stealth=True)
def scrape_heading_task(request: AntiDetectRequests, data):
    response = request.get('https://www.g2.com/products/github/reviews')
    print(response.status_code)
    return response.text

scrape_heading_task()
```

- Use a real Chrome browser with Selenium and visit via Google. Example Code:
```python
from botasaurus import *

@browser()
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.google_get("https://www.g2.com/products/github/reviews")
    driver.prompt()
    heading = driver.text('h1')
    return heading

scrape_heading_task()
```

*JS Challenge*

This challenge requires performing JS computations that differentiates a Chrome controlled by Selenium/Puppeteer/Playwright from a real Chrome. 

It's commonly used to protect:
- Login/Sign Up pages
- Sign Up Flows

Example Pages: https://nowsecure.nl/, https://www.000webhost.com/cpanel-login, https://signup.live.com/

#### What Does Not Work?

Bare `selenium` and `puppeteer` definitely do not work due to a lot of automation noise. `undetected-chromedriver` and `puppeteer-stealth` also fail to access sites protected by JS Challenge like https://nowsecure.nl/. 

#### What Works?

The Stealth Browser can easily bypass JS Challenges. See the truth for yourself by running this code:

```python
from botasaurus import *
from botasaurus.create_stealth_driver import create_stealth_driver

@browser(
    create_driver=create_stealth_driver(
        start_url="https://nowsecure.nl/",
    ),
)
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.prompt()
    heading = driver.text('h1')
    return heading

scrape_heading_task()    
```

*JS with Captcha Challenge*

This challenge involves JS computations plus solving a Captcha. It's used to protect pages which are rarely but sometimes visited by humans, like:
- 5th Page of G2 Reviews
- 8th Page of Google Search Results

Example Page: https://www.g2.com/products/github/reviews.html?page=5&product_id=github

#### What Does Not Work?

Again, tools like `selenium`, `puppeteer`, `undetected-chromedriver`, and `puppeteer-stealth` fail.

#### What Works?

The Stealth Browser can easily bypass these challenges. See it in action by running this code:

```python
from botasaurus import *
from botasaurus.create_stealth_driver import create_stealth_driver

@browser(
    create_driver=create_stealth_driver(
        start_url="https://www.g2.com/products/github/reviews.html?page=5&product_id=github",
    ),
)
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.prompt()
    heading = driver.text('h1')
    return heading

scrape_heading_task()
```

*Notes:*
1. In stealth browser mode, we default to an 8-second wait before connecting to the browser via Selenium because connecting too early gets us detected. You can customize the wait time by using the `wait` argument. 
```python
from botasaurus import *
from botasaurus.create_stealth_driver import create_stealth_driver

@browser(
    create_driver=create_stealth_driver(
        start_url="https://nowsecure.nl/",
        wait=4, # Waits for 4 seconds before connecting to browser
    ),
)
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.prompt()
    heading = driver.text('h1')
    return heading

scrape_heading_task()
```

Here are some recommendations for wait times:

- For active development with fast internet, set the wait time to **4 seconds**. You most likely have a fast internet connection, so set the wait time to **4 seconds** when developing your Bot.
- If during development you have a slow internet connection, then stick with the default **8 seconds**.
<!-- - When running your bot in the cloud via proxies, increase the wait time to **20 seconds** due to longer data download times.
- For slow proxies, set the wait time to **28 seconds**. -->

2. If you get detected, try changing your IP. Let me share with you  The **fastest**, **simplest**, and best of all, the **free** way to change your IP:

- **Connect your PC to the Internet via a Mobile Hotspot.**
- **Toggle airplane mode off and on on your mobile device.** This will assign you a new IP address.
- **Turn the hotspot back on.**
- **Voila, you have a new, high-quality mobile IP for free!**

<!-- 3. If you are running the bot in Docker on a server and experiencing detection issues, it's suggested to use residential proxies. -->
3. Anti Detection Systems can detect fake randomly generated user agents. So, if you are getting detected, especially on Ubuntu with Cloudflare JS with Captcha Challenge, we recommend using your real user agent and window size, not a randomly generated one. Here's how you can do it:
```python
from botasaurus import *
from botasaurus.create_stealth_driver import create_stealth_driver

@browser(
    user_agent=bt.UserAgent.REAL, 
    window_size=bt.WindowSize.REAL,
    create_driver=create_stealth_driver(
        start_url="https://nowsecure.nl/",
    ),
)
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.prompt()
    heading = driver.text('h1')
    return heading

scrape_heading_task()
```

If you are doing web scraping of publicly available data, then the above code is good and recommended to be used. However, if you are creating multiple accounts, then we don't recommend using the above code because the website may use tools like [fingerprint](https://fingerprint.com/) to capture fingerprints and uniquely identify that bots are creating multiple accounts.

4. We expect to bypass Cloudflare 9 out of 10 times. However, in some cases, they do detect us for reasons like IP blacklisting. In such cases, you can use the following code snippet to make your scraper more robust:
```python
from botasaurus import *
from botasaurus.create_stealth_driver import create_stealth_driver

def get_start_url(data):
    return data

@browser(
    # proxy="http://username:password@proxy-domain:12321" # optionally use proxy
    # user_agent=bt.UserAgent.REAL, # Optionally use REAL User Agent
    # window_size=bt.WindowSize.REAL, # Optionally use REAL Window Size
    max_retry=5,
    create_driver=create_stealth_driver(
        start_url=get_start_url,
        raise_exception=True, 
    ),
)
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.prompt()
    heading = driver.text('h1')
    return heading

scrape_heading_task(["https://nowsecure.nl/", "https://steamdb.info/sub/363669/apps"])
``` 

The above code makes the scraper more robust by raising an exception when detected and retrying up to 5 times to visit the website.

### I want to Scrape a large number of Links, a new selenium driver is getting created for each new link, this increases the time to scrape data. How can I reuse Drivers?

Utilize the `reuse_driver` option to reuse drivers, reducing the time required for data scraping:

```python
@browser(reuse_driver=True)
def scrape_heading_task(driver: AntiDetectDriver, data):
  # ...
```

### Could you show me a practical example where all these Botasaurus Features Come Together to accomplish a typical web scraping project?

Below is a practical example of how Botasaurus features come together in a typical web scraping project to scrape a list of links from a blog, and then visit each link to retrieve the article's heading and date:

```python
from botasaurus import *

@browser(block_resources=True,
         cache=True, 
         parallel=bt.calc_max_parallel_browsers, 
         reuse_driver=True)
def scrape_articles(driver: AntiDetectDriver, link):
    driver.get(link)

    heading = driver.text("h1")
    date = driver.text("time")

    return {
        "heading": heading, 
        "date": date, 
        "link": link, 
    }

@browser(block_resources=True, cache=True)
def scrape_article_links(driver: AntiDetectDriver, data):
    # Visit the Omkar Cloud website
    driver.get("https://www.omkar.cloud/blog/")
    
    links = driver.links("h3 a")

    return links

if __name__ == "__main__":
    # Launch the web scraping task
    links = scrape_article_links()
    scrape_articles(links)
```

### How to Clean Data?
Botasaurus provides a module named `cl` that includes commonly used cleaning functions to save development time. Here are some of the most important ones:

1. **`cl.select`**  
   What `document.querySelector` is to js, is what `cl.select` is to json. This is the most used function in Botasaurus and is incredibly useful.

   This powerful function is popular for safely selecting data from nested JSON.

   Instead of using flaky code like this:
   ```python
   from botasaurus import cl

   data = {
     "person": {
       "data": {
         "name": "Omkar",
         "age": 21
       }
     },
     "data": {
       "friends": [
         {"name": "John", "age": 21},
         {"name": "Jane", "age": 21},
         {"name": "Bob", "age": 21}
       ]
     }
   }

   name = data.get('person', {}).get('data', {}).get('name', None)
   if name:
       name = name.upper()
   else:
       name = None
   print(name)
   ```

   You can write it as:
   ```python
   from botasaurus import cl

   data = {
     "person": {
       "data": {
         "name": "Omkar",
         "age": 21
       }
     },
     "data": {
       "friends": [
         {"name": "John", "age": 21},
         {"name": "Jane", "age": 21},
         {"name": "Bob", "age": 21}
       ]
     }
   }
   print(cl.select(data, 'name', map_data=lambda x: x.upper()))
   ```

   `cl.select` returns `None` if the key is not found, instead of throwing an error.
   ```python
   from botasaurus import cl

   print(cl.select(data, 'name'))  # Omkar
   print(cl.select(data, 'friends', 0, 'name'))  # John
   print(cl.select(data, 'friends', 0, 'non_existing_key'))  # None
   ```

   You can also use `map_data` like this:
   ```python
   from botasaurus import cl

   cl.select(data, 'name', map_data=lambda x: x.upper())  # OMKAR
   ```

   And use default values like this:
   ```python
   from botasaurus import cl

   cl.select(None, 'name', default="OMKAR")  # OMKAR
   ```

2. **`cl.extract_numbers`**
   ```python
   from botasaurus import cl

   print(cl.extract_numbers("I can extract numbers with decimal like 4.5, or with comma like 1,000."))  # [4.5, 1000]
   ```

3. **More Functions**
   ```python
   from botasaurus import cl

   print(cl.extract_links("I can extract links like https://www.omkar.cloud/ or https://www.omkar.cloud/blog/"))  # ['https://www.omkar.cloud/', 'https://www.omkar.cloud/blog/']
   print(cl.rename_keys({"name": "Omkar", "age": 21}, {"name": "full_name"}))  # {"full_name": "Omkar", "age": 21}
   print(cl.sort_object_by_keys({"age": 21, "name": "Omkar"}, "name"))  # {"name": "Omkar", "age": 21}
   print(cl.extract_from_dict([{"name": "John", "age": 21}, {"name": "Jane", "age": 21}, {"name": "Bob", "age": 21}], "name"))  # ["John", "Jane", "Bob"]
   # ... And many more
   ```
### How to Read/Write JSON and CSV Files?

Botasaurus provides convenient methods for reading and writing data:

```python
# Data to write to the file
data = [
    {"name": "John Doe", "age": 42},
    {"name": "Jane Smith", "age": 27},
    {"name": "Bob Johnson", "age": 35}
]

# Write the data to the file "data.json"
bt.write_json(data, "data.json")

# Read the contents of the file "data.json"
print(bt.read_json("data.json"))

# Write the data to the file "data.csv"
bt.write_csv(data, "data.csv")

# Read the contents of the file "data.csv"
print(bt.read_csv("data.csv"))
```

### How Can I Pause the Scraper to Inspect Things While Developing?

To pause the scraper and wait for user input before proceeding, use `bt.prompt()`:

```python
bt.prompt()
```

### How Does AntiDetectDriver Facilitate Easier Web Scraping?

AntiDetectDriver is a patched Version of Selenium that has been modified to avoid detection by bot protection services such as Cloudflare. 

It also includes a variety of helper functions that make web scraping tasks easier.

You can learn about these methods [here](https://github.com/omkarcloud/botasaurus/blob/master/anti-detect-driver.md).

### What Features Does @request Support, Similar to @browser?

Similar to @browser, @request supports features like 
 - asynchronous execution [Will Learn Later]
 - parallel processing
 - caching
 - user-agent customization
 - proxies, etc.

Below is an example that showcases these features:


```python
@request(parallel=40, cache=True, proxy="http://your_proxy_address:your_proxy_port", data=["https://www.omkar.cloud/", ...])
def scrape_heading_task(request: AntiDetectDriver, link):
  soup = request.bs4(link)
  heading = soup.find('h1').get_text()
  return {"heading": heading}
```

### I have an existing project into which I want to integrate the AntiDetectDriver/AntiDetectRequests.

You can create an instance of `AntiDetectDriver` as follows:
```python
driver = bt.create_driver()
# ... Code for scraping
driver.quit()
```

You can create an instance of `AntiDetectRequests` as follows:
```python
anti_detect_request = bt.create_request()
soup = anti_detect_request.bs4("https://www.omkar.cloud/")
# ... Additional code
```

--- 

## Sign Up Bots

Sometimes, when scraping the web, data is hidden behind an authentication wall, requiring you to sign up via email or Google to access it.

Now, let's explore how to use Botasaurus utilities that empower us to create hundreds of accounts on a website. With hundreds of bots at your command:

  - You can mass message thousands of people on platforms like Twitter, LinkedIn, or Reddit to promote your product.

  - Platforms like MailChimp offer free plans with limited usage. With bots, you can maximize the benefits of these plans. For instance, if MailChimp allows you to send 500 emails per month for free, with 100 bots, you can send 50,000 emails monthly.

---

### How to Generate Human-Like User Data?

To create human-like user data, use the `generate_user` function:

```python
user = bt.generate_user(country=bt.Country.IN)
```

This will generate user profiles similar to the one shown below:

![Account](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/generated-account.png)

The data generated is very realistic, reducing the likelihood of being flagged as a bot.

### The Target Website Has Sent a Verification Email: How to Get the Link and Verify It?

To get the verification link from an email and then delete the mailbox, use `bt.TempMail.get_email_link_and_delete_mailbox` as shown below:

```python
user = bt.generate_user(country=bt.Country.IN)
email = user["email"]  # Example: madhumitachavare@1974.icznn.com

link = bt.TempMail.get_email_link_and_delete_mailbox(email)  # Retrieves the Verification Link and Deletes the Mailbox

driver.get(link)
```

### I have automated the Creation of User Account's. Now I want to store the User Account Credentials like Email and Password. How to store it?

To store user-related data, such as account credentials, use the `ProfileManager` module:

```python
bt.Profile.set_profile(user)
```

In cases where you want to store metadata related to a user, such as API keys:

```python
bt.Profile.set_item("api_key", "BDEC26...")
```

To retrieve a list of all users, use `bt.Profile.get_all_profiles()`:

```python
profiles = bt.Profile.get_all_profiles()
```

### The Chrome Profiles of User's are getting very large like 100MBs, is there a way to Compress them? 

You can use tiny_profile feautre of Botasaurus which are a replacement for Chrome Profiles.

Each Tiny Profile only stores cookies from visited websites, making them extremely lightweight—around 1KB. Here's how to use them:

```python
@browser(
    tiny_profile=True, 
    profile='my-profile',
)
def sign_up_task(driver: AntiDetectDriver, data):
    # Your sign-up code here
```

### How to Dynamically Specify the Profile Based on a Data Item?

You can dynamically select a profile by passing a function to the `profile` option, which will receive the data item:

```python

def get_profile(data):
    return data["username"]

@browser(
    data=[{"username": "mahendra-singh-dhoni", ...}, {"username": "virender-sehwag", ...}],
    profile=get_profile,
)
def sign_up_task(driver: AntiDetectDriver, data):
    # Your sign-up code here
```

user_agent, proxy, and other options can also be passed as functions.

### Is there a Tutorial that integrates tiny_profile, temp mail, user generator, profile to sign up on a Website and Perform Actions on Website. So I can get a Complete Picture?

For a comprehensive guide on using Botasaurus features such as `tiny_profile`, `temp_mail`, `user_generator`, and `profile` to sign up on a website and perform actions, read the Sign-Up Tutorial [Here](https://www.omkar.cloud/botasaurus/docs/sign-up-tutorial/). 

This tutorial will walk you through signing up for 3 accounts on Omkar Cloud and give you a complete understanding of the process.

### How to Run Botasaurus in Docker?

To run Botasaurus in Docker, use the Botasaurus Starter Template, which includes the necessary Dockerfile and Docker Compose configurations:

```
git clone https://github.com/omkarcloud/botasaurus-starter my-botasaurus-project
cd my-botasaurus-project
docker-compose build && docker-compose up
```

### How to Run Botasaurus in Gitpod?

Botasaurus Starter Template comes with the necessary `.gitpod.yml` to easily run it in Gitpod, a browser-based development environment. Set it up in just 5 minutes by following these steps:

1. Open Botasaurus Starter Template, by visiting [this link](https://gitpod.io/#https://github.com/omkarcloud/botasaurus-starter) and sign up using your GitHub account.
   
   ![Screenshot (148)](https://github.com/omkarcloud/google-maps-scraper/assets/53407137/f498dda8-5352-4f7a-9d70-c717859670d4.png)
  
<!-- 2. To speed up scraping, select the Large 8 Core, 16 GB Ram Machine and click the `Continue` button.   

   ![16gb select](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/16gb-select.png) -->

2. In the terminal, run the following command to start scraping:
```bash
python main.py
```

<!-- Please understand:
   - The internet speed in Gitpod is extremely fast at around 180 Mbps.

      ![speedtest](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/speedtest.png)

   - When Scraping, You need to interact with Gitpod, such as clicking within the environment, every 30 minutes to prevent the machine from automatically closing. -->


## Advanced Features


### How Do I Configure the Output of My Scraping Function in Botasaurus?
To configure the output of your scraping function in Botasaurus, you can customize the behavior in several ways:

1. **Change Output Filename**: Use the `output` parameter in the decorator to specify a custom filename for the output. 
   ```python
   @browser(output="my-output")
   def scrape_heading_task(driver: AntiDetectDriver, data): 
       # Your scraping logic here
   ```

2. **Disable Output**: If you don't want any output to be saved, set `output` to `None`.
   ```python
   @browser(output=None)
   def scrape_heading_task(driver: AntiDetectDriver, data): 
       # Your scraping logic here
   ```

3. **Dynamically Write Output**: To dynamically write output based on data and result, pass a function to the `output` parameter:
   ```python
   def write_output(data, result):
       bt.write_json(result, 'data')
       bt.write_csv(result, 'data')

   @browser(output=write_output)  
   def scrape_heading_task(driver: AntiDetectDriver, data): 
       # Your scraping logic here
   ```

4. **Save Outputs in Multiple Formats**: Use the `output_formats` parameter to save outputs in different formats like CSV and JSON.
   ```python
   @browser(output_formats=[bt.Formats.CSV, bt.Formats.JSON])  
   def scrape_heading_task(driver: AntiDetectDriver, data): 
       # Your scraping logic here
   ```

These options provide flexibility in how you handle the output of your scraping tasks with Botasaurus.

### How to Run Drivers Asynchronously from the Main Process?

To execute drivers asynchronously, enable the `async` option and use `.get()` when you're ready to collect the results:

```python
from time import sleep

@browser(
    run_async=True,  # Specify the Async option here
)
def scrape_heading(driver: AntiDetectDriver, data):
    print("Sleeping for 5 seconds.")
    sleep(5)
    print("Slept for 5 seconds.")
    return {}

if __name__ == "__main__":
    # Launch web scraping tasks asynchronously
    result1 = scrape_heading()  # Launches asynchronously
    result2 = scrape_heading()  # Launches asynchronously

    result1.get()  # Wait for the first result
    result2.get()  # Wait for the second result
```

With this method, function calls run concurrently. The output will indicate that both function calls are executing in parallel.

### How to Asynchronously Add Multiple Items and Get Results?

The `async_queue` feature allows you to perform web scraping tasks in asyncronously in a queue, without waiting for each task to complete before starting the next one. To gather your results, simply use the `.get()` method when all tasks are in the queue.

#### Basic Example:

```python
from time import sleep
from your_scraping_library import browser, AntiDetectDriver  # Replace with your actual scraping library

@browser(async_queue=True)
def scrape_data(driver: AntiDetectDriver, data):
    print("Starting a task.")
    sleep(1)  # Simulate a delay, e.g., waiting for a page to load
    print("Task completed.")
    return data

if __name__ == "__main__":
    # Start scraping tasks without waiting for each to finish
    async_queue = scrape_data()  # Initializes the queue

    # Add tasks to the queue
    async_queue.put([1])
    async_queue.put(2)
    async_queue.put([3, 4])

    # Retrieve results when ready
    results = async_queue.get()  # Expects to receive: [1, 2, 3, 4]
```

#### Practical Application for Web Scraping:

Here's how you could use `async_queue` to scrape webpage titles while scrolling through a list of links:

```python
from your_scraping_library import browser, AntiDetectDriver  # Replace with your actual scraping library

@browser(async_queue=True)
def scrape_title(driver: AntiDetectDriver, link):
    driver.get(link)  # Navigate to the link
    return driver.title  # Scrape the title of the webpage

@browser()
def scrape_all_titles(driver: AntiDetectDriver):
    # ... Your code to visit the initial page ...

    title_queue = scrape_title()  # Initialize the asynchronous queue
    
    while not end_of_page_detected(driver):  # Replace with your end-of-list condition
        title_queue.put(driver.links('a'))  # Add each link to the queue
        driver.scroll(".scrollable-element")
        

    return title_queue.get()  # Get all the scraped titles at once

if __name__ == "__main__":
    all_titles = scrape_all_titles()  # Call the function to start the scraping process
```

**Note:** The `async_queue` will only invoke the scraping function for unique links, avoiding redundant operations and keeping the main function (`scrape_all_titles`) cleaner.

### I want to repeatedly call the scraping function without creating new Selenium drivers each time. How can I achieve this?

Utilize the `keep_drivers_alive` option to maintain active driver sessions. Remember to call `.close()` when you're finished to release resources:

```python
@browser(
    keep_drivers_alive=True, 
    parallel=bt.calc_max_parallel_browsers,  # Typically used with `keep_drivers_alive`
    reuse_driver=True,  # Also commonly paired with `keep_drivers_alive`
)
def scrape_data(driver: AntiDetectDriver, data):
    # ... (Your scraping logic here)

if __name__ == "__main__":
    for i in range(3):
        scrape_data()
    # After completing all scraping tasks, call .close() to close the drivers.
    scrape_data.close()
```


### How do I manage the Cache in Botasaurus?

You can use The Cache Module in Botasaurus to easily manage cached data. Here's a simple example explaining its usage:

```python
from botasaurus import *
from botasaurus.cache import Cache

# Example scraping function
@request
def scrape_data(data):
    # Your scraping logic here
    return {"processed": data}

# Sample data for scraping
input_data = {"key": "value"}

# Adding data to the cache
Cache.put(scrape_data, input_data, scrape_data(input_data))
# Checking if data is in the cache
if Cache.has(scrape_data, input_data):
    # Retrieving data from the cache
    cached_data = Cache.get(scrape_data, input_data)
# Removing specific data from the cache
Cache.remove(scrape_data, input_data)
# Clearing the complete cache for the scrape_data function
Cache.clear(scrape_data)
```

### Any Tips for Scraping Cloudflare-Protected Websites?
- To scrape Cloudflare-protected sites, you need to use a browser; the request module won't work, as it gets detected and results in a 403 error.
- Use the `google_get` method to scrape the target website.
- For large-scale scraping, opt for Data Center Proxies over Residential as Residential Proxies are really expensive. Sometimes you will get blocked; so, use retries as demonstrated in the code below:
```python
  from botasaurus import *

  @browser(
          proxy="http://username:password@datacenter-proxy-domain:12321", 
          max_retry=5, # A reliable default for most situations
          block_resources=True, # Enhances efficiency and cost-effectiveness
          )
  def scrape_heading_task(driver: AntiDetectDriver, data):
      driver.google_get("https://www.g2.com/products/github/reviews")
      if driver.is_bot_detected():
          raise Exception("Bot detected")
      heading = driver.text('h1')
      print(heading)
      return heading
```



### How Do I Close All Running Chrome Instances When Developing with Botasaurus?

While developing a scraper, you might need to interrupt the scraping process, often done by pressing `Ctrl + C`. However, this action does not automatically close the Chrome browsers, which can cause your computer to hang due to resource overuse.

![Many Chrome processes running in Task Manager](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/chrome-running.png)

To prevent your PC from hanging, you need to close all running Chrome instances. 

You can run following command to close all chromes

```shell
python -m botasaurus.close
```

Executing above command will close all Chrome instances, thereby helping to prevent your PC from hanging.
 
---


### What feautres are Coming in Botasaurus 4?
Botasaurus 4, which is currently in its beta phase, allows you to:
  - A sms API to receive OTPs.
  - Run bots in the cloud using a website UI and control their schedules, starting/stopping times, and view bot outputs in a web UI. 
  - Use Kubernetes to run thousands of bots in parallel.
  - Schedule Scraping Tasks at specific times or intervals
  - Whatsapp/Email Alerts
  - An API to interface with Gmail and Outlook accounts.
  - MySQL/PostgreSQL Integration
  - Integrated Captcha Solving
  - And Many More :)
  
Developers are actively using Botasaurus 4 in production environments and saving hours of Development Time. To get access to Botasaurus 4, please [reach out to us](mailto:chetan@omkar.cloud?subject=Access%20Botasaurus%204&body=I%20want%20to%20use%20Botasaurus%204%20and%20gain%20access%20to%20feature%3A%20%5BTELL%20YOUR%20FEATURE%5D) and let us know which feature you would like to access.
 


### Conclusion

Botasaurus is a powerful, flexible tool for web scraping. 

Its various settings allow you to tailor the scraping process to your specific needs, improving both efficiency and convenience. Whether you're dealing with multiple data points, requiring parallel processing, or need to cache results, Botasaurus provides the features to streamline your scraping tasks.

### ❓ Need More Help or Have Additional Questions?

If you need guidane on your web scraping Project or have some questions, message us on WhatsApp and we'll be happy to help you out.

[![Contact Us on WhatsApp](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/mwa.png)](https://api.whatsapp.com/send?phone=918295042963&text=Hi,%20I%20would%20like%20to%20learn%20more%20about%20your%20products.)


## Thanks

- Kudos to the Apify Team for creating the `got-scraping` and `proxy-chain` libraries. The implementation of stealth Anti Detect Requests and SSL-based Proxy Authentication wouldn't have been possible without their groundbreaking work on `got-scraping` and `proxy-chain`.
- Shout out to zfcsoftware for developing `puppeteer-real-browser`; it helped us in creating Botasaurus Anti Detected. Show your appreciation by subscribing to their [YouTube channel](https://www.youtube.com/@zfcsoftware/videos) ⚡.
- A special thanks to the Selenium team for creating Selenium, an invaluable tool in our toolkit.
- Thanks to Cloudflare, DataDome, Imperva, and all bot detectors. Had you not been there, we wouldn't be either 😅.
- Finally, a humongous thank you for choosing Botasaurus.

## Love It? [Star It! ⭐](https://github.com/omkarcloud/botasaurus)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/botasaurus](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=botasaurus)](https://github.com/omkarcloud/botasaurus/stargazers)

## Made with ❤️ in Bharat 🇮🇳 - Vande Mataram
