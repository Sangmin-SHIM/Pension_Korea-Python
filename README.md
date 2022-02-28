# Pension_Korea-Python

<h3>1) Why do I have to make this application ?</h3>
  Nowadays people are interested in dividend stocks such as KOSPI and KOSDAQ. In Naver, one of the biggest web sites in Korea, users can FIND the information of enterprise that they want to research. The problem is, given that there are lots of pages (more than 10 pages), users can’t SEARCH immediately what they want to check. They have to scroll over the pages until finding the company they need. So, I’d like to make an application for users to SEARCH directly their company interested. To ease the use, I formed a User Interface (UI) like  button, message box, scroll etc.  Finally, users can see the visualized data with graph. They are able to figure out the changes at one glance. With this application (called “Dividend Tracker Korea”) users can find the information at once.

<br>
<h3>2) How is Dividend Tracker Korea organized ? </h3>
<img width="80%" src="https://user-images.githubusercontent.com/93679283/155987432-d19d47bd-044b-4060-8dc7-7b4ebba3e8ad.png">
It consists of 2 python files, 
(1. KOSPI(KOSDAQ)_Write.py) and (2. KOSPI(KOSDAQ)_Load.py). 
  First of all, in 1. KOSPI(KOSDAQ)_Write.py, this application gets an URL in which they have the data, information that we want. And then, the application requests an access to the URL for parsing, which means that we could extract the data according to HTML Tag (<>,</>). Through this process we can make a CSV file and save the data.

 Secondly, in 2. KOSPI(KOSDAQ)_Load.py, this application opens a User Interface (UI). Based on the data taken from 1. KOSPI(KOSDAQ)_Write.py, the application lists the names of enterprises on left. If users could not find easily by scrolling up/down, they search directly by typing its name. On right, it shows the data related in the enterprise. And by clicking the button “Graph”, the changes for 3 years show in the form of graph.
<br>
- List
<img width="100%" src="https://user-images.githubusercontent.com/93679283/155987885-6a937713-4fc4-49b7-b59d-c0af52088e09.png">

- Search
<img width="100%" src="https://user-images.githubusercontent.com/93679283/155987903-80f4b7ff-4e69-4bc9-b9cd-e95920f8455e.png">
<br>
<h3>3)	What kind of libraries (packages) did I use ?</h3>
<h4>(1) Requests</h4>
- It allows to access a certain site. It’s the first step of Web Crawling.  
<h4>(2) Beautiful Soup</h4>
- It allows to parse the data based on HTML’s Tag. Once we success requesting the site, this library collects the data. As programmers, they have to consider how the tags are related to each other. We can think about subordinate relation for example. 
<h4>(3) Csv</h4>
- It allows to make a CSV file and to write in. Once the HTML Text are well parsed, we can easily use the data.
<h4>(4) Tkinter</h4>
- It allows to design a User Interface (UI). Thanks to this library, I could make a window, scroll box, list box, button, message box and Grid to arrange the data showed on application.
<h4>(5) Matplotlib</h4>
- It’s a powerful library to visualize the data. There are various forms of graph, and I chose a simple plot for this application.

<br>
<h3>4) What kind of libraries (packages) did I use ?</h3>
<h4>(1) Up-To-Dateness </h4>
It takes a time to gather the data from Web Server (URL). And sometimes, some Web Server refuses the access of Request. Therefore, it’s highly recommended to find other ways to extract the data.
<h4>(2)	Slowness of run </h4>
It takes a time to gather the data from Web Server (URL). And sometimes, some Web Server refuses the access of Request. Therefore, it’s highly recommended to find other ways to extract the data.
