import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def perform_search(query):
    api_key = "a31fe86bc223c5e541c2e1f0d5c64b53"
    url = f"http://api.scraperapi.com?api_key={api_key}&url=https://www.google.com/search?q={query.replace(' ', '+')}"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        search_results = []

        # Extract titles and snippets from Google search results
        for result in soup.select("div.tF2Cxc"):
            title = result.select_one("h3").get_text() if result.select_one("h3") else "No Title"
            print("title: ", title)
            link = result.select_one("a")["href"] if result.select_one("a") else "No Link"
            snippet = result.select_one("span.aCOpRe").get_text() if result.select_one("span.aCOpRe") else "No Snippet"
            search_results.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n")
            print("search results: ", search_results)

        return "\n\n".join(search_results)
    else:
        return f"Failed to fetch search results. Status Code: {response.status_code}"

def parse_results(raw_results, query, openai_api_key):
    # Define your OpenAI API endpoint
    api_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }

    # Construct the request payload
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{
            "role": "user",
            "content": f"Extract relevant information from the following search results about '{query}':\n\n{raw_results}",
        }],
        "max_tokens": 500,  # Adjust tokens based on your requirement
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No result found.")
    else:
        return f"Error: {response.status_code}, {response.text}"