<div class="card">
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img
            src="https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg"
            alt="Real Python Logo"
          />
        </figure>
      </div>
      <div class="media-content">
        <h2 class="title is-5">Senior Python Developer</h2>
        <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
      </div>
    </div>

    <div class="content">
      <p class="location">Stewartbury, AA</p>
      <p class="is-small has-text-grey">
        <time datetime="2021-04-08">2021-04-08</time>
      </p>
    </div>
    <footer class="card-footer">
      <a
        href="https://www.realpython.com"
        target="_blank"
        class="card-footer-item"
        >Learn</a
      >
      <a
        href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
        target="_blank"
        class="card-footer-item"
        >Apply</a
      >
    </footer>
  </div>
</div>
It can be challenging to wrap your head around a long block of HTML code. To make it easier to read, you can use an HTML formatter to clean it up automatically. Good readability helps you better understand the structure of any code block. While it may or may not help improve the HTML formatting, it’s always worth a try.

Note: Keep in mind that every website will look different. That’s why it’s necessary to inspect and understand the structure of the site you’re currently working with before moving forward.

The HTML you’ll encounter will sometimes be confusing. Luckily, the HTML of this job board has descriptive class names on the elements that you’re interested in:

class="title is-5" contains the title of the job posting.
class="subtitle is-6 company" contains the name of the company that offers the position.
class="location" contains the location where you’d be working.
In case you ever get lost in a large pile of HTML, remember that you can always go back to your browser and use the developer tools to further explore the HTML structure interactively.

By now, you’ve successfully harnessed the power and user-friendly design of Python’s requests library. With only a few lines of code, you managed to scrape static HTML content from the Web and make it available for further processing.

However, there are more challenging situations that you might encounter when you’re scraping websites. Before you learn how to pick the relevant information from the HTML that you just scraped, you’ll take a quick look at two of these more challenging situations.

Hidden Websites
Some pages contain information that’s hidden behind a login. That means you’ll need an account to be able to scrape anything from the page. The process to make an HTTP request from your Python script is different from how you access a page from your browser. Just because you can log in to the page through your browser doesn’t mean you’ll be able to scrape it with your Python script.

However, the requests library comes with the built-in capacity to handle authentication. With these techniques, you can log in to websites when making the HTTP request from your Python script and then scrape information that’s hidden behind a login. You won’t need to log in to access the job board information, which is why this tutorial won’t cover authentication.

Dynamic Websites
In this tutorial, you’ll learn how to scrape a static website. Static sites are straightforward to work with because the server sends you an HTML page that already contains all the page information in the response. You can parse that HTML response and immediately begin to pick out the relevant data.

On the other hand, with a dynamic website, the server might not send back any HTML at all. Instead, you could receive JavaScript code as a response. This code will look completely different from what you saw when you inspected the page with your browser’s developer tools.

Note: In this tutorial, the term dynamic website refers to a website that doesn’t return the same HTML that you see when viewing the page in your browser.

Many modern web applications are designed to provide their functionality in collaboration with the clients’ browsers. Instead of sending HTML pages, these apps send JavaScript code that instructs your browser to create the desired HTML. Web apps deliver dynamic content in this way to offload work from the server to the clients’ machines as well as to avoid page reloads and improve the overall user experience.

What happens in the browser is not the same as what happens in your script. Your browser will diligently execute the JavaScript code it receives from a server and create the DOM and HTML for you locally. However, if you request a dynamic website in your Python script, then you won’t get the HTML page content.

When you use requests, you only receive what the server sends back. In the case of a dynamic website, you’ll end up with some JavaScript code instead of HTML. The only way to go from the JavaScript code you received to the content that you’re interested in is to execute the code, just like your browser does. The requests library can’t do that for you, but there are other solutions that can.

For example, requests-html is a project created by the author of the requests library that allows you to render JavaScript using syntax that’s similar to the syntax in requests. It also includes capabilities for parsing the data by using Beautiful Soup under the hood.

Note: Another popular choice for scraping dynamic content is Selenium. You can think of Selenium as a slimmed-down browser that executes the JavaScript code for you before passing on the rendered HTML response to your script.

You won’t go deeper into scraping dynamically-generated content in this tutorial. For now, it’s enough to remember to look into one of the options mentioned above if you need to scrape a dynamic website.


 Remove ads
Step 3: Parse HTML Code With Beautiful Soup
You’ve successfully scraped some HTML from the Internet, but when you look at it, it just seems like a huge mess. There are tons of HTML elements here and there, thousands of attributes scattered around—and wasn’t there some JavaScript mixed in as well? It’s time to parse this lengthy code response with the help of Python to make it more accessible and pick out the data you want.

Beautiful Soup is a Python library for parsing structured data. It allows you to interact with HTML in a similar way to how you interact with a web page using developer tools. The library exposes a couple of intuitive functions you can use to explore the HTML you received. To get started, use your terminal to install Beautiful Soup:

