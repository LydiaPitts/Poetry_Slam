from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json


"""
In this function, we are crawling the website sally's baking addiction for cookie recipes for our inspiring set

Essentially, we start the crawl from the link to the category of the website listing cookie recipes, then
go to the page for each recipe and extract the ingredients

@params:
    link_list --> the links to recipes we want!

@returns:
    recipes --> a dictionary where the keys are recipe names, and the values are dictionaries mapping each ingredient to its quantity

"""
def getCookieRecipes(link_list):
    recipes = {}
    #the below 5 lines set up the conditions for our web browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")

    # create our webdriver object
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

    #now, we want to loop through the recipe links
    for link in link_list:
        #open link to recipe
        driver.get (link) 
       
        ingredients = driver.find_element_by_class_name("entry-summary poem-excerpt")
        #list_items = ingredients.find_elements_by_tag_name("li")

       #list_items = driver.find_elements_by_tag_name("em") # get list items for ingredients
        i = 0
        for item in ingredients: # loop through ingredients
            file_name = 
            print(item)
            print(i)
            i += 1
        
    driver.close()
    #with open('recipes.json', 'w') as fp:
    #    json.dump(recipes, fp)

    #fp.close()
    return recipes


def read_file():
    i = 1
    while(i <= 13):
        print("hello")
        i +=1 






def main():
    read_file()

"""
Driver for the entire program
"""
if __name__ == "__main__":
    main()
