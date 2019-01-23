from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class Actioneligibility(Action):
  def name(self):
    return 'action_eligibility'

  def run(self, dispatcher, tracker, domain):
    loc=tracker.get_slot('course')
    dic={"B.tech":"'10+2 with minimum 50% (45% for “SC/ST/OBC/SBC) marks from CBSE/equivalent\
    board along with 45% (40% for ST/SC/OBC/SBC) marks in Mathematics and Physics\
                  and any one of Chemistry/Computer Science/IP/Biology/Bio-technology.",
        "M.tech":"BE/ BTech/ equivalent in relevant discipline from a recognized\
                  university with 55% marks or 6.25 CGPA on 10 points scale (50% or 5.75\
                  CGPA on 10 points scale for ST/SC/OBC/SBC).Candidates with MCA/MSc IT also\
                  considered.",
        "MSc":"10+2 (PCM) with 50% marks (45% for SC/ST/OBC/SBC) from CBSE/equivalent board.",
        "B.arch":"10 + 2 With Maths (50 % Aggregate) from CBSE/equivalent board + valid NATA Score\
                  as per NATA 2018 guidelines or valid JEE paper 2 score.",
        "BCA":"10+2 (any stream) of CBSE / equivalent board.",
        "MBA":"Minimum 48% (43% for ST/SC/OBC/SBC) in Bachelor’s Degree from a recognized University or equivalent.",
        "BBA":"10+2(any stream) with Minimum 50% marks (45% for SC/ST/OBC/SBC) from CBSE/equivalent.",
        "B.Com":"10+2 (Science/Commerce stream) from CBSE/equivalent board.",
        "BA":"10+2 (Science/Commerce stream) from CBSE/equivalent board.",
        "BSc":"10+2 (Science/Commerce stream) from CBSE/equivalent board.",
        "M.Des":"Bachelor's Degree from a University/ equivalent.",
        "B.Des":"10+2 (any stream) with minimum 50% marks (45% for SC/ST/OBC/SBC) from CBSE/equivalent board.",
        "Ph.D":"Candidates should have passed BE/ B Tech /M Sc. in CS/ IT/ECE/EE/EIC from recognized Institution / University. 2. ME / M Tech degree with minimum 55 % marks or equivalent CGPA score in concerned discipline of Engineering from the recognized Universities / Institutions OR an Engineering graduate with Industry/ Research experience equivalent to Master’s degree in Engineering, which shall be decided by the competent authority of the University. "

    }
    response = "Eligibility criteria for {} is {} \nFor more information Contact our Addmission Cell [+91-8875 666 617]".format(loc,dic[loc])
    dispatcher.utter_message(response)
    return []

class Actionstreams(Action):
  def name(self):
    return 'action_streams'

  def run(self, dispatcher, tracker, domain):
    loc=tracker.get_slot('course')
    dic={"B.tech":"Civil Engineering \nComputer Engineering \nElectrical Engineering \nElectronics & Communication Engineering \nMechanical Engineering \nCloud Technology & Information Security \nData Science",
        "M.tech":"Computer Engineering \nDigital Communication \nEnergy And Environment \nPower System Engineering \nProduction Engineering \nStructural Engineering \nThermal Engineering \nTransportation Engineering \nVlsi Design",
        "MSc":"Mathematics",
        "BCA":"Information Security And Mobile Applications \nCloud Technology \nData Science \nInternet of Things \nGeneral BCA",
        "MBA":"Banking \nFinance \nHospital Management \nMarketing \nHuman Resource",
        "BBA":"General \nFinance \nRetail Management",
        "BA":"Economics \nEnglish \nMathematics \nStatistics \n Drawing \nPainting Sculpture",
        "BSc":"Chemistry \nComputer Science \nMathematics \nPhysics",
        "M.Des":"Product Design \nInterior Design",
        "B.Des":"Interior Design \nFashion & Textile Design",
        "Ph.D":"Ph.D. in Engineering (Part Time) \nPh.D. in Basic and Applied Sciences \nPh.D. in Management (Part Time) \nPh.D. in Planning and Architecture \nPh.D. in Engineering \nPh.D. in Basic and Applied Science (Part Time) \nPh.D. in Planning and Architecture (Part Time) "

    }
    response = dic[loc]
    dispatcher.utter_message(response)
    return []


class Actionfee(Action):
  def name(self):
    return 'action_fee'

  def run(self, dispatcher, tracker, domain):
    loc=tracker.get_slot('course')
    dic={"btech":"1.5lac",
        "mtech":"2.55lac",
        "msc":"1lac",
        "bca":"0.6lac"
    }
    dispatcher.utter_message(dic[loc])
    return []

