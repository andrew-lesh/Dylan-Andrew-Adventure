
label oatmeal:
scene bg 304
show d norm t
show a happy
d "Alright, so what exactly makes oatmeal 'industrial grade'?"
show d norm
show a norm t
a "Well, pretty much all oatmeal sold has been produced industrially."
show a norm
show d norm t
d "As opposed to being milled by hand?"
show d norm
show a happy t
a "Yeah, exactly!"
a "So pretty much any oatmeal should do, right?"
show a happy
show d norm t
d "Huh.  I suppose so."
show d happy t
d "We could just use one of our instant oatmeal packets then!"
show d happy
show a happy t
a "Doesn't get any more industrial than that!"
show a happy
play music "Final Fantasy VII 11 Fanfare 8-BIT 1.mp3"
show snowblossom 1
show snowblossom 2
show oats at Transform(function=floppy_transform)
show d happy t
d "Well that was much easier than I expected."
show d norm
show a norm t
a "Wait a second, we probably need to cook it, right?"
show d norm t
show a norm
d "Oh, I guess."
show a happy t
show d norm
a "I mean, we can't just feed uncooked oats to Ronald Reagan's bee costume, right?"
show d norm t
show a happy
d "Is that what we're doing?"
hide snowblossom 1
hide snowblossom 2
hide oats
play music "Automation.mp3"
show d norm
show a happy t
a "And that means we'll need a bowl to contain the cooked oatmeal!"
show a happy
show d norm t
d "Oh right.  Well Adam on the first floor still hasn't returned my dinosaur bowl."
d "But we could just grab a bowl from the kitchenette or something."
show d norm
hide a happy with fade
a "Nope, your property rights as an American citizen have been violated!  You need justice!"
show d norm t
d "Uh, what?"
d "And what are you getting out of your closet?"
show d norm
show fm norm t with dissolve
a "Your bowl's missing, Dylan.  And we won't rest until we have the culprit behind bars."
show fm norm
show d norm t
d "Did you tape a construction paper badge to your raincoat?"
show d norm
show fm happy t
a "Yeah dude, I made a badge for you too!  Good cop, bad cop!"
show fm happy
show d happy t
d "Oh sweet!"
hide d happy t with fade
d "What are our cop names again?  We haven't played police detectives in a while."
show fm happy t
a "I'm Flint McSteel and you're Ace Jenkins."
show fm happy
show aj happy t with dissolve
aj "Oh yeah, that's right!"
show aj norm t
aj "But how can we solve a mystery if we already know Adam has it?"
show aj norm
show fm norm t
fm "Purely circumstantial evidence!  It'll never stick in court."
fm "We need a smoking gun!"
show fm norm
show aj norm t
aj "We gotta catch him dead to rights!"
show aj norm
show fm norm t
fm "We gotta catch him red herringed!"
show aj norm t
show fm norm
aj "Um, you mean red handed?"
show aj norm
show fm norm t
fm "He's in Room 110 downstairs, right?  Let's bust in there and gather some evidence!"
show aj norm t
show fm norm
aj "Whoa, we can't just go in his room!  We could get in trouble."
show aj norm
show fm happy t
fm "He'll let us in when he sees we have a signed search warrant!"
show fm happy
show aj norm t
aj "Did you also make a search warrant out of construction paper?"
show aj norm
show fm norm t
fm "I definitely might have."
fm "But we still need a judge to sign it.  Would a law student be close enough?"
show fm norm
show aj norm t
aj "I don't think we know any law students.  And it would not be."
show aj norm
show fm happy t
fm "Let's just have Javarcia sign it.  He's a pre-med major."
show fm happy
show aj norm t
aj "And in what way is that similar to being a judge?"
show aj norm
show fm happy t
fm "You see, police detective Jenkins, the word 'judge' starts with the letter J."
fm "Javarcia's name also starts with the letter J."
fm "Coincidence?"
show fm happy
show aj norm t
aj "...Yes."
aj "And don't we bother Javarcia enough already?  I think he's studying for a midterm this week."
show aj norm
show fm happy t
fm "Great, let's go!"
scene bg javarcia closed with dissolve
show aj norm with dissolve
show fm norm with dissolve
show fm norm t
fm "Alright Jenkins, we're here at the judge's penthouse suite."
show fm norm
show aj norm t
d "I think this just a dorm room, Andrew."
show aj norm
show fm happy t
a "Come on man, stay in character!"
show fm happy
show aj norm t
aj "Oh right, sorry."
show aj norm
show fm norm t
fm "This is how the judge stays safe from the criminals he puts away.  He had it made to look like a regular dorm room on the outside!"
show fm norm
show aj norm t
aj "The judge is a smart fella."
show aj norm
show fm norm t
fm "Alright, enough chit-chat."
play sound "door-bang-1.ogg"
fm "It's detectives Jenkins and McSteel!  We need your signature!"
show fm norm
show aj norm t
aj "Easy, McSteel, don't break his door down!"
show aj norm
show fm norm t
fm "I'm a loose cannon, Jenkins!  I fly off the handle and I knock hard on doors!"
play sound "dorm-door-opening.ogg"
scene bg javarcia open
show fm norm
show aj norm
show j norm t with dissolve
j "Dang, what's going on out here?"
show j happy t
j "Oh!  You guys are doing the police detective bit.  I love this one!"
show j stern t
j "But I'm not signing any more warrants for you guys."
show j happy
show fm norm t
fm "But Judge-varcia, searching the dining hall for leftover cheesecake after hours was crucial for our last case!"
show fm norm
show j happy t
j "Yeah, that was pretty funny!"
show j norm t
j "But for real, I don't need any more dining hall staff coming after me while I'm studying."
j "Also you guys smell like rotten eggs."
show j happy
show aj norm t
aj "You got cheesecake without me?"
show aj norm
show fm norm t
fm "Whoa judge, you got us all wrong!  That smell is brimstone!"
fm "And, uh, we don't need you to sign a warrant!"
show fm norm
show j norm t
j "You don't?"
show j norm
show aj norm t
aj "Uh... No!  No way, there's a totally different legal document we need you for..."
show aj norm
init:
    $ document = "document"
    $ war_flag = False
    $ auto_flag = False
    $ adamline = "potato"
