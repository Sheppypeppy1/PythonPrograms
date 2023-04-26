from selenium import webdriver

chrome_driver_path = "/Users/mitchelshephard/Documents/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.co.uk/Lamborghini-Behind-Legend-Frank-Grillo/dp/B0B6T2BPSH/ref=zg-bs_instant-video_sccl_5/257-9811452-0321953?pd_rd_w=HoJ6N&content-id=amzn1.sym.3f9daf0e-df48-4e4c-9b03-d5dd85519204&pf_rd_p=3f9daf0e-df48-4e4c-9b03-d5dd85519204&pf_rd_r=88DA35PDQEHNG9F1G2ZS&pd_rd_wg=vG9tv&pd_rd_r=1fa04198-45fd-43c4-b4ac-2e1ce8b95de4&pd_rd_i=B0B6T2BPSH&psc=1")
price = driver.find_element(by=By.CLASS_NAME, value='tvod-btn-ab-movie-hd-tvod_purchase')
print(price.text)


driver.quit()