def get_country_codes(prices):
    country_codes = ''
    # your code here
    # print(prices)
    new_prices = prices.split()
  # print(new_prices)
    for prices in new_prices:
    # print(prices[0:2])
        country_codes += prices[0:2] + ", "
  # print(country_codes)

    new_country_codes = ( len(country_codes) - 2)

    print(country_codes[0:new_country_codes])
  # print(len(country_codes))

  # if len(country_codes) > 2:


  


# don't include these tests in Vocareum
# from test import testEqual

get_country_codes("NZ$300, KR$1200, DK$5")
# , "NZ, KR, DK")
get_country_codes("US$40, AU$89, JP$200")
#, "US, AU, JP")
get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2")
#, "AU, NG, MX, BG, ES")
get_country_codes("CA$40")
#, "CA")