menu:
    "Search warrant":
        jump warrant
    "Chest Autograph":
        jump autograph
    "Adoption papers":
        $ document = "we have signed adoption papers!  You're our son now and you have to do as we say!"
        jump adoption
    "Petition":
        $ document = "we have a signed petition to save the whales!"
        jump petition
        
label warrant:
show fm norm t
fm "We need you to sign a search warrant!"
show fm norm
show aj norm t
show j stern
aj "But he just said-"
show aj norm
show j stern t
j "No more warrants!"
show j stern
show fm norm t
fm "Hey, did I say search warrant?"
fm "I meant to say wearch sarrant!"
show fm norm
show aj norm t
aj "Get a grip, McSteel.  You're floundering."
aj "What my partner meant to say is..."
show aj norm
$ war_flag = True
if war_flag == True and auto_flag == True:
    menu:
        "Adoption papers":
            $ document = "we have signed adoption papers!  You're our son now and you have to do as we say!"
            jump adoption
        "Petition":
            $ document = "we have a signed petition to save the whales!"
            jump petition
elif war_flag == True:
    menu:
        "Chest Autograph":
            jump autograph
        "Adoption papers":
            $ document = "we have signed adoption papers!  You're our son now and you have to do as we say!"
            jump adoption
        "Petition":
            $ document = "we have a signed petition to save the whales!"
            jump petition
 
label autograph:
show fm norm t
fm "We need you to sign my chest!"
show fm norm
show j happy t
j "Um, what?"
show j happy
show fm norm t
fm "Wait, that's weird.  Why did I say that?"
show fm norm
show aj norm t
aj "Take it easy, McSteel!  The stress of this case is getting to your head."
show aj norm
show fm norm t
fm "Yeah, I guess you're right."
fm "But you can still totally sign my chest if you want, Javarcia."
show fm norm
show j norm t
j "Uhhhhhh..."
show j norm
show aj norm t
aj "What my partner meant to say is..."
show aj norm
$ auto_flag = True
if war_flag == True and auto_flag == True:
    menu:
        "Adoption papers":
            $ document = "we have signed adoption papers!  You're our son now and you have to do as we say!"
            jump adoption
        "Petition":
            $ document = "we have a signed petition to save the whales!"
            jump petition

elif auto_flag == True:
    menu:
        "Search warrant":
            jump warrant
        "Adoption papers":
            $ document = "we have signed adoption papers!  You're our son now and you have to do as we say!"
            jump adoption
        "Petition":
            $ document = "we have a signed petition to save the whales!"
            jump petition


label petition:
$ adamline = "Well if it will save our cetacean brothers and sisters, I suppose I cannot refuse.  Come, come."
show fm norm t
fm "We need you to sign a petition!"
show fm norm
show j happy t
j "Uh, maybe?  What's it for?"
show j happy
show aj norm t
aj "It's to uh, save the whales?"
show aj norm
show fm happy t
fm "I thought it was to make whiney congressmen play violent video games."
show fm happy
show aj norm t
aj "Topical reference there, McSteel."
show fm norm
aj "It's to stop Adam from holding my dinosaur bowl hostage so we can cook some oatmeal."
show aj norm
#show fm norm t
#fm "And feed that oatmeal to Ronald Reagan's ghost's bee-themed mechsuit."
#show fm norm
show j happy t
#j "Ha, well what else would you feed it to?"
j "Oh, he still hasn't gotten that back to you?"
j "Sure, I'll sign a petition for that."
show j happy
jump gotoadam

label adoption:
$ adamline = "Well I couldn't possibly disobey my questionably scented new patriarchs, now could I?  Please enter."
show fm norm t
fm "We need you to sign our adoption papers."
show fm norm
show j happy t
j "Um, what?"
show j happy
show aj happy t
play sound "sfx-realization.ogg"
aj "If we adopt Adam as our legal son, we can force him to give me my dinosaur bowl back."
show aj happy
show j happy t
j "Ha!  Now those are some classic Dylan and Andrew hijinks."
j "Alright sure, I'll sign your pretend adoption thing."
show j happy
jump gotoadam

label gotoadam:
play sound "signature.ogg"
n "Got judge's signature!"
show fm happy t
fm "Thank you for your cooperation in this urgent matter, Judge-varcia."
show fm happy
show j happy t
j "Okay, whatever you guys say."
#j "But I have one question before you go."
show j happy
show fm norm t
fm "Alright Jenkins, let's roll."
show fm norm
show aj norm t
aj "You got it, McSteel."
show aj happy t
aj "Bye, Javarcia!"
show aj happy
show fm happy
show j happy t
j "See you guys!"
scene bg adam closed with dissolve
show aj norm with dissolve
show fm norm with dissolve
show fm norm t
fm "Here we are, Jenkins!  Get ready!"
show fm norm
show aj norm t
aj "Hold on there, McSteel.  You're forgetting something important."
aj "Who's going to be the bad cop?  We're doing good cop, bad cop, right?"
show aj norm
show fm happy t 
fm "More like bad cop, worse cop.  Zing!"
show fm happy
show aj norm t
aj "Don't say 'zing.'  Police detectives don't say zing."
show aj norm
show fm norm t
fm "Fine, no zing."
fm "But I should be the worse cop, because my insults to the perp will be more colorful."
show fm norm
show aj norm t
aj "Actually I should be the worse cop because because I never graduated from cop school."
show aj norm
show fm norm t
fm "That's a good point, but let's let [name] decide."
show fm norm
menu:
    "Ace Jenkins is worse":
        jump aceworse
    "Flint McSteel is worse.":
        jump flintworse

label aceworse:
show aj happy t
aj "Woo!"
show aj happy
show fm norm t
fm "Fiddlesticks."
show fm norm
show aj norm t
aj "Alright, rookie, it's time to move in!"
play sound "door-bang-1.ogg"
aj "Open the door, Adam!  We know you're in there!"
show aj norm
show fm norm t
fm "Come on, dude.  You can do it worse than that!"
show fm norm
show aj norm t
play sound "door-bang-1.ogg"
aj "Open the premises so we can do some policings on ya, ya dirty rat!"
show aj norm
show fm happy t
fm "Now that's more like it!"
jump adamenter

