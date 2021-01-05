from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

driver = webdriver.Chrome()
driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSd3PZLvGWrGgEjGiSfWrnRr4ZW9jqZPbRTj9B2bnlzOOIOZJA/viewform"
)

dataset = [
    ["Anonymous", "anonymous@gmail.com", "1234567890", "Some random stuff", "NA"],
    ["Anonymous2", "anonymous2@gmail.com", "012345678", "Some random stuff", "NA"],
]

for data in dataset:
    cnt = 0

    textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")

    textareaboxes = driver.find_elements_by_class_name(
        "quantumWizTextinputPapertextareaInput"
    )

    for value in textboxes:
        value.send_keys(data[cnt])
        cnt += 1

    for value in textareaboxes:
        value.send_keys(data[cnt])
        cnt += 1

    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
    )
    submit.click()

    another_response = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    )
    another_response.click()

driver.close()

