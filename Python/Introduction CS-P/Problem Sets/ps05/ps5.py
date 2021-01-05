# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Alon Parag
# Collaborators:
# Time:From 04.01.2021 19:31
# NOTE: TEST TIME ON ANCIENT CASE FAILS BECAUSE ANCIENT CASE IS NAIVE AND BREAKS THE ASSUMPTION THAT THE SUPPLIED DATETIME TIMEZONE IS EST

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import string
import re

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    """
    Class to manipulate RSS feed News
    Takes in
    guid: string
    title: string
    description: string
    link: string
    pubdate: datetime
    """
    def __init__(self, guid, title, description, link, pubdate):
        try:
            assert type(guid) == str, 'Error: guid should be of type str'
            assert type(title) == str, 'Error: title should be of type str'
            assert type(description) == str, 'Error: description should be of type str'
            assert type(link) == str, 'Error: link should be of type str'
            assert type(pubdate) == datetime, 'Error: pubdate should be of type datetime'
        except AssertionError as identifier:
            print(identifier)
        except:
            print('Unexpected Error occoured')
        else:
            self.__guid = guid
            self.__title = title
            self.__description = description
            self.__link = link
            self.__pubdate = pubdate
    def get_guid(self):
        """Returns:
             string representing GUid
        """
        return self.__guid
    def get_title(self):
        """Returns:
             string representing title
        """
        return self.__title
    def get_description(self):
        """
        Returns:
             string representing desacription
        """
        return self.__description
    def get_link(self):
        """Returns:
             string representing link
        """
        return self.__link
    def get_pubdate(self):
        """Returns:
             datetime object representing pubdate
        """
        return self.__pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS
# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    """
    docstring
    """
    def __init__(self, phrase):
        """
        Assumes:
             phrase: alphabetic string
        Returns:
            instance of class PhraseTrigger
             
        """
        try:
            for char in string.punctuation:
                assert char not in phrase, "Error, Phrase should be without the following charachters: " + string.punctuation
            assert len(phrase.split(' ')) >= 1, "Error, String should have at least one word in it"
            for e in phrase.split(' '):
                assert len(e)>0, 'Error, spaces in phrase should be seperated by a single space'
        except AssertionError:
            pass
        else:
            self.__phrase = phrase.lower()

    def is_phrase_in(self, text):
        """
        Assumes:
             text: string
        Returns:
             True if self.__phrase in text
             otherwise False
        """
        # remove punctuation and multiple spaces
        text = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '  ', text)
        text = re.sub('( )+', ' ', text).lower()
        # check if phrase is in text
        return True if re.search(r'\b%s\b' %self.__phrase, text) else False
        

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    """
    Inherits from PhrasesTrigger, Fires when given phrase is in title
    """
    def __init__(self, phrase):
        """
        Assumes:
             phrase is a alphabetic string
        Returns:
             a titleTrigger object
        """
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """
        Assumes:
             story: NewsStory instance
        Returns:
             True if phrase in title, otherwise False
        """
        title = story.get_title()
        return self.is_phrase_in(title)
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    """
    Inherits from PhrasesTrigger, Fires when given phrase is in Description
    """
    def __init__(self, phrase):
        """
        Assumes:
             phrase is a alphabetic string
        Returns:
             a DescriptionTrigger object
        """
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """
        Assumes:
             story: NewsStory instance
        Returns:
             True if phrase in Description, otherwise False
        """
        description = story.get_description()
        return self.is_phrase_in(description)
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    """
    abstract class for time triggers
    """
    def __init__(self, time):
        """
        Assumes:
             time: datetime object with tzname "EST"
        Returns:
             TimeTrigger object
        """
        try:
            pattern = re.compile(r'([1-9]|(0[1-9])|([1-2][0-9])|(3[0-1]))\s[A-z][a-z]{2}\s[0-9]{4}\s(([2][0-3])|([0-1][0-9])):[0-5][0-9]:[0-5][0-9]')
            assert bool(pattern.match(time)), 'Error, time should follow the pattern "01 Oct 2009 00:00:00"'
        except AssertionError:
            pass
        else:
            est = pytz.timezone('EST')
            self.__time = datetime.strptime(time, r'%d %b %Y %H:%M:%S')
            self.__time = self.__time.replace(tzinfo = est)

    def get_time(self):
        return self.__time

    def evaluate(self, story):
        """
        abstarct method, not to be implemented
        """
        raise NotImplementedError

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """
    TimeTrigger that fires when a NewsStory object pubdate is strictly before the given time
    """
    def __init__(self, time):
        super().__init__(time)
        print('object:', self.__dict__)
        print('trigger time:', self.get_time())

    def is_before(self, time):
        """
        Assumes:
            time: datetime object tz=EST
        Returns:
            True if time is before self.get_time(), otherwise false
        """
        return time<self.get_time()

    def evaluate(self, story: NewsStory):
        """
        Assumes:
             story: NewsStory object
        Returns:
             True if NewsStory was published before self.get_time(), otherwise False
        """
        return self.is_before(story.get_pubdate())

class AfterTrigger(TimeTrigger):
    """
    TimeTrigger that fires when a NewsStory object pubdate is strictly after the given time
    """
    def __init__(self, time):
        super().__init__(time)
        print('object:', self.__dict__)
        print('trigger time:', self.get_time())

    def is_after(self, time):
        """
        Assumes:
            time: datetime object tz=EST
        Returns:
            True if time is after self.get_time(), otherwise false
        """
        return time>self.get_time()

    def evaluate(self, story: NewsStory):
        """
        Assumes:
             story: NewsStory object
        Returns:
             True if NewsStory was published after self.get_time(), otherwise False
        """
        return self.is_after(story.get_pubdate())
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

