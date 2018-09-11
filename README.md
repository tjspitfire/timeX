# timeX - LATEST - Branch: timeX 0.1.0
Portable productivity GUI with export options and motivational features.

MACINTOSH: If you are running a Macintosh, youu may need to update your ActiveTCL, which can be found at https://www.activestate.com/activetcl/downloads. It'll run on either 8.5 or 8.6, depending on your platform requirements.
The cool thing about this is that it will run on Windows, Macintosh, and Linux with zero scripting changes. There will be minute visual differences, but if you're like me, and you're constantly going between Macintosh, Windows, and Linux machines, it is quite convenient to have a cross platform graphics solution.

USAGE:
 1. Make a directory somewhere titled timeX (or call it something else if you want to be that way :p).
 2. Copy timex.py and image.gif to the timeX folder. If you are iffy about the giffy, see the "IFFY GIFFY" section at the     bottom of this page. I typically place the image.gif in a folder called file, but I removed that path dependency from the   script so do what you will.
 3. Open up the terminal, and run using python3.5 (the latest security-only release, unless I need to read up on 3.6). For     you python noobs, it's, 
  "python3.5 timex.py",
  assuming you have multiple python installations. If you are a super noob and have ONLY just installed python3.5, it will     probably run under either, "python timex.py", or "python3 timex.py".
 4. Enjoy my attempts to utilize the tkinter library.
  
USER INTERFACE:
 1. Start Timer - Starts the timer.
 2. Reset Timer - Resets the timer after you've reached zero.
 3. Pause Timer - Pauses the fucking timer.
 4. Exit - Exits the program. Sometimes if you click on the red cancel icon it will take a shart so I added that feature. Unfortunately, sometimes when you click on the Exit button, it sharts as well... in this case, simply terminate the terminal window by clicking on the big red X at the left hand or right hand side of the screen.
  
UPCOMING FEATURES/WISHLIST:
 1. Advanced graphic interpretation of the oscillation parameter. I was thinking some moving gears or something like that.
 2. Additional graphic representation of completed tasks. I was thinking of using a Listbox. That is my next point of       implementation, unless I find a gear gif I really like (btw, it's gif, not jif...).
 3. MOAR FEATURES. Basically I figure that if I can implement this tool throughout the rest of my engineering career, it     will, in the long run, save time. So let's feature this thing-a-ma-jig up!
 4. Colors 'n Sich. If you're the color it up guy or gal, please help me out. I typically think "MOAR FEATURES", over,       "Let's add Color". It could most certainly use some color! I'd say the initial step would be to liken it to the rest of      the operating system color scheme based on platform. I'll get that going as well...
 5. Literally anything else... as long as you don't make it fugly, I don't care. If it's fugly,... we no likes fugly          engineering.
  
Hopefully it works. I'm a mechanical guy, so if it doesn't, help a guy out.

kthanksbye
  
"IFFY GIFFY": 
  If you're super paranoid or something (I understand, honestly...), comment out the "image" labelframe in    "TimeX.task_complete". It's Rosey the Riveter pumping her arm, showcasing the classic American Spirit of, "We can do it!" I haven't taken the time to include any frames other than the zeroith; if you want to help me out with that, that'd be super sick bro... Regardless, It's a nice little pep up when you're frustrated on some scripting item and you want to bash your keyboard with some large, blunt object, such as your coffee mug.
