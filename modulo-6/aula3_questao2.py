def extract_domains(url_list):
    return [url[4:-4] for url in url_list]

url_list = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

domains = extract_domains(url_list)
print("dominios:", domains)