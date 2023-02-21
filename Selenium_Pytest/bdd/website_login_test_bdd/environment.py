from selenium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(2)

def after_feature(context, feature):
    context.driver.quit()