label flintworse:
show fm happy t
fm "Sweet."
show fm happy
show aj norm t
aj "Womp womp."
show aj norm
show fm norm t
fm "Let's light this candle!  Look alive Jenkins!"
play sound "door-bang-1.ogg"
fm "Open up, Adam!  Room 304 Police!  This is a raid!"
show fm norm
show aj norm t
aj "Come on, do it worse!"
show aj norm
show fm norm t
play sound "door-bang-1.ogg"
fm "Open the door, you foul-smelling, wall-eyed, mouth-breathing, scum-sucking, yellow-bellied, purple-nosed, chartreuse-naveled, seafoam-eared, cerulean-tongued, bowl-thieving varmint!"
show fm norm

show aj happy t
aj "Wow, now that was a colorful insult."
jump adamenter

label adamenter:
play sound "dorm-door-opening.ogg"
scene bg adam open
show fm norm
show aj norm
show da evil t with dissolve
da "Hello, gentlemen.  It's a fine day we're having, isn't it?"
show da evil
show fm norm t
fm "Spare us the idle chatter, Mr. Adam.  You know why we're here."
show fm norm
show da evil t
da "Oh really?  I haven't the faintest idea."
da "Please, detectives, enlighten me as to the reason for your sudden visit."
show da evil
show aj norm t
aj "You agreed to borrow the bowl of a certain Dylan so you could eat cereal with it the next morning."
aj "But that morning came and went four days ago!"
show aj norm
show da evil t
da "That's an amusing narrative, detective Jenkins, but I'm afraid I have no memory of the incident you describe."
show da evil 
show fm norm t
fm "We weren't born yesterday, buddy-boy!  We know the bowl's in your room."
fm "And if you're not gonna fork it over, we're busting in there!"
show fm norm
show da evil t
da "Oh?  And why should I let you-"
show da norm t
da "Wait."
show da norm
da "*sniff sniff*"
show da norm t
da "Why do you guys smell like sulfur?  It's really strong."
show da norm
show fm norm t
fm "That's the smell of justice, punk!"
show fm norm
show aj norm t
aj "Actually we went to Hell and met the literal devil and are kind of doing this bit to distract ourselves while we subconsciously process it."
show aj norm
show fm norm t
fm "We are?  I feel fine."
fm "I was already taught the devil is a giant anime bee monster in Sunday school."
show fm norm
show aj norm t
aj "Oh.  I guess it's just me then."
show aj norm
show da norm t
da "Uh, are we still doing the police bit, or..."
show da norm
show aj norm t
show fm happy
aj "Yeah, sorry.  Um..."
aj "Let us investigatize your premises, dirtbag!"
show aj norm
show da evil t
da "Oh?  And why should I let you enter my humble, crime-free abode?"
da "What reason have I to facilitate the concoction of some fantastical charade to slight my character?"
show da evil
show fm norm t
fm "The reason is [document]"
show fm norm
show da evil t
da "Signed by the honorable Judge Javarcia himself, I presume?"
show da evil
show aj norm t
aj "The very same, bub!"
show aj norm
show da evil t
da "[adamline]"
scene bg adam room with dissolve
show aj norm with dissolve
show fm norm with dissolve
show da evil with dissolve
show da evil t
da "Bienvenue, detectives.  I think you'll find that everything here is in order."
da "And, most importantly, that this scene is entirely inconsistent with the notion that I took and am somehow withholding a dinosaur-themed bowl."
show da evil
show fm norm t
fm "The bowl's here somewhere, Jenkins.  I can smell it!"
show fm norm
show aj norm t
aj "You can smell bowls?"
show aj norm
show fm norm t
$ default_mouse = "magnify_blue"
fm "I've got my trusty magnifying glass here.  Let's find that bowl!"
show fm norm

jump adam_map

# ---Beeprints Legit
screen adam_imagemap:
    imagemap:
        auto "bg_adam_room_%s.png "
        hotspot (9, 19, 141, 171) action Return("peace_poster") mouse "magnify_gold"
        hotspot (669, 10, 130, 170) action Return("dc_poster") mouse "magnify_gold"
        hotspot (539, 270, 41, 29) action Return("phone_plug") mouse  "magnify_gold"
        hotspot (539, 380, 41, 71) action Return("socket") mouse  "magnify_gold"
        hotspot (319, 299, 161, 41) action Return("drawer_one") mouse "magnify_gold"
        hotspot (319, 349, 161, 41) action Return("drawer_two") mouse "magnify_gold"
        hotspot (319, 399, 161, 41) action Return("drawer_three") mouse "magnify_gold"
        hotspot (679, 200, 121, 99) action Return("laptop") mouse "magnify_gold"
        hotspot (388, 238, 24, 8) action Return("bowl") mouse "magnify_gold"
label adam_map:  
scene bg adam room
window hide None
call screen adam_imagemap
window show None
if _return == "peace_poster":
    jump adam_map_peace
if _return == "dc_poster":
    jump adam_map_dc
if _return == "phone_plug":
    jump adam_map_phone
if _return == "socket":
    jump adam_map_socket
if _return == "drawer_one":
    jump adam_map_drawer1
if _return == "drawer_two":
    jump adam_map_drawer2
if _return == "drawer_three":
    jump adam_map_drawer3
if _return == "laptop":
    jump adam_map_laptop
if _return == "bowl":
    jump adam_map_bowl
    
label adam_map_peace:
fm "What's this poster?"
da "That tapestry, detective McSteel, belongs to my roommate."
da "It says 'salam', or 'peace' in Arabic.  He is studying the language."
fm "Jenkins, take a note that Mr. Adam is a flight risk to the Arabian peninsula."
aj "I think that's a stretch."
jump adam_map

label adam_map_dc:
fm "What does D.C. stand for?  That some kinda secret criminal code?"
da "That would be the District of Columbia, my dear detective, where I work summers."
da "It happens to be the capital of the United States of America."
fm "Jenkins, take a note that Mr. Adam is a flight risk to the United States of America."
aj "Uhhhhh..."
jump adam_map

label adam_map_phone:
aj "Where's your phone, Adam?"
da "In the current year, a room phone simply isn't of much use."
da "I've safely stowed it away in my bottom dresser drawer."
fm "A likely story!  Jenkins, take a note that Mr. Adam swallowed his phone to defraud the phone company."
aj "If you insist."
jump adam_map

label adam_map_socket:
play sound "zap.ogg"
fm "OUCH!"
fm "Jenkins!  He booby-trapped his electrical socket!"
aj "With what?"
fm "Electricity!"
da "Your skills of detection truly know no bounds, detective McSteel."
jump adam_map

