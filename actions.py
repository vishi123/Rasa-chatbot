# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction



class NearestAttraction(Action):
 def name(self):
  """name of the custom action"""
  return "action_nearest_attractions"

 def run(self,dispatcher,tracker,domain):	
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Marine Drive",
                            "image_url":"https://www.trawell.in/admin/images/upload/486072642MarineDrive_Main.jpg",
                            "subtitle": "Marine Drive is a buzzing waterfront district known for the Marine Walkway, popular for evening strolls,..",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/marine_drive",
                                    "title": "Read More"
                                },
                              {
                                    "type": "web_url",
                                    "url": "https://www.google.com/maps/d/viewer?ie=UTF8&source=embed&oe=UTF8&msa=0&mid=1TQ2nVI6cF8LtWZxKIdXSkIJs5JI&ll=49.21193400000003%2C-123.10863&z=17",
                                    "title": "Location"
                                },  
                            ]
                        }
                        
                        
                        
                    ]
                }
            }
        }
  dispatcher.utter_message(gt)
  return []
class BookRooms(Action):
 def name(self):
  """name of the custom action"""
  return "action_book_rooms"

 def run(self,dispatcher,tracker,domain):	
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Deluxe Room",
                            "image_url":"https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/125/2017/05/25023446/Rooms-Suites-Section-2nd-Room-Deluxe-Room.jpg",
                            "subtitle": "These Deluxe Rooms let you relax as you admire a beautiful view of the pool. Stay connected as you enjoy our free WiFi and watch movies with our 32-inch LCD TV and DVD player.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/dulex_room_details",
                                    "title": "Read More"
                                },
                              {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                },  
                            ]
                        },
                        
                        {
                            "title": "Club Suite",
                            "image_url":"https://media-cdn.tripadvisor.com/media/photo-s/12/77/d8/18/club-suite-living-room.jpg",
                            "subtitle": "The Club Suite is the ideal choice for a comfortable and lavish stay for both small families and business travelers alike. The gently soothing views and the calming ambiance of the suite add to an enriching experience for our guests.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/club_suite_details",
                                    "title": "Read More"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                }, 
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_message(gt)
  return []  

class BookRoomForm(FormAction):
 def name(self):
  return "book_room_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["check_in","check_out","adults","child","room","name","phno","email"]
 
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "check_in": [
                self.from_text(),
            ],
            "check_out": [
                self.from_text(),
            ],
            
            "adults": [
                self.from_text(),
            ],
            "child": [
                self.from_text(),
            ],
            "room": [
                self.from_text(),
            ],
            "name": [
                self.from_text(),
            ],
            "phno": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("Your booking details are here")    
    return []
class BookRoomsDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_book_rooms_details"

 def run(self,dispatcher,tracker,domain):
  check_in=tracker.get_slot("check_in")
  check_out=tracker.get_slot("check_out")
  adults=tracker.get_slot("adults")
  child=tracker.get_slot("child")
  room=tracker.get_slot("room")
  name=tracker.get_slot("name")
  phno=tracker.get_slot("phno")
  email=tracker.get_slot("email")
  message="BOOKING DETAILS:"+"\n\n"+"Checkin Date:"+check_in+"\n"+"Checkout Date:"+check_out+"\n"+"No. of Adults:"+adults+"\n"+"No. of Children:"+child+"\n"+"No.of Rooms:"+room+"\n"+"Phone Number:"+phno+"\n"+"Email:"+email
  dispatcher.utter_message(message)  