$ python -m pip install beautifulsoup4
Then, import the library in your Python script and create a Beautiful Soup object:

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
When you add the two highlighted lines of code, you create a Beautiful Soup object that takes page.content, which is the HTML content you scraped earlier, as its input.

Note: You’ll want to pass page.content instead of page.text to avoid problems with character encoding. The .content attribute holds raw bytes, which can be decoded better than the text representation you printed earlier using the .text attribute.

The second argument, "html.parser", makes sure that you use the appropriate parser for HTML content.

Find Elements by ID
In an HTML web page, every element can have an id attribute assigned. As the name already suggests, that id attribute makes the element uniquely identifiable on the page. You can begin to parse your page by selecting a specific element by its ID.

Switch back to developer tools and identify the HTML object that contains all the job postings. Explore by hovering over parts of the page and using right-click to Inspect.

Note: It helps to periodically switch back to your browser and interactively explore the page using developer tools. This helps you learn how to find the exact elements you’re looking for.

The element you’re looking for is a <div> with an id attribute that has the value "ResultsContainer". It has some other attributes as well, but below is the gist of what you’re looking for:

<div id="ResultsContainer">
  <!-- all the job listings -->
</div>
Beautiful Soup allows you to find that specific HTML element by its ID:

results = soup.find(id="ResultsContainer")
For easier viewing, you can prettify any Beautiful Soup object when you print it out. If you call .prettify() on the results variable that you just assigned above, then you’ll see all the HTML contained within the <div>:

print(results.prettify())
When you use the element’s ID, you can pick out one element from among the rest of the HTML. Now you can work with only this specific part of the page’s HTML. It looks like the soup just got a little thinner! However, it’s still quite dense.


 Remove ads
Find Elements by HTML Class Name
You’ve seen that every job posting is wrapped in a <div> element with the class card-content. Now you can work with your new object called results and select only the job postings in it. These are, after all, the parts of the HTML that you’re interested in! You can do this in one line of code:

job_elements = results.find_all("div", class_="card-content")
Here, you call .find_all() on a Beautiful Soup object, which returns an iterable containing all the HTML for all the job listings displayed on that page.

Take a look at all of them:

for job_element in job_elements:
    print(job_element, end="\n"*2)
That’s already pretty neat, but there’s still a lot of HTML! You saw earlier that your page has descriptive class names on some elements. You can pick out those child elements from each job posting with .find():

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()
Each job_element is another BeautifulSoup() object. Therefore, you can use the same methods on it as you did on its parent element, results.

With this code snippet, you’re getting closer and closer to the data that you’re actually interested in. Still, there’s a lot going on with all those HTML tags and attributes floating around:

<h2 class="title is-5">Senior Python Developer</h2>
<h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
<p class="location">Stewartbury, AA</p>
Next, you’ll learn how to narrow down this output to access only the text content you’re interested in.

Extract Text From HTML Elements
You only want to see the title, company, and location of each job posting. And behold! Beautiful Soup has got you covered. You can add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains:

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()
Run the above code snippet, and you’ll see the text of each element displayed. However, it’s possible that you’ll also get some extra whitespace. Since you’re now working with Python strings, you can .strip() the superfluous whitespace. You can also apply any other familiar Python string methods to further clean up your text:

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
The results finally look much better:

Senior Python Developer
Payne, Roberts and Davis
Stewartbury, AA

Energy engineer
Vasquez-Davidson
Christopherville, AA

Legal executive
Jackson, Chambers and Levy
Port Ericaburgh, AA
That’s a readable list of jobs that also includes the company name and each job’s location. However, you’re looking for a position as a software developer, and these results contain job postings in many other fields as well.


 Remove ads
Find Elements by Class Name and Text Content
Not all of the job listings are developer jobs. Instead of printing out all the jobs listed on the website, you’ll first filter them using keywords.

You know that job titles in the page are kept within <h2> elements. To filter for only specific jobs, you can use the string argument:

python_jobs = results.find_all("h2", string="Python")
This code finds all <h2> elements where the contained string matches "Python" exactly. Note that you’re directly calling the method on your first results variable. If you go ahead and print() the output of the above code snippet to your console, then you might be disappointed because it’ll be empty:

>>> print(python_jobs)
[]
There was a Python job in the search results, so why is it not showing up?

When you use string= as you did above, your program looks for that string exactly. Any differences in the spelling, capitalization, or whitespace will prevent the element from matching. In the next section, you’ll find a way to make your search string more general.

Pass a Function to a Beautiful Soup Method
In addition to strings, you can sometimes pass functions as arguments to Beautiful Soup methods. You can change the previous line of code to use a function instead:

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
Now you’re passing an anonymous function to the string= argument. The lambda function looks at the text of each <h2> element, converts it to lowercase, and checks whether the substring "python" is found anywhere. You can check whether you managed to identify all the Python jobs with this approach:

>>> print(len(python_jobs))
10
Your program has found 10 matching job posts that include the word "python" in their job title!

Finding elements depending on their text content is a powerful way to filter your HTML response for specific information. Beautiful Soup allows you to use either exact strings or functions as arguments for filtering text in Beautiful Soup objects.

However, when you try to run your scraper to print out the information of the filtered Python jobs, you’ll run into an error:

AttributeError: 'NoneType' object has no attribute 'text'
This message is a common error that you’ll run into a lot when you’re scraping information from the Internet. Inspect the HTML of an element in your python_jobs list. What does it look like? Where do you think the error is coming from?

Identify Error Conditions
When you look at a single element in python_jobs, you’ll see that it consists of only the <h2> element that contains the job title:

<h2 class="title is-5">Senior Python Developer</h2>
When you revisit the code you used to select the items, you’ll see that that’s what you targeted. You filtered for only the <h2> title elements of the job postings that contain the word "python". As you can see, these elements don’t include the rest of the information about the job.

The error message you received earlier was related to this:

AttributeError: 'NoneType' object has no attribute 'text'
You tried to find the job title, the company name, and the job’s location in each element in python_jobs, but each element contains only the job title text.

Your diligent parsing library still looks for the other ones, too, and returns None because it can’t find them. Then, print() fails with the shown error message when you try to extract the .text attribute from one of these None objects.

The text you’re looking for is nested in sibling elements of the <h2> elements your filter returned. Beautiful Soup can help you to select sibling, child, and parent elements of each Beautiful Soup object.


 Remove ads
Access Parent Elements
One way to get access to all the information you need is to step up in the hierarchy of the DOM starting from the <h2> elements that you identified. Take another look at the HTML of a single job posting. Find the <h2> element that contains the job title as well as its closest parent element that contains all the information that you’re interested in:

<div class="card">
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img
            src="https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg"
            alt="Real Python Logo"
          />
        </figure>
      </div>
      <div class="media-content">
        <h2 class="title is-5">Senior Python Developer</h2>
        <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
      </div>
    </div>

    <div class="content">
      <p class="location">Stewartbury, AA</p>
      <p class="is-small has-text-grey">
        <time datetime="2021-04-08">2021-04-08</time>
      </p>
    </div>
    <footer class="card-footer">
      <a
        href="https://www.realpython.com"
        target="_blank"
        class="card-footer-item"
        >Learn</a
      >
      <a
        href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
        target="_blank"
        class="card-footer-item"
        >Apply</a
      >
    </footer>
  </div>
</div>
The <div> element with the card-content class contains all the information you want. It’s a third-level parent of the <h2> title element that you found using your filter.

With this information in mind, you can now use the elements in python_jobs and fetch their great-grandparent elements instead to get access to all the information you want:

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
You added a list comprehension that operates on each of the <h2> title elements in python_jobs that you got by filtering with the lambda expression. You’re selecting the parent element of the parent element of the parent element of each <h2> title element. That’s three generations up!

When you were looking at the HTML of a single job posting, you identified that this specific parent element with the class name card-content contains all the information you need.

Now you can adapt the code in your for loop to iterate over the parent elements instead:

for job_element in python_job_elements:
    # -- snip --
When you run your script another time, you’ll see that your code once again has access to all the relevant information. That’s because you’re now looping over the <div class="card-content"> elements instead of just the <h2> title elements.

Using the .parent attribute that each Beautiful Soup object comes with gives you an intuitive way of stepping through your DOM structure and addressing the elements you need. You can also access child elements and sibling elements in a similar manner. Read up on navigating the tree for more information.

Extract Attributes From HTML Elements
At this point, your Python script already scrapes the site and filters its HTML for relevant job postings. Well done! However, what’s still missing is the link to apply for a job.

While you were inspecting the page, you found two links at the bottom of each card. If you handle the link elements in the same way as you handled the other elements, you won’t get the URLs that you’re interested in:

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())
If you run this code snippet, then you’ll get the link texts Learn and Apply instead of the associated URLs.

That’s because the .text attribute leaves only the visible content of an HTML element. It strips away all HTML tags, including the HTML attributes containing the URL, and leaves you with just the link text. To get the URL instead, you need to extract the value of one of the HTML attributes instead of discarding it.

The URL of a link element is associated with the href attribute. The specific URL that you’re looking for is the value of the href attribute of the second <a> tag at the bottom the HTML of a single job posting:

    <!-- snip -->
    <footer class="card-footer">
        <a href="https://www.realpython.com" target="_blank"
           class="card-footer-item">Learn</a>
        <a href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
           target="_blank"
           class="card-footer-item">Apply</a>
    </footer>
  </div>
</div>






 




