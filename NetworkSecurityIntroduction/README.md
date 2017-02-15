Basic of Information Security: Concepts, 
===
```
第一週                    由新聞事件(Pokemon & 一銀事件 & 勒索軟體 )看資訊安全
                                說明資訊安全定義及後續八週課程概要
第二週                    說明國際資訊安全標準與發展(管理系統標準簡介)
第三週                    資訊安全管理系統(ISO27001)與風險管理(ISO31000 & ISO 27005等)標準重點摘要介紹(配合部分電影片段)
第四週                    透過影片或TED演講影片探討網路攻擊之資訊安全技術
第五週                    網路安全架構簡介及相關防護機制
第六週                    網路攻擊手法探討
第七週                    由電影片段看社交工程與社群網路
第八週                    個資保護及防護介紹
第九週                    課程總結及測驗
```
<div align="center">莊子●列禦寇</div>
===
<big><big>
朱泙漫學屠龍於支離益，殫千金之家，三年技成，而無所用其巧。<br>
...<br>

Greatest Art, Little Gain.<br>
</big></big>


``` 
                            ȯ __
    _a' /(     ,>         \./\)              o
  ~~ }\ \(    (             <.\             '-) 
    ͝͝  \(,_(,)'                 .           / /<
       _>, _>,             ^^--=-^^     
```

Prelude of the Second Run
===
1. Internet, the most important environment of computers working on, including data creation, interchanging, sharing, collection; and security problem is always the users' nightmare and becomes more important than ever.
- During the left short time, let us study the related topics by using impressive and useful **Python** and **Jupyter IPython platform**, maybe still not effortless on our concerns.
   - Try Ansconda Integration to prevant any problem of installation; <font color="red">**note** we can not solve all the problem in the system of installation</font>.
- Topics include:
  - [Basic Python, the tool we use<sup>4,9</sup>](AutomaticTheStaffWithPython/index.ipynb#Ch06---Manipulating-Strings) data layout, passwork ckeck,
  - Internet detect tools 
    - [TCPIP related<sup>1</sup>](tcp_py/TCPIP.ipynb) ICMP, TCP, ZeroMQ, server/client implement 
    - [Penetration Testing, port scan<sup>2</sup>](PythonViolent/PythonViolent/CH2/ch2.ipynb) port scan, ping ips at work,
  - data retrieve and investigation
    - [Forensic Investigations<sup>2</sup>](PythonViolent/PythonViolent/CH3/ch3.ipynb) find killer by exploring meta data,
    - [Web Scrapy Introduction<sup>3</sup>](WebScrapingWithPython/python-scraping-master/index.ipynb) Basic of scraper (1), HTML analysis (2), data storing (5), reading web resource, txt,csv,pdf, docx, (6), Image recognition (11), 
  - log Analysis
    - [Network traffic analysis<sup>2</sup>](apache/nginx-log-analysis.ipynb#Nginx-log-analysis-with-pandas-and-matplotlib), httpd access log analysis and visualization,
    - [pcap with log<sup>6</sup>](pcap/data_hacking-master/index.ipynb#data_hacking) pcap introduction (?)
  - [Voyage on Web, read data in detail<sup>3</sup>](WebScrapingWithPython/python-scraping-master/index.ipynb)
  - [Cryptography](PythonCipher/hackingciphers/GermanEnigma.ipynb#Cryptography) Enigma within World War II
  - [Descrypted Data and Recognition<sup>3,4</sup>](WebScrapingWithPython/python-scraping-master/index.ipynb)
  - [Security Concerns Come from PHP and related<sup>5</sup>](PHPHacher/hackerPHP.ipynb#Hacker) Server-client's Security Introduction





References
--
1. [Bill Lubanovic, Introducing Python, O’Reilly, 2015. (<font color="brown">Python3</font>)](introducing-python-master/Introducing%20Python.pdf)
- [T.J. OCannor: Violent Python Violent Python, 1st Edition, 2013. (<font color="#ee22ee">Python2</font>)](PythonViolent/ViolentPython.ipynb)
- [Ryan Mitchell, Web Scraping with Python, O’Reilly, 2015. (<font color="brown">Python3</font>)](WebScrapingWithPython/OReilly.Web.Scraping.with.Python.2015.6.pdf)
- [Cyrille Rossant, IPython Interactive Computing and Visualization Cookbook, Packt Pub, 2014.](http://localhost:8888/files/Documents/prepare/IPython%20Interactive%20Computing%20and%20Visualization%20Cookbook.pdf)(<font color="brown">Python3</font>)
- GIJOE, 網頁程式駭客攻防實戰－以PHP 為例, 旗標出版社, 2007. 
- [GitHub, data Hacking](https://github.com/ClickSecurity/data_hacking)(<font color="#ee22ee">Python2</font>)
- [Al Sweigart, Hacking Secret Ciphers with Python, 2013](PythonCipher/HackingSecretCiphersWithPython.pdf),(<font color="#ee22ee">Python2</font>)
- [Bastian Ballmann, Understanding Network Hacks, Springer, 2012, (<font color="#ee22ee">Python2 and wifi module only for Linux</font>)](PythonHacker/PythonHaching.pdf)
- [Al Sweigart, Automate the Boring Stuff with Python, No Starch Press, Inc, 2015. (<font color="brown">Python3</font>)](Automate%20the%20Boring%20Stuff%20with%20Python.pdf)

Softwares and Tools
===
[Anaconda](https://www.continuum.io/downloads) Try to install it on your Laptop/pc, and bring it to the field!