label adam_map_drawer1:
fm "Dresser drawers.  The perfect hiding place for contraband."
fm "Hmmmm..."
fm "Jenkins, take a note that Mr. Adam is in possession of a suspicious number of unmatched socks."
da "It's not my fault that the dryers downstairs eat them!"
aj "Can confirm."
jump adam_map

label adam_map_drawer2:
aj "Let's see what's in this drawer."
aj "Oh, uh.  That's concerning."
fm "Whaddaya see, Jenkins?"
aj "There's probably a million dollars here in cash, a handgun, and two rubber chickens."
fm "What's so concerning about rubber chickens?  My dresser drawers are filled with them!"
aj "That's not what I-"
aj "Nevermind."
jump adam_map

label adam_map_drawer3:
fm "A drawer!  How enticing."
fm "Hmmmm..."
fm "There's just a plastic phone like the one in our room and five sticks of butter."
aj "I'll admit that I fail to see the connection between the phone and the butter."
fm "We're dealing with a true criminal mastermind here.  Stay frosty, Jenkins."
jump adam_map

label adam_map_laptop:
aj "It looks like a regular laptop to me."
fm "Open your eyes, Jenkins!  That's no laptop!"
aj "Huh?  Then what is it, McSteel?"
fm "It's obviously a tabletop."
aj "What?"
fm "Because it's on top of a table, not a lap."
aj "That's got to be the worst attempt at a joke in this whole game."
jump adam_map

label adam_map_bowl:
aj "Huh.  It looks like there's a loop of fishing line around the base of the divider between the windows."
aj "I'll pull it up and see what's on the other end..."
play music "Final Fantasy VII 11 Fanfare 8-BIT 1.mp3"
show snowblossom 1
show snowblossom 2
show dino_bowl at Transform(function=floppy_transform)
aj "Aha!  Take a look, McSteel!"

fm "Well well well!  You really are an ace, Jenkins!"
fm "Looks like it's curtains for ya, Mr. Adam!"
da "What a strange bowl that is, dangling outside my window for no obvious reason."
da "I assure you gentlemen that I have never seen this object in my life."
fm "Time for an interrogation!"
jump adam_interrogation

label adam_interrogation:
$ default_mouse = "default"
scene bg adam open with dissolve
show fm norm with dissolve
show aj norm with dissolve
show da evil with dissolve
show aj norm t
#hide snowblossom 1
#hide snowblossom 2
#hide oats
play music "Automation.mp3"
aj "Wait, we have the bowl and we know he had it.  What do we need to interrogate him for?"
show aj norm
show fm norm t
fm "We have to prove he did it!  We need a smoking gun!"
show fm norm
show aj norm t
aj "What?  We literally found it in his room after he said he didn't have it!"
aj "And I, I mean Dylan, gave it to him in person four days ago!"
show fm norm t
show aj norm
fm "That'll never hold up in court!  It's all circumstantial!"
show aj norm t
show fm norm
aj "With all due respect, McSteel, I don't think you know a lot about court proceedings."
show aj norm
show fm norm t
fm "I know plenty!  We have to review the perp's testimony and catch him in a contradiction!"
#show fm norm
#show aj norm t
#aj "This isn't an Ace Attorney game, McSteel."
#show aj norm
#show fm happy t
3fm "You're right, this is a loose parody of one."
#show fm norm t
fm "Okay Adam, what's your claim regarding this bowl situation?"
show da evil t
show fm norm
da "I quite simply have never seen your bowl before.  Someone else must have hung it from my window."
show da evil
show fm norm t
fm "See?  Finding it in his room doesn't contradict the claim that someone else did it."
fm "And Dylan giving it to him in person doesn't matter because [name] wasn't there for it."
show fm norm
show aj norm t
aj "Hmph."
show aj norm
show fm happy t
show da norm
fm "Fortunately I tape recorded our conversation with him before we conducted our search."
show fm happy
show da norm t
da "You what?!"
show fm happy t
show da norm
fm "[name], can you pick the recorded line that reveals a contradiction?"
show fm happy
"Adam's claim: 'I quite simply have never seen your bowl before.'"

label adam_menu:
menu:
    "'...I have no memory of the incident you describe.":
        jump nomemory
    "'Why do you guys smell like sulfur?  It's really strong.'":
        jump sulfursmell
    "'Uh, are we still doing the police bit, or...'":
        jump policebit
    "'...why should I let you enter my humble, crime-free abode?'":
        jump crimefree
    "'...this scene is entirely inconsistent with the notion that I took ... a dinosaur-themed bowl.'":
        jump bingozingo

label nomemory:
show fm happy t
fm "Mr. Adam, you claim to have never seen the bowl..."
fm "but you previously said you have no memory of the bowl!"
show fm norm
show da norm t
da "Uh, I mean yeah?"
show da norm
show fm norm t
if stepahead == True:
    fm "Darn, he's three point four steps ahead of us!"
    show fm norm
    show aj norm t
    aj "Three point four steps?  What is that supposed to mean?"
    show aj norm
    show fm norm t
    fm "Oh, I just didn't want to say he's one step ahead of us twice."
    show fm norm
    show aj norm t
    aj "But of course."
    show aj norm
else:
    fm "Darn, he's one step ahead of us!"
    show fm norm
$ stepahead = True
jump adam_menu

label sulfursmell:
show fm happy t
fm "Mr. Adam, you claim to have never seen the bowl..."
fm "but you previously said we smell bad!"
show fm norm
show da evil t
da "You two do indeed smell, gentlemen detectives though you may be."
show da evil
show fm norm t
fm "Darn, that's a perfect alibi!"
show fm norm
jump adam_menu

label policebit:
show fm happy t
fm "Mr. Adam, you claim to have never seen the bowl..."
fm "but you previously were confused as to whether we stopped pretending to be police detectives!"
show fm norm
show da norm t
da "I... huh?"
show da norm
show fm norm t
fm "Darn, his story's airtight!"
show fm norm
jump adam_menu

