# imports
from robocorp.tasks import task
from browser_bot import BrowserBot
from RPA.Robocorp.WorkItems import WorkItems
import datetime
from dateutil.relativedelta import relativedelta
from selenium.common.exceptions import TimeoutException


@task
def main():  # sourcery skip: use-contextlib-suppress
    # setting workitems to be used in the task
    wi = WorkItems()
    wi.get_input_work_item()
    wi.clear_work_item()
    wi.set_work_item_variable("search_phrase", "Ai Chat")
    wi.set_work_item_variable("news_section", ["Business", "Technology"])
    wi.set_work_item_variable("number_months", 1)
    wi.save_work_item()

    # initialise bot
    browser = BrowserBot()
    # call the browser bot to open URL
    try:
        browser.open_available_browser(
            "https://www.nytimes.com/search?query=ai+chat", headless=False)
        browser.wait_until_page_contains_element(
            "//button[@data-test-id='search-button']")
    except TimeoutException:
        # increase timeout
        # browser.set_browser_timeout(6000)
        pass
    # call browser to remove popup - terms and conditions update
    browser.click_button("//button[@class='css-1fzhd9j']")
    # # call the browser bot to click on the search button
    # browser.click_button("//button[@data-test-id='search-button']")
    # # call the browser bot to input text in the search field
    # browser.input_text(
    #     "//input[@data-testid='search-input']", wi.get_work_item_variable("search_phrase"))
    # # call the browser bot to click on the search submit button
    # browser.click_button("//button[@data-test-id='search-submit']")
    # browser.wait_until_page_contains_element(
    #     "//button[@data-testid='search-date-dropdown-a']")
    # call browser bot to set date range
    browser.click_button("//button[@data-testid='search-date-dropdown-a']")
    browser.click_button("//button[@value='Specific Dates']")
    # date range TODO - add the date to a function
    current_date = datetime.date.today()
    end_date = current_date.strftime("%m/%d/%Y")
    start_date = (current_date - relativedelta(months=(wi.get_work_item_variable(
        'number_months')) - 1)).strftime("%m/%d/%Y")  # type: ignore
    if wi.get_work_item_variable('number_months') < 2:  # type: ignore
        start_date = current_date.replace(day=1).strftime("%m/%d/%Y")

    browser.input_text('//input[@id="startDate"]', start_date)
    browser.input_text('//input[@id="endDate"]', end_date)
    browser.press_keys('//input[@id="endDate"]', "ENTER")
    # select sections
    browser.click_button(
        '//button[@data-testid="search-multiselect-button"]')
    browser.wait_until_page_contains_element(
        '//input[@data-testid="DropdownLabelCheckbox"]')
    # using selenium to get all elements in a list
    browser_sections = browser.get_webelements(
        'css:.css-1qtb2wd label.css-1a8ayg6')
    browser_sections_text = []
    browser_sections_text = [
        browser_section.text for browser_section in browser_sections]

    for work_item_section in wi.get_work_item_variable("news_section"):
        for browser_section in browser_sections_text:
            if work_item_section.upper() in browser_section.upper():
                browser_section = ''.join(
                    [i for i in browser_section if not i.isdigit()])
                browser.click_element(
                    f'//label[@class="css-1a8ayg6"]/span[text()="{browser_section}"]')
    # browser.press_keys('css:.css-1qtb2wd label.css-1a8ayg6 ', "ESCAPE")

    # check if SHOW MORE button is present and click it
    while browser.is_element_visible("//button[@data-testid='search-show-more-button']"):
        browser.click_button(
            "//button[@data-testid='search-show-more-button']")

    # get all the articles
    for article in browser.get_webelements("//article"):
        # get the title
        title = browser.get_text(f"{article}/div/h4")
        # get the date
        date = browser.get_text(f"{article}//time")
        # get the link
        link = browser.get_element_attribute(f"{article}//a", "href")
        # get the summary
        summary = browser.get_text(f"{article}//p")
        # get the section
        section = browser.get_text(f"{article}//ul/li/a")
        # get the author
        author = browser.get_text(f"{article}//ul/li[2]/a")
        # get the image
        image = browser.get_element_attribute(f"{article}//img", "src")
        # create dictionary
        article_dict = {
            "title": title,
            "date": date,
            "link": link,
            "summary": summary,
            "section": section,
            "author": author,
            "image": image
        }
        # add the dictionary to the list
        wi.create_output_work_item(article_dict, "article")
        wi.save_work_item()

    # close the browser
    # browser.close_browser()
# run main
if __name__ == "__main__":
    main()
