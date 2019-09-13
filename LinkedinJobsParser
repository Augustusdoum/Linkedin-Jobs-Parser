from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

keywords = ['esg','sustainable','climate','Climate%20Change','durable','Carbone',
            'developpement%20durable','rse',
            'Changement%20climatique','environnement']

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\Auguste Roca\Desktop\Python\chromedriver.exe", options=options)

def get_links(keywords):
    
    links = []
    
    for word in keywords:
        
        partial = 'https://www.linkedin.com/jobs/search?keywords=' + word + '&location=Paris%2C%20Île-de-France%2C%20France&trk=guest_job_search_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0&f_TP=1%2C2'
        
        links.append(str(partial))
        
    return (links) 

def get_soup(link):
    
    driver.get(link)
    
    while True:
        try:
            driver.find_element_by_class_name('see-more-jobs').click()
        except Exception:
            pass
            break
    
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    
    return (soup)

def get_header(soup):
    
    header_raw = soup.find_all('h3', attrs={'class': lambda e: e.startswith('result-card__title job-result-card__title') if e else False})
    header_raw_comp = soup.find_all('a', attrs={'class': lambda e: e.startswith('result-card__subtitle-link job-result-card__subtitle-link') if e else False})
    header_url = soup.find_all("a", href=lambda href: href and href.startswith("https://fr.linkedin.com/jobs/view"))
    header_time = soup.find_all("time", attrs={'class': lambda e: e.startswith('job-result-card__listdate') if e else False})
    
    job_titles = []
    company_names = []
    job_link = []
    times = []
    
    for element in header_raw_comp:
        
        company_names.append(element.get_text())
        
    for element in header_raw:
        
        job_titles.append(element.get_text())
    
    for element in header_url:
    
        job_link.append(element['href'])
    
    if len(job_link) != len(job_titles):    
        job_link.pop()
        
    for element in header_time:

        times.append(element.get_text())
    
    d = {'Job_Desc':job_titles,'Creation' : times ,'Link': job_link}
    
    df = pd.DataFrame(d)
    
    df['Job_Desc'] = df['Job_Desc'].str.lower()
    
    return (df)

def get_relevance(df):
    
    to_exclude = ['ingénieur','ingenieur','Ingénieur','engineer','stage',
                  'stagiaire','contrôleur','alternant','alternance',
                  'developpeur','développeur','commercial','rh','bâtiment',
                  'acheteur','internship','plomberie','chantiers','editeur',
                  'hardware','chauffage','distribution','juriste','auditeur',
                  'chauffeur','technicien','vehicule','sales','ecommerce',
                  'digitalisation','cuisine','architecture','securite',
                  'industriel','logiciel','architecte']
    
    for element in to_exclude:
    
        df = df[~df.Job_Desc.str.contains(element)]
         
    keywords = ['esg','csr','sustainable','environnement','climate','climat',
                'ethic','change','changement','climat','développement',
                'durable','developpement','carbone','sustainability','erp',
                'urban','diversity','eco','changement','energy','bio']
    
    top_choices = df[df.Job_Desc.str.contains('|'.join(keywords))]

    return(top_choices,df)

def get_results():
    
    links = get_links(keywords)
    
    top_frames = []
    all_frames = []
    
    for link in links:
        
        soup = get_soup(link)
        
        df = get_header(soup)
        
        top_choices = get_relevance(df)[0]
        
        df = get_relevance(df)[1]

        top_frames.append(top_choices)
        all_frames.append(df)
        
    top_results = pd.concat(top_frames).drop_duplicates(subset='Job_Desc',keep='first').reset_index(drop=True)
    results = pd.concat(all_frames).drop_duplicates(subset='Job_Desc',keep='first').reset_index(drop=True)
    
    return(top_results,results)
 
a = get_results()[0]
b = get_results()[1]
c = a[a.Creation.str.contains('hours')]

a.to_excel('top_results.xlsx')
b.to_excel('all_results.xlsx')
c.to_excel('recent_top_results.xlsx')
