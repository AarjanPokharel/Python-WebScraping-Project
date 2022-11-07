from bs4 import BeautifulSoup
import requests
import time

print("Enter skills that you are not familiar with")
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        post_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in post_date:

            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')

            details = job.header.h2.a['href']

            if unfamiliar_skills.upper() not in skills.upper():
                with open(f'posted_jobs/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"Details: {details}\n")
            
                print(f'File saved : {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting for {time_wait} minutes........')
        time.sleep(time_wait*60)