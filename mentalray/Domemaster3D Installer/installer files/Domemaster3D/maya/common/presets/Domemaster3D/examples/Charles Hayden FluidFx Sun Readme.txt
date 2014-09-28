
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



Whats going on here?
=====================================
Have you ever wanted to fly up close to a sun? To see those dynamic boiling details, shimmering corona, and mesmerizing surface textures patterns... But creating an animated volumetric sun with all these attributes is quite difficult.

It turns out that you can constrain a Maya fluid into a sphere. But the fluid system is tricky to work with since there are so many different attributes to explore and figure out their intertwined relationships. So its important that you already have in mind the type of star you want to create. Otherwise you'll end up tweaking details endlessly without any basis for when its finished.

The foundation of this fluid sun is actually an example found within the Maya Visor. But it has since been highly customized to reach the current look. We wanted the sun to have more detailed surface textures, wispy corona, and controllable animation.

Just to say it upfront, understand that this approach is meant to be more stylized than realistic. We lean in this direction because its believable, dynamic, and beautiful. Audiences undoubtedly know that its a star. The trade-off is that solar prominence's are ignored, though I'm sure you could create a separate fluid system to address this. Obviously it can't solve all of our problems but it offers us many options to work with.

The most difficult and time consuming part is just setting up the fluid. But you can skip over this step since I've shared Maya scene below. But you can watch this video tutorial if you're curious how to make a fluid sun from scratch.

Example render:
https://vimeo.com/71172540



How to Customize the sun
=====================================
This sun can be easily customized once you understand some specific attributes outlined below. All of these attributes can be found within the sunFluidShape tab of the attribute editor. As you will undoubtedly see, there are TONS of other attributes that I’m not covering here simply because narrowing your options makes things manageable and you can focus on being creative.

Speed Up Render Times to Experiment Quicker
--- While experimenting with the attributes listed below, I would suggest lowering the Shading Quality to greatly reduce render times. (sunFluidShape/Shading Quality/Quality)
--- Adjusting the Resolution can change the overall look of how much detail is in the sun, but not in a way you expect. Resolution determines how many voxels (volumetric pixels) are allowed. So a higher resolution does not mean better quality, its just a different look. I suggest keeping the Resolution XYZ values equal. Higher values mean longer render times. The default values are a good place to begin. (sunFluidShape/Resolution)

Need the sun to be a different color and brightness?
(sunFluidShape/Shading/Color tab & Incandescence tab)
--- First play with the color gradient and then the incandescence gradient. There is a relationship here that can only be understood by playing with it and doing test renders. Its best to try and keep these two gradient looking similar, this reduced confusion.
--- Glow plays an important role in making it seem blown out and bright. (sunFluidShape/Shading/Glow Intensity) Be aware that if you don't let a test render fully finish, then the post-render glow won't be applied. I mention this because the post-render glow plays an important part in making it appear bright but still controlling the amount of blown out details.

Need the sun surface texture to have bigger/smaller elements?
(sunFluidShape/Textures tab)
--- Play with the Ratio attribute first to get foundation. Then adjust the Frequency Radio attribute to adjust the detail added ontop. The Implode attribute can do some interesting things too. Threshold and Amplitude can be weird but fun to experiment with.
--- The textures play a particularly important role in a fluid sun. For instance, if you are creating a blue super-giant; by making the surface elements smaller then it will help to make the star feel truly huge.

Need the sun to look like its in the process of forming?
(sunFluidShape/Textures tab)
--- Reducing the Frequency attribute to very low numbers (between .001 to .5) can produce some interesting effects that make the sun appear as if its missing chunks. Almost like swiss cheese. This is an experimental technique that could be animated to create the moment of a sun igniting.

Need the corona to be more opaque or reach farther out?
(sunFluidShape/Shading/Opacity tab)
--- This gradient is where your sun is restricted to a tight sphere but still allow some rays to leak through. Think of the vertical peaks in the gradient as where you want the fluid to show up. The horizontal being how close to the center of the fluid container you are. By adjusting the gradient and watching the viewport you can get a rough preview of whats being affected.

Need the surface textures and corona to boil (animate)?
(sunFluidShape/Textures tab)
--- Key the Texture Time attribute. For a subtle but effective simmering look, I generally have an increase of .25 per 30 frames. This is already keyed in the downloadable example.

Need the sun to spin? Or move around?
(sunFluid = Rotate XYZ of the channel box)
--- Simple. Just key the Rotate X, Y, or Z of the sunFluid. In other words, just animate the fluid container itself. To move the sun just key the Translate XYZ. The same for Scale XYZ.



Possible Problems and Solutions
=====================================
--- This fluid setup renders pretty fast. Know that the closer you get to the sun, the higher your render times will be. I'm not talking drastic just something to be aware of. Rendering at production quality is definitely overkill and you won't see a different from preview quality. You might even be able to away with draft quality, but beware of flickering or aliasing. A simple batch render test of 90 frames will inform you of whats best.
--- If you want to better understand how fluids work, then here are two tutorials that will really lay the groundwork for you. Maya fluid testing and Fire effect.
--- To avoid any problems with different fluids overlapping or any flickering: go to the Render Globals/Features/Extra Features/Volume Samples: 4
--- If a moiré pattern is visible during animation, you can slowly increase the shading quality. (sunFluidShape/Shading Quality tab) Be aware that this will increase render times. But there is a delicate relationship between Quality and Contrast Tolerance to balance this.
--- We have never needed a need to cache our fluids, even with a renderfarm.
--- If you want to light-link a fluid, make sure not to have it grouped. Instead point-constrain it. This is due to how the fluidshape node show up within the light linking editor.
--- If for some reason you have a shadow casting from the sun, then select the sun and go to the sunFluid within the attribute editor, then spin down the mental ray tab, flags tab, uncheck 'derive from maya', and then set shadows to no.
