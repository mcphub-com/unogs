import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/unogs/api/unogs'

mcp = FastMCP('unogs')

@mcp.tool()
def search_titles(end_rating: Annotated[Union[str, None], Field(description='number between 1 and 10, aligns with imdb rating, if there is one')] = None,
                  country_list: Annotated[Union[str, None], Field(description='CSV list of country IDs e.g. 46,78')] = None,
                  start_year: Annotated[Union[int, float, None], Field(description='year date > 1900 Minimum: 1900')] = None,
                  person: Annotated[Union[str, None], Field(description='name of person in title')] = None,
                  offset: Annotated[Union[int, float, None], Field(description='where you want the response to start e.g. 10 starts with the 10th element')] = None,
                  order_by: Annotated[Union[str, None], Field(description='Order of Response')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='limit of object returned Maximum: 100')] = None,
                  end_year: Annotated[Union[int, float, None], Field(description='year date > 1900 Minimum: 1900')] = None,
                  top250: Annotated[Union[int, float, None], Field(description='IMDB top 250 Movies number 0-250')] = None,
                  start_rating: Annotated[Union[str, None], Field(description='number between 1 and 10, aligns with imdb rating, if there is one')] = None,
                  new_date: Annotated[Union[str, None], Field(description='2018-01-01 or 2010-01-01,2012-01-01 see Parameter Notes')] = None,
                  top250tv: Annotated[Union[int, float, None], Field(description='IMDB top 250 Series number 0-250')] = None,
                  title: Annotated[Union[str, None], Field(description='search all titles by name')] = None,
                  expiring: Annotated[Union[str, None], Field(description="if 'true' show all titles set to expire")] = None,
                  subtitle: Annotated[Union[str, None], Field(description='name of subtitle language e.g. english')] = None,
                  type: Annotated[Union[str, None], Field(description='movie or series')] = None,
                  genre_list: Annotated[Union[str, None], Field(description='CSV list of genres, see misc/genre endpoint')] = None,
                  audio: Annotated[Union[str, None], Field(description='name of audio language e.g english')] = None,
                  audio_sub_andor: Annotated[Union[str, None], Field(description='and=language in bot audio and sub, or=language in either audio or sub')] = None,
                  country_andorunique: Annotated[Union[str, None], Field(description='and=titles in all countries, or=any title in these countries, unique=unique titles in chosen countries')] = None) -> dict: 
    '''Parameter Notes: new_date will either take a single date and check for all titles added after that date or it will take 2 dates separated by a comma to check titles added between them.'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/search/titles'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'end_rating': end_rating,
        'country_list': country_list,
        'start_year': start_year,
        'person': person,
        'offset': offset,
        'order_by': order_by,
        'limit': limit,
        'end_year': end_year,
        'top250': top250,
        'start_rating': start_rating,
        'new_date': new_date,
        'top250tv': top250tv,
        'title': title,
        'expiring': expiring,
        'subtitle': subtitle,
        'type': type,
        'genre_list': genre_list,
        'audio': audio,
        'audio_sub_andor': audio_sub_andor,
        'country_andorunique': country_andorunique,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_people(netflix_id: Annotated[Union[int, float, None], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')] = None,
                  person_type: Annotated[Union[str, None], Field(description='what the person did on the project')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='limit of object returned Maximum: 100')] = None,
                  name: Annotated[Union[str, None], Field(description='search all titles by name')] = None,
                  offset: Annotated[Union[int, float, None], Field(description='where you want the response to start e.g. 10 starts with the 10th element')] = None) -> dict: 
    '''Search for people by title name, person name, or netflix_id'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/search/people'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflix_id': netflix_id,
        'person_type': person_type,
        'limit': limit,
        'name': name,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_deleted(title: Annotated[Union[str, None], Field(description='search all titles by name')] = None,
                   delete_date: Annotated[Union[str, None], Field(description='2018-01-01 or 2010-01-01,2012-01-01 see Parameter Notes')] = None,
                   netflix_id: Annotated[Union[int, float, None], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')] = None,
                   limit: Annotated[Union[int, float, None], Field(description='limit of object returned Maximum: 100')] = None,
                   offset: Annotated[Union[int, float, None], Field(description='where you want the response to start e.g. 10 starts with the 10th element')] = None,
                   country_list: Annotated[Union[str, None], Field(description='CSV list of country IDs e.g. 46,78')] = None) -> dict: 
    '''Search for Deleted Titles by Country or Title Name delete_date will either take a single date and check for all titles added after that date or it will take 2 dates separated by a comma to check titles added between them.'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/search/deleted'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'title': title,
        'delete_date': delete_date,
        'netflix_id': netflix_id,
        'limit': limit,
        'offset': offset,
        'country_list': country_list,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def static_genres() -> dict: 
    '''Get Static list of Genres (updated daily)'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/static/genres'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def static_countries() -> dict: 
    '''Get Static list of Supported Countries'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/static/countries'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_genres(netflix_id: Annotated[Union[int, float], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')]) -> dict: 
    '''All Genres Associated with a Title'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/title/genres'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflix_id': netflix_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_images(netflix_id: Annotated[Union[int, float], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')]) -> dict: 
    '''All Images associated with a Title'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/title/images'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflix_id': netflix_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_details(netflix_id: Annotated[Union[int, float], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')]) -> dict: 
    '''General Details associated with a Title'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/title/details'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflix_id': netflix_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_episodes(season_id: Annotated[Union[int, float], Field(description='actual netflix season ID e.g. 70105286 for Breaking Bad season 1')],
                   netflix_id: Annotated[Union[int, float], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')]) -> dict: 
    '''All Episodes associated with a Title'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/title/episodes'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season_id': season_id,
        'netflix_id': netflix_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_countries(netflix_id: Annotated[Union[int, float], Field(description='actual netflix ID for the title e.g. 70143836 for Breaking Bad')]) -> dict: 
    '''All Country/Language information associated with a Title'''
    url = 'https://unogs-unogs-v1.p.rapidapi.com/title/countries'
    headers = {'x-rapidapi-host': 'unogs-unogs-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflix_id': netflix_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    mcp.run(transport="stdio")
