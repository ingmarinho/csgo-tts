# CS:GO TTS (with Python)
 This Python program makes *actual text-to-speech from game-chat or custom binds possible!

## How it works
 If you add the following launch option to your CS:GO launch options: '-condebug' every console command will be logged into a logfile.  
 This logfile than gets read out by the program to detect whether or not anything was said by you, if so it will activate your voice key and speak with the Google translate voice.  

## Requirements
 **-condebug** in CSGO launch options  
 VBCable needs to be installed on your system (https://vb-audio.com/Cable/)  

 
## Python libraries used
 file_read_backwards  
 gtts  
 keyboard  
 pygame  

## Usage
Please check and fill in the .ini files first!  
'CABLE OUTPUT' should be set as your default device in your Sound/recording settings (in Windows)  
'CABLE OUTPUT' should also be set as your microphone in the Steam settings  
(From my experience you need to mess around a little bit with these settings for it to work)  

## License

Copyright © Ingmar Fontijne, 2021.

Distributed under the Boost Software License, Version 1.0. (See accompanying file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt).

Note: See license file for a detailed description.
