{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "PROJECT OBJECTIVE: TO ANALYZE WHICH APPS GENERATE MORE REVENUE."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "from csv import reader\n",
    "opened_file = open('googleplaystore.csv')\n",
    "read_file = reader(opened_file)\n",
    "android = list(read_file)\n",
    "android_header = android[0]\n",
    "android = android[1:]\n",
    "\n",
    "opened_file = open('AppleStore.csv')\n",
    "read_file = reader(opened_file)\n",
    "ios = list(read_file)\n",
    "ios_header = ios[0]\n",
    "ios = ios[1:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For the ease of coding create a function to read the rows of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']\n",
      "\n",
      "\n",
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "Number of rows: 10841\n",
      "Number of columns: 13\n"
     ]
    }
   ],
   "source": [
    "def explore_data(dataset, start, end, rows_and_columns=False):\n",
    "    dataset_slice = dataset[start:end]    \n",
    "    for row in dataset_slice:\n",
    "        print(row)\n",
    "        print('\\n') # adds a new (empty) line between rows\n",
    "        \n",
    "    if rows_and_columns:\n",
    "        print('Number of rows:', len(dataset))\n",
    "        print('Number of columns:', len(dataset[0]))\n",
    "\n",
    "print(android_header)\n",
    "print('\\n')\n",
    "explore_data(android, 0, 3, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Deleting the wrong data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']\n",
      "\n",
      "\n",
      "['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']\n",
      "\n",
      "\n",
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n"
     ]
    }
   ],
   "source": [
    "print(android[10472])  # incorrect row\n",
    "print('\\n')\n",
    "print(android_header)  # header\n",
    "print('\\n')\n",
    "print(android[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10841\n",
      "10840\n"
     ]
    }
   ],
   "source": [
    "print(len(android))\n",
    "del android[10472]  \n",
    "print(len(android))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Removing duplicate entries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "['Instagram', 'SOCIAL', '4.5', '66577446', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "['Instagram', 'SOCIAL', '4.5', '66509917', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n"
     ]
    }
   ],
   "source": [
    "for app in android:\n",
    "    name = app[0]\n",
    "    if name == 'Instagram':\n",
    "        print(app)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate apps: 1181\n",
      "\n",
      "\n",
      "Examples of duplicate apps: ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box', 'Zenefits', 'Google Ads', 'Google My Business', 'Slack', 'FreshBooks Classic', 'Insightly CRM', 'QuickBooks Accounting: Invoicing & Expenses', 'HipChat - Chat Built for Teams', 'Xero Accounting Software']\n"
     ]
    }
   ],
   "source": [
    "duplicate_apps = []\n",
    "unique_apps = []\n",
    "\n",
    "for app in android:\n",
    "    name = app[0]\n",
    "    if name in unique_apps:\n",
    "        duplicate_apps.append(name)\n",
    "    else:\n",
    "        unique_apps.append(name)\n",
    "    \n",
    "print('Number of duplicate apps:', len(duplicate_apps))\n",
    "print('\\n')\n",
    "print('Examples of duplicate apps:', duplicate_apps[:15])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "reviews_max = {}\n",
    "\n",
    "for app in android:\n",
    "    name = app[0]\n",
    "    n_reviews = float(app[3])\n",
    "    \n",
    "    if name in reviews_max and reviews_max[name] < n_reviews:\n",
    "        reviews_max[name] = n_reviews\n",
    "        \n",
    "    elif name not in reviews_max:\n",
    "        reviews_max[name] = n_reviews"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Expected length: 9659\n",
      "Actual length: 9659\n"
     ]
    }
   ],
   "source": [
    "print('Expected length:', len(android) - 1181)\n",
    "print('Actual length:', len(reviews_max))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "android_clean = []\n",
    "already_added = []\n",
    "\n",
    "for app in android:\n",
    "    name = app[0]\n",
    "    n_reviews = float(app[3])\n",
    "    \n",
    "    if (reviews_max[name] == n_reviews) and (name not in already_added):\n",
    "        android_clean.append(app)\n",
    "        already_added.append(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']\n",
      "\n",
      "\n",
      "Number of rows: 9659\n",
      "Number of columns: 13\n"
     ]
    }
   ],
   "source": [
    "explore_data(android_clean, 0, 3, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "since our targetted users dont use the non-english apps I will be remoivng them. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def string_eng (string):\n",
    "    non_ascii =0\n",
    "    for char in string:\n",
    "        if ord(char) > 127 :\n",
    "            non_ascii += 1\n",
    "    if non_ascii > 3:\n",
    "        return False\n",
    "    else:\n",
    "        return True\n",
    "print(string_eng('Docs To Go™ Free Office Suite'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Isolating the non free apps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']\n",
      "\n",
      "\n",
      "Number of rows: 9614\n",
      "Number of columns: 13\n",
      "\n",
      "\n",
      "['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']\n",
      "\n",
      "\n",
      "['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']\n",
      "\n",
      "\n",
      "['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']\n",
      "\n",
      "\n",
      "Number of rows: 6183\n",
      "Number of columns: 16\n"
     ]
    }
   ],
   "source": [
    "android_eng =[]\n",
    "ios_eng=[]\n",
    "\n",
    "for app in  android_clean:\n",
    "    name = app[0]\n",
    "    if string_eng(name):\n",
    "        android_eng.append(app)\n",
    "for app in  ios:\n",
    "    name = app[1]\n",
    "    if string_eng(name):\n",
    "        ios_eng.append(app)\n",
    "explore_data(android_eng,0,3, True)\n",
    "print('\\n')\n",
    "explore_data(ios_eng,0,3,True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Isolating free apps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8864\n",
      "3222\n"
     ]
    }
   ],
   "source": [
    "android_last = []\n",
    "ios_last =[]\n",
    "for app in android_eng:\n",
    "    price =app[7]\n",
    "    if price == '0':\n",
    "        android_last.append(app)\n",
    "for app in ios_eng:\n",
    "    price =app[4]\n",
    "    if price == '0.0':\n",
    "        ios_last.append(app)\n",
    "print (len(android_last))\n",
    "print(len(ios_last))\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Evaluate the most commonly used app. So, that we can build a minimal android version of the app and add it on google play. if the response is good then we can go ahead with a better version of the app and release it in both google play and app store.\n",
    "Evaluating based on the genre and category."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "def freq (dataset, index):\n",
    "    table ={}\n",
    "    total = 0\n",
    "    for row in dataset:\n",
    "        total +=1\n",
    "        value = row[index]\n",
    "        if value in table:\n",
    "            table[value]+=1\n",
    "        else:\n",
    "            table[value]=1\n",
    "    table_percent ={}\n",
    "    for key in table:\n",
    "        percent = (table[key]/total)*100\n",
    "        table_percent[key]=percent\n",
    "    return table_percent\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the frequency table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_table(dataset, index):\n",
    "    table = freq (dataset, index)\n",
    "    table_display =[]\n",
    "    for key in table:\n",
    "        val_key =(table[key],key)\n",
    "        table_display.append(val_key)\n",
    "    sorted_table = sorted(table_display, reverse=True)\n",
    "    for entry in sorted_table:\n",
    "        print(entry[1], ':', entry[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FAMILY : 18.907942238267147\n",
      "GAME : 9.724729241877256\n",
      "TOOLS : 8.461191335740072\n",
      "BUSINESS : 4.591606498194946\n",
      "LIFESTYLE : 3.9034296028880866\n",
      "PRODUCTIVITY : 3.892148014440433\n",
      "FINANCE : 3.7003610108303246\n",
      "MEDICAL : 3.531137184115524\n",
      "SPORTS : 3.395758122743682\n",
      "PERSONALIZATION : 3.3167870036101084\n",
      "COMMUNICATION : 3.2378158844765346\n",
      "HEALTH_AND_FITNESS : 3.0798736462093865\n",
      "PHOTOGRAPHY : 2.944494584837545\n",
      "NEWS_AND_MAGAZINES : 2.7978339350180503\n",
      "SOCIAL : 2.6624548736462095\n",
      "TRAVEL_AND_LOCAL : 2.33528880866426\n",
      "SHOPPING : 2.2450361010830324\n",
      "BOOKS_AND_REFERENCE : 2.1435018050541514\n",
      "DATING : 1.861462093862816\n",
      "VIDEO_PLAYERS : 1.7937725631768955\n",
      "MAPS_AND_NAVIGATION : 1.3989169675090252\n",
      "FOOD_AND_DRINK : 1.2409747292418771\n",
      "EDUCATION : 1.1620036101083033\n",
      "ENTERTAINMENT : 0.9589350180505415\n",
      "LIBRARIES_AND_DEMO : 0.9363718411552346\n",
      "AUTO_AND_VEHICLES : 0.9250902527075812\n",
      "HOUSE_AND_HOME : 0.8235559566787004\n",
      "WEATHER : 0.8009927797833934\n",
      "EVENTS : 0.7107400722021661\n",
      "PARENTING : 0.6543321299638989\n",
      "ART_AND_DESIGN : 0.6430505415162455\n",
      "COMICS : 0.6204873646209386\n",
      "BEAUTY : 0.5979241877256317\n"
     ]
    }
   ],
   "source": [
    "display_table(android_last, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Games : 58.16263190564867\n",
      "Entertainment : 7.883302296710118\n",
      "Photo & Video : 4.9658597144630665\n",
      "Education : 3.662321539416512\n",
      "Social Networking : 3.2898820608317814\n",
      "Shopping : 2.60707635009311\n",
      "Utilities : 2.5139664804469275\n",
      "Sports : 2.1415270018621975\n",
      "Music : 2.0484171322160147\n",
      "Health & Fitness : 2.0173805090006205\n",
      "Productivity : 1.7380509000620732\n",
      "Lifestyle : 1.5828677839851024\n",
      "News : 1.3345747982619491\n",
      "Travel : 1.2414649286157666\n",
      "Finance : 1.1173184357541899\n",
      "Weather : 0.8690254500310366\n",
      "Food & Drink : 0.8069522036002483\n",
      "Reference : 0.5586592178770949\n",
      "Business : 0.5276225946617008\n",
      "Book : 0.4345127250155183\n",
      "Navigation : 0.186219739292365\n",
      "Medical : 0.186219739292365\n",
      "Catalogs : 0.12414649286157665\n"
     ]
    }
   ],
   "source": [
    "display_table(ios_last,-5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tools : 8.449909747292418\n",
      "Entertainment : 6.069494584837545\n",
      "Education : 5.347472924187725\n",
      "Business : 4.591606498194946\n",
      "Productivity : 3.892148014440433\n",
      "Lifestyle : 3.892148014440433\n",
      "Finance : 3.7003610108303246\n",
      "Medical : 3.531137184115524\n",
      "Sports : 3.463447653429603\n",
      "Personalization : 3.3167870036101084\n",
      "Communication : 3.2378158844765346\n",
      "Action : 3.1024368231046933\n",
      "Health & Fitness : 3.0798736462093865\n",
      "Photography : 2.944494584837545\n",
      "News & Magazines : 2.7978339350180503\n",
      "Social : 2.6624548736462095\n",
      "Travel & Local : 2.3240072202166067\n",
      "Shopping : 2.2450361010830324\n",
      "Books & Reference : 2.1435018050541514\n",
      "Simulation : 2.0419675090252705\n",
      "Dating : 1.861462093862816\n",
      "Arcade : 1.8501805054151623\n",
      "Video Players & Editors : 1.7712093862815883\n",
      "Casual : 1.7599277978339352\n",
      "Maps & Navigation : 1.3989169675090252\n",
      "Food & Drink : 1.2409747292418771\n",
      "Puzzle : 1.128158844765343\n",
      "Racing : 0.9927797833935018\n",
      "Role Playing : 0.9363718411552346\n",
      "Libraries & Demo : 0.9363718411552346\n",
      "Auto & Vehicles : 0.9250902527075812\n",
      "Strategy : 0.9138086642599278\n",
      "House & Home : 0.8235559566787004\n",
      "Weather : 0.8009927797833934\n",
      "Events : 0.7107400722021661\n",
      "Adventure : 0.6768953068592057\n",
      "Comics : 0.6092057761732852\n",
      "Beauty : 0.5979241877256317\n",
      "Art & Design : 0.5979241877256317\n",
      "Parenting : 0.4963898916967509\n",
      "Card : 0.45126353790613716\n",
      "Casino : 0.42870036101083037\n",
      "Trivia : 0.41741877256317694\n",
      "Educational;Education : 0.39485559566787\n",
      "Board : 0.3835740072202166\n",
      "Educational : 0.3722924187725632\n",
      "Education;Education : 0.33844765342960287\n",
      "Word : 0.2594765342960289\n",
      "Casual;Pretend Play : 0.236913357400722\n",
      "Music : 0.2030685920577617\n",
      "Racing;Action & Adventure : 0.16922382671480143\n",
      "Puzzle;Brain Games : 0.16922382671480143\n",
      "Entertainment;Music & Video : 0.16922382671480143\n",
      "Casual;Brain Games : 0.13537906137184114\n",
      "Casual;Action & Adventure : 0.13537906137184114\n",
      "Arcade;Action & Adventure : 0.12409747292418773\n",
      "Action;Action & Adventure : 0.10153429602888085\n",
      "Educational;Pretend Play : 0.09025270758122744\n",
      "Simulation;Action & Adventure : 0.078971119133574\n",
      "Parenting;Education : 0.078971119133574\n",
      "Entertainment;Brain Games : 0.078971119133574\n",
      "Board;Brain Games : 0.078971119133574\n",
      "Parenting;Music & Video : 0.06768953068592057\n",
      "Educational;Brain Games : 0.06768953068592057\n",
      "Casual;Creativity : 0.06768953068592057\n",
      "Art & Design;Creativity : 0.06768953068592057\n",
      "Education;Pretend Play : 0.056407942238267145\n",
      "Role Playing;Pretend Play : 0.04512635379061372\n",
      "Education;Creativity : 0.04512635379061372\n",
      "Role Playing;Action & Adventure : 0.033844765342960284\n",
      "Puzzle;Action & Adventure : 0.033844765342960284\n",
      "Entertainment;Creativity : 0.033844765342960284\n",
      "Entertainment;Action & Adventure : 0.033844765342960284\n",
      "Educational;Creativity : 0.033844765342960284\n",
      "Educational;Action & Adventure : 0.033844765342960284\n",
      "Education;Music & Video : 0.033844765342960284\n",
      "Education;Brain Games : 0.033844765342960284\n",
      "Education;Action & Adventure : 0.033844765342960284\n",
      "Adventure;Action & Adventure : 0.033844765342960284\n",
      "Video Players & Editors;Music & Video : 0.02256317689530686\n",
      "Sports;Action & Adventure : 0.02256317689530686\n",
      "Simulation;Pretend Play : 0.02256317689530686\n",
      "Puzzle;Creativity : 0.02256317689530686\n",
      "Music;Music & Video : 0.02256317689530686\n",
      "Entertainment;Pretend Play : 0.02256317689530686\n",
      "Casual;Education : 0.02256317689530686\n",
      "Board;Action & Adventure : 0.02256317689530686\n",
      "Video Players & Editors;Creativity : 0.01128158844765343\n",
      "Trivia;Education : 0.01128158844765343\n",
      "Travel & Local;Action & Adventure : 0.01128158844765343\n",
      "Tools;Education : 0.01128158844765343\n",
      "Strategy;Education : 0.01128158844765343\n",
      "Strategy;Creativity : 0.01128158844765343\n",
      "Strategy;Action & Adventure : 0.01128158844765343\n",
      "Simulation;Education : 0.01128158844765343\n",
      "Role Playing;Brain Games : 0.01128158844765343\n",
      "Racing;Pretend Play : 0.01128158844765343\n",
      "Puzzle;Education : 0.01128158844765343\n",
      "Parenting;Brain Games : 0.01128158844765343\n",
      "Music & Audio;Music & Video : 0.01128158844765343\n",
      "Lifestyle;Pretend Play : 0.01128158844765343\n",
      "Lifestyle;Education : 0.01128158844765343\n",
      "Health & Fitness;Education : 0.01128158844765343\n",
      "Health & Fitness;Action & Adventure : 0.01128158844765343\n",
      "Entertainment;Education : 0.01128158844765343\n",
      "Communication;Creativity : 0.01128158844765343\n",
      "Comics;Creativity : 0.01128158844765343\n",
      "Casual;Music & Video : 0.01128158844765343\n",
      "Card;Action & Adventure : 0.01128158844765343\n",
      "Books & Reference;Education : 0.01128158844765343\n",
      "Art & Design;Pretend Play : 0.01128158844765343\n",
      "Art & Design;Action & Adventure : 0.01128158844765343\n",
      "Arcade;Pretend Play : 0.01128158844765343\n",
      "Adventure;Education : 0.01128158844765343\n"
     ]
    }
   ],
   "source": [
    "display_table(android_last,-4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conclusion: Google play has more fun and practical apps and app store has more fun and games realted apps as the most used apps."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most popular apps by genre on the app store. calculate the average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Social Networking : 71548.34905660378\n",
      "Photo & Video : 28441.54375\n",
      "Games : 22788.6696905016\n",
      "Music : 57326.530303030304\n",
      "Reference : 74942.11111111111\n",
      "Health & Fitness : 23298.015384615384\n",
      "Weather : 52279.892857142855\n",
      "Utilities : 18684.456790123455\n",
      "Travel : 28243.8\n",
      "Shopping : 26919.690476190477\n",
      "News : 21248.023255813954\n",
      "Navigation : 86090.33333333333\n",
      "Lifestyle : 16485.764705882353\n",
      "Entertainment : 14029.830708661417\n",
      "Food & Drink : 33333.92307692308\n",
      "Sports : 23008.898550724636\n",
      "Book : 39758.5\n",
      "Finance : 31467.944444444445\n",
      "Education : 7003.983050847458\n",
      "Productivity : 21028.410714285714\n",
      "Business : 7491.117647058823\n",
      "Catalogs : 4004.0\n",
      "Medical : 612.0\n"
     ]
    }
   ],
   "source": [
    "genre_ios = freq(ios_last,-5)\n",
    "\n",
    "for genre in genre_ios:\n",
    "    total = 0\n",
    "    len_genre =0\n",
    "    for app in ios_last:\n",
    "        genre_app = app[-5]\n",
    "        if genre_app == genre:\n",
    "            n_ratings =float (app[5])\n",
    "            total+=n_ratings\n",
    "            len_genre+=1\n",
    "    avg_n_ratings =total/len_genre\n",
    "    print(genre, ':',avg_n_ratings)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "   Navigation realted apps are the most used in app store.\n",
    "   analyzing the navigation apps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Waze - GPS Navigation, Maps & Real-time Traffic : 345046\n",
      "Google Maps - Navigation & Transit : 154911\n",
      "Geocaching® : 12811\n",
      "CoPilot GPS – Car Navigation & Offline Maps : 3582\n",
      "ImmobilienScout24: Real Estate Search in Germany : 187\n",
      "Railway Route Search : 5\n"
     ]
    }
   ],
   "source": [
    "for app in ios_last:\n",
    "    if app[-5] == 'Navigation':\n",
    "        print(app[1], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "for app in ios_last:\n",
    "    if app[-5] == 'Reference':\n",
    "        print(app[1], ':', app[5])\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bible : 985920\n",
      "Dictionary.com Dictionary & Thesaurus : 200047\n",
      "Dictionary.com Dictionary & Thesaurus for iPad : 54175\n",
      "Google Translate : 26786\n",
      "Muslim Pro: Ramadan 2017 Prayer Times, Azan, Quran : 18418\n",
      "New Furniture Mods - Pocket Wiki & Game Tools for Minecraft PC Edition : 17588\n",
      "Merriam-Webster Dictionary : 16849\n",
      "Night Sky : 12122\n",
      "City Maps for Minecraft PE - The Best Maps for Minecraft Pocket Edition (MCPE) : 8535\n",
      "LUCKY BLOCK MOD ™ for Minecraft PC Edition - The Best Pocket Wiki & Mods Installer Tools : 4693\n",
      "GUNS MODS for Minecraft PC Edition - Mods Tools : 1497\n",
      "Guides for Pokémon GO - Pokemon GO News and Cheats : 826\n",
      "WWDC : 762\n",
      "Horror Maps for Minecraft PE - Download The Scariest Maps for Minecraft Pocket Edition (MCPE) Free : 718\n",
      "VPN Express : 14\n",
      "Real Bike Traffic Rider Virtual Reality Glasses : 8\n",
      "教えて!goo : 0\n",
      "Jishokun-Japanese English Dictionary & Translator : 0\n"
     ]
    }
   ],
   "source": [
    "for app in ios_last: \n",
    "    if app[-5] == 'Reference': \n",
    "        print(app[1], ':', app[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Facebook : 2974676\n",
      "Pinterest : 1061624\n",
      "Skype for iPhone : 373519\n",
      "Messenger : 351466\n",
      "Tumblr : 334293\n",
      "WhatsApp Messenger : 287589\n",
      "Kik : 260965\n",
      "ooVoo – Free Video Call, Text and Voice : 177501\n",
      "TextNow - Unlimited Text + Calls : 164963\n",
      "Viber Messenger – Text & Call : 164249\n",
      "Followers - Social Analytics For Instagram : 112778\n",
      "MeetMe - Chat and Meet New People : 97072\n",
      "We Heart It - Fashion, wallpapers, quotes, tattoos : 90414\n",
      "InsTrack for Instagram - Analytics Plus More : 85535\n",
      "Tango - Free Video Call, Voice and Chat : 75412\n",
      "LinkedIn : 71856\n",
      "Match™ - #1 Dating App. : 60659\n",
      "Skype for iPad : 60163\n",
      "POF - Best Dating App for Conversations : 52642\n",
      "Timehop : 49510\n",
      "Find My Family, Friends & iPhone - Life360 Locator : 43877\n",
      "Whisper - Share, Express, Meet : 39819\n",
      "Hangouts : 36404\n",
      "LINE PLAY - Your Avatar World : 34677\n",
      "WeChat : 34584\n",
      "Badoo - Meet New People, Chat, Socialize. : 34428\n",
      "Followers + for Instagram - Follower Analytics : 28633\n",
      "GroupMe : 28260\n",
      "Marco Polo Video Walkie Talkie : 27662\n",
      "Miitomo : 23965\n",
      "SimSimi : 23530\n",
      "Grindr - Gay and same sex guys chat, meet and date : 23201\n",
      "Wishbone - Compare Anything : 20649\n",
      "imo video calls and chat : 18841\n",
      "After School - Funny Anonymous School News : 18482\n",
      "Quick Reposter - Repost, Regram and Reshare Photos : 17694\n",
      "Weibo HD : 16772\n",
      "Repost for Instagram : 15185\n",
      "Live.me – Live Video Chat & Make Friends Nearby : 14724\n",
      "Nextdoor : 14402\n",
      "Followers Analytics for Instagram - InstaReport : 13914\n",
      "YouNow: Live Stream Video Chat : 12079\n",
      "FollowMeter for Instagram - Followers Tracking : 11976\n",
      "LINE : 11437\n",
      "eHarmony™ Dating App - Meet Singles : 11124\n",
      "Discord - Chat for Gamers : 9152\n",
      "QQ : 9109\n",
      "Telegram Messenger : 7573\n",
      "Weibo : 7265\n",
      "Periscope - Live Video Streaming Around the World : 6062\n",
      "Chat for Whatsapp - iPad Version : 5060\n",
      "QQ HD : 5058\n",
      "Followers Analysis Tool For Instagram App Free : 4253\n",
      "live.ly - live video streaming : 4145\n",
      "Houseparty - Group Video Chat : 3991\n",
      "SOMA Messenger : 3232\n",
      "Monkey : 3060\n",
      "Down To Lunch : 2535\n",
      "Flinch - Video Chat Staring Contest : 2134\n",
      "Highrise - Your Avatar Community : 2011\n",
      "LOVOO - Dating Chat : 1985\n",
      "PlayStation®Messages : 1918\n",
      "BOO! - Video chat camera with filters & stickers : 1805\n",
      "Qzone : 1649\n",
      "Chatous - Chat with new people : 1609\n",
      "Kiwi - Q&A : 1538\n",
      "GhostCodes - a discovery app for Snapchat : 1313\n",
      "Jodel : 1193\n",
      "FireChat : 1037\n",
      "Google Duo - simple video calling : 1033\n",
      "Fiesta by Tango - Chat & Meet New People : 885\n",
      "Google Allo — smart messaging : 862\n",
      "Peach — share vividly : 727\n",
      "Hey! VINA - Where Women Meet New Friends : 719\n",
      "Battlefield™ Companion : 689\n",
      "All Devices for WhatsApp - Messenger for iPad : 682\n",
      "Chat for Pokemon Go - GoChat : 500\n",
      "IAmNaughty – Dating App to Meet New People Online : 463\n",
      "Qzone HD : 458\n",
      "Zenly - Locate your friends in realtime : 427\n",
      "League of Legends Friends : 420\n",
      "豆瓣 : 407\n",
      "Candid - Speak Your Mind Freely : 398\n",
      "知乎 : 397\n",
      "Selfeo : 366\n",
      "Fake-A-Location Free ™ : 354\n",
      "Popcorn Buzz - Free Group Calls : 281\n",
      "Fam — Group video calling for iMessage : 279\n",
      "QQ International : 274\n",
      "Ameba : 269\n",
      "SoundCloud Pulse: for creators : 240\n",
      "Tantan : 235\n",
      "Cougar Dating & Life Style App for Mature Women : 213\n",
      "Rawr Messenger - Dab your chat : 180\n",
      "WhenToPost: Best Time to Post Photos for Instagram : 158\n",
      "Inke—Broadcast an amazing life : 147\n",
      "Mustknow - anonymous video Q&A : 53\n",
      "CTFxCmoji : 39\n",
      "Lobi : 36\n",
      "Chain: Collaborate On MyVideo Story/Group Video : 35\n",
      "botman - Real time video chat : 7\n",
      "BestieBox : 0\n",
      "MATCH ON LINE chat : 0\n",
      "niconico ch : 0\n",
      "LINE BLOG : 0\n",
      "bit-tube - Live Stream Video Chat : 0\n"
     ]
    }
   ],
   "source": [
    "for app in ios_last: \n",
    "    if app[-5] == 'Social Networking': \n",
    "        print(app[1], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most popular apps by genre on Google app. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1,000,000+ : 15.726534296028879\n",
      "100,000+ : 11.552346570397113\n",
      "10,000,000+ : 10.548285198555957\n",
      "10,000+ : 10.198555956678701\n",
      "1,000+ : 8.393501805054152\n",
      "100+ : 6.915613718411552\n",
      "5,000,000+ : 6.825361010830325\n",
      "500,000+ : 5.561823104693141\n",
      "50,000+ : 4.7721119133574\n",
      "5,000+ : 4.512635379061372\n",
      "10+ : 3.5424187725631766\n",
      "500+ : 3.2490974729241873\n",
      "50,000,000+ : 2.3014440433213\n",
      "100,000,000+ : 2.1322202166064983\n",
      "50+ : 1.917870036101083\n",
      "5+ : 0.78971119133574\n",
      "1+ : 0.5076714801444043\n",
      "500,000,000+ : 0.2707581227436823\n",
      "1,000,000,000+ : 0.22563176895306858\n",
      "0+ : 0.04512635379061372\n",
      "0 : 0.01128158844765343\n"
     ]
    }
   ],
   "source": [
    "display_table(android_last, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ART_AND_DESIGN : 1986335.0877192982\n",
      "AUTO_AND_VEHICLES : 647317.8170731707\n",
      "BEAUTY : 513151.88679245283\n",
      "BOOKS_AND_REFERENCE : 8767811.894736841\n",
      "BUSINESS : 1712290.1474201474\n",
      "COMICS : 817657.2727272727\n",
      "COMMUNICATION : 38456119.167247385\n",
      "DATING : 854028.8303030303\n",
      "EDUCATION : 1833495.145631068\n",
      "ENTERTAINMENT : 11640705.88235294\n",
      "EVENTS : 253542.22222222222\n",
      "FINANCE : 1387692.475609756\n",
      "FOOD_AND_DRINK : 1924897.7363636363\n",
      "HEALTH_AND_FITNESS : 4188821.9853479853\n",
      "HOUSE_AND_HOME : 1331540.5616438356\n",
      "LIBRARIES_AND_DEMO : 638503.734939759\n",
      "LIFESTYLE : 1437816.2687861272\n",
      "GAME : 15588015.603248259\n",
      "FAMILY : 3695641.8198090694\n",
      "MEDICAL : 120550.61980830671\n",
      "SOCIAL : 23253652.127118643\n",
      "SHOPPING : 7036877.311557789\n",
      "PHOTOGRAPHY : 17840110.40229885\n",
      "SPORTS : 3638640.1428571427\n",
      "TRAVEL_AND_LOCAL : 13984077.710144928\n",
      "TOOLS : 10801391.298666667\n",
      "PERSONALIZATION : 5201482.6122448975\n",
      "PRODUCTIVITY : 16787331.344927534\n",
      "PARENTING : 542603.6206896552\n",
      "WEATHER : 5074486.197183099\n",
      "VIDEO_PLAYERS : 24727872.452830188\n",
      "NEWS_AND_MAGAZINES : 9549178.467741935\n",
      "MAPS_AND_NAVIGATION : 4056941.7741935486\n"
     ]
    }
   ],
   "source": [
    "categories_android = freq(android_last, 1)\n",
    "\n",
    "for category in categories_android:\n",
    "    total=0\n",
    "    len_category=0\n",
    "    for app in android_last:\n",
    "        category_app =app[1]\n",
    "        if category_app == category:\n",
    "            n_installs =app[5]\n",
    "            n_installs = n_installs.replace(',','')\n",
    "            n_installs = n_installs.replace('+','')\n",
    "            total += float(n_installs)\n",
    "            len_category +=1\n",
    "    avg_n_installs = total / len_category\n",
    "    print(category, ':', avg_n_installs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WhatsApp Messenger : 1,000,000,000+\n",
      "imo beta free calls and text : 100,000,000+\n",
      "Android Messages : 100,000,000+\n",
      "Google Duo - High Quality Video Calls : 500,000,000+\n",
      "Messenger – Text and Video Chat for Free : 1,000,000,000+\n",
      "imo free video calls and chat : 500,000,000+\n",
      "Skype - free IM & video calls : 1,000,000,000+\n",
      "Who : 100,000,000+\n",
      "GO SMS Pro - Messenger, Free Themes, Emoji : 100,000,000+\n",
      "LINE: Free Calls & Messages : 500,000,000+\n",
      "Google Chrome: Fast & Secure : 1,000,000,000+\n",
      "Firefox Browser fast & private : 100,000,000+\n",
      "UC Browser - Fast Download Private & Secure : 500,000,000+\n",
      "Gmail : 1,000,000,000+\n",
      "Hangouts : 1,000,000,000+\n",
      "Messenger Lite: Free Calls & Messages : 100,000,000+\n",
      "Kik : 100,000,000+\n",
      "KakaoTalk: Free Calls & Text : 100,000,000+\n",
      "Opera Mini - fast web browser : 100,000,000+\n",
      "Opera Browser: Fast and Secure : 100,000,000+\n",
      "Telegram : 100,000,000+\n",
      "Truecaller: Caller ID, SMS spam blocking & Dialer : 100,000,000+\n",
      "UC Browser Mini -Tiny Fast Private & Secure : 100,000,000+\n",
      "Viber Messenger : 500,000,000+\n",
      "WeChat : 100,000,000+\n",
      "Yahoo Mail – Stay Organized : 100,000,000+\n",
      "BBM - Free Calls & Messages : 100,000,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_last:\n",
    "    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+'\n",
    "                                      or app[5] == '500,000,000+'\n",
    "                                      or app[5] == '100,000,000+'):\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "E-Book Read - Read Book for free : 50,000+\n",
      "Download free book with green book : 100,000+\n",
      "Wikipedia : 10,000,000+\n",
      "Cool Reader : 10,000,000+\n",
      "Free Panda Radio Music : 100,000+\n",
      "Book store : 1,000,000+\n",
      "FBReader: Favorite Book Reader : 10,000,000+\n",
      "English Grammar Complete Handbook : 500,000+\n",
      "Free Books - Spirit Fanfiction and Stories : 1,000,000+\n",
      "Google Play Books : 1,000,000,000+\n",
      "AlReader -any text book reader : 5,000,000+\n",
      "Offline English Dictionary : 100,000+\n",
      "Offline: English to Tagalog Dictionary : 500,000+\n",
      "FamilySearch Tree : 1,000,000+\n",
      "Cloud of Books : 1,000,000+\n",
      "Recipes of Prophetic Medicine for free : 500,000+\n",
      "ReadEra – free ebook reader : 1,000,000+\n",
      "Anonymous caller detection : 10,000+\n",
      "Ebook Reader : 5,000,000+\n",
      "Litnet - E-books : 100,000+\n",
      "Read books online : 5,000,000+\n",
      "English to Urdu Dictionary : 500,000+\n",
      "eBoox: book reader fb2 epub zip : 1,000,000+\n",
      "English Persian Dictionary : 500,000+\n",
      "Flybook : 500,000+\n",
      "All Maths Formulas : 1,000,000+\n",
      "Ancestry : 5,000,000+\n",
      "HTC Help : 10,000,000+\n",
      "English translation from Bengali : 100,000+\n",
      "Pdf Book Download - Read Pdf Book : 100,000+\n",
      "Free Book Reader : 100,000+\n",
      "eBoox new: Reader for fb2 epub zip books : 50,000+\n",
      "Only 30 days in English, the guideline is guaranteed : 500,000+\n",
      "Moon+ Reader : 10,000,000+\n",
      "SH-02J Owner's Manual (Android 8.0) : 50,000+\n",
      "English-Myanmar Dictionary : 1,000,000+\n",
      "Golden Dictionary (EN-AR) : 1,000,000+\n",
      "All Language Translator Free : 1,000,000+\n",
      "Azpen eReader : 500,000+\n",
      "URBANO V 02 instruction manual : 100,000+\n",
      "Bible : 100,000,000+\n",
      "C Programs and Reference : 50,000+\n",
      "C Offline Tutorial : 1,000+\n",
      "C Programs Handbook : 50,000+\n",
      "Amazon Kindle : 100,000,000+\n",
      "Aab e Hayat Full Novel : 100,000+\n",
      "Aldiko Book Reader : 10,000,000+\n",
      "Google I/O 2018 : 500,000+\n",
      "R Language Reference Guide : 10,000+\n",
      "Learn R Programming Full : 5,000+\n",
      "R Programing Offline Tutorial : 1,000+\n",
      "Guide for R Programming : 5+\n",
      "Learn R Programming : 10+\n",
      "R Quick Reference Big Data : 1,000+\n",
      "V Made : 100,000+\n",
      "Wattpad 📖 Free Books : 100,000,000+\n",
      "Dictionary - WordWeb : 5,000,000+\n",
      "Guide (for X-MEN) : 100,000+\n",
      "AC Air condition Troubleshoot,Repair,Maintenance : 5,000+\n",
      "AE Bulletins : 1,000+\n",
      "Ae Allah na Dai (Rasa) : 10,000+\n",
      "50000 Free eBooks & Free AudioBooks : 5,000,000+\n",
      "Ag PhD Field Guide : 10,000+\n",
      "Ag PhD Deficiencies : 10,000+\n",
      "Ag PhD Planting Population Calculator : 1,000+\n",
      "Ag PhD Soybean Diseases : 1,000+\n",
      "Fertilizer Removal By Crop : 50,000+\n",
      "A-J Media Vault : 50+\n",
      "Al-Quran (Free) : 10,000,000+\n",
      "Al Quran (Tafsir & by Word) : 500,000+\n",
      "Al Quran Indonesia : 10,000,000+\n",
      "Al'Quran Bahasa Indonesia : 10,000,000+\n",
      "Al Quran Al karim : 1,000,000+\n",
      "Al-Muhaffiz : 50,000+\n",
      "Al Quran : EAlim - Translations & MP3 Offline : 5,000,000+\n",
      "Al-Quran 30 Juz free copies : 500,000+\n",
      "Koran Read &MP3 30 Juz Offline : 1,000,000+\n",
      "Hafizi Quran 15 lines per page : 1,000,000+\n",
      "Quran for Android : 10,000,000+\n",
      "Surah Al-Waqiah : 100,000+\n",
      "Hisnul Al Muslim - Hisn Invocations & Adhkaar : 100,000+\n",
      "Satellite AR : 1,000,000+\n",
      "Audiobooks from Audible : 100,000,000+\n",
      "Kinot & Eichah for Tisha B'Av : 10,000+\n",
      "AW Tozer Devotionals - Daily : 5,000+\n",
      "Tozer Devotional -Series 1 : 1,000+\n",
      "The Pursuit of God : 1,000+\n",
      "AY Sing : 5,000+\n",
      "Ay Hasnain k Nana Milad Naat : 10,000+\n",
      "Ay Mohabbat Teri Khatir Novel : 10,000+\n",
      "Arizona Statutes, ARS (AZ Law) : 1,000+\n",
      "Oxford A-Z of English Usage : 1,000,000+\n",
      "BD Fishpedia : 1,000+\n",
      "BD All Sim Offer : 10,000+\n",
      "Youboox - Livres, BD et magazines : 500,000+\n",
      "B&H Kids AR : 10,000+\n",
      "B y H Niños ES : 5,000+\n",
      "Dictionary.com: Find Definitions for English Words : 10,000,000+\n",
      "English Dictionary - Offline : 10,000,000+\n",
      "Bible KJV : 5,000,000+\n",
      "Borneo Bible, BM Bible : 10,000+\n",
      "MOD Black for BM : 100+\n",
      "BM Box : 1,000+\n",
      "Anime Mod for BM : 100+\n",
      "NOOK: Read eBooks & Magazines : 10,000,000+\n",
      "NOOK Audiobooks : 500,000+\n",
      "NOOK App for NOOK Devices : 500,000+\n",
      "Browsery by Barnes & Noble : 5,000+\n",
      "bp e-store : 1,000+\n",
      "Brilliant Quotes: Life, Love, Family & Motivation : 1,000,000+\n",
      "BR Ambedkar Biography & Quotes : 10,000+\n",
      "BU Alsace : 100+\n",
      "Catholic La Bu Zo Kam : 500+\n",
      "Khrifa Hla Bu (Solfa) : 10+\n",
      "Kristian Hla Bu : 10,000+\n",
      "SA HLA BU : 1,000+\n",
      "Learn SAP BW : 500+\n",
      "Learn SAP BW on HANA : 500+\n",
      "CA Laws 2018 (California Laws and Codes) : 5,000+\n",
      "Bootable Methods(USB-CD-DVD) : 10,000+\n",
      "cloudLibrary : 100,000+\n",
      "SDA Collegiate Quarterly : 500+\n",
      "Sabbath School : 100,000+\n",
      "Cypress College Library : 100+\n",
      "Stats Royale for Clash Royale : 1,000,000+\n",
      "GATE 21 years CS Papers(2011-2018 Solved) : 50+\n",
      "Learn CT Scan Of Head : 5,000+\n",
      "Easy Cv maker 2018 : 10,000+\n",
      "How to Write CV : 100,000+\n",
      "CW Nuclear : 1,000+\n",
      "CY Spray nozzle : 10+\n",
      "BibleRead En Cy Zh Yue : 5+\n",
      "CZ-Help : 5+\n",
      "Modlitební knížka CZ : 500+\n",
      "Guide for DB Xenoverse : 10,000+\n",
      "Guide for DB Xenoverse 2 : 10,000+\n",
      "Guide for IMS DB : 10+\n",
      "DC HSEMA : 5,000+\n",
      "DC Public Library : 1,000+\n",
      "Painting Lulu DC Super Friends : 1,000+\n",
      "Dictionary : 10,000,000+\n",
      "Fix Error Google Playstore : 1,000+\n",
      "D. H. Lawrence Poems FREE : 1,000+\n",
      "Bilingual Dictionary Audio App : 5,000+\n",
      "DM Screen : 10,000+\n",
      "wikiHow: how to do anything : 1,000,000+\n",
      "Dr. Doug's Tips : 1,000+\n",
      "Bible du Semeur-BDS (French) : 50,000+\n",
      "La citadelle du musulman : 50,000+\n",
      "DV 2019 Entry Guide : 10,000+\n",
      "DV 2019 - EDV Photo & Form : 50,000+\n",
      "DV 2018 Winners Guide : 1,000+\n",
      "EB Annual Meetings : 1,000+\n",
      "EC - AP & Telangana : 5,000+\n",
      "TN Patta Citta & EC : 10,000+\n",
      "AP Stamps and Registration : 10,000+\n",
      "CompactiMa EC pH Calibration : 100+\n",
      "EGW Writings 2 : 100,000+\n",
      "EGW Writings : 1,000,000+\n",
      "Bible with EGW Comments : 100,000+\n",
      "My Little Pony AR Guide : 1,000,000+\n",
      "SDA Sabbath School Quarterly : 500,000+\n",
      "Duaa Ek Ibaadat : 5,000+\n",
      "Spanish English Translator : 10,000,000+\n",
      "Dictionary - Merriam-Webster : 10,000,000+\n",
      "JW Library : 10,000,000+\n",
      "Oxford Dictionary of English : Free : 10,000,000+\n",
      "English Hindi Dictionary : 10,000,000+\n",
      "English to Hindi Dictionary : 5,000,000+\n",
      "EP Research Service : 1,000+\n",
      "Hymnes et Louanges : 100,000+\n",
      "EU Charter : 1,000+\n",
      "EU Data Protection : 1,000+\n",
      "EU IP Codes : 100+\n",
      "EW PDF : 5+\n",
      "BakaReader EX : 100,000+\n",
      "EZ Quran : 50,000+\n",
      "FA Part 1 & 2 Past Papers Solved Free – Offline : 5,000+\n",
      "La Fe de Jesus : 1,000+\n",
      "La Fe de Jesús : 500+\n",
      "Le Fe de Jesus : 500+\n",
      "Florida - Pocket Brainbook : 1,000+\n",
      "Florida Statutes (FL Code) : 1,000+\n",
      "English To Shona Dictionary : 10,000+\n",
      "Greek Bible FP (Audio) : 1,000+\n",
      "Golden Dictionary (FR-AR) : 500,000+\n",
      "Fanfic-FR : 5,000+\n",
      "Bulgarian French Dictionary Fr : 10,000+\n",
      "Chemin (fr) : 1,000+\n",
      "The SCP Foundation DB fr nn5n : 1,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_last:\n",
    "    if app[1] == 'BOOKS_AND_REFERENCE':\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Google Play Books : 1,000,000,000+\n",
      "Bible : 100,000,000+\n",
      "Amazon Kindle : 100,000,000+\n",
      "Wattpad 📖 Free Books : 100,000,000+\n",
      "Audiobooks from Audible : 100,000,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_last:\n",
    "    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+'\n",
    "                                            or app[5] == '500,000,000+'\n",
    "                                            or app[5] == '100,000,000+'):\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CONCLUSION and RECOMMENDATION:\n",
    "Analyzed the datasets for google play and app store and created an app profiles for improving the revenue.\n",
    "The communication apps and social networking are doing good in the market and are so are the navigation apps on apple store. The scope of improvement can be seen in the books and references genre. More features and interacing GUI can increase new installs also, regular updates with new features in the previously exsisting apps can be a plus point to keep the users.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
