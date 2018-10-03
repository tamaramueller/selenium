# selenium
How to interact with websites using Python and Selenium

Run the Python script "DevChallenge.py" to interact with the website "http://www.quantbet.com/quiz/dev" and solve the Developer Challenge.

The Program uses Selenium and Firefox (headless).

Optional "DevChallence_withC.py" calculates the greates common divisor with a C program. See how to call a C program from within Python. But the C program has to be compiled before running the Python file. Compile C Program with

```
cgg gcd.c -o gcd
```

Also, make sure that the PATH variable is updated with the path to the executable file 'geckodriver' wich can be downloaded here: https://github.com/mozilla/geckodriver/releases

To update PATH variable run the following command in your terminal:

```
export PATH=$PATH:path/to/geckodriver/file
```

In case the geckodriver file isn't executable, go to the folder where the geckodriver file is stored and enter the following command:
```
chmod +x geckodriver
```


The code contains starting the connection to a website (driver.get(url)), getting specific information from the website (here everything between the HTML brackets <strong></strong>), sending an input value with send_keys, pressing a button (click()) and getting the feedback from the website.
