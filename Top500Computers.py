{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "link = \"https://www.top500.org/list/2019/06/?page={}\"\n",
    "\n",
    "def get_data(link):\n",
    "    for url in [link.format(page) for page in range(1,6)]:\n",
    "        res = requests.get(url)\n",
    "        soup = BeautifulSoup(res.text,\"lxml\")\n",
    "\n",
    "        for items in soup.select(\"table.table tr\"):\n",
    "            td = [item.get_text(strip=True) for item in items.select(\"th,td\")]\n",
    "            writer.writerow(td)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    with open(\"tabularitem.csv\",\"w\",newline=\"\") as infile: #if encoding issue comes up then replace with ('tabularitem.csv', 'w', newline=\"\", encoding=\"utf-8\")\n",
    "        writer = csv.writer(infile)\n",
    "        get_data(link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
