
TERMS OF USE
=====================================
Creative Commons - Attribution-ShareAlike 4.0 International
http://creativecommons.org/licenses/by-sa/4.0/

My Simple Request:
--- If used in a production, then please include a credit to the 'Charles Hayden Planetarium Staff' and let me know.
--- Share your work with me. I'd enjoy seeing your creations based off my hard work.



Questions? Feel free to contact me:
=====================================
Jason Fletcher
nuclearsugar@gmail.com
www.thefulldomeblog.com



Whats happening here?
=====================================
Maya has an excellent particle system that is fisheye compatible. So we use a spherical volume emitter and adjust the ‘away from center’ to 0. This insures that particles are emitted randomly throughout the volume and stay stationary. We use sprites as the particle render type. Sprites are simply a special type of image plane that will always face the camera. We then map a texture onto the image plane. This texture is an stylistic image of a star; I created it from scratch in Photoshop. All of this is already setup in the star field template maya scene. I’m just sharing a bit of framework thoughts for those interested.

Example Render
https://vimeo.com/70506981



Workflow
=====================================
1) Open the StarFieldTemplate.mb maya scene file.
2) Make sure you have your scene project setup. Otherwise your initial state will get lost when you open up this scene again.
3) Choose density by ticking the timeline frame-by-frame. I always tend to need much more than I initially imagine. Try placing a test camera in the star field and doing some renders.
4) When satisfied, set an initial state for each of the 4 particle shapes.
5) Zero out the rate for each of the emitters. (but do not ever delete them!)
6) Delete the ppScale creation expression for each of the emitters.
7) Done! Now you can scrub the timeline and the sprites are locked. Try a test render!



Star Field Stats
=====================================
— Emitter1: Orange stars – 5000/sec – scale .8 to 1.2
— Emitter2: Yellow stars – 4500/sec – scale 1 to 1.5
— Emitter3: White stars – 600/sec – scale 1.5 to 2
— Emitter4: Blue stars – 300/sec – scale 2 to 4



Don’t Add Lights to the Stars
=====================================
These stars don’t need to be lit with a light. They have incandescence that makes them self-lit. Any added lights should be light linked away or else it will contribute to lighting the sprites and make the stars brighter than expected.



If you have any issues rendering the sprites…
=====================================
Go to the Render Globals / Quality / Raytracing / Acceleration / Acceleration Method: change to Regular BSP. Then try BS2.



Editing the Randomized Scale Range
=====================================
1) Go to the sprite shape node in the attribute editor / Per Particle (Array) Attributes / right click on ‘Expression…’ next to Sprite Scale Y PP / click Creation Expression.
2) Edit the numbers in the last part of the expression text area: rand(.8,1.2)
3) When finished, click ‘Edit’ in the Expression Editor and then close.



Hide Certain Sprites within the Star Field
=====================================
1) Set your particle lifespan to ‘lifespanPP only’.
2) Right click on the particles and enter component mode.
3) Go to Window > General Editors > Component Editor
4) Find the ‘Particles’ tab, then find the ‘lifespanPP’ field.
5) Now you can select the sprites you want hidden in the viewport. Then type in 0 for their lifespanPP in the Component Editor.
6) After finished you MUST initial state.
