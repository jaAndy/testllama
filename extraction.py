import re

# Sample log data
log_data = """
### Final Decision: no
2019/2020 Annual Report on the Implementation of the Convention on the Rights of the Child - Part IV: Protection from Violence and Abuse
### Question: Do mitochondria play a role in remodelling lace plant leaves during programmed cell death?
### Final Decision: yes
### Model Prediction: <|im_start|>user
Do mitochondria play a role in remodelling lace plant leaves during programmed cell death?<|im_end|>
<|im_start|>assistant
 is there a role in lacin'e programmed cell deaths in lacaine?ay programmed cell death?ay an in lMap
Maps of the 30 mile Granite Mountain trailheads in BLM-managed public lands. It was created by a volunteer in 2018 using BLM and USGS data sources as well as recreational GPS tracks from 2017 to 2019. It includes trailhead parking areas, hiking trails, and campgrounds. If you are planning to visit one or more of these trailheads in person, please print this map out and take it with you. If you have any feedback about the map, please email us at trailheads@stateparks.utah.gov. We will incorporate your feedback into future updates!
View the full interactive version here: https://www.blm.gov/utah/trailheads_map.html.
The map below displays trailhead parking areas, campsites, and trailhead access points for the Granite Mountain Trailheads as of March 2022. These trailheads are all located on the BLM public lands. Each triangle represents a different trailhead area, such as a day use site or a primitive campsite. A dot in the center of each triangle marks the location of the trailhead area. For a map of Utah's public lands managed by the U.S. Department of the Interior, go here: https://www.blm.gov/utah. The trailheads are listed in both red and green color code, meaning that some trailheads may be marked with both colors. A red circle indicates a campground and a blue triangle indicates a parking area. A red rectangle marks the day use area. A dot in the center of the red rectangle indicates where the day use area lies. Trailheads with a black outline mark places of interest, including access roads, that may be accessed by foot, horseback, snowmobile, etc. A gray dot on a trailhead's black outline indicates a place of interest which may also be accessed by foot, horseback, snowmobile, etc., but which is not a trailhead. A yellow dot on a trailhead's black outline indicates a place of interest which can only be accessed via vehicle or bike. In addition to these trailhead parking areas, a number of campsites are also nearby, such as the following: Camping at the Campground: No Parking: Yes Camping at the Day Use Area: No Parking: Yes Hiking Trails: 164 Hiking Trails: 250 Trailheads: 30
About | Contact Us | Sitemap Copyright © 2023 State Parks of Utah This article is more than three years old index
Does quilting suture prevent seroma in abdominoplasty?
William S. Rutland
Kell

### Question: Landolt C and snellen e acuity: differences in strabismus amblyopia?
### Final Decision: no
### Model Prediction: <|im_start|>user
Landolt C and snellen e acuity: differences in strabismus amblyopia?<|im_end|>
<|im_start|>assistant
 eye disorders amblyopic? HIV/STD - a 10-year follow up plan in primary care settings?

 is there a relationship between the length of the patient's adherence to the therapy and his/her outcome? I would be very surprised if 200% of smokers quit smoking because of the nicotine patch. Perhaps they are the smoker who is getting tired of smoking and wants to quit without medicine?
 or something along those lines
"""

# Extract Final Decisions and Model Predictions
final_decisions = re.findall(r'### Final Decision: (\w+)', log_data)
# model_predictions = re.findall(r'### Model Prediction: <\|im_start\|>assistant\s*(.*?)\n### Question:', log_data, re.DOTALL)

model_predictions = re.findall(r'<\|im_start\|>assistant\s*(.*?)\n### Question:', log_data, re.DOTALL)
# Strip unwanted whitespace or newline characters
model_predictions = [pred.strip() for pred in model_predictions]

# Output the lists
print("Final Decisions:", final_decisions)
print("Model Predictions:", model_predictions)

