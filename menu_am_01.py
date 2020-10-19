from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_01

browser = Drivers().chrome()
ap = AmazonPage(driver=browser)

# test start
ap.go()

ap.open_menu_button.click()
title = ap.shop_by_category_title.text
print(title)
assert title == 'SHOP BY CATEGORY'

ap.amazon_music_button.click()
music_title = ap.amazon_music_title.text
assert music_title == 'STREAM MUSIC'
print(music_title)
ap.main_menu_button1.click()

ap.kindle_button.click()
ki_title = ap.kindle_title.text
assert ki_title == 'KINDLE E-READERS'
print(ki_title)
ap.main_menu_button2.click()

ap.app_android_button.click()
app_title = ap.app_android_title.text
assert app_title == 'APPSTORE FOR ANDROID'
print(app_title)
ap.main_menu_button3.click()

ap.electronic_button.click()
el_title = ap.electronic_title.text
assert el_title == 'ELECTRONICS'
print(el_title)
ap.main_menu_button4.click()

ap.computers_button.click()
comp_title = ap.computers_title.text
assert comp_title == 'COMPUTERS'
print(comp_title)
ap.main_menu_button5.click()

ap.smart_home_button.click()
smart_title = ap.smart_home_title.text
assert smart_title == 'SMART HOME'
print(smart_title)
ap.main_menu_button6.click()

ap.arts_crafts_button.click()
art_title = ap.arts_crafts_title.text
assert art_title == 'ARTS & CRAFTS'
print(art_title)
ap.main_menu_button7.click()

ap.automotive_button.click()
auto_title = ap.automotive_title.text
assert auto_title == 'AUTOMOTIVE'
print(auto_title)
ap.main_menu_button8.click()

ap.baby_button.click()
bab_title = ap.baby_title.text
assert bab_title == 'BABY'
print(bab_title)
ap.main_menu_button9.click()

ap.beauty_care_button.click()
beauty_title = ap.beauty_care_title.text
assert beauty_title == 'BEAUTY AND PERSONAL CARE'
print(beauty_title)
ap.main_menu_button10.click()

ap.women_fashion_button.click()
women_title = ap.women_fashion_title.text
assert women_title == "WOMEN'S FASHION"
print(women_title)
ap.main_menu_button11.click()

ap.man_fashion_button.click()
man_title = ap.man_fashion_title.text
assert man_title == "MEN'S FASHION"
print(man_title)
ap.main_menu_button12.click()

ap.girl_fashion_button.click()
girl_title = ap.girl_fashion_title.text
assert girl_title == "GIRLS' FASHION"
print(girl_title)
ap.main_menu_button13.click()

ap.boy_fashion_button.click()
boy_title = ap.boy_fashion_title.text
assert boy_title == "BOYS' FASHION"
print(boy_title)
ap.main_menu_button14.click()

ap.healt_house_button.click()
health_title = ap.healt_house_title.text
assert health_title == 'HEALTH AND HOUSEHOLD'
print(health_title)
ap.main_menu_button15.click()

ap.home_kitchen_button.click()
home_title = ap.home_kitchen_title.text
assert home_title == 'HOME AND KITCHEN'
print(home_title)
ap.main_menu_button16.click()

ap.industrial_science_button.click()
indust_title = ap.industrial_science_title.text
assert indust_title == 'INDUSTRIAL AND SCIENTIFIC'
print(indust_title)
ap.main_menu_button17.click()

ap.luggage_button.click()
lug_title = ap.luggage_title.text
assert lug_title == 'LUGGAGE'
print(lug_title)
ap.main_menu_button18.click()

ap.movie_tv_button.click()
movie_title = ap.movie_tv_title.text
assert movie_title == 'MOVIES & TELEVISION'
print(movie_title)
ap.main_menu_button19.click()

ap.pet_supplies_button.click()
pet_title = ap.pet_supplies_title.text
assert pet_title == 'PET SUPPLIES'
print(pet_title)
ap.main_menu_button20.click()


ap.software_button.click()
sof_title = ap.software_title.text
assert sof_title == 'SOFTWARE'
print(sof_title)
ap.main_menu_button21.click()

ap.sport_outdoor_button.click()
sport_title = ap.sport_outdoor_title.text
assert sport_title == 'SPORTS AND OUTDOORS'
print(sport_title)
ap.main_menu_button22.click()

ap.tools_home_button.click()
tools_title = ap.tools_home_title.text
assert tools_title == 'TOOLS & HOME IMPROVEMENT'
print(tools_title)
ap.main_menu_button23.click()

ap.toys_games_button.click()
toys_title = ap.toys_games_title.text
assert toys_title == 'TOYS AND GAMES'
print(toys_title)
ap.main_menu_button24.click()

ap.video_games_button.click()
video_title = ap.video_games_title.text
assert video_title == 'VIDEO GAMES'
print(video_title)
print()
print('menu_am_01 test passed')
browser.quit()









