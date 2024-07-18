import enum
import os
import uuid

import aiohttp
import requests
from dotenv import load_dotenv

load_dotenv()

LIMIT = 2

class Location(enum.Enum):
    US = "en-US"
    INDIA = "en-IN"

class Device(enum.Enum):
    DESKTOP = "desktop"
    ANDROID = "mobile_android"
    IOS = "mobile_ios"

class Engine(enum.Enum):
    GOOGLE = "google"
    BING = "bing"
    YAHOO = "yahoo"

def base_api(body: dict) -> dict:
    url = "https://api.moz.com/jsonrpc"
    headers = {
        "x-moz-token": os.getenv("MOZ_API_KEY"),
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()

async def abase_api(body: dict) -> dict:
    url = "https://api.moz.com/jsonrpc"
    headers = {
        "x-moz-token": os.getenv("MOZ_TOKEN"),
        "Content-Type": "application/json",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=body) as response:
            return await response.json()
        
def keyword_metrics(
        keyword: str, 
        locale: Location = Location.US, 
        device: Device = Device.DESKTOP, 
        engine: Engine = Engine.GOOGLE, 
        vicinity: str = None
    ) -> dict:
    if len(keyword) > 255:
        raise ValueError("Keyword length should be less than 255 characters")
    _dict = {
        "keyword": keyword,
        "locale": locale.value,
        "device": device.value,
        "engine": engine.value
    }
    if vicinity:
        _dict["vicinity"] = vicinity
    _id = str(uuid.uuid4())
    body = {
        "jsonrpc": "2.0",
        "id": _id,
        "method": "beta.data.keyword.metrics.fetch",
        "params": {
            "data": {
                "serp_query": _dict
            }
        }
    }
    return base_api(body)

async def akeyword_metrics(
        keyword: str, 
        locale: Location = Location.US, 
        device: Device = Device.DESKTOP, 
        engine: Engine = Engine.GOOGLE, 
        vicinity: str = None
    ) -> dict:
    if len(keyword) > 255:
        raise ValueError("Keyword length should be less than 255 characters")
    _dict = {
        "keyword": keyword,
        "locale": locale.value,
        "device": device.value,
        "engine": engine.value
    }
    if vicinity:
        _dict["vicinity"] = vicinity
    _id = str(uuid.uuid4())
    body = {
        "jsonrpc": "2.0",
        "id": _id,
        "method": "beta.data.keyword.metrics.fetch",
        "params": {
            "data": {
                "serp_query": _dict
            }
        }
    }
    return await abase_api(body)

def related_keywords(
        keyword: str, 
        locale: Location = Location.US, 
        device: Device = Device.DESKTOP, 
        engine: Engine = Engine.GOOGLE,
        limit: int = LIMIT
    ) -> dict:
    if len(keyword) > 255:
        raise ValueError("Keyword length should be less than 255 characters")
    _dict = {
        "keyword": keyword,
        "locale": locale.value,
        "device": device.value,
        "engine": engine.value
    }
    _id = str(uuid.uuid4())
    body = {
        "jsonrpc": "2.0",
        "id": _id,
        "method": "beta.data.keyword.suggestions.list",
        "params": {
            "data": {
                "serp_query": _dict,
                "page": {
                    "limit": limit
                }
            }
        }
    }
    return base_api(body)

async def arelated_keywords(
        keyword: str, 
        locale: Location = Location.US, 
        device: Device = Device.DESKTOP, 
        engine: Engine = Engine.GOOGLE,
        limit: int = LIMIT
    ) -> dict:
    if len(keyword) > 255:
        raise ValueError("Keyword length should be less than 255 characters")
    _dict = {
        "keyword": keyword,
        "locale": locale.value,
        "device": device.value,
        "engine": engine.value
    }
    _id = str(uuid.uuid4())
    body = {
        "jsonrpc": "2.0",
        "id": _id,
        "method": "beta.data.keyword.suggestions.list",
        "params": {
            "data": {
                "serp_query": _dict,
                "page": {
                    "limit": limit
                }
            }
        }
    }
    return await abase_api(body)

if __name__ == "__main__":
    # print(keyword_metrics("seo", locale=Location.INDIA))
    print(related_keywords("seo", locale=Location.INDIA))