label crimefree:
show fm happy t
fm "Mr. Adam, you claim to have never seen the bowl..."
fm "but you previously said your room was devoid of crime!"
show fm norm
show da evil t
da "I suppose a crime of bowl theft and concealment may have occurred in my room."
da "But if so, it was of course done by someone else!  You simply have no proof, gentlemen."
show da evil
show fm norm t
if stepahead == True:
    fm "Darn, he's three point four steps ahead of us!"
    show fm norm
    show aj norm t
    aj "Three point four steps?  What is that supposed to mean?"
    show aj norm
    show fm norm t
    fm "Oh, I just didn't want to say he's one step ahead of us twice."
    show fm norm
    show aj norm t
    aj "But of course."
    show aj norm
else:
    fm "Darn, he's one step ahead of us!"
    show fm norm
$ stepahead = True
jump adam_menu

label bingozingo:
show fm happy t
fm "Mr. Adam, you claim to have never seen the bowl..."
play sound "sfx-realization.ogg"
fm "but if that were true, then why did you correctly describe it as dinosaur-themed?"
show fm norm
show aj norm t
aj "That's right!  We told him we were here to get the bowl, but we never mentioned it was a dinosaur bowl!"
show aj norm
show da evil t
da "I should have known the great detectives Jenkins and McSteel would eventually find the truth."
da "Yes, I took the dinosaur bowl!  It was me, Adam!  Despite every indication to the contrary, it was me all along!"
show da evil
show fm norm t
fm "What a crazy plot twist!"
show fm norm
show aj happy t
aj "It's almost worthy of a Ronald Reagan flick."
show aj happy
show fm norm t 
fm "Alright Jenkins, put him in imaginary handcuffs and read him his imaginary Miranda rights."
show fm norm
show aj norm t
aj "You have the right to imagine yourself remaining silent."
aj "Anything you pretend to say can and will be used against you in a court of imaginary law."
show aj norm
show da evil t
da "I'll plead the imaginary fifth ammendment at every opportunity!"
show da evil
show fm norm t
fm "Our imaginary future trial is in the bag.  Let's head back to our room and make that oatmeal!"
show fm norm
show aj norm t
aj "Roger that, McSteel."
show fm norm
scene bg 304 with dissolve
show aj norm with dissolve
show fm norm with dissolve
show aj norm t
aj "Alright, now that the 'mystery' is solved, let's take these raincoats off!  It's like 90 degrees today."
show aj norm
show fm norm t
fm "Sounds good.  We can stay undercover until the next mystery."
show fm norm
hide fm norm with fade
hide aj norm with fade
d "Ahhhh.  I missed these cargo shorts."
a "Hold it!"
d "What's up?"
a "Someone broke our chocolate walrus!"
d "What?!"
show a stern with dissolve
show d norm with dissolve
show a stern t
a "I repeat, our North Pole Pals™ milk chocolate walrus has been messily duct-taped to the floor and broken into three pieces!"
show a stern
show walrus with dissolve
show d norm t
d "Oh, huh.  That's weird."
show d norm
show a stern t
a "We left the room locked!  Either someone picked the lock or used a master dorm key."
show a stern
show d norm t
d "Well we can deal with this later.  We need to make Ronald Reagan's ghost a bowl of oatmeal, right?"
show d norm
show a stern t
a "No way, this takes priority!  Someone has violated the sovereignty of Room 304!"
a "It seems like a prank at first, but they actually broke it!  That's aggravated chocowalricide!"
a "We need to lock down the whole floor, dust for fingerprints, interrogate witnesses, and-"
play music "police_siren.ogg"
hide walrus

image cop_alarm:
    "cop_alarm_red.png"
    pause 0.4
    "cop_alarm_blu.png"
    pause 0.4
    repeat
show cop_alarm
show walrus
show a norm
show d norm t
d "Whoa!  It's the actual cops!"
show d norm
show a happy t
a "Great!  They must have come to help with the walrus investigation!"
show a norm t
a "Sure, they'll mostly get in the way, but how else will those rookies learn?"
show a norm
show d norm t
d "Maybe it's a noise complaint for us banging on people's doors."
show d norm
play sound "door-bang-1.ogg"
cop "It's the police!  Open up!"
show d norm t
d "It's unlocked!"
show d norm
hide walrus with dissolve
show cop norm with dissolve
show cop norm t
cop "I'm officer Dirk Peebles with the Stanford Department of Public Safety."
cop "Which one of you lowlifes is Andrew?"
show cop norm 
show a happy t
a "Me!"
a "Are you here to find who broke our chocolate walrus?"
show a happy 
show d norm t
d "Or are you here to help with the communist thing we've mostly forgotten about by now?"
show d norm
show a norm
show cop norm t
cop "Andrew, you're under arrest for the murder of Jane Stanford."
show cop norm t
show a norm t
show cop norm
a "Wait, what?!"
show a norm
show d norm t 
d "Jane Stanford, the co-founder of Stanford University, died under mysterious circumstances over a century ago."
d "And you're arresting my eighteen-year-old roommate for killing her?"
show d norm
show cop norm t
cop "Yup."
show cop norm
play sound "lock_cuffs.ogg"
show a cuff norm t
a "Whoa, hey man!  Easy on my highly photogenic wrists!"
show a cuff norm
show d norm t
d "This isn't like a prank show thing?  A judge signed a warrant and everything?"
show d norm
show cop norm t
cop "Yup."
show cop norm
show a cuff stern t
a "Dang, the one time we actually don't want Javarcia to sign something..."
show a cuff stern
show d norm t
d "I don't think Javarcia signed a real arrest warrant."
show d norm
show cop norm t
cop "Alright, that's enough chit-chat.  We're taking you in."
show cop norm 
show a cuff norm t
a "Oh, okay.  I guess this is actually real."
a "Uhhhhh..."
a "Dude! You have to represent me!  Your dad's a divorce lawyer!  It'll be exactly the same!"
show a cuff norm
show d norm t
d "I really don't think that's a good idea."
show d norm
show a cuff norm t
a "You have to, dude!  I already spent all my money renting Bill Murray!"
show a cuff norm
show cop norm t
cop "Come on, let's go."
show cop norm
hide cop norm with dissolve
show a cuff norm t
a "I'm freaking out here, Ace Jenkins!  You have to be my attorney!"
show a cuff norm
hide a cuff norm with dissolve
a "Ace!  You have to be my attorneeeeeeeeey!"
hide a cuff norm
show d norm t
d "I must admit I didn't see this coming."
d "Wait a second."
d "Attorney.  Ace Jenkins.  Ace."
d "Attorney.  Ace..."
show d stern t
d "Oh son of a-"
#scene bg ace dylan
#show bg ace dylan 2 with dissolve
jump ace_start 


# ---Beeprints Legit
screen ace_dylan:
    imagemap:
        auto "ace_dylan_%s.png "
        hotspot (308, 461, 182, 68) action Return("start_ace") hover_sound "sfx-selectblip.ogg"
label ace_start:
play music "ace_attorney_trial.ogg"
scene bg ace dylan 2
window hide None
call screen ace_dylan
window show None
if _return == "start_ace":
    play sound "sfx-selectblip2.ogg"
    jump start_ace

label start_ace:
scene bg 304 with dissolve
#show d norm with dissolve
#show d norm t
#dd "Yay, the jame is tarted."
dd "Alright, what should I do now?"
dd "Are the cops going to come back and search this place for, uh..."
dd "Evidence that my eighteen-year-old roommate killed someone a hundred years ago?"
dd "I guess I should grab anything I think will be useful for the trial.  To uh, disprove that."
dd "That's how these attorney games work, right?"
jump search304

# ---Beeprints Legit
screen room304_imagemap:
    imagemap:
        auto "bg_room_304_dingus_%s.png "
        hotspot (400, 230, 100, 49) action Return("normal_phone") mouse "magnify_gold"
        hotspot (19, 31, 92, 88) action Return("owl_kite") mouse "magnify_gold"
        hotspot (669, 10, 130, 170) action Return("duck_poster") mouse "magnify_gold"
        hotspot (680, 200, 119, 100) action Return("dylan_laptop") mouse "magnify_gold"
        hotspot (0, 211, 110, 88) action Return("andrew_laptop") mouse "magnify_gold"
        hotspot (539, 380, 41, 70) action Return("safe_socket") mouse "magnify_gold"
        hotspot (320, 300, 160, 40) action Return("drawer304_1") mouse "magnify_gold"
        hotspot (319, 350, 161, 40) action Return("drawer304_2") mouse "magnify_gold"
        hotspot (319, 400, 161, 40) action Return("drawer304_3") mouse "magnify_gold"
        hotspot (170, 29, 461, 199) action Return("window304") mouse "magnify_gold"
        
init:
    $ photo_flag = False
    #$ flag_flag = False
    $ book_flag = False
    $ chicken_flag = False
    $ id_flag = False
    $ ev_counter = 0
    $ pistachio_count = 0
    
label search304:
if photo_flag == True and chicken_flag == True and id_flag == True and pistachio_count > 0:
    jump search_304over
$ default_mouse = "magnify_blue"
scene bg 304
window hide None
call screen room304_imagemap
window show None
if _return == "normal_phone":
    jump normal_phone
if _return == "owl_kite":
    jump owl_kite
if _return == "duck_poster":
    jump duck_poster
if _return == "dylan_laptop":
    jump dylan_laptop
if _return == "andrew_laptop":
    jump andrew_laptop
if _return == "safe_socket":
    jump safe_socket
if _return == "drawer304_1":
    jump drawer304_1
if _return == "drawer304_2":
    jump drawer304_2
if _return == "drawer304_3":
    jump drawer304_3
if _return == "window304":
    jump window304



label normal_phone:
dd "It's just a regular phone, I don't think that could help."
dd "We already called everyone we could think of back on the first disk."
jump search304

label owl_kite:
dd "That's Andrew's owl-shaped kite."
dd "Maybe we can fly it after this weird situation blows over."
jump search304

label duck_poster:
dd "I don't actually have a poster like this in real life."
dd "It's meant to convey to the player that I like ducks a lot, which is true enough."
dd "Ugh, now that Andrew's gone, I'm the one breaking the fourth wall!"
jump search304

label dylan_laptop:
dd "That's my laptop."
dd "I don't think it has any proof that Andrew doesn't murder people in his spare time."
jump search304

label andrew_laptop:
if photo_flag == False:
    dd "That's Andrew's laptop."
    dd "It looks like it's running 'Dylan Andrew Adventure'."
    dd "If I touch it, I'm a little worried I'll explode, so let's not do that."
    dd "Oh, there's a photo tucked underneath it.  Let's see..."
    play sound "sfx-realization.ogg"
    dd "Hey!  It's a picture of us from the dorm ski trip to Tahoe.  Maybe he was using it as a drawing reference."
    show ev_photo with dissolve
    dd "We couldn't afford the skiing, but we had a great time making a snowman and messing around."
    #dd "Maybe this can prove he has friends if they try to paint him as a dangerous loner type."
    dd "Maybe this'll be useful somehow."
    $ photo_flag = True
else:
    dd "Yup, that's Andrew's laptop alright."
    dd "I already grabbed the photo I found underneath it."
jump search304

label safe_socket:
dd "It's an electrical outlet."
dd "I'm not jamming my fingers in it if that's what you were hoping."
dd "It would only be worth doing if I had a fork."
jump search304

label drawer304_1:
if chicken_flag == False:
    dd "I mostly just use the closet.  Let's see what Andrew leaves in here..."
    play sound "rubber_chicken.ogg"
    dd "Whoa!"
    # Rubber Chicken 2.wav by dogwomble -- https://freesound.org/s/475733/ -- License: Attribution 4.0
    show ev_chicken with dissolve
    dd "I should have guessed.  This drawer is stuffed full with rubber chickens."
    dd "Maybe I should take one."
    dd "After all, like Andrew always says, you never know when a rubber chicken will come in handy."
    $ chicken_flag = True
else:
    play sound "rubber_chicken.ogg"
    dd "Yup, still full of rubber chickens."
    dd "I already took one, though I'm not sure why."
jump search304

label drawer304_2:
dd "Alright, let's see what's in the middle drawer..."
dd "It's empty, except for a post-it note stuck on the bottom."
dd "It says 'note to self: buy more rubber chickens'."
jump search304

label drawer304_3:
if id_flag == False:
    dd "Let's see what's in the bottom drawer..."
    dd "Oh geez, it's like a million empty pistachio shells."
    dd "I guess this is where he puts the shells he doesn't leave in my shoes."
    dd "Yeah, he thinks the ol' pistachio shells in your roommate's shoes routine is just as funny the thirtieth time."
    dd "Hmmm, but it looks like something is sticking out of the pile..."
    play sound "sfx-realization.ogg"
    dd "Hey!  It's his ID card.  He's been missing this for a while."
    show ev_id with dissolve
    dd "Wow, what a handsome guy."
    dd "The info on the card might be useful during the trial."
    $ id_flag = True
elif pistachio_count < 23:
    if pistachio_count == 0:
        dd "It's just filled with pistachio shells now."
        dd "Oh nice, I found one that wasn't cracked yet."
        play sound "pistachio.ogg"
        dd "*cracks pistachio open*"
        dd "Delicious!"
        $ pistachio_count += 1
        "You have eaten 1 pistachio!"
    else:
        dd "I found another pistachio!"
        play sound "pistachio.ogg"
        dd "*cracks pistachio open*"
        dd "Delicious!"
        $ pistachio_count += 1
        "You have eaten [pistachio_count] pistachios!"
else:
    dd "I can't eat any more pistachios."
    dd "My doctor has me on a strict 'only eat fewer than 24 pistachios per drawer per day' diet."
jump search304

label window304:
dd "There are more cop cars out there, but their sirens are off now."
dd "I should get out of here soon before they arrest me for breaking the Sphinx's nose off."
jump search304

label search_304over:
scene bg 304
$ default_mouse = "default"
if pistachio_count == 1:
    dd "I think I found everything potentially useful in here, and I ate at least one pistachio, so it's time to bounce."
else:
    dd "I think I found everything potentially useful in here, and I ate [pistachio_count] pistachios, so it's time to bounce."
dd "Maybe I should check if any of the random objects we taped to the outside of our door would come in handy."
scene bg 304 door with dissolve
jump search_304door

# ---Beeprints Legit
screen room304door_imagemap:
    imagemap:
        auto "bg_304_door_%s.png "
        hotspot (423, 182, 51, 30) action Return("flaggy") mouse "magnify_gold"
        hotspot (332, 181, 51, 32) action Return("flaggy") mouse "magnify_gold"
        hotspot (393, 182, 20, 100) action Return("flaggy") mouse "magnify_gold"
        hotspot (222, 231, 68, 81) action Return("flyer304") mouse "magnify_gold"
        hotspot (412, 284, 61, 38) action Return("goldstar") mouse "magnify_gold"
        #hotspot (401, 344, 79, 85) action Return("bigblue") mouse "magnify_gold"
        #hotspot (324, 319, 46, 61) action Return("lowgreen") mouse "magnify_gold"
        #hotspot (343, 263, 40, 48) action Return("loworange") mouse "magnify_gold"
        #hotspot (321, 220, 43, 27) action Return("lowpink") mouse "magnify_gold"
        #hotspot (447, 224, 34, 21) action Return("smallgreen") mouse "magnify_gold"
        #hotspot (424, 111, 46, 40) action Return("tallblue") mouse "magnify_gold"
        hotspot (324, 73, 78, 58) action Return("tallgold") mouse "magnify_gold"
        hotspot (121, 114, 157, 101) action Return("bigbrown") mouse "magnify_gold"
        hotspot (511, 50, 169, 129) action Return("biggreen") mouse "magnify_gold"
        #hotspot (184, 323, 106, 79) action Return("lowbigpurple") mouse "magnify_gold"
        #hotspot (554, 191, 57, 72) action Return("bigpink") mouse "magnify_gold"
        
init:
    $ flag_flag = False
    $ poster_count = 0
    
label search_304door:
$ default_mouse = "magnify_blue"
scene bg 304 door
if flag_flag == True and poster_count > 2:
    jump search_304doorover
window hide None
call screen room304door_imagemap
window show None
if _return == "flaggy":
    jump flaggy
if _return == "flyer304":
    jump flyer304
if _return == "bigbrown":
    jump doge_poster
if _return == "biggreen":
    jump dino_poster
if _return == "tallgold":
    jump adam_poster
if _return == "goldstar":
    jump goldstar
    
label flaggy:
play sound "sfx-realization.ogg"
dd "It's the Room 304 declaration of independence and a pair of official Room 304 flags."
show ev_flag with dissolve
dd "Yeah, our declaration is written on toilet paper."
dd "Andrew mentioned earlier that whoever entered our room to mess with our chocolate walrus 'violated Room 304's sovereignty'."
dd "Maybe there's some sort of legal argument I can make with this stuff."
$ flag_flag = True
jump search_304door2

label flyer304:
dd "That's an official Room 304 flyer."
show poster_304 with dissolve
dd "You can take another look at it, I guess."
$ poster_count += 1
jump search_304door

label doge_poster:
dd "It's a poster of a bunch of doge faces Andrew put up."
show poster_doge with dissolve
dd "I don't think there's any hidden meaning here."
$ poster_count += 1
jump search_304door

label dino_poster:
dd "It's a poster of a still frame from that Italian dinosaur cartoon."
show poster_dino with dissolve
dd "Ya know, the one where this dinosaur goes 'boop boop boop boop'?"
dd "And the other one goes 'yee'?"
dd "No?"
dd "I swear it was all the rage back in 2016."
$ poster_count += 1
jump search_304door

label adam_poster:
dd "It's a poster we made to poke fun at Adam, good-natured of course."
show poster_adam with dissolve
#dd "He really dislikes the Minion™ franchise."
dd "I don't think Andrew's pixel art captures his likeness very well, if I'm being honest."
$ poster_count += 1
jump search_304door

label goldstar:
dd "It's a foil star my a cappella group put on our door when they rolled me out."
show poster_star with dissolve
dd "It's not particularly amusing, but it would have been inaccurate to leave out."
$ poster_count += 1
jump search_304door






# ---Beeprints Legit
screen room304door2_imagemap:
    imagemap:
        auto "bg_304_doo2r_%s.png "
        #hotspot (423, 182, 51, 30) action Return("flaggy") mouse "magnify_gold"
        #hotspot (332, 181, 51, 32) action Return("flaggy") mouse "magnify_gold"
        #hotspot (393, 182, 20, 100) action Return("flaggy") mouse "magnify_gold"
        hotspot (222, 231, 68, 81) action Return("flyer3042") mouse "magnify_gold"
        hotspot (412, 284, 61, 38) action Return("goldstar2") mouse "magnify_gold"
        #hotspot (401, 344, 79, 85) action Return("bigblue") mouse "magnify_gold"
        #hotspot (324, 319, 46, 61) action Return("lowgreen") mouse "magnify_gold"
        #hotspot (343, 263, 40, 48) action Return("loworange") mouse "magnify_gold"
        #hotspot (321, 220, 43, 27) action Return("lowpink") mouse "magnify_gold"
        #hotspot (447, 224, 34, 21) action Return("smallgreen") mouse "magnify_gold"
        #hotspot (424, 111, 46, 40) action Return("tallblue") mouse "magnify_gold"
        hotspot (324, 73, 78, 58) action Return("tallgold2") mouse "magnify_gold"
        hotspot (121, 114, 157, 101) action Return("bigbrown2") mouse "magnify_gold"
        hotspot (511, 50, 169, 129) action Return("biggreen2") mouse "magnify_gold"
        #hotspot (184, 323, 106, 79) action Return("lowbigpurple") mouse "magnify_gold"
        #hotspot (554, 191, 57, 72) action Return("bigpink") mouse "magnify_gold"
        
