from os.path import dirname, join

from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.pgh_public_schools import PghPublicSchoolsSpider

test_detail_response = file_response(
    join(dirname(__file__), "files", "pgh_public_schools", "detail.json"),
    url="https://awsapieast1-prod2.schoolwires.com/REST/api/v4/CalendarEvents/GetEventDate/1/17864",
)
spider = PghPublicSchoolsSpider()

freezer = freeze_time("2019-02-26")
freezer.start()

# need to authenticate, so a test page is not so straightfoward

parsed_items = [item for item in spider._parse_detail_api(test_detail_response)]

freezer.stop()
"""
Uncomment below
"""


def test_title():
    assert parsed_items[0]["title"] == "2nd Report Card"


# def test_description():
#     assert parsed_items[0]["description"] == "EXPECTED DESCRIPTION"

# def test_start():
#     assert parsed_items[0]["start"] == datetime(2019, 1, 1, 0, 0)

# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)

# def test_time_notes():
#     assert parsed_items[0]["time_notes"] == "EXPECTED TIME NOTES"

# def test_id():
#     assert parsed_items[0]["id"] == "EXPECTED ID"

# def test_status():
#     assert parsed_items[0]["status"] == "EXPECTED STATUS"

# def test_location():
#     assert parsed_items[0]["location"] == {
#         "name": "EXPECTED NAME",
#         "address": "EXPECTED ADDRESS"
#     }

# def test_source():
#     assert parsed_items[0]["source"] == "EXPECTED URL"

# def test_links():
#     assert parsed_items[0]["links"] == [{
#       "href": "EXPECTED HREF",
#       "title": "EXPECTED TITLE"
#     }]

# def test_classification():
#     assert parsed_items[0]["classification"] == NOT_CLASSIFIED

# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
