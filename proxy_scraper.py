import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from tqdm import tqdm
import random
import logging
import yaml
import argparse
import time

# Configure logging
def configure_logging(log_file, log_level):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ])

# Load configuration
def load_config(config_path):
    with open(config_path, "r") as config_file:
        return yaml.safe_load(config_file)

# Fungsi Scraping Proxy
def scrape_proxies(proxy_sources, user_agents, request_timeout, max_retries, retry_backoff_factor):
    proxies = set()
    headers = {"User-Agent": random.choice(user_agents)}

    for url in proxy_sources:
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, timeout=request_timeout)
                soup = BeautifulSoup(response.text, "html.parser")

                # Parsing Proxy List
                for row in soup.find_all("tr"):
                    columns = row.find_all("td")
                    if len(columns) >= 2:
                        ip = columns[0].text.strip()
                        port = columns[1].text.strip()
                        if ip and port.isdigit():
                            proxy = f"{ip}:{port}"
                            proxies.add(proxy)
                break
            except Exception as e:
                logging.warning(f"Error scraping {url} on attempt {attempt + 1}: {e}")
                time.sleep(retry_backoff_factor ** attempt)

    return list(proxies)

# Fungsi Cek Proxy Valid
async def check_proxy(session, proxy, semaphore, validation_timeout):
    async with semaphore:
        try:
            async with session.get("http://www.google.com", proxy=f"http://{proxy}", timeout=validation_timeout) as response:
                if response.status == 200:
                    return proxy
        except:
            return None

# Fungsi Cek Semua Proxy
async def validate_proxies(proxies, concurrency_limit, validation_timeout):
    valid_proxies = []
    semaphore = asyncio.Semaphore(concurrency_limit)
    async with aiohttp.ClientSession() as session:
        tasks = [check_proxy(session, proxy, semaphore, validation_timeout) for proxy in proxies]
        results = []
        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Validating Proxies"):
            results.append(await f)
    
    for proxy in results:
        if proxy:
            valid_proxies.append(proxy)
    
    return valid_proxies

# Fungsi Utama
async def main(config):
    logging.info("Scraping proxy list...")
    proxy_list = scrape_proxies(
        config['proxy_sources'],
        config['user_agents'],
        config['request_timeout'],
        config['max_retries'],
        config['retry_backoff_factor']
    )
    logging.info(f"Total proxies found: {len(proxy_list)}")

    logging.info("Checking proxy validity...")
    valid_proxies = await validate_proxies(
        proxy_list,
        config['concurrency_limit'],
        config['validation_timeout']
    )
    
    logging.info(f"Valid proxies: {len(valid_proxies)}")
    for proxy in valid_proxies[:10]:  # Tampilkan 10 proxy valid pertama
        logging.info(f"  - {proxy}")

    with open(config['output_file'], "w") as f:
        for proxy in valid_proxies:
            f.write(proxy + "\n")
    
    logging.info(f"Proxy list saved in {config['output_file']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proxy Scraper and Validator")
    parser.add_argument("--config", type=str, help="Path to configuration file", default="config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    configure_logging(config['log_file'], config['log_level'])
    
    asyncio.run(main(config))