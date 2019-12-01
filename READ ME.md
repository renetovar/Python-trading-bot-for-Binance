# Python-trading-bot-for-Binance
Steps to get started with a trading bot for binance.com

Scope is to help you get started, from scratch, even on a fresh windows install.  

Pre-requisites:

Apart from some trading and some programming background, your computer might be:
Windows 7, 8.1 or 10.
32-bit or 64-bit.
Some 10 GB hard disk available space.
Any RAM as recommended for Microsoft Office.
So far, I've used Intel i3 with 8GB, Intel i5 with 4GB, Intel i7 with 6GB with windows home, 64-bits.

Steps to setup a development environment to run the binance.com example provided in this project, hopefully allowing you to go from there.


1. Update your JRE (Java Runtime Environment) or JDK (Java Development Kit).

This step is optional if you've been installing tools and developing before.  You may find that this is required for step 4, otherwise the step itself would tell you if an update is required or just goes thru.
If you are new to Python, eclipse IDE, etc., then you may prefer to download the latest JDK from:
https://www.java.com/es/download/

Make sure you download the one for your 32-bit / 64-bit version (and for your operating system).


2. Ensure you have "Microsoft Visual C++ 14.0 build tools" installed in your computer.

Step 3.1 may show an error ... "Microsoft Visual C++ 14.0 is required".
If you are a Visual Studio developer, it's likely you have resolved or went thru this issue before, however if not, you may still prefer to skip this step waiting to see if that error actually shows up during step 3.1.

If you wish to get "Microsoft Visual C++ 14.0 build tools" I am not the expert to tell you, but I've resolved this slightly differently a few times by searching for "Microsoft Visual C++ 14.0 build tools" in your favorite search engine.
At some point you would need to check that you are downloading the right one for your 32-bit or 64-bit (and for your operating system), for your windows version, as well as from Visual Studio 2015, 2017 or 2019.  The important thing is to download "build tools".

The correct one would be that allowing you to finish step 3.1 without the "C++ 14.0 is required" error.


3. Python

This might be the easier.
Just go to www.python.org

Click on download and find the latest "stable" version for your windows and your 32-bit / 64-bit version (and for your operating system).
"Stable" is a keyword I read at that site meaning it's not a legacy version, nor the pre-lease fresh one.
As of November, 2019, it's 3.8.

The only installation particular is to check "Add python to PATH".  By default that checkbox is unchecked, but it's required to be checked.
The rest is just going thru any standard install picking up any default action.


3.1 Importing binance.com libraries for Python

Once Python is fully installed, you need to open the legacy D.O.S. windows (or console) to run a few commands.
One is to switch your current directory to the Python directory.  If you can't find it, a clue is to type PATH in the command line and find where Python was installed.  You should see the following directories once you find the right path: DLLs, DOC, INCLUDE, LIB, LIBS, etc.

Once in the right directory, execute:
pip install python-binance

It takes a few minutes, and here is where you may find the "Microsoft Visual C++ 14.0 is required" error.

Once is successfully installed, move on with:
pip install keyword

It's not mandatory but I found it useful to start with a console-like program for binance.com


4. Eclipse IDE

This is an appropriate IDE for Python.  Get a free copy from:
www.eclipse.org

Again, browse to download the right package for your 32-bit or 64-bit version (and for your operating system).
In any case, the ECLIPSE IDE that you need is:

ECLIPSE IDE for Committers

Once downloaded, unzip it to the location where you would like to run your IDE.
You may prefer to create a shortcut for "eclipse.exe" to your desktop of start menu, however you prefer.

Doubleclick "eclipse.exe" or your shortcut to start the IDE.
If you experience any Java related error, please check step 1.  If you get runtime 13 ... maybe Java is not installed, or the wrong 32-bit / 64-bit version.

You would need to setup the IDE for Python.  There is a PDF below with the overall instructions I grab from the web "eclipse IDE setup.pdf".
I've recorded a video that describes most of the process, if that helps you better.  Find it below in .mp4 format.


5. Credits to Sam Mac Hardy

I am just helping to get others started, as it took me a significant effort to figure it out all the above steps, but from here, you would credit Sam Mac Hardy for his contribution building the Python librearies for binance at:

https://github.com/sammchardy/python-binance

You may download it to your computer following the license terms and instructions from his GIT project.


6. My first project.
If you prefer to start something from scratch, I am sharing below a raw example "test.py" to help you kick-off your own project. This is your first project to connect to binance.com (without a user/password) and checking some prices.

First, make sure your computer's time & timezone are accurate.
I use www.time.is to ensure it's less than 1 second different otherwise binance.com may return errors or not return data if your time is in the future.

You just need to create a "Py Project", and inside, create a "Py Module".
Choose the option of an "empty module".
Then replace the source with the "test.py" example below, and click run (green play button).
You should get an Python array with all price details from the given symbol (i.e. BTCUSDT), and the price extracted from that array.

Give a try, and stay connected to find more examples.
