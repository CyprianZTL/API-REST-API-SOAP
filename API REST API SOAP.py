import requests
from zeep import Client

#GitHub R API
def github_rest_api(username, repo):
    user_url = f"https://api.github.com/users/{username}"
    repo_url = f"https://api.github.com/repos/{username}/{repo}"

    user_info = requests.get(user_url).json()
    repo_info = requests.get(repo_url).json()

    return user_info, repo_info

#CIS S API
def country_info_soap_api(country_name):
    WSDL_URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    client = Client(WSDL_URL)

    country_ISO_code = client.service.CountryISOCode(country_name)
    country_currency = client.service.CountryCurrency(country_ISO_code)

    return country_ISO_code, country_currency

#test polaczenia
print(github_rest_api("octocat", "Hello-World"))

country_name = input("Podaj nazwę kraju: ")
print(country_info_soap_api(country_name))