init:
    $ flag_flag = False
    $ poster_count = 0
    
label search_304door2:
$ default_mouse = "magnify_blue"
scene bg 304 door2
if flag_flag == True and poster_count > 2:
    jump search_304doorover
window hide None
call screen room304door2_imagemap
window show None
#if _return == "flaggy":
#    jump flaggy
if _return == "flyer3042":
    jump flyer3042
if _return == "bigbrown2":
    jump doge_poster2
if _return == "biggreen2":
    jump dino_poster2
if _return == "tallgold2":
    jump adam_poster2
if _return == "goldstar2":
    jump goldstar2
    

label flyer3042:
dd "That's an official Room 304 flyer."
show poster_304 with dissolve
dd "You can take another look at it, I guess."
$ poster_count += 1
jump search_304door2

label doge_poster2:
dd "It's a poster of a bunch of doge faces Andrew put up."
show poster_doge with dissolve
dd "I don't think there's any hidden meaning here."
$ poster_count += 1
jump search_304door2

label dino_poster2:
dd "It's a poster of a still frame from that Italian dinosaur cartoon."
show poster_dino with dissolve
dd "Ya know, the one where this dinosaur goes 'boop boop boop boop'?"
dd "And the other one goes 'yee'?"
dd "No?"
dd "I swear it was all the rage back in 2016."
$ poster_count += 1
jump search_304door2

label adam_poster2:
dd "It's a poster we made to poke fun at Adam, good-natured of course."
show poster_adam with dissolve
#dd "He really dislikes the Minion™ franchise."
dd "I don't think Andrew's pixel art captures his likeness very well, if I'm being honest."
$ poster_count += 1
jump search_304door2

label goldstar2:
dd "It's a foil star my a cappella group put on our door when they rolled me out."
show poster_star with dissolve
dd "It's not particularly amusing, but it would have been inaccurate to leave out."
$ poster_count += 1
jump search_304door2






label search_304doorover:
dd "Okay, I should probably get out of here now."





# -----Ace Lawyer Guy Animations

# Judge
init:
    image judge warn:
        "court_judge_norm1"
        pause 0.2
        "court_judge_norm2"
        pause 0.2
        "court_judge_norm3"
        pause 0.2
        "court_judge_norm2"
        pause 0.2
        repeat
        
    image judge surp:
        "court_judge_surprised1"
        pause 0.2
        "court_judge_surprised2"
        pause 0.2
        "court_judge_surprised3"
        pause 0.2
        "court_judge_surprised2"
        pause 0.2
        repeat
        
    image judge norm:
        "court_judge_warning1"
        pause 0.2
        "court_judge_warning2"
        pause 0.2
        "court_judge_warning3"
        pause 0.2
        "court_judge_warning2"
        pause 0.2
        repeat
        
    image pros norm:
        "court_pros_norm1"
        pause 0.2
        "court_pros_norm2"
        pause 0.2
        "court_pros_norm3"
        pause 0.2
        "court_pros_norm4"
        pause 0.2
        "court_pros_norm2"
        pause 0.2
        repeat
        
    image pros con:
        "court_pros_con1"
        pause 0.2
        "court_pros_con2"
        pause 0.2
        "court_pros_con3"
        pause 0.2
        "court_pros_con4"
        pause 0.2
        "court_pros_con5"
        pause 0.2
        repeat
        
    image pros nerv:
        "court_pros_nerv1"
        pause 0.2
        "court_pros_nerv2"
        pause 0.2
        "court_pros_nerv3"
        pause 0.2
        "court_pros_nerv4"
        pause 0.2
        repeat
        
    image pros obj:
        "court_pros_obj1"
        pause 0.08
        "court_pros_obj2"
        pause 0.08
        "court_pros_obj3"
        
    image defe slam:
        #"court_dylan_slam1"
        #pause 0.2
        "court_dylan_slam2"
        pause 0.2
        "court_dylan_slam3"
        pause 0.2
        "court_dylan_slam4"
        pause 0.2
        "court_dylan_slam5"
        pause 0.2
        "court_dylan_slam6"
        pause 0.2
        
    image defe slamt:
        "court_dylan_slam6"
        pause 0.2
        "court_dylan_slamtalk1"
        pause 0.2
        "court_dylan_slamtalk2"
        pause 0.2
        "court_dylan_slamtalk1"
        pause 0.2
        repeat
        
    image defe norm:
        "court_dylan_norm1"
        pause 0.2
        "court_dylan_norm2"
        pause 0.2
        "court_dylan_norm3"
        pause 0.2
        "court_dylan_norm2"
        pause 0.2
        repeat
        
    image defe paper:
        "court_dylan_paper1"
        pause 0.2
        "court_dylan_paper2"
        pause 0.2
        "court_dylan_paper3"
        pause 0.2
        "court_dylan_paper2"
        pause 0.2
        repeat
        
    image defe think:
        "court_dylan_think1"
        pause 0.35
        "court_dylan_think2"
        pause 0.35
        "court_dylan_think3"
        pause 0.35
        repeat

scene bg court d
show defe slam
pause 1.2
show defe slamt
dd "BEES"
show defe norm
dd "BEES"
show defe paper
dd "BEES"
show defe think
dd "BEES"
        
scene bg court j
show judge norm
jj "BEEES"
show judge surp
jj "BEEES"
show judge warn
jj "BEEES"

scene bg court p
show pros norm
pp "BEES"
show pros con
pp "BEES"
show pros nerv
pp "BEES"
show pros obj
pp "BEES"

