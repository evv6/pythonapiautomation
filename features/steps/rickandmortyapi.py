from behave import *
from resources.functions import *
import requests


@given(u'I set url to "{url}"')
def step_impl(context, url):
    global request
    global json
    request = geturl(requests, url)
    json = getjson(request)


@then(u'I should expect a "{request_response:d}" response')
def step_impl(context, request_response):
    code = getstatuscode(request)
    assert code == request_response, "Code does not match"


@then(u'character count to "{character_count:d}"')
def step_impl(context, character_count):
    characters = getcount(json)
    assert characters == character_count


@then(u'location count to "{location_count:d}"')
def step_impl(context, location_count):
    locations = getcount(json)
    assert locations == location_count


@then(u'episode count to "{episode_count:d}"')
def step_impl(context, episode_count):
    episodes = getcount(json)
    assert episodes == episode_count


@then(u'character name is expected to be "{expected_character_name}"')
def step_impl(context, expected_character_name):
    character_name = getname(json)
    assert character_name == expected_character_name, "Not the Expected character Name"


@then(u'"{character}" appeared in "{number_of_episodes}" episodes')
def step_impl(context, character, number_of_episodes):
    character = getname(json)
    number_of_episodes = getepisodecount(json)
    print("%s appeared in %d episodes" % (character, number_of_episodes))


@then(u'"{number_of_characters}" characters appeared in episode "{episode_number}"')
def step_impl(context, number_of_characters, episode_number):
    number_of_characters = getcharactercount(json)
    episode_number = getid(json)
    print("%d characters appeared in episode %d" %
          (number_of_characters, episode_number))


@then(u'alive genderless characters are "{expected_characters:d}"')
def step_impl(context, expected_characters):
    characters = getcount(json)
    assert characters == expected_characters
