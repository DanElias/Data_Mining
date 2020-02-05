
from IPython.core.display import display, HTML
from IPython.display import IFrame


import urllib.request
import bs4
from bs4 import BeautifulSoup
import pandas

def extract_job_title_from_result(soup): 
    jobs = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
    return(jobs)

def extract_company_from_result(soup): 
    companies = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        company = div.find_all(name="span", attrs={"class":"company"})       
        for b in company:
            companies.append(b.text.strip())
    return(companies)

url = "https://www.indeed.com.sg/jobs?q=data%20scientist&l=Central%20Business%20District"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

html = response.read().decode('unicode_escape')

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
#print(soup.get_text())

jobnames = extract_job_title_from_result(soup)
print(jobnames)

companynames = extract_company_from_result(soup)
print(companynames)

job_info = pandas.DataFrame({'num':"0",'jobtitle':jobnames, 'companyname': companynames})
job_info.head()
print(job_info.head())

display(HTML("<h1>Hello World!</h1>"))
IFrame(src='index.html', width=700, height=600)