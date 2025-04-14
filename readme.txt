This is a minimal mpf game related to https://github.com/missionpinball/mpf/pull/1888

I built a minimum mpf game to explore the shot problem I have.

You will have to use the monitor to see the light of the shots.

I set up a mode "mode1", that contains 7 shots: "sh_triangle1" et "sh_triangle7". They are identical
These shots are activated with keys "1-7"

Here is how to use:
- start mpf with DEBUG enabled (mpf both -Xt -v -V) and monitor (mpf monitor)
- The screen should say "Attract mode"
- Push enter to start the game: screen should say "Player1 Ball 1"
- Push "a" key to start "mode1": screen should say "Mode 1"
- Hit "1" : this enable shot "sh_triangle1" (the led on the playfield will blink)
- with the mouse enable the switch to advance the shot. The light will stop blinking
- Hit "1" again : log should say "Received jump request. State: 1, Force: True" (and the led blinks again)
- Push "shift+a", this will stop "mode1"
- Push "a", to start "mode1" again
- Hit "2" instead of "1", the shot "sh_triangle2" will be enabled, but the led will not blink
- Hit "2" again: the log won't say "Received jump request" !

With the patch, the shots can be enabled/jumped to state 1 after "mode1" has been restarted
