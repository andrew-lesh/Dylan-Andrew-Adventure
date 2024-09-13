# You can place the script of your game in this file.
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Declare characters used by this game.

image confetti 1 = anim.Filmstrip("confetti.png", (20, 20), (2, 1), .15)
image snowblossom 2 = SnowBlossom("confetti")

# Disable annoying developer/director thing that messes with wasd movement in JRPG
python:
    config.keymap['director'].remove('d')

# Room 304 Flyer Viewport Code
screen viewport_screen:

    viewport:
        scrollbars "both"
        xmaximum 400
        ymaximum 518

        side_xpos 200
        side_ypos 10
        side_spacing 5

        draggable True
        mousewheel True

        add "Room_304_Flyer_Small.png"

    textbutton _("Dismiss"):
        xpos 0.5
        xanchor 0.5
        ypos 570
        yanchor 0.5

        action Return(True)

# Ghost of President Herbert Hoover Pong Code
init:

    image bg pong field = "pong_field.png"

    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # Some displayables we use.
                self.paddle = Image("pong.png")
                self.ball = Image("pong_ball.png")
                self.player = Text(_("Player"), size=36)
                self.Hoover = Text(_("Ghost of Herbert Hoover"), size=36)
                self.ctb = Text(_("Lol pong sux"), size=10)

                # The sizes of some of the images.
                self.PADDLE_WIDTH = 8
                self.PADDLE_HEIGHT = 79
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 108
                self.COURT_BOTTOM = 543

                # If the ball is stuck to the paddle.
                self.stuck = True

                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # The speed of the computer.
                self.computerspeed = 350.0

                # The position, dental-position, and the speed of the
                # ball.
                self.bx = 88
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 300.0

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.Hoover, self.ctb ]

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Move the computer's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                # Handle bounces.

                # Bounce off of top.
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("pong_beep.wav", channel=0)

                # Bounce off bottom.
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("pong_beep.wav", channel=0)

                # This draws a paddle, and checks for bounces.
                def paddle(px, py, hotside):

                    # Render the paddle image. We give it an 800x600 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, 800, 600, st, at)

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                        hit = False

                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True

                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True

                        if hit:
                            renpy.sound.play("pong_boop.wav", channel=1)
                            self.bspeed *= 1.10

                # Draw the two paddles.
                paddle(68, self.playery, 68 + self.PADDLE_WIDTH)
                paddle(724, self.computery, 724)

                # Draw the ball.
                ball = renpy.render(self.ball, 800, 600, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))

                # Show the player names.
                player = renpy.render(self.player, 800, 600, st, at)
                r.blit(player, (20, 25))

                # Show Eileen's name.
                Hoover = renpy.render(self.Hoover, 800, 600, st, at)
                ew, eh = Hoover.get_size()
                r.blit(Hoover, (790 - ew, 25))

                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.ctb, 800, 600, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (400 - cw / 2, 30))


                # Check for a winner.
                if self.bx < -200:
                    self.winner = "Ghost of Herbert Hoover"

                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)

                elif self.bx > 1000:
                    self.winner = "player"
                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Handles events.
            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y

                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()







# Spinning Button Code
init python:
    def button_transform(t, st, at):
        t.rotate = (90 * st) % 360.0
        return 0
        
# Spinning Reagan Code
init python:
    def logo_transform(t, st, at):
        st = st % 7.0
        done = min(st / 5.0, 1.0)
        t.xpos = done
        t.xanchor = 1.0 - done
        t.ypos = .5
        t.yanchor = .5
        t.rotate = 360 * done
        t.alpha = 1.0 - done
        t.zoom = 1.0  + done

        return 0
        
# Spinning Floppy Code
init python:
    def floppy_transform(t, st, at):
        st = st % 7.0
        done = min(st / 5.0, 1.0)
        t.xpos = done
        t.xanchor = 1.0 - done
        t.ypos = .5
        t.yanchor = .5
        t.rotate = 360 * done
        t.zoom = 1.0  + done

        return 0
        
# First Stanford Image Map
screen demo_imagemap:
    imagemap:
        auto "galaxy_%s.png"

        hotspot (330, 459, 260, 66) action Return("stanford") alt "Stanford"
        
# Second Stanford Image Map
screen weber_imagemap:
    imagemap:
        auto "weber_%s.png"

        hotspot (174, 41, 195, 129) action Return("dangit") alt "Dangit"
        
# Transitions
init:
    $ teleport = MultipleTransition([False, dissolve, "#fff", dissolve, False, 
                                     dissolve, "#fff", dissolve,
                                     True, dissolve, "#fff", dissolve, True])

# Character Voices
init:
    $ renpy.music.register_channel("blips", mixer=None, loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)


init python:
    def d_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_papyrus.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")

init python:
    def a_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_asgore.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
init python:
    def cp_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_alphys.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
            
init python:
    def cop_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_metta_1.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
        
init python:
    def navy_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_metta_3.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
            
init python:
    def internet_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_metta_4.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
            
init python:
    def king_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_asriel.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
            
init python:
    def reagan_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("bonzodoe.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
            
init python:
    def reagan2_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("BONZO.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
init python:
    def virgil_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_undyne.wav", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
                        
            
             
# Character Definitions
define d = Character('Dylan', color="#00f9ff", callback=d_voice)
define ad = Character('Dylan-senpai', color="#00f9ff", callback=d_voice)
define a = Character('Andrew', color="#51e130", callback=a_voice)
define aa = Character('Andrew-san', color="#51e130", callback=a_voice)
define cp = Character('Comrade Pichael', color ="#ff0000", callback=cp_voice)
define n = Character('Narrator', color ="#000000")
define cop = Character('Cop Dude', color ="#0045ff", callback=cop_voice)
define navy = Character('The Navy', color ="#acbce5", callback=navy_voice)
define king = Character('King of Bhutan', color ="#62c8d0", callback=king_voice)
define internet = Character('The Internet', color ="#2fff00", callback=internet_voice)
define ghostbusters = Character('Ghostbusters', color ="#ffffff", callback=virgil_voice)
define r2 = Character('Reaghost', color ="#d83000", callback=reagan_voice)
define r = Character('Ghost of Ronald Reagan AKA Reaghost', color ="#d83000", callback=reagan2_voice)
define h = Character('Ghost of Herbert Hoover', color = "#b37400", callback=cop_voice)
define b = Character('Chibee', what_font="LinLibertine_R.ttf", color ="#ffe700", callback=king_voice)
define sag = Character('Hypersexualized Anime Girl', color ="#ffc0cb", callback=navy_voice)
define v = Character('Virgil', color ="#bd47dd", callback=virgil_voice)
define demon = Character('Y̵o҉̟̦̭̼̤̥g-̺͍̠̙̲Ś̮̘̥̳̬̻̰o̹̣͈͔̫͉͘h̛̥̘͙̺̯̼o͏t̬͍̤h͎̯̠̘͍', color ="#c50202", callback=cp_voice)
define homer = Character('Homer', color ="#0092ff", callback=internet_voice)
define rumi = Character('Jalal ad-Din Muhammad Rumi', color ="#df7fb9", callback=cop_voice)
#define rumi = Character('Jalal ad-Din Muhammad Rumi', what_font="LinLibertine_R.ttf", color ="#df7fb9", callback=cop_voice)
define shakespeare = Character('William Shakespeare', color ="#f4c500", callback=navy_voice)
define poe = Character('Edgar Allen Poe', color ="#a54c36", callback=cp_voice)
define shel = Character('Shel Silverstein', color ="#0c96ea", callback=king_voice)
define game = Character(' ', color ="#0c96ea")
define plutus = Character('Plutus', color ="#ff0000", callback=internet_voice)
define phlegyas = Character('Phlegyas', color ="#ffffff", callback=navy_voice)
define p = Character(' ', what_font="Pokemon GB.ttf", color ="#ffffff")
define be = Character('Lucipher', color ="#ff0000")

# , what_font="LinLibertine_R.ttf"

# --- CHARACTER IMAGES ---

# Dylan Images
image d happy = "d_hap.png"
image d happy t = "d_hap_talk.png"
image d norm = "d_norm.png"
image d norm t = "d_norm_talk.png"
image d mad = "d_mad.png"
image d mad t = "d_mad_talk.png"
image d stern = "d_stern.png"
image d stern t = "d_stern_talk.png"

# Andrew Images
image a happy = "a_hap.png"
image a happy t = "a_hap_talk.png"
image a norm = "a_norm.png"
image a norm t = "a_norm_talk.png"
image a mad = "a_mad.png"
image a mad t = "a_mad_talk.png"
image a stern = "a_stern.png"
image a stern t = "a_stern_talk.png"

# Dylan-senpai Images
image ad happy = "ad_hap.png"
image ad happy t = "ad_hap_t.png"
image ad norm = "ad_norm.png"
image ad norm t = "ad_norm_t.png"
image ad stern = "ad_stern.png"
image ad stern t = "ad_stern_t.png"
image ad ppbt = "ad_ppbt.png"
image ad bleh = "ad_bleh.png"
image ad rage = "ad_angry.png"
image ad vein = "ad_angry_vein.png"
image ad spin = "ad_angry_vein_spin.png"

# Andrew-san Images
image aa happy = "aa_hap.png"
image aa happy t = "aa_hap_t.png"
image aa norm = "aa_norm.png"
image aa norm t = "aa_norm_t.png"
image aa stern = "aa_stern.png"
image aa stern t = "aa_stern_t.png"
image aa ppbt = "aa_ppbt.png"
image aa bleh = "aa_bleh.png"

# Virgil Images
image v = "virgil_silent.png"
image v t = "virgil_talk.png"
image v norm = "virgil_norm.png"
image v norm t = "virgil_norm_t.png"
image v happy = "virgil_hap.png"
image v happy t = "virgil_hap_t.png"

# Limbo Images
image homer = "limbo_homer_norm.png"
image rumi = "limbo_rumi_norm.png"
image shakespeare = "limbo_shakespeare_norm.png"
image poe = "limbo_poe_norm.png"
image shel = "limbo_shel_norm.png"

# Comrade Pichael Images
image cp norm = "cp_norm.png"
image cp norm t = "cp_norm_talk.png"

# Reagan Images
image r norm = "reagan_norm.png"
image r cinnamon = "reagan_norm_crop.png"

# Hoover Images
image h norm = "hooverhead.png"

# Apple II Images
image ii off = "images.duckduckgo.png"
image ii start = "images.duckduckgo.startup.png"
image ii smile = "images.duckduckgo.smiley.png"
image ii read = "images.duckduckgo.floppy.png"
image ii crabs = "images.duckduckgo.crabs.png"
image ii find = "images.duckduckgo.document.png"
image ii printing = "images.duckduckgo.printing.png"
image ii bye = "images.duckduckgo.bye.png"

# Bee Images
image b hap = "bee_1.png"
image b yell = "bee_3.png"
image b look = "bee_6.png"
image byar = "bee_4.png"
image byar noseeum = "beenime3_noseeum.png"
image b sarcastic = "bee_2.png"
image b sexy = "bee_5.png"
image b horror = "horror-bee.png"

# DEEéMON Images
image lovecraft = "mon_lovecraft.png"
image rival1 = "mon_rival1.png"
image rival2 = "mon_rival2.png"
image rival3 = "mon_rival3.png"
image rival4 = "mon_rival4.png"
image rival5 = "mon_rival5.png"
image pika = "mon_pikathulhu.png"
image trainer1 = "mon_trainer1.png"
image trainer2 = "mon_trainer2.png"
image trainer3 = "mon_trainer3.png"
image trainer4 = "mon_trainer4.png"
image lovebat = "deeemon_lovecraft_battle.png"
image pikabat = "deeemon_pikathulhu_battle.png"
image pikacatch = "deeemon_pikathulhu_catch.png"
image trainbat = "deeemon_trainer_battle.png"
image victim = "deeemon_victim.png"
image victim_text = "deeemon_victim_text.png"
image pika_text = "deeemon_pikathulhu_catch_text.png"
image pikabat_text = "deeemon_pikathulhu_battle_text.png"
image pikabat_text2 = "deeemon_pikathulhu_battle_text_2.png"
image pentaspell = "deeemon_penta.png"
image orb = "deeemon_orb.png"
image orbl = "deeemon_orb_left.png"
image orbr = "deeemon_orb_right.png"
image orbc = "deeemon_orb_full.png"
image trainenemy = "deeemon_enemytrainer_battle.png"
image ghatbat = "deeemon_ghat_battle.png"
image ghat_text = "deeemon_ghat_battle_text.png"
image ball_train = "deeemon_oneball_trainer.png"
image ball_enemy = "deeemon_oneball_enemy.png"
image ball_full = "deeemon_orb_full.png"

# Misc. Images
image floppy = "floppy.png"
image honey = "honey.png"
image beeprints = "blueprints.png"
image scary anime girl = "scary_anime_girl.png"
image hellboy = "heendadeen.png"
image quit = "quit.png"

# Don't worry Bill Murray
image 1bill = "billbill.png"
image 6bill = "billmageddon.png"

# --- BACKGROUNDS ---
image bg 304 = "bg_room_304_dingus.png"
image bg 304 dingus = "bg_room_304.png"
image bg hoover = "hootow.jpeg"
image bg hooverinside = "hootervower.jpeg"
image bg beeprints = "blueprints_screen.jpeg"
image bg 304 beeprints = "bg_room_304_beeprints.png"
image bg cherry = "bg_blossoms_1.png"
image bg jrpg-start = "jrpg-start.png"
image bg daatalescreen = "daatale-screen.png"
image bg eternity = "LDN_622.jpg"


# The game starts here.

label start:
    # $ save_name = "Twas brillig, and the slithy toves"
    play music "Automation.mp3"
    scene bg 304 dingus
    with dissolve
    d "Hey.  How's it going?"
    show d happy t
    with dissolve

    d "My name is Dylan."

    d "And this–"
    show a happy
    with dissolve
    
    d "is my best buddy and roommate Andrew."
    show a happy t
    show d happy
       
    a "What's up, Dylan?  Talking to the air again?"
    show d norm t
    show a happy
    
d "Huh?  Oh, no.  I was just introducing the player to us."
show a norm t
show d happy
a "Wuh?"
show d happy t
show a happy
d "You know, the player of our adventure game."
show d happy
show a happy t
a "Wait.  You mean somebody actually downloaded and is currently running 'Dylan Andrew Adventure'?"
show d happy t
show a happy
d "Yep!"
show d happy
show a happy t
a "Wow.  That's pretty cool considering that it's basically a flaming pile of garbage."
show d stern t
show a happy
d "Jeez.  Way to sell our game, dude."
show a happy t
show d stern
a "Hey, I'm just being honest.  The player deserves to know after paying the $60.00 price tag."
show d norm t
show a happy
d "This game is free."
show a norm t
show d norm
a "What?!  Then how are we going to make any money?"
show d norm t
show a norm
d "We're not."
show d norm
show a happy t
a "Oh, right."
show d happy t
show a happy
d "Anyway, welcome to our dorm room, player.  Room 304!"  
show a happy t
show d happy
a "This is where we eat and sleep!"
show d happy t
show a happy
d "Sometimes we even do work in here."
show d happy
show a happy t
a "But not really.  We basically just watch YouTube videos and slack off."
show d norm
show a norm
a "..."
show d happy
show a happy t
a "This is where we watch YouTube videos and slack off!"
show d happy t
show a happy
d "Well, I guess we need a conflict or else we don't have much of a game, right?"

d "Adam Forsyth from the first floor took my dinosaur bowl a couple days ago and still hasn't returned it."
show d happy
show a norm t
a "Then how have you been eating your instant oatmeal?"
show d happy t
show a norm
d "I've just been holding it in my hands."
show a norm t
show d happy
a "Makes sense."
show d happy t
show a happy
d "So I was thinking the player could go ask Adam for it back!  What do you think, player?"

show d happy
menu:
    "Okay!":
        jump okay
    "No.  That sounds boring and lame.":
        jump lame
        
label okay:
    
    show d happy t
    d "Great!  Let's go get it before we get distracted by something."
    jump huh
    
    
label lame:
    show d happy t
    d "Well, uh...  Did you program any other conflicts, Andrew?"
    show d happy
    show a happy t
    a "Nope.  That would have taken time and effort."
    show d happy t
    show a happy
    d "In that case, you're stuck retrieving my dinosaur bowl, player."
    show d mad t     
    d "You ungrateful swine."
    jump huh
    
    
label huh:
play music "Soviet 8-bit.mp3"
show d norm
show a norm t
a "Huh?  What's that music?"
show d stern t
show a norm
d "Andrew, have you been sympathizing with communists again?"
show d stern
show a stern t
a "Come on, dude.  I barely went to one party meeting."
show a norm
d "..."
show a norm t
a "Okay.  Five party meetings."
show a norm
d "..."
show a norm t
a "Hey!  They had free pizza and I was out of meal plan dollars, okay?"
show d norm
show a norm
show cp norm t 
with dissolve

cp "Greetings, comrades!"

show cp norm
show a stern t   
a "Get out of here, Pichael."
show a stern
show cp norm t

cp "I think not, comrade." 

show cp norm
show d norm t
d "His name is 'Pichael'?"
   
d "Is that like 'Michael', but with a 'P'?"
show d norm
show a stern t
a "Yep."
show d norm t
show a stern
d "That's dumb."
show d norm
show a stern t
a "What do you want, Pichael?"
show a stern
show cp norm t

cp "Well, comrade Andrew, since you haven't been replying to our Myspace messages, I was required to find you in person."
show cp norm
show a stern t
a "Why?"
show cp norm t
show a stern
cp "Because I have to tell you our big secret plan, comrade!"
show cp norm
show d norm t
d "To do what?"
show d norm
show cp norm t
cp "To ignite the will of the people and begin the world revolution, comrade!"
show cp norm
show a norm t
a "What?"
show a norm
show cp norm t
cp "We are going to flood this bourgeois institution with Mountain Dew™, thereby inspiring the masses to rise up against the filthy capitalist elite ruling this planet..."
show a norm
cp "comrade."
show cp norm
show d norm t
d "That's a really bad idea."
show d norm
show a norm t
a "Are you serious?"
show cp norm t
show a norm
cp "Certainly, comrade.  This is a serious matter.  The Party is lining Stanford's steam tunnels with Mountain Dew™ barrels as we speak."
show cp norm
show d stern t
d "That's dumb."
show d stern
show a stern t
a "Why is your plan so dumb?"
show a stern
show cp norm t
cp "Because, comrade, nobody will believe you if you tell them what it is!"
cp "'Oh, the communists are going to begin the world revolution by flooding what is arguably the world's most prestigous research institution with the soda that everyone makes fun of on the internet?'"
cp "'Yeah, right!'"
cp "It is the perfect plan, comrade!"
show cp norm
show a stern t
a "Well, we're calling the cops anyway, dude."
show d stern t
show a stern
d "Let's hold him down!"
show d stern
show cp norm t
cp "I'm disappointed that you've lost your revolutionary spirit, comrade Andrew.  But very well."
cp "Toodaloo, comrades.  Pichael away!"
hide cp stern t
with fade
show d norm t
stop music fadeout 1.0
play music "Automation.mp3"
d "Maybe we should have closed the door."
show d norm
show a norm t
a "I'll add that to our list of things to remember."
show a happy t
a "As soon as I remember where I put it."
show a happy
show d norm t
d "Anyway, we should call the cops now, right?"
show a happy t
show d norm
a "I guess so.  Hopefully they'll believe us."
show d norm t
show a happy
d "Do you at least remember the campus police station's number?"
show d norm
show a happy t
a "Yeah.  It's 1-800-PO-LICE, right?"
show d norm t
show a happy
d "That sounds right.  I'll dial."
show d norm
stop music
d "..."
play music "Automation.mp3"
show d norm t
d "There's something wrong with the phone.  I can't even hear a dial tone."
show a norm 
show d norm
a "Hmm."
show a happy
show d happy t
play music "_Speedball_ title music, Atari ST 1.mp3"
d "Wait!  This is the perfect opportunity for user interaction!"
show d happy
show a happy t
a "Yeah!  Can you repair our phone, o wise player?"
show d happy t
show a happy 
d "O courageous and godlike player?"
show a happy t
show d happy
a "I know what we're asking of you is frightening, but you have to do it."
a "You just have to find the resolve in your heart and persevere."
show d happy t
show a happy
d "You just have to believe in yourself!  You can do it!"
show a happy t
show d happy
a "Do it, player.  DO IT TO DEFEAT COMMUNISM!"
show d happy t
show a happy
d "DO IT TO ACHIEVE YOUR DESTINY AS SAVIOR OF THE HUMAN RACE!"
show d happy
menu:
    "You guys plugged the phone into a power socket instead of a phone jack.":
        jump oh
    "You dingalings plugged the phone into a power socket instead of a phone jack.":
        jump offensive

label offensive:
stop music
show d mad t
show a stern
d "Hey.  That term is very offensive."
show d mad
show a stern t
a "Yeah.  We each personally identify as a 'dingus'."
show d mad t
show a stern
d "We show you the courtesy of accepting you into our own dorm room and this is the thanks we get?"
d "Get your labels straight and try again.  And show some respect.  This is your only warning."
jump dingus
show d stern
show a stern

label dingus:
show d stern
play music "_Speedball_ title music, Atari ST 1.mp3"
menu:
    "You dinguses plugged the phone into a power socket instead of a phone jack.":
        jump respect
        
label respect:
stop music
show d stern t
d "Thank you for your sensitivity."
show a happy
show d happy t
d "Now where were we?"
jump victory

label oh:
show d norm t
show a norm
stop music
d "Oh."
show a happy t
show d happy
a "That explains why none of my friends have called me for the last year!"
show a norm t
a "...right?"
jump victory

label victory:
stop music
show d norm
show a norm
play sound "click sound.mp3"
n "Click!"
scene bg 304
with dissolve
show d norm t
show a norm
d "It works now."
show d happy t
show a happy
play music "Final Fantasy VII 11 Fanfare 8-BIT 1.mp3"
show snowblossom 1
show snowblossom 2
d "YOU'VE SAVED US ALL!"
show d happy
show a happy t
a "Player be praised!"
show d norm t
show a happy
d "Wait, where's the confetti?"
show d norm 
show a happy t
a "I couldn't find any."
a "Sorry."
show a happy
show d norm t
d "Oh, no problem, I guess."
show d stern t
d "Don't get cocky just because we tried to shower you in confetti, player."
play music "Automation.mp3"
hide snowblossom 1
hide snowblossom 2
show d happy
show a happy t
a "Time to call the cops!"
show a happy
show d happy t
d "On it!"
show d happy
play sound "phone ring sound.mp3"
n "Dialing..."
stop sound
cop "Stanford Police Department.  What's the situation?"
show d happy t
d "We'd like to report a threat to Stanford's security!"
show d happy
cop "Oh?  What is it?"
show d happy t
d "A bunch of communists are going to flood the campus with Mountain Dew™!"
show d happy
cop "Are you telling me that the communists are going to begin the world revolution by flooding what is arguably the world's most prestigous research institution with the soda that everyone makes fun of on the internet?"
show d norm
cop "Yeah, right!"
cop "Wait, this is Dylan and Andrew isn't it?"
show d norm t
d "Uhh..."
show d norm
play sound "hang up sound.mp3"
n "Click."
show d norm t
d "They hung up."
show d norm
show a norm t
a "They're probably still mad about the time we–"
show a norm
show d norm t
d "LET'S maybe not tell the player about that, alright?"
show d norm
show a happy t
a "Then who else should we call?"

label phone:
show a happy 
show d happy
menu:
    "Call the navy":
        jump navy
    "Call the internet":
        jump internet
    "Call Ghostbusters":
        jump bustin
    "Call the king of Bhutan":
        jump Bhutan
    "Stop calling":
        jump nocall
        
label navy:
play sound "phone ring sound.mp3"
n "Dialing..."
stop sound
navy "Yo ho ho, this is the navy.  How can we help you?"
show d happy t
d "I'd like to report a communist plot to destroy Stanford University."
show d happy
navy "Oh my goodness!  I'll warn the fleet admiral at once!"
show d norm
navy "Wait..."
navy "Are the communists on a boat?"
show d norm t
d "I don't think so."
show d norm
play sound "hang up sound.mp3"
n "Click."
jump phone

label internet:
play sound "AOL (Sign On - Dial Up).mp3"
n "ONLY 90'S KIDS WILL GET THIS AMIRITE XD XD XD ROTFLMAO"
jump AOL

label AOL:
play sound "AOL Mail Sound.mp3"
internet "Lol yur gmae so fayk n u smel bad"
show d norm t
d "What are you talking about?  This game is real and I smell quite nice!"
show d stern
play sound "AOL Mail Sound.mp3"
internet "u smel lyk a big fat losr nd Adrew alzo smel goat"
show d stern t
d "I already told you that I smell quite nice!" 
d "And Andrew smells only moderately goatish today!"
show d stern
show a stern t
a "Hey, man.  I have a condition."
show a happy
show d mad
play sound "AOL Mail Sound.mp3"
internet "if evlushin is IRL how come pistachios still exist? checkm8, athists!!"
show d mad t
d "I WILL TEAR OUT YOUR SPLEEN AND FEED IT TO MY CAT!"
show d mad
play sound "AOL Mail Sound.mp3"
internet "lol u mad~?"
show d mad t
d "I AM MAD, YES!  THAT SHOULD BE EVIDENT FROM THE VOLUME OF MY VOICE AND USE OF CAPS LOCK!"
show d mad
play sound "AOL Mail Sound.mp3"
internet "lol l8er"
play sound "hang up sound.mp3"
n "Clik, m8."
show a happy t
show d norm
a "Don't feed the trolls, Dylan."
a "Or talk to them over the telephone, apparently."
show a happy
show d happy
jump phone

label bustin:
play sound "phone ring sound.mp3"
n "Dialing..."
stop sound
show d happy
ghostbusters "You've reached the Ghostbusters.  How can we help you today?"
show d happy t
d "My college campus is currently being haunted by the spectre of communism!"
show d happy
ghostbusters "Then you've called the right place!"
show d norm
ghostbusters "Our standard service will cost thirty thousand dollars per Bill Murray per hour."
ghostbusters "How many Bill Murrays would you like us to send over?"
show d norm t
d "Uh... Could you please wait one moment?"
show d norm
ghostbusters "Take your time, valued customer!"
ghostbusters "Or should I say GHOST-omer?"
show a norm t
a "Probably not."
show a norm
show d norm t
d "Andrew!  The guy on the phone says their ghostbusting costs thirty thousand dollars per Bill Murray per hour."
show d norm
show a happy t
a "Nice."
show a happy
show d norm t
d "What do you mean?  There's no way we can afford this."
show d norm
show a happy t
a "Nonsense.  If I spend the twenty five dollars and thirty-three cents I have left in my college fund and you pawn that bag of oranges you bought at Walmart yesterday..."
a "We can afford one Bill Murray for 3.401 seconds or six Bill Murrays for 0.567 seconds!"
show a happy
show d norm t
d "Then how many Bill Murrays should we order?"
show d norm
menu:
    "Order one Bill Murray for 3.401 seconds":
        jump onebill
    "Order six Bill Murrays for 0.567 seconds":
        jump sixbills   
   
init:
    python:

        # This function will run a countdown of the given length. It will
        # be white until 5 seconds are left, and then red until 0 seconds are
        # left, and then will blink 0.0 when time is up.
        def countdown(st, at, length=0.0):
            remaining = length - st

            if remaining > 5.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=72)), None
                

    # Show a countdown for 10 seconds.
    image billdown1 = DynamicDisplayable(countdown, length=3.401)
    image billdown6 = DynamicDisplayable(countdown, length=0.6)


label onebill:
    show d norm t
    d "Uh, I'd like one Bill Murray for about 3.401 seconds, please."
    show d norm
    ghostbusters "You got it!"
    ghostbusters "Though I'm afraid I'll have to round that off to one decimal place for accounting purposes."
    show d norm t
    d "Seems reasonable."
    show d norm
    image debbie:
        "billbill.png"
        pause 3.4
        "nada.png"
    show debbie
    show billdown1 at Position(xalign=.1, yalign=.1)
    ghostbusters "That'll be twenty eight dollars and thirty-three cents."
    ghostbusters "Make the check out to Sony Pictures."
    play sound "hang up sound.mp3"
    n "Click."
    show d norm t
    d "I feel like that didn't work."
    hide billdown1
    show d norm
    jump phone
    
label sixbills:
    show d norm t
    d "Uh, I'd like six Bill Murrays for about 0.567 seconds, please."
    show d norm
    ghostbusters "You got it!"
    ghostbusters "Though I'm afraid I'll have to round that off to one decimal place for accounting purposes."
    show d norm t
    d "Seems reasonable."
    show d norm
    image beckie:
        "billmageddon.png"
        pause 0.6
        "nada.png"
    show beckie
    show billdown6 at Position(xalign=.1, yalign=.1)
    ghostbusters "That'll be twenty eight dollars and thirty-three cents."
    ghostbusters "Make the check out to Sony Pictures."
    play sound "hang up sound.mp3"
    n "Click."
    show d norm t
    d "I feel like that didn't work."
    hide billdown6
    show d norm
    jump phone
              
label Bhutan:
play sound "phone ring sound.mp3"
n "Dialing..."
stop sound
king "Hello there!  I am the king of Bhutan!  I am having a wonderful day! :)"
show d happy t
d "Hello, your majesty.  This is Dylan.  I'm glad you're having a wonderful day!"
show d happy
king "Thank you very much!  Nice to speak with you again, Dylan! :)"  
king "What can I do for you and Andrew?! :)"
show d happy t
d "We need help foiling a communist plot to flood Stanford University with Mountain Dew™."
show d happy
king "Oh no!  Those dang communists!  I'll be there as soon as I can! :)" 
king "I'm getting on my horse right now! :)"
show d happy t
d "Thank you, your majesty!"
show d happy
king "Hang in there, Dylan and Andrew!  I will see you soon! :)"
play sound "hang up sound.mp3"
n "Click."
show d happy t
d "The king of Bhutan will help us, but it sounds like it'll be a while."  
d "Riding a horse across the Pacific Ocean should take at least an hour or two."
show d happy
jump phone

label nocall:
show a happy t
a "Then I guess we'd better defeat communism by ourselves for now."
show a happy
show d norm t
d "That sounds like a lot of work."
show d norm
show a norm t
a "Fortunately communism has been almost entirely discredited through the failure of its supposed followers to establish a true Marxist state."
show a norm t
a "Since true communism has no national governments or borders, a communist state must be founded with the purpose of eventual self-dissolution and the collective authority of the proletariat superseding that of any government."  
show a norm t
a "This means those in power must voluntarily work to dismantle the entity giving them such power, making the existence of communist states paradoxical."  
show a norm t
a "Communism, a philosophy intended to give all humans a fair life with equal opportunities ultimately became just another way for the elite to justify arbitrary rule and mass cruelty."  
show a norm t
a "Karl Marx and Friedrich Engels roll in their graves.  They will never know their work to free humanity was hijacked to enslave us all."
show d happy t
show a norm
d "Lol."
show d happy
show a happy t
a "Get rekt."
show a happy
show d norm t
d "So what should we do to defeat the spectre of this obsolete worldview?"
show d norm
show a norm t
a "We must call upon the spectre of another obsolete worldview!"
show d norm t
show a norm
d "You don't mean..."
show d norm
show a norm t
a "Yes."
a "We must summon the ghost of Ronald Reagan."
show a norm
show d norm t
d "That sounds like a lot of work."
show d norm
show a happy t
a "I don't know.  Summoning ghosts is pretty easy in horror films.  Maybe we can use a ouija board or something."
show a happy
show d norm t
d "Nah, those don't work.  They just run off of the ideomotor effect.  People just reflexively act our their unconscious desires to communicate with the dead and spell out words without realizing it."
d "They're also made by Hasbro."
show a happy t
show d norm
a "Maybe we just say 'Tear down this wall' three times in front of a mirror with the lights turned off?"
show a happy
show d norm t
d "That wouldn't make sense either.  How can mirrors be real if our eyes aren't real?"
show d norm t
d "We need a spirit-summoning method based in cold hard science."
show d norm
show a happy t
a "What if I just code in a big spinning 'Summon the ghost of Ronald Reagan' button for the player to press?"
show d norm t
show a happy
d "Yeah, I guess that makes sense."
show d happy
show a happy t
a "Code code code.  Aaaand enter!"

with dissolve

python hide:
    ui.transform(function=button_transform, xalign=0.5, yalign=0.5)
    ui.textbutton(_("Cinammon the ghost of Ronald Reagan"), clicked=ui.returns(True))
jump cinnamon
            
label cinnamon:
show a happy t
a "Oops, autocorrect.  It should still work."

show a happy
play sound "cinnamon.wav"
show r cinnamon:
    alignaround (.5, .5)
    linear 2.0 xalign .5 yalign .2 clockwise circles 3

show d happy t
d "Wow, great ghost cinnamoning skills, player."
show d happy
r "Who dares cinnamon me?"
show a happy t
a "Just Dylan and Andrew, Mr. President."
show a happy
r "Oh, alright then.  What's the occasion, fellas?  Need some acting tips?"
show d norm t
d "Um, if you don't mind me asking, Mr. President, why are you shouting the word 'bonzo' at us?"
show d norm
r "An excellent question.  That's because I had the starring role in the 1951 family comedy movie 'Bedtime for Bonzo'."
r "I played a handsome psychologist who had to babysit a chimpanzee named Bonzo."
r "Roll the clip!"
$ renpy.movie_cutscene("reagan_is_an_actor.mpg")
show d norm t
d "Oh my God."
show d norm
show a happy t
a "That was without a doubt the best thing I've ever seen."
show a happy
r "And that's why I keep saying 'Bonzo Bonzo Bonzo'.  It's because I'm so proud.  Without a doubt the shining moment of my political career."
show a happy t
a "Don't you mean your acting career?"
show a happy
r "You would think so, but no.  Sometime you should listen to my famous speech where I asked my friend Mikhail Gorbachev to 'Bonzo down this wall'."
show d norm t
d "I don't think that's right."
show d norm
show a happy t
a "Come on, Dylan!  Don't you remember like one minute ago when I asked if we could cinnamon the ghost of Ronald Reagan by saying 'Bonzo down this wall' three times in front of a mirror with the lights turned off?"
show a happy
show d stern t
d "What?  No!  You said 'TEAR down this wall'!"
show d norm
r "I decided to let the Soviets dub over my speech and ruin my proudest moment so they could save face."
r "It's one of the compromises I made to end the Cold War and save humanity from nuclear annihilation."
r "You're welcome. Dylan."
show a stern t
a "Yeah, Dylan.  You're welcome."
show a stern
show d norm
d "..."
show a happy
r "Anyway, why did you guys cinnamon me today?  Did you want me to recite the script from one of my famous movies?"
show a happy t
a "You bet!"
show a happy
show d stern t
d "What?!  No!"
show d stern 
r "Then I'll give y'all a choice between my three personal favorites:  'Tugboat Annie Sails Again', 'Million Dollar Baby', and as previously mentioned, 'Bedtime for Bonzo'."
show d stern t
d "That's not why we cinnamoned you!"
show d stern
show a happy t
a "Can you give us a synopsis of each film to help us choose?"
show a happy
show d stern t
d "We're getting really off track, guys."
show d stern
r "Excellent idea!  In 'Tugboat Annie Sails Again', the 1940 sequel to 1933 smash hit 'Tugboat Annie', I play as a handsome sailor alongside Annie, played by Marjorie Rambeau, who is a tugboat captain that is forced to salvage an old boat by her arch nemesis, Captain Bullwinkle."
r "But it turns out that she was tricked and that the old boat is actually a whale!"  
show a happy t
a "Wow!  What a twist!"
show a happy
show d stern t
d "I don't think we have time for this guys."
show d stern
r "In 'Million Dollar Baby', a 1941 romantic comedy, I play a handsome boyfriend, piano player, and composer who must help actress Priscilla Lane starring as Pam McCallister claim her million dollar inheritance."
r "But it turns out that there was only seven hundred thousand dollars!  And I was the baby the whole time!"
show a happy t
a "Wow!  Another incredible twist!"
show a happy
show d mad t
d "We don't have time for th–"
show d mad
show a mad t
a "Stop talking over the President, Dylan.  It's rude."
show a stern
r "Yeah, Dylan.  It's rude.  I don't talk over you when your ghost gives synopses of three of his famous movies!"
show d norm
d "..."
show a happy
r "And in 'Bedtime for Bonzo', as I previously mentioned, I play as a handsome psychologist who has to babysit a chimpanzee named Bonzo."
r "But it turns out that the chimpanzee was a actually a whale the whole time!"
show a happy t
a "Wow!  You really were the greatest president."
show a happy
r "You betcha!  Now, brave American and/or not American patriot playing this game, which movie would you like me to read the entire script of?"

menu:
    "Tugboat Annie Sails Again (1940)":
        jump Bees
    "Million Dollar Baby (1941)":
        jump Bees
    "Bedtime for Bonzo (1951)":
        jump Bees
        
label Bees:
r "According to all known laws of aviation, there is no way a bee should be able to fly.  Its wings are too small to get its fat little body off the ground.  The bee, of course, flies anyway because bees don't care what humans think is impossible.  Yellow, black. Yellow, black.  Yellow, black. Yellow, black.  Ooh, black and yellow! Let's shake it up a little.  Barry! Breakfast is ready!  Coming!  Hang on a second.  Hello?  Barry?  Adam?  Can you believe this is happening?  I can't. I'll pick you up.  Looking sharp.  Use the stairs. Your father paid good money for those. Sorry. I'm excited.  Here's the graduate.  We're very proud of you, son.  A perfect report card, all B's.  Very proud.  Ma! I got a thing going here.  You got lint on your fuzz.  Ow! That's me!  Wave to us! We'll be in row 118,000.  Bye!  Barry, I told you, stop flying in the house!  Hey, Adam.  Hey, Barry.  Is that fuzz gel?  A little. Special day, graduation.  Never thought I'd make it.  Three days grade school, three days high school.  Those were awkward.  Three days college. I'm glad I took a day and hitchhiked around the hive.  You did come back different.  Hi, Barry.  Artie, growing a mustache? Looks good.  Hear about Frankie?  Yeah.  You going to the funeral?"

show d norm t
d "Isn't this the script to 'Bee Movie'?"
d "The 2007 computer animated film where comedian Jerry Seinfeld is a wisecracking bee?"
show d norm
show a norm t
a "The plot twist is that you, the player, live in a world where millions of dollars were spent producing an animated film where Jerry Seinfeld stars as a wisecracking bee."
a "The same world where millions of people go hungry whose lives could be saved with even small donations."
a "This is the world we live in, and you can't look away.  You can never escape the moral cowardice and greed that spawned 'Bee Movie'."
show d norm t
show a norm
d "Wow.  That's really dark."
show d norm
show a norm t
a "And you know as well as I do that it's true."
show a norm
r "I understand your confusion.  This is the movie I most wanted to show you, but I wanted there to be a good plot twist."
show d norm t
d "Oh, uh...  Okay."
show d norm 
r "I recorded my lines for this movie back in the eighties while I was still president."
show d norm t
d "Wait, what?"
show d norm
r "I had always wanted to play as a really unfunny version of Jerry Seinfeld playing a wisecracking bee, but the technology just wasn't there yet."
r "I knew it was what I had to do to defeat the Soviet Union and save humanity from nuclear annihilation."
r "The shock of the mere existence of 'Bee Movie' was what it took to wake up those living under communist oppression.  It's what finally got them to realize the moral cowardice and greed that was used to justify the authoritarian brutality of communism."
r "To realize that the perfect society Marx and Engels envisioned could never possibly exist in the same world that spawned 'Bee Movie.'"
r "You're welcome."
show d norm t
d "But 'Bee Movie' came out in 2007.  How could it have defeated the Soviet Union?"
show d norm
r "Dylan, I'm going to make this explanation as simple as possible."
r "When you look around, do you see any more Soviet Union?"
show d norm t
d "...No?"
show d norm
r "I rest my case."
show a happy t
a "Wow!  You really were the greatest president!"
show a happy
r "You betcha!"
r "Shall I continue reading?"
show d norm t
d "Actually, Mr. President, we cinnamoned you here for something else."
show d norm 
r "Really?  Something even more important than reading the entire script of 'Bee Movie'?"
show a happy t
a "Yeah.  We need your help to stop communists from destroying Stanford University."
show a happy 
r "What?  Again?!"
show d norm t
d "...Again?"
show d norm
r "You should have cinnamoned me sooner!  What are the details, boys?"
show d norm t
d "Uh, they're trying to ignite the world revolution by flooding the school with Mountain Dew™."
show d norm
r "So the communists are going to begin the world revolution by flooding what is arguably the world's most prestigous research institution with the soda that everyone makes fun of on the internet?"
r "My God."
r "It's the perfect plan.  I should have seen this coming when I was president."
r "Wait.  How did you find this out?"
show a happy t
a "One of them stopped by here to tell us and ran away."
show a happy
r "You let a known communist escape your grasp?"
show d norm t
d "Well, yeah.  We had to let him go so our adventure game could have a central conflict."
show d norm 
show a norm t
a "Wait, I thought fetching your dinosaur bowl was the central conflict."
a "I thought we let Pichael go because we're lazy and don't actually care about any of this."
show a norm
show d norm t
d "Oh, well yeah.  Mostly that."
show d norm
show a happy t
a "So what do we do, Mr. President?"
show a happy
r "There's only one thing we can do.  We have to remind the communists of the nihilistic horror of 'Bee Movie'."
r "When I was president, I prepared for the worse.  We drew up the plans for the ultimate weapon, but thank God, we never had to build it."
r "A massive mechanical bee suit, the likes of which the second world has never seen."
r "If the war began, I was to pilot that suit and force the communists to grasp the meaninglessness of this world mono y mono."
r "The local conservative thinktank, the Hoover Institute, was entrusted with a floppy disk bearing the blueprints to this weapon in case the communists regrouped."
r "Unfortunately, I fear that the modern conservative movement is too distracted to realize the threat of the communists forgetting the nihilistic horror of 'Bee Movie'."
r "You boys must travel there under cover of darkness and copy that floppy."
show d norm t
d "So we have to break into Hoover tower to retrieve a copy of the blueprints for a robot bee suit?"
show d norm
r "Yes, so that you can then construct, program, and activate that suit in such a way that my spirit can inhabit it and use it to defeat communism."
show a happy t
a "That doesn't sound like very much work."
show a happy
show d norm t
d "I guess we could do that."
show d norm
r "Then it is settled!  Cinnamon me again when you have the device ready."
r "Good luck, boys.  The whole world is counting on you."
r "I'll just be chilling at my sweet ghost mansion in the mean time."

play sound "cinnamon.wav"
show r cinnamon at Transform(function=logo_transform)

r "Reaghost away!"

hide r cinnamon
with dissolve
    
show d norm t
d "Now what?"
show d norm
show a happy t
a "You heard the man.  We boys must travel to Hoover Tower under cover of darkness and copy that floppy."
show a happy
show d norm t
d "How will we even read a floppy disk?"
show d norm
show a happy t
a "We'll figure it out as we go along.  Now let's go!"
show a happy 
show d norm t
d "But it's still daytime!  The conservative political theorists will see us!"
show d norm
show a happy t
a "Nah, it's fine.  We'll just fight them floor by floor until we make it to the top of the tower."
show a happy
show d norm t
d "Oh, okay then."
d "So how do we get there in this game?"
show d norm
show a happy t
a "I could put in a map with Stanford University and have the player click on the location they want us to go."
show a happy
show d happy t
d "Yeah!  Good idea.  Let's do that."
show d happy
show a happy t
a "You got it.  Here we go!"

window hide None
call screen demo_imagemap
window show None
    
 # Call screen assignes the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.

if _return == "stanford":
    show a happy t
    a "Great choice!  Let's go to Stanford!"

show a happy
show d norm t
d "Wait, why did you put up a map of the entire Milky Way Galaxy?"
show d norm
show a norm t
a "That was actually a map of the NGC 6744 Galaxy."
show a norm
show d norm t
d "Oh."
d "Why did you put up a map of the NGC 6744 Galaxy?"
show d norm
show a norm t
a "That's because we're inside the Milky Way Galaxy right now, so we don't know what it looks like from the outside."
a "It probably looks like NGC 6744, another spiral galaxy, so I thought it would make a good approximation."
show d norm t
show a happy
d "Uh..."
d "Why did you put up a map of an entire galaxy?"
show d norm
show a happy t
a "I wanted to give the player as many options as possible."
a "I'm working really hard to create a sense of immersion and the illusion of a nuanced, branching story line."
show a happy
show d norm t
d "But you only let them go to Stanford."
d "And we're already at Stanford."
d "And you put it in comic sans."
d "How could you?"
show d norm
show a norm t
a "I..."
a "I had no choice."
show a stern t
a "Don't ask too many questions, Dylan.  You'll want to stay out of this."
show a stern
show d norm t
d "Um..."
d "Can you at least put up a map of the Stanford Campus so the player can select Hoover Tower?"
show d norm
show a happy t
a "Sure!  Here we go!"

window hide None
call screen weber_imagemap
window show None
    
 # Call screen assignes the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.

if _return == "stevereed":
    show a happy t
    a "Great choice!  Let's go to Hoover Tower!"
    
show a happy
show d norm t
d "Dude.  That wasn't even Stanford."
d "That's the college in the Midwest with that guy that makes the weird microwave food videos."
show d norm
show a happy t
a "Roll the clip!"
show a happy
show d norm t
d "Noooooooo–"

$ renpy.movie_cutscene("revensteed.mpg")

show a happy
show d stern t
d "What?"
show d norm t
d "What happens when it's done?"
show a happy t
show d norm
a "That's the beauty of it."
a "Steven Reed keeps us in suspense."
a "Forever."
show a happy
show d norm t
d "Oh.  Right."
d "So can we put up an actual map of Stanford this time that actually leads us to Hoover Tower?"
show d norm
show a stern t
a "Fine."

window hide None
call screen weber_imagemap
window show None
    
 # Call screen assignes the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.

if _return == "dangit":
    scene bg hoover
    with Dissolve(.5)
    pause .5
    scene bg hoover
    show d stern
    with Dissolve(.5)
    show a happy t
    with Dissolve(.5)
    a "Great choice!  Here we are at Hoover Tower!"

show a happy
show d stern t
d "That was still a map of Weber State University!"
show d stern
show a happy t
a "Who cares, hombre?  It got us here, didn't it?"
show a happy
show d stern t
d "Ugh."
show d stern
show a happy t
a "The tower is open during the day, so I think we can just go inside."
show a happy
show d norm t
d "Don't we need to equip ourselves before we fight a bunch of conservative political theorists?"
show d norm
show a happy t
a "Nah."
show a happy
show d happy t
d "Oh, cool.  Alright then."

scene bg hooverinside
with Dissolve(.5)
pause .5
show a happy
with Dissolve(.5)
show d norm
with Dissolve(.5)
d "Hmm..."
show d norm t
d "Where are all the conservative political theorists?"
show d norm
show a happy t
a "Maybe the ghost of President Herbert Hoover ate them all."
show a happy
show d norm t
d "Yeah, maybe."
d "So, uh...  What should we–"

play sound "cinnamon.wav"
show h norm:
    alignaround (.5, .5)
    linear 2.0 xalign .5 yalign .2 clockwise circles 3

show d norm t
d "Uh-oh."
show d norm
h "Who dares trespass in the sacred tower of President Herbert Hoover?"
show a happy t
a "Dylan and Andrew!"
show a happy
h "Dylan and Andrew, eh?  Those sound like the names of poor people."
show d norm t
show a norm
d "...They are."
show d norm
show a norm t
a "I have to attend meetings of the Bay Area Communist Party just to eat bad pizza."
a "They always get them topped with bell peppers."
show d stern
a "Gross."
show d stern t
show a norm
d "What?  Bell peppers are delicious on pizza!"
show d stern
show a stern t
a "Are not!  Their nasty pepper taste overwhelms the flavor of the cheese and tomato sauce!"
show a stern
show d stern t
d "You're tripping!"
show a norm
show d norm
h "Silence!"
show a happy t
a "Oh yeah, we forgot about you, Mr. President."
show a happy
show d stern t
d "What did you do with all the conservative political theorists, you fiend?!"
show d norm
h "I'd hardly call them conservative!  They were classic bleeding heart liberals."
show a norm
h "They didn't even want to dismantle the welfare system or reinstate child labor!"
h "So I ate them."
show a happy t
a "Called it!"
show a happy
show d norm t
d "So, um, Mr. Hoover–"
show d norm
h "That's Mr. Herbert Hoover to you, you ossified lollygagger!"
show d stern
show a happy t
a "Is that 20's slang?"
show d stern t
show a happy
d "Mr. HERBERT Hoover..."
d "Do you have a floppy disk containing the blueprints for a mechanical bee suit that is meant to be piloted by Ronald Reagan?"
show d norm
h "You bet your bottom dollar I do!"
show d norm 
show a happy t
a "Can you give it to us so that we can defeat communism?"
show a stern
show d stern
h "Nonsense!  I'd rather make a small donation to save the life of a starving child than help you scoundrels freeloading off of this once-proud institution's financial aid."
h "Your kind makes me sick.  Ghost sick."
show d stern t
d "You're really mean."
show d stern
show a stern t
a "Could you at least make that donation you were talking about?"
show a mad
show d mad
h "Nonsense!  I'd rather not insult a homeless person than make a small donation to save the life of a starving child!"
h "Just what kind of ossified lollygagger do you take me for?"
show d mad t
d "Give us that floppy or everyone at this school will drown in Mountain Dew™!"
show d mad
h "I'd actually like that a lot."
show a mad t
a "Why are you so mean?"
show a mad
h "Oh, I'll tell you why."
show a norm
show d norm
h "I used to be famous for my humanitarian work.  During the Great War, my American Relief Administration fed eleven million starving Belgians a day."
h "Then I worked to feed millions more when the war was over.  Many of them civilians from the nations we just defeated."
h "Now I'm only remembered for my failures as president.  After the stock market crash, nobody cared about all the lives I saved."
h "I recognize my mistakes now, but I really was doing my best.  And it just wasn't good enough."
h "Now I'm an outcast in the American memory."
h "So all y'all can go jump in a lake."
h "A Mountain Dew™ lake."
h "And drown."
show a stern
show d stern
h "Because you suck."
show a stern t
a "Is there any way we can pursuade you, Mr. President?"
show a stern
h "Well, I suppose there is one way."
h "You can try to best me at the world's oldest and most cherished game."
h "The game I spent the days of my youth playing when I wasn't busy not insulting homeless people."
show a norm t
a "What's he talking about, Dylan?  Hacky sack?"
show a norm
show d norm t
d "Maybe ball in a cup?"
show a norm t
show d norm
a "Maybe spilling a bag of rice on the ground and bending over and counting each rice grain and writing the total number of rice grains on a piece of parchment and attaching that piece of parchment to a passenger pigeon so you can mail it to the Kaiser of Germany?"
show a norm
stop music
h "Silence!"
h "The game..."
h "I refer to..."
h "Is..."
play music "_Speedball_ title music, Atari ST 1.mp3"
h "Pong."
show a norm t
a "Dear God."
show a norm 
show d norm t
d "You... You monster."
show d norm
h "Yes, that is correct.  The player must best me at pong if you want to save your pathetic school."
show d norm t
d "Here we go."
show d norm
show a norm t
a "Good luck player.  Try to win so we don't all die, okay?"



label demo_minigame_pong:

    window hide None

    # Put up the pong background, in the usual fashion.
    scene bg pong field

    # Run the pong minigame, and determine the winner.
    python:
        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene bg hooverinside
    show h norm:
        align (.5, .2)
    show d norm
    show a norm

    window show None


    if winner == "Ghost of Herbert Hoover":
        show a norm
        show d norm
        show h norm:
            align (.5, .2)
        h "Hah!  No mortal can best the everlasting phantasm of Herbert Hoover!"
        show d norm t
        d "Sorry, but you have to beat him.  It's the only way for us to copy that floppy."
        show d norm
        
        menu:
            h "Indeed.  Would you like to play again, you worthless excuse for a human being?"
            "Sure, dork.":
                jump demo_minigame_pong
            "Lol nope.":
                jump Awww
    else:
        show d happy
        show a happy
        show h norm:
            align (.5, .2)
        play music "Automation.mp3"
        h "You... You won."
        h "You bested the everlasting phantasm of Herbert Hoover."
        h "How can this be?"
        show a happy t
        a "Maybe it's because ghosts aren't very good at playing video games?"
        show a happy
        h "Oh yeah.  I forgot."
        show d happy t
        d "Hand over the floppy, so we can copy, Mr. President!"
        jump floppy
        
label Awww:
show d norm
show a norm
show h norm:
    align (.5, .2)
stop music
h "What?"
h "You don't want to play pong with me anymore?"
play music "Automation.mp3"
h "Awww."
h "That's the first time in years I've gotten to play pong."
h "None of the political theorists wanted to play it with me."
h "Well, not after I ate them."
show a happy
show d happy
h "I guess I'll just give you the stupid floppy disk then."
h "It's not like I have anything better to do."
h "Other than eat political theorists and not insult homeless people, of course."
jump floppy

label floppy:
show a happy
show d happy
play music "Final Fantasy VII 11 Fanfare 8-BIT 1.mp3"
show snowblossom 1
show snowblossom 2
show floppy at Transform(function=floppy_transform)
h "Here you go."
h "Just make sure to return it to the Hoover institute's library after you copy it, okay?"
h "Or I'll eat you."
show a happy t
a "Woo!  Great job, player!"
show a happy
show d happy t
d "Now we can copy that floppy!"
show d happy
show a happy
h "Yes, yes.  Now beat it!"
show a happy t
a "Okay!"

scene bg hoover
with Dissolve(.5)
pause .5
scene bg hoover
show d happy
with Dissolve(.5)
show a happy t
with Dissolve(.5)
play music "Automation.mp3"

a "Let's head back to our dorm and copy that floppy!"
show a happy
show d norm t 
show a norm
d "We should stop saying 'copy that floppy'.  It's getting really annoying."
show a norm t
show d norm
a "Yeah.  I'm getting annoyed just thinking about all of the effort it's going to take to read the information stored on this outdated medium, let alone duplicate it!"
show a norm
show d norm t
d "That's not what I–"
show d stern t
d "Never mind."

scene bg 304
with Dissolve(.5)
pause .5
scene bg 304
show d happy
with Dissolve(.5)
show a happy t
with Dissolve(.5)

a "Got the floppy coppier ready?"
show a happy
show d norm t
d "Ugh."
show d norm
show a happy t
a "At least I didn't say 'copy that floppy'!"
show a happy
show d norm t
d "Stooooooop."
show d norm
show a stern t
a "Fiiiiiiine."
show a happy
show d norm t
d "Anyway, how are we going to read the floppy disk?"
d "And if we can read it to get the blueprints, why would we need to copy it?"
show d norm
show a happy t
a "For starters, I was thinking we can read the disk with this Apple II I always keep in my pants."
show a happy
show d norm t
show ii off:
    align (.55, .45)
with fade
d "Ohhh.  So that's why your pants are so heavy!"
show d norm 
show a happy t
a "As for needing to copy it, I have no idea."
a "I just wrote the dialogue that way because it's fun to say 'copy that floppy'."
show a happy
show d norm t
d "Makes sense."
show d happy
show a happy t
a "Okay, I'm just going to insert the disk, run its contents, and print out what we need."
show a happy
show d norm t
d "But how can we print from an Apple II?  There's no way we could connect to that thing."
show d norm
show a norm t
a "You must have faith."
a "Player, does it or does it not say in the ''Free'' Services section of the official Room 304 flyer that we offer on demand printing?"
window hide
show a happy 


call screen viewport_screen
with dissolve

show a happy
show d norm t
d "Those scroll bars didn't work."
show d norm
show a happy t
a "That's because I could display the whole image on the screen!  There wasn't anything to scroll to."
show a happy
show d norm t
d "So why did you include scroll bars?"
show d norm
show a happy t
a"So was I right about the printing thing, player?"
show a happy

menu:
    "You were!":
        jump yep
    "No.":
        jump nope

label nope:
show a happy t
a "See, Dylan?  We offer on demand printing."
show a stern t
a "And I demand that we print."
show a happy
show d stern t
d "But the player said that it doesn't say that!"
show d stern
show a happy t
a "You must both have faith in the printer."
show a happy
show d norm
jump printing

label yep:
show a happy t
a "See, Dylan?  We offer on demand printing."
show a stern t
a "And I demand that we print."
show a happy
jump printing

label printing:
show a happy
show d norm t
d "I don't think that's how printers work."
show d norm
show a happy t
a "It'll work!  Let's turn on the II!"

play sound "applechime.mp3"
show ii start:
    align (.55, .45)
show a happy
show d norm t
d "Wow.  I'm honestly surprised it functions after being in your pants for so long."
show d happy
show ii smile:
    align (.55, .45)
show a happy t
a "Now let's insert the floppy!"
show d norm
show floppy at Transform(function=floppy_transform)
a "(This is an animation of me inserting the floppy.)"
show a happy
show d norm t
d "Sure it is."
show d norm
hide floppy
show a happy t
play sound "click sound.mp3"
a "Inserted!"
show ii read:
    align (.55, .45)
show a norm t
stop music
a "Wait, what?"
show a norm
show d norm t
d "What's wrong?"
show d norm
show a norm t
a "These aren't the blueprints for a mechanical bee suit that is meant to be piloted by Ronald Reagan!"
show ii crabs:
    align (.55, .45)
show a norm t
play music "Crabcakes.mp3"
a "This looks like a surrealist point-and-click adventure game with graphics made in a knockoff of MS Paint."
show a norm
show d stern t
d "As if our adventure game wasn't surreal or of low enough quality already."
show d stern 
show a norm t
a "It's called 'The Semi-exciting Adventures of Crabcakes Linguini: Super Spy'."
show a norm t
show d norm
a "Maybe it's a security program and we have to beat it to get the blueprints."
show a happy
show d norm t
d "I don't think that's how security programs work."
show d norm
show a happy t
a "I guess the player will just have to beat it for us!  Let's go!"
jump begin

# ---Start Screen
screen start_imagemap:
    imagemap:
        auto "tartjame_%s.png"
        hotspot (297, 539, 207, 45) action Return("start") alt "Start"  

label begin:
window hide None
call screen start_imagemap
window show None
if _return == "start":
    label vicki:
    window hide None
    call screen vicki_imagemap
    window show None
if _return == "vickichat":
    window hide None
    call screen dialogue_imagemap   
    window show None
    
# ---Reception
screen vicki_imagemap:
    imagemap:
        auto "room1_%s.png"
        hotspot (217, 8, 170, 261) action Return("vickichat") alt "Vickichat"      

# ---Receptionist Dialogue
screen dialogue_imagemap:
    imagemap:
        auto "room1_talk1_%s.png"
        hotspot (27, 407, 321, 162) action Return("option1") alt "Option1"
        hotspot (407, 410, 326, 172) action Return("option2") alt "Option2"
if _return == "option1":
    jump vicki
if _return == "option2":
    jump open
    
# ---Open Reception Door
screen opendoor_imagemap:
    imagemap:
        auto "room1_opendoor_%s.png"
        hotspot (217, 8, 170, 261) action Return("vickichat2") alt "Vickichat2"
        hotspot (558, 21, 162, 344) action Return("goroom2") alt "Goroom2"
        
label open:
window hide None
call screen opendoor_imagemap
window show None
if _return == "vickichat2":
    jump vicki2
if _return == "goroom2":
    jump room2
    
# ---Open Reception Speech
screen opendoorchat_imagemap:
    imagemap:
        auto "room1_go_%s.png"
        hotspot (558, 21, 162, 344) action Return("goroom2") alt "Goroom2"

label vicki2:
window hide None
call screen opendoorchat_imagemap
window show None
if _return == "goroom2":
    jump room2
    
# ---Room 2 Unpressed
screen room2_imagemap:
    imagemap:
        auto "room2_%s.png"
        hotspot (108, 111, 157, 135) action Return("spoons_u") alt "Spoons_u"
        hotspot (106, 335, 200, 158) action Return("rags_u") alt "Rags_u"
        hotspot (309, 121, 125, 115) action Return("obama_u") alt "Obama_u"
        hotspot (511, 257, 33, 36) action Return("press") alt "Press"
        hotspot (615, 98, 114, 350) action Return("speardeath") alt "Speardeath"

# ---Room 2 Pressed
screen room2pressed_imagemap:
    imagemap:
        auto "room2_pressed_%s.png"
        hotspot (108, 111, 157, 135) action Return("spoons_p") alt "Spoons_p"
        hotspot (106, 335, 200, 158) action Return("rags_p") alt "Rags_p"
        hotspot (309, 121, 125, 115) action Return("obama_p") alt "Obama_p"
        hotspot (511, 257, 33, 36) action Return("unpress") alt "Unpress"
        hotspot (615, 98, 114, 350) action Return("spearhall") alt "Spearhall"
        
label room2:
window hide None
call screen room2_imagemap
window show None
if _return == "press":
    jump room2pressed
if _return == "spoons_u":
    jump spoons_u
if _return == "rags_u":
    jump rags_u
if _return == "obama_u":
    jump obama_u
if _return == "speardeath":
    jump speardeath
    
label spoons_u:
window hide None
call screen spoons_u_imagemap
window show None
if _return == "room2_u":
    jump room2    
    
label spoons_p:
window hide None
call screen spoons_p_imagemap
window show None    
if _return == "room2_p":
    jump room2pressed

label room2pressed:
window hide None
call screen room2pressed_imagemap
window show None    
if _return == "unpress":
    jump room2
if _return == "spoons_p":
    jump spoons_p
if _return == "rags_p":
    jump rags_p
if _return == "obama_p":
    jump obama_p
if _return == "spearhall":
    jump hallway
# ---Spoons Unpressed
screen spoons_u_imagemap:
    imagemap:
        auto "spoons_%s.png"
        hotspot (0, 0, 800, 600) action Return("room2_u") alt "Room2_u"
        
# ---Spoons Pressed
screen spoons_p_imagemap:
    imagemap:
        auto "spoons_%s.png"
        hotspot (0, 0, 800, 600) action Return("room2_p") alt "Room2_p"
        
# ---Rags Unpressed
screen rags_u_imagemap:
    imagemap:
        auto "rags_%s.png"
        hotspot (0, 0, 800, 600) action Return("room2_u") alt "Room2_u"
        
# ---Rags Pressed
screen rags_p_imagemap:
    imagemap:
        auto "rags_%s.png"
        hotspot (0, 0, 800, 600) action Return("room2_p") alt "Room2_p"

label rags_u:
window hide None
call screen rags_u_imagemap
window show None
if _return == "room2_u":
    jump room2  
    
    
label rags_p:
window hide None
call screen rags_p_imagemap
window show None
if _return == "room2_p":
    jump room2pressed
    
# ---Obama Unpressed
screen obama_u_imagemap:
    imagemap:
        auto "plavex_%s.png"
        hotspot (14, 501, 202, 81) action Return("obamadeath") alt "obamadeath"
        hotspot (279, 499, 203, 85) action Return("room2_u") alt "Room2_u"
        
# ---Obama Pressed
screen obama_p_imagemap:
    imagemap:
        auto "plavex_%s.png"
        hotspot (14, 501, 202, 81) action Return("obamadeath") alt "obamadeath"
        hotspot (279, 499, 203, 85) action Return("room2_p") alt "Room2_p"
        
# ---Obama Lazor Death
screen obamadeath_imagemap:
    imagemap:
        auto "laserdeath_%s.png"
        hotspot (0, 0, 800, 600) action Return("gameover") alt "Gameover"
        
# ---Spear Death
screen speardeath_imagemap:
    imagemap:
        auto "speardeath_%s.png"
        hotspot (0, 0, 800, 600) action Return("gameover") alt "Gameover" 
        
# ---Game Over
screen gameover_imagemap:
    imagemap:
        auto "jameover_%s.png"
        hotspot (0, 0, 800, 600) action Return("restart") alt "Restart"
        
label obama_u:
window hide None
call screen obama_u_imagemap
window show None
if _return == "room2_u":
    jump room2
if _return == "obamadeath":
    jump obamadeath


label obama_p:
window hide None
call screen obama_p_imagemap
window show None
if _return == "room2_p":
    jump room2pressed
if _return == "obamadeath":
    jump obamadeath


label obamadeath:
window hide None
call screen obamadeath_imagemap
window show None
if _return == "gameover":
    jump gameover
    
label speardeath:
window hide None
call screen speardeath_imagemap
window show None
if _return == "gameover":
    jump gameover

label gameover:
window hide None
call screen gameover_imagemap
window show None
if _return == "restart":
    jump begin
    
# ---hallway
screen hallway_imagemap:
    imagemap:
        auto "hallway_%s.png"
        hotspot (323, 99, 95, 195) action Return("control") alt "Control"

label hallway:
window hide None
call screen hallway_imagemap
window show None
if _return == "control":
    jump control1

    
label control1:
window hide None
call screen control1_imagemap
window show None
if _return == "elements":
    jump elements1
if _return == "unroll":
    jump control2
if _return == "keybox":
    jump keybox4
if _return == "phant":
    jump phant1
    
label control2:
window hide None
call screen control2_imagemap
window show None
if _return == "elements":
    jump elements2   
if _return == "keybox":
    jump keybox3
if _return == "phant":
    jump phant2
    
label control3:
window hide None
call screen control3_imagemap
window show None
if _return == "elements":
    jump elements3
if _return == "tart":
    jump tart3
if _return == "phant":
    jump phant3
    
label control4:
window hide None
call screen control4_imagemap
window show None
if _return == "elements":
    jump elements4
if _return == "unroll":
    jump control3
if _return == "tart":
    jump tart4
if _return == "phant":
    jump phant4
    
# ---Control Room 1(no key, rolled)
screen control1_imagemap:
    imagemap:
        auto "spaceship_%s.png"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"
        hotspot (77, 349, 154, 124) action Return("unroll") alt "Unroll"
        hotspot (662, 462, 91, 109) action Return("keybox") alt "Keybox"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"

# ---Control Room 2(no key, unrolled)
screen control2_imagemap:
    imagemap:
        auto "posters_unrolled_%s.png"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"

        hotspot (662, 462, 91, 109) action Return("keybox") alt "Keybox"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        
# ---Control Room 3(yes key, unrolled)
screen control3_imagemap:
    imagemap:
        auto "posters_unrolled_%s.png"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"
        
        
        hotspot (347,384, 114, 89) action Return("tart") alt "Tart"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        
# ---Control Room 4(yes key, rolled)
screen control4_imagemap:
    imagemap:
        auto "spaceship_%s.png"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"
        hotspot (77, 349, 154, 124) action Return("unroll") alt "Unroll"
        
        hotspot (347,384, 114, 89) action Return("tart") alt "Tart"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        
# ELEMENTSES

# ---Elements 1
screen elements_imagemap:
    imagemap:
        auto "periodictable_%s.png"
        hotspot (0, 0, 800, 600) action Return("leave") alt "leave"
        

# EASTER EGG 1

# ---Pucephant
screen pucephant_imagemap:
    imagemap:
        auto "easteregg_%s.png"
        hotspot (0, 0, 800, 600) action Return("leave") alt "leave"
        
label phant1:
window hide None
call screen pucephant_imagemap
window show None
if _return == "leave":
    jump control1
    
label phant2:
window hide None
call screen pucephant_imagemap
window show None
if _return == "leave":
    jump control2

label phant3:
window hide None
call screen pucephant_imagemap
window show None
if _return == "leave":
    jump control3
    
label phant4:
window hide None
call screen pucephant_imagemap
window show None
if _return == "leave":
    jump control4
        
label phant5:
window hide None
call screen pucephant_imagemap
window show None
if _return == "leave":
    jump tart3
    
label phant6:
window hide None
call screen pucephant_imagemap
window show None
if _return == "leave":
    jump tart4
        
        
label elements1:
window hide None
call screen elements_imagemap
window show None
if _return == "leave":
    jump control1

label elements2:
window hide None
call screen elements_imagemap
window show None
if _return == "leave":
    jump control2

label elements3:
window hide None
call screen elements_imagemap
window show None
if _return == "leave":
    jump control3
    
label elements4:
window hide None
call screen elements_imagemap
window show None
if _return == "leave":
    jump control4
    
label elements5:
window hide None
call screen elements_imagemap
window show None
if _return == "leave":
    jump tart3

label elements6:
window hide None
call screen elements_imagemap
window show None
if _return == "leave":
    jump tart4
#KEYBOXESES

# ---Keybox
screen keybox_imagemap:
    imagemap:
        auto "keyout_%s.png"
        hotspot (352, 171, 116, 223) action Return("grab") alt "Grab"
        
label keybox4:
window hide None
call screen keybox_imagemap
window show None
if _return == "grab":
    jump keyin4
    
label keybox3:
window hide None
call screen keybox_imagemap
window show None
if _return == "grab":
    jump keyin3
    
# ---Key In
screen keyin_imagemap:
    imagemap:
        auto "keyin_%s.png"
        hotspot (213, 222, 38, 109) action Return("turn") alt "Turn"
        
label keyin4:
window hide None
call screen keyin_imagemap
window show None
if _return == "turn":
    jump keyturnt4

label keyin3:
window hide None
call screen keyin_imagemap
window show None
if _return == "turn":
    jump keyturnt3
    
# ---Key Turned
screen keyturnt_imagemap:
    imagemap:
        auto "keyturnt_%s.png"
        hotspot (0, 0, 800, 600) action Return("leave") alt "leave"

label keyturnt4:
window hide None
call screen keyturnt_imagemap
window show None
if _return == "leave":
    jump control4

label keyturnt3:
window hide None
call screen keyturnt_imagemap
window show None
if _return == "leave":
    jump control3
    
# ---Tart 4 (rolled)
screen spaceshipinspace_imagemap:
    imagemap:
        auto "spaceshipinspace_%s.png"
        hotspot (214, 0, 371, 274) action Return("space") alt "space"
        hotspot (77, 349, 154, 124) action Return("unroll") alt "Unroll"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        
# ---Tart 3 (unrolled)
screen spaceship_unrolled_imagemap:
    imagemap:
        auto "spaceship_unrolled_%s.png"
        hotspot (214, 0, 371, 274) action Return("space") alt "space"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        
label tart3:
window hide None
call screen spaceship_unrolled_imagemap
window show None
if _return == "space":
    jump space1
if _return == "phant":
    jump phant5
if _return == "elements":
    jump elements5
    
label tart4:
window hide None
call screen spaceshipinspace_imagemap
window show None
if _return == "space":
    jump space1
if _return == "unroll":
    jump tart3
if _return == "phant":
    jump phant6
if _return == "elements":
    jump elements6
    
# ---Space1
screen space1_imagemap:
    imagemap:
        auto "1_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space1:
window hide None
call screen space1_imagemap
window show None
if _return == "click":
    jump space2

# ---Space2
screen space2_imagemap:
    imagemap:
        auto "2_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space2:
window hide None
call screen space2_imagemap
window show None
if _return == "click":
    jump space3

# ---Space3
screen space3_imagemap:
    imagemap:
        auto "3_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space3:
window hide None
call screen space3_imagemap
window show None
if _return == "click":
    jump space4
    
# ---Space4
screen space4_imagemap:
    imagemap:
        auto "4_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space4:
window hide None
call screen space4_imagemap
window show None
if _return == "click":
    jump space5
    
# ---Space5
screen space5_imagemap:
    imagemap:
        auto "5_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space5:
window hide None
call screen space5_imagemap
window show None
if _return == "click":
    jump space6

# ---Space6
screen space6_imagemap:
    imagemap:
        auto "6_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space6:
window hide None
call screen space6_imagemap
window show None
if _return == "click":
    jump space7   
    
# ---Space7
screen space7_imagemap:
    imagemap:
        auto "7_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space7:
window hide None
call screen space7_imagemap
window show None
if _return == "click":
    jump space8    
    
# ---Space8
screen space8_imagemap:
    imagemap:
        auto "8_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"

label space8:
window hide None
call screen space8_imagemap
window show None
if _return == "click":
    jump space9
    
# ---Space9
screen space9_imagemap:
    imagemap:
        auto "9_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"
label space9:
window hide None
call screen space9_imagemap
window show None
if _return == "click":
    jump victoire
    
# ---Victoire
screen victoire_imagemap:
    imagemap:
        auto "victoire_%s.png"
        hotspot (195, 552, 460, 29) action Return("click") alt "click"
        hotspot (515, 42, 69, 90) action Return("boxart") alt "Boxart"
        
label victoire:
window hide None
call screen victoire_imagemap
window show None
if _return == "click":
    jump success  
if _return == "boxart":
    jump boxart
    
# ---Box Art
screen boxart_imagemap:
    imagemap:
        auto "boxart_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"
        
label boxart:
window hide None
call screen boxart_imagemap
window show None
if _return == "click":
    jump victoire  
    

label success:
stop music
play music "Automation.mp3"
scene bg 304
show ii find:
    align (.55, .45)
show d norm
show a norm t
a "Good job, player!  You beat the surrealist security program and located the blueprints for a mechanical bee suit that is meant to be piloted by Ronald Reagan!"
show d norm t
show a happy
d "I have no words to describe the events that just transpired."
d "But yeah.  Good job getting through all that, player."
show d norm
show a happy t
show ii smile:
    align (.55, .45)
a "That was without a doubt the second best thing I've ever seen."
a "The first of course being 'Bedtime for Bonzo'."
show a norm
show d norm t
d "Wait, but why did the people that coded everything try to protect the blueprints with a surrealist point-and-click adventure game?"
d "And how did they get their knockoff MS paint graphics to run on an Apple II?"
show a stern
d "And if the floppy disk is from the 1980s how did they know about Barack Obama becoming president and the shoop da woop meme?"
d "And who was Crabcakes Linguini?  Was he supposed to be the player character?"
show d norm
show a stern t
a "The United States Department of Defense's methods are perfect."
a "That's how they keep us safe and protect our freedom."
a "Never question their abilities, Dylan."
a "Ever."
a "Or else."
show a stern
show d norm
d "..."
show d norm t
d "Dang."
show d norm
show a happy t
a "Lol."
a "As for the identity of Crabcakes Linguini..."
a "I like to think that each of us is Crabcakes Linguini."
a "In our heart."
show a happy
show d norm t
d "I wish I liked to think the same way."
show d norm 
show a happy t
a "Alright, let's print the blueprints so we can figure out how to build this thing!"
show ii printing:
    align (.55, .45)
show d happy t
show a happy
show ii printing
d "Wow, it's actually printing!"
show d happy
show a happy t
a "My faith has been rewarded!  I am vindicated!"
show a happy
show d norm t
d "Hey, wait.  How is your Apple II displaying comic sans?"
show d norm
show a stern t
a "What did I tell you about questioning the United States Department of Defense, Dylan?!"
show a stern
show d norm t
d "No, that's not what I–"
d "Actually, nevermind.  I don't need to know."
show d norm
show a happy t
a "That's the spirit!"
a "Alright, we have the blueprints!  Now we can turn off the computer and put it away."
show ii bye:
    align (.55, .45)
a "Bye, Apple II!"
show a happy
show d norm t
d "Uh, yeah.  Bye, Apple II."
play sound "click sound.mp3"
show ii off:
    align (.55, .45)
show d norm 
show a happy t
a "Back in my pants you go!"
hide ii off
with fade
show d norm t
show a happy
d "Those are some stretchy pants you have there."
d "Shall we look at the blueprints now?"
show d norm
show a happy t
a "You bet!  Let's check 'em out!"
hide d norm
hide a happy t
stop music
play sound "guitar_riff.wav"
hide bg 304
scene bg beeprints:
    crop (519, 396, 224, 157)
    size (800, 450)
    
    linear 2.5 crop (313, 210, 196, 145)    

    crop (129, 375, 162, 119)
    size (800, 450)
    
    linear 2.0 crop (316, 312, 175, 116)

    crop (40, 181, 293, 185)
    size (800, 450)
    
    linear 2.0 crop (257, 40, 282, 206)
    
    crop (257, 40, 282, 206)
    size (800, 450)
    
    linear 3.0 crop (0, 0, 800, 600)
    
d "This is terrifying."
stop music
play music "Automation.mp3"
scene bg 304 beeprints
show d norm 
show a norm t
a "Yeah.  It really is."
show a norm
show d norm t
d "I don't think the world is ready for this."
show d norm
show a norm t
a "We have no choice."
show a norm
show d happy t
d "Hey!  You put up a picture of the blueprints without putting in pointless scroll bars!"
show d happy
show a norm t
a "Pointless scroll bars are too festive for this solemn occasion."
show a norm t
show d norm
a "We're about to construct the most powerful weapon in human history."
a "And use it."
show a norm
d "..."
show d norm t
d "It's Ronald Reagan in a bee costume."
show d norm
show a norm t
a "Yeah, that's what I said."
show d norm t
show a norm
d "There's no way it could be that bad."
d "...Right?"
show d norm
show a norm t
a "We'll see."
show a happy t
show d happy
a "Alright, player!  When the blueprints go fullscreen, click on each of the four listed components to learn my plan for obtaining them."
a "When you're confident that you understand them all, click on Ronald Beegan's left sneaker to confirm."
a "Let's hustle!"

# ---Beeprints Fake
screen beeprints_fake_imagemap:
    imagemap:
        auto "blueprints_screen_%s.jpeg"
        hotspot (347, 461, 44, 79) action Return("sneaker") alt "Sneaker"
        hotspot (552, 77, 90, 48) action Return("code") alt "Code"
        hotspot (44, 244, 292, 46) action Return("quantum computer") alt "Quantum Computer"
        hotspot (165, 407, 93, 54) action Return("beena") alt "Beena"
        hotspot (551, 414, 174, 136) action Return("industrial grade oatmeal") alt "Industrial Grade Oatmeal"
label beeprint_map_fake:        
window hide None
call screen beeprints_fake_imagemap
window show None
if _return == "code":
    jump code_fake
if _return == "quantum computer":
    jump quantum_fake
if _return == "beena":
    jump beena_fake
if _return == "industrial grade oatmeal":
    jump oatmeal_fake
if _return == "sneaker":
    jump sneaker
    
label oatmeal_fake:
scene bg 304
show d norm t
show a happy
d "How does a bee suit require oatmeal?"
show d norm 
show a stern t
a "Very carefully."
jump beeprint_map_fake

label quantum_fake:
scene bg 304
show d norm t
show a happy 
d "How are we supposed to get a quantum computer?"
show d norm
show a stern t
a "Very carefully."
jump beeprint_map_fake

label beena_fake:
scene bg 304
show a happy
show d norm t
d "What's BeeNA?"
d "Is that like DNA, but from Bees?"
show d norm
show a happy t
a "The suit's quantum computer must use genetic algorithms, so we gotta rustle up some bee genes."
show a happy
show d norm t
d "I don't think you know what any of those words mean, but given our previous track record you must be correct."
show d norm t
d "Still, how are we supposed to collect Bee DNA for this suit?"
show d norm
show a stern t
a "Very carefully."
jump beeprint_map_fake

label code_fake:
scene bg 304
show a happy
show d norm t
d "What?  We need to write code for a quantum computer that allows the ghost of Ronald Reagan to pilot a mechanical bee suit?"
d "How are we supposed to do that?"
show d norm
show a stern t
a "Very carefully."
jump beeprint_map_fake

label sneaker:
scene bg 304
show d happy 
show a happy t
a "Did you enjoy that bit we just did, player?"
a "The whole thing that just happened where Dylan asked each time how we're supposed to do each thing?"
show a happy
show d happy t
d "And Andrew said each time we had to do it"
show d stern t
d "'very carefully'!"
show d happy
show a happy t
a "I'm telling ya, that is classic Dylan and Andrew schtick."
a "Wasn't that worth the cost of admission?"
show d happy
show a happy
menu:
    "Sure, I guess.":
        jump sweet
    "I expected nothing when I downloaded this, but somehow I'm still disappointed.":
        jump ohdang
        
label sweet:
show a happy
show d happy t
d "Yeah!  Alright!"
show d happy
show a happy t
a "There's plenty more where that came from!"
show d norm t
show a happy
d "Hopefully not too much more."
jump business

label ohdang:
show a norm
show d norm
a "..."
d "..."
show a norm
show d norm t
d "That's really hurtful."
show d happy
show a happy t
a "Just kidding.  We're cycling .png images linked to prewritten dialogue, so we don't actually care what you think."
show a happy
show d happy t
d "Yeah.  And we're really just doing all this schtick to entertain ourselves anyway."
jump business

label business:
show a happy t
show d happy
a "Alright, to business!"
a "I say we should get that oatmeal first."
a "Since it's nearly..."
show d norm 
a "Five OAT clock!"
a "Eh?  Ehhh?"
show d norm t
show a happy
d "You have no idea what time it is and I think we might be starting to push it too far."
show d norm 
show a norm t
a "Starting?"
show a norm
show d norm t
d "Poor choice of words."
show a norm t
show d norm
a "The audience retention rate by this point is only twelve percent, so does it really matter what happens now?"
show d norm t
show a norm
d "The fourth wall is already broken and on fire from meta jokes about audience retention rates and similar things, so I guess not."
show d norm
show a happy t
a "Cool!"
show a norm
show d norm t
d "I do however think it would be wise to nix the obnoxious self-referential tangents for a while and get on with whatever it is we're actually doing."
show d norm
show a norm t
a "Yeah.  Alright."
a "Player, when the blueprints go fullscreen again, click on the component you want to hunt down and we'll actually do something."
show a happy
show d stern t
d "Hey!  Your fingers are crossed behind your back!"
show d stern
show a happy t
a "Not that the player can tell from how I drew the–"
show a happy
show d stern t
d "No more obnoxious self-referential tangents!"
show d stern
show a norm t
a "Okay, jeez."

# ---Beeprints Legit
screen beeprints_imagemap:
    imagemap:
        auto "blueprints_screen_%s.jpeg"
        hotspot (552, 77, 90, 48) action Return("code") alt "Code"
        hotspot (44, 244, 292, 46) action Return("quantum computer") alt "Quantum Computer"
        hotspot (165, 407, 93, 54) action Return("beena") alt "Beena"
        hotspot (551, 414, 174, 136) action Return("industrial grade oatmeal") alt "Industrial Grade Oatmeal"
label beeprint_map:        
window hide None
call screen beeprints_imagemap
window show None
if _return == "code":
    jump code
if _return == "quantum computer":
    jump quantum
if _return == "beena":
    jump beena
if _return == "industrial grade oatmeal":
    jump oatmeal

label code:
jump beeprint_map

label quantum:
jump beeprint_map

label oatmeal:
jump beeprint_map

label beena:
scene bg cherry
show aa happy t
show ad norm
play music "Indoors Two.mp3"
aa "Alright, so I guess we'll find some BeeNA, then!"
aa "Ready, Dylan?"
show aa happy
show ad norm t
ad "Where are we?!"
show ad norm
show aa happy t
aa "If BeeNA is just the DNA of bees, then it would probably suffice to put some bees in a jar."
show aa happy
show ad stern t
ad "What's with this music?!"
show ad stern
show aa happy t
aa "We can get a bee jar, go to the Beekeeping Club's hive, and borrow a few bees!  Sound like a plan?"
show aa happy
show ad rage
ad "WHY ARE WE ANIME?"
show ad stern
show aa norm t
aa "Huh?"
aa "Oh.  No idea."
show aa norm
show ad spin:
    xpos 0.05 ypos 0.05 xanchor 0.05 yanchor 0.05
    rotate 0
    linear 2.0 rotate 360
    repeat
ad "WHAT DO YOU MEAN 'NO IDEA'?"
show aa norm t
aa "Woah!  Take it easy!  You're going all anime on me!"
show aa norm
show ad spin:
    xpos 0.05 ypos 0.05 xanchor 0.05 yanchor 0.05
    rotate 0
    linear 0.1 rotate 360
    repeat
ad "RAAAAAAAAAAHHHHH!!!"
show aa bleh
aa "Relax, alright?  And stop spinning around like that!  You're making me sick."
show ad spin:
    xpos 0.05 ypos 0.05 xanchor 0.05 yanchor 0.05
    rotate 0
    linear 2.0 rotate 360
    repeat
show aa norm t
aa "That's a little better.  Now stop all the way."
hide ad vein
show ad vein
aa "Now just pop that weird forehead vein symbol thing back in..."
show ad rage
aa "And stop making that weird face that protrudes from the outline of your head."
show ad norm
show aa happy t
aa "There we go!"
show aa happy
show ad norm t
ad "I...  I don't know what happened just now."
show aa norm 
show ad norm
show b hap:
    xalign .5 yalign .2
    linear .5 xalign .5 yalign .5
    linear .5 xalign .5 yalign .2
    repeat
b "But I know!"
show aa norm t
aa "You're creepy."
show aa norm
b "I'm a member of a colony of anime bees, also known as chibees!"
b "Our queen heard that you were coming to steal our BeeNA, so we put an anime curse on you to stop you!"
b "The only way to lift the curse is to play a bee-themed JRPG and defeat her and her minions through monotonous turn-based combat!"
show ad norm t
ad "I don't really want to do that."
show ad norm
show aa norm t
aa "Why are they called 'chibees'?  Shouldn't they be called bnimes?"
show aa norm
b "That's because a 'chibi' is a super deformed version of an anime character drawn with a huge head, small body, and exaggerated facial expression."
b "citation: https://en.wikipedia.org/wiki/Chibi_(term)"
b "It's an anime pun!"
show aa norm t 
aa "I don't like that."
show aa norm
show ad norm t
ad "Let's just get out of here and find a different way to get BeeNA.  This isn't worth it."
show ad norm
show aa norm t
aa "Agreed."
show aa norm
b "No!  You can't go now!  If you leave you'll be stuck as anime forever!"
show aa norm t
aa "Could be worse."
aa "Like our characters could have been made with an even lower quality anime character creator from deviantart.com."
show aa norm
b "It actually couldn't be!  If you're stuck as anime, all the girls you interact with will be hypersexualized and have one-dimensional personalities!"
b "Just take a look at this girl over here!"
hide b hap
show scary anime girl
show ad ppbt
show aa ppbt
sag "Oh hai boys~~~ ^^ Wanna rub some oil on me and then have me scream at you that I hate you but be secretly obsessed with you?"
show ad stern t
show aa ppbt
ad "This isn't okay."
show ad stern
show aa stern t
aa "You win, bee.  We'll play the game."
aa "We'll do it for feminism."
hide scary anime girl
show b hap:
    xalign .5 yalign .2
    linear .5 xalign .5 yalign .5
    linear .5 xalign .5 yalign .2
    repeat
show aa stern
b "Excellent!  Let us begin!"
hide b hap
ad "..."
show aa norm
show ad norm t
ad "Where did it go?"
show ad norm
show aa norm t
aa "It's probably just taking a little while for the game to load up."
aa "I guess we'll just have to shoot the breeze."
show aa norm
show ad norm t
ad "Oh, alright."
ad "So I was thinking this may not be a fair representation of anime."
ad "While many successful programs feature hypersexualized female characters, many anime also subvert the stereotype and portray capable women with complex character arcs."
ad "I'm just concerned that we're criticizing a straw man and oversimplifying a broad and rich cultural tradition."
show ad norm
show aa norm t
aa "That's all true, but bees only enjoy the hypersexualized anime."
aa "Bees are perverts, Dylan.  It's the way nature made them."
show aa norm 
show ad norm t
ad "Oh yeah.  I forgot."
show ad norm

# ---Lord of the Bees Start Screen
screen lotb_intro_imagemap:
    imagemap:
        auto "lotb_intro_1_%s.png"
        hotspot (249, 488, 322, 56) action Return("maygodhelpyou") alt "Maygodhelpyou"
label lotb_intro_map:
play music "Battle NO5.mp3"
window hide None
call screen lotb_intro_imagemap
window show None
if _return == "maygodhelpyou":
    jump startbees
    
label startbees:
    $playerX = None
    $playerY = None
label map:
    $map_on = True
    window hide None
    scene black
    play music "happy.ogg" fadein .5
    with dissolve
    scene jrpg-start
    show aa norm
    show ad ppbt
    ad "Ugh.  Now we're all JRPG-y."
    show ad norm
    show b hap:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
        repeat
    b "Indeed!  Or should I say inBEEd?!"
    show ad norm t
    ad "No."
    show ad norm
    b "You're ready to begin your quest!  All you have to do it head through the front gates and you'll be in the hive."
    show aa norm t
    aa "Alright, then.  Let's get this over with."
    show aa norm
    show ad norm t
    ad "Is there a particular reason the gates have a sign saying 'Abandon all hope, ye who enter here'?"
    show ad norm
    b "Well look at the time!  I'd better get out of here!"
    show aa norm t
    aa "Is it five oat clock?"
    show aa norm
    b "Good luck, Dylan and Andrew!  I'll BEE seeing you!"
    hide b hap
    show ad norm t
    ad "I have a really bad feeling about this."
    show ad norm
    show aa norm t
    aa "It missed the perfect opportunity for a bee pun with that 'ye who enter' bit."
    aa "That's downright ominous."
    show aa norm
    show ad norm t
    ad "I guess we don't have a choice.  There's just those gates and infinite darkness in all directions."
    show ad norm
    show aa norm t
    aa "You can use the arrow keys to move and space to interact, player."
    aa "The WASD keys are buggy, so I can't recommend them."
    aa "Good luck!"
    hide aa norm
    hide ad norm t
    scene black
    python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = gateway_layout, tileList = gateway_tiles,
            portals = gateway_portals, portal_tiles = gateway_portal_tiles,
            enemy_layout = gateway_enemies_layout, enemySprites = gateway_enemies,
            
            NPCSprites = gateway_villagers, #villagers, uses the same layout as enemies
            groundLayout = gateway_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
        
label betrayal:
    scene black
    play music "Undertale - Genocide run - The End.mp3"
    n "   "
    n "You idiot."
    n "I have no intention of lifting your curse."
    n "Now I have you right where I want you."
    n "Heh heh."
    stop music
    image hbee:
        "hbee1.png"
        pause 0.1
        "hbee2.png"
        pause 0.1
        "hbee3.png"
        pause 0.1
        "hbee4.png"
        pause 0.1
        "hbee5.png"
        pause 0.1
        "hbee3.png"
        pause 0.1
        "hbee2.png"
        pause 0.1
        repeat
    # show hbee
    show b horror:
        xalign .5 yalign .2
    n "WELCOME TO HELL."  
    hide b horror
    play sound "charas laugh.mp3"
    n "   "
    scene black
    

screen daatalescreen_imagemap:
    imagemap:
        auto "daatalescreen_%s.png"
        hotspot (1, 1, 799, 599) action Return("hellintro") alt "Hellintro"

label daatalescreen_imagemap:
play sound "Undertale Sound Effect - Intro.mp3"
window hide None
call screen daatalescreen_imagemap
window show None
if _return == "hellintro":
    jump hellintro
    
label hellintro:
# image movie = Movie(size=(800, 600), xpos=0, ypos=0, xanchor=0, yanchor=0)
# play movie "Inferno.mov" loop
play music "Undertale - Genocide run - The End.mp3"
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = hell01_layout, tileList = hell01_tiles,
            portals = hell01_portals, portal_tiles = hell01_portal_tiles,
            enemy_layout = hell01_enemies_layout, enemySprites = hell01_enemies,
            
            NPCSprites = hell01_villagers, #villagers, uses the same layout as enemies
            groundLayout = hell01_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
        
label demon_catch:
scene black
image demon_throne:
    "throne_1.png"
    pause 0.1
    "throne_2.png"
    pause 0.1
    "throne_6.png"
    pause 0.1
    "throne_4.png"
    pause 0.1
    "throne_5.png"
    pause 0.1
    "throne_7.png"
    pause 0.1
    "throne_3.png"
    pause 0.1
    repeat
show demon_throne
demon "̳͎̺̖e̟̘͔̳͎̺m̙̘̤ ̟̮d͉̭̘̝̕l͚̱̠̯̦̜̖o̰̳͈̺̙̰̲͟t̞̲̦̹̠͕̫ ͙̭̭͢ͅe͈̭̰c͓̬̞n̻̖͚̲̼̮͕o̶̘ ̮͓̹ͅͅy̡̹̠͚̦̘̦ͅd̺̲̱ǫ̳͍̫̬͔̖̺b̥̻ḙ̲͉͡m̠̕o̦̙̼͚͓̺͖s͓͉"
demon "e̸̳͕̝m͏͇ ̫̪l̖͠l̫̹̠̯o̲̩͔ͅr͈̠̙̣͉͝ ̳̀ạ͙͔̯̹͕̖n҉̝͔͍̱n͖͎͇ǫ̜g͓̲͔ ̫s̸̝a̴̱͙̰w̪͇͠ ͠d̛͇l͎̗̞r̖͚o͏̫̬̞̱̱̥̪w҉̟̳̙̼̣ e͇͉̦̰h̲ṱ̛̜̱͎̭"
stop music
v "Be gone, wretched spirit!"
demon "Aww man.  Okay."
hide demon_throne
show v t
play music "TheDiscovery.mp3"
v "You're safe now, my children."
show v
show aa norm t
show ad rage
aa "Who are you?"
show aa norm
ad "AAAAAAAAAAAAAAAAH!!!!!!!"
show v t
v "My name is Virgil, author of the Aeneid and favorite poet of Augustus Caesar."
show v
show ad rage
ad "WHAT WERE THOSE THINGS?!!!"
show aa norm t
aa "Can you tell us what's going on?"
show aa norm
ad "WHAT THE HELL IS GOING ON??!!"
show v t
v "Quite right!  You have both been sent to Hell."
show aa happy t
show v
aa "Bogus!"
show aa happy
ad "WE JUST GOT ATTACKED BY A DEMON WITH CREEPY GLITCHY DIALOGUE AND IT WAS SPOOKY AND I DIDN'T LIKE IT."
show v t
v "I was brought here after writing book four of my poem, the Georgics, which discusses a bee colony as an ideal model for human society."
show ad norm t
show v
ad "Oh, I read that for Latin class."
ad "You're a pretty good poet, Virgil."
ad "Even if you believed the weird Roman superstition that bees are spontaneously generated from ox carcasses."
show ad norm
show v t
v "As it happens, bees are not really born out of ox carcasses.  The bees saw my poem and its mention of ox carcass birth as a slight against them."
v "So they put an anime curse on me and threw me down here."
v "Turns out they run the place."
v "And they transform everyone into anime creatures to punish them."
show v
show ad norm t
ad "How do you know what anime is?"
show ad norm
show aa happy t
aa "I guess that's what happened to us, then."
aa "Minus the poetry and ox carcass part."
aa "So do you know how we can get out of here and stop being anime and find BeeNA?"
show aa norm
show v t
v "The only way to escape, break the curse, and attain the apian essence you seek is by defeating the prince of Hell and queen of all Bees..."
show ad stern
v "Beelzebub."
v "Or should I say BEE-elzebub?"
show aa happy t
show v
aa "I get it!"
show aa happy
show ad stern t
ad "We have to fight SATAN?!"
show ad stern
show v t
v "But before you do that you must navigate the nine circles of Hell without getting eaten alive by demons."
v "After spending thousands of years here I know it pretty well, so I shall be your guide and guarantee you safe passage through the inferno."
show v
show aa norm t
aa "That sounds pretty good, but what's in it for us?"
show aa norm
show ad norm t
ad "Um..."
ad "What?"
show ad norm
show v t
v "If you are able to defeat Beelzebub and leave this horrid place, I will return with you to the overworld and finally publish this poem I have been working on for thousands of years."
v "It shall be about these two paths diverging in some woods and how one of them made all the difference."
v "It shall be really cool and awesome."
v "As a reward for your heroism, I shall pay you five bucks."
show v
show aa happy t
aa "Deal!"
show aa happy
show ad stern t
ad "Um hello?!  How are we supposed to DEFEAT SATAN?!  I think we overlooked that teensy detail."
show ad stern
show v t
v "You'll just punch him really hard.  That ought to do it."
show v
show aa happy t
aa "Sounds good!  We have no more questions!"
show aa happy
show ad stern t
ad "WE HAVE SEVERAL QUESTIONS!"
show ad stern
show v t
v "Very good, gentlemen.  Let us begin our journey!"
show ad norm t
ad "Nooooooooo-"

$playerX = None
$playerY = None
$map_on = True
window hide None
play music "Ave Marimba.mp3"
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = limbo_layout, tileList = limbo_tiles,
            portals = limbo_portals, portal_tiles = limbo_portal_tiles,
            enemy_layout = limbo_enemies_layout, enemySprites = limbo_enemies,
            
            NPCSprites = limbo_villagers, #villagers, uses the same layout as enemies
            groundLayout = limbo_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
label virgiltalk:
    show v
    v "This is the first circle of Hell, Limbo."
    v "Bees have only a moderate dislike for poetry, so they put all the poets here."
    v "In order to exit, you must complete a game of limbo so difficult that history's greatest artistic minds have failed to conquer it for thousands of years."
    v "Save for me, of course.  But I'll get eaten by demons if I tell you how to win."
    v "Best of luck!"
    hide v
    return
label homertalk:
    show homer onlayer npcPortraits 
    homer "D'oh!"
    hide homer 
    return
label rumitalk:
    show rumi onlayer npcPortraits 
    rumi "My friend Attar of Nishapur recounts the following parable."
    rumi "A powerful king assembled all the kingdom's wise men to create a ring that would make him happy when he was sad."
    rumi "Each wise man submitted a ring with an engraved message for this purpose."
    rumi "Upon deliberation, the king chose a ring with the message 'This too will pass'."
    rumi "It indeed made him happy when he was sad, but it also became a curse, for he was taught the ephemerality of both sadness and happiness."
    rumi "All emotions, as life, are fleeting."
    rumi "Too bad I'm stuck in Bee Hell forever."
    hide rumi 
    return
label shakespearetalk:
    show shakespeare onlayer npcPortraits 
    shakespeare "To bee, or not to bee, that is the question:"
    shakespeare "Whether 'tis nobler in the mind to suffer the stings and venom of outrageous bees,"
    shakespeare "Or to take Fly swatters against a Bee of troubles and by opposing..."
    shakespeare "Um..."
    shakespeare "Sorry.  I ran out of bee schtick."
    hide shakespeare 
    return
label poetalk:
    show poe onlayer npcPortraits
    poe "'Villains!' I shrieked, 'dissemble no more!  I admit the deed!'"
    poe "'Tear up the planks!  Here, here!'"
    poe "'It is the buzzing of this hideous bee!'"
    hide poe 
    return
label sheltalk:
    show shel onlayer npcPortraits
    shel "'I am writing these poems from inside a lion, and it's rather dark in here.'"
    shel "'So please excuse the handwriting which may not be too clear.'"
    shel "'But this afternoon by the lion's cage I'm afraid I got too near.'"
    shel "'And I'm writing these lines from inside a lion, and it's rather dark in here.'"
    shel "That's my poem 'It's Dark in Here', one of my best works."
    shel "Unlike my friends Bill and Ed who shoehorn bees into their poems in a vain attempt to please our captors, I've managed to preserve my artistic integrity."
    shel "Oh?"
    shel "Why don't I have anime eyes?"
    shel "That's because I was already an anime the whole time!"
    hide shel
    return
    
label limbogame:
    game "It's a limbo pole.  It's definitely too low for you to limbo under."
    game "Remove the pole?"
    menu:
        "Remove":
            jump limbo2
        "Do not":
            jump limbo3
            
label limbo3:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = limbo3_layout, tileList = limbo_tiles,
            portals = limbo3_portals, portal_tiles = limbo3_portal_tiles,
            enemy_layout = limbo3_enemies_layout, enemySprites = limbo3_enemies,
            
            NPCSprites = limbo3_villagers, #villagers, uses the same layout as enemies
            groundLayout = limbo3_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 

        
label limbo2:
$playerX = None
$playerY = None
$map_on = True
window hide None
play music "Ave Marimba.mp3"
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = limbo2_layout, tileList = limbo2_tiles,
            portals = limbo2_portals, portal_tiles = limbo2_portal_tiles,
            enemy_layout = limbo2_enemies_layout, enemySprites = limbo2_enemies,
            
            NPCSprites = limbo2_villagers, #villagers, uses the same layout as enemies
            groundLayout = limbo2_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)

label virgiltalk2:
    show v
    v "You solved the demonic puzzle!  Good show!"
    v "Now let us continue onward to Circle II!"
    hide v
    return
label homertalk2:
    show homer onlayer npcPortraits 
    homer "Mmmmmmmm..."
    homer "Donut."
    hide homer 
    return
label rumitalk2:
    show rumi onlayer npcPortraits 
    rumi "It appears that limbo, too, will pass."
    hide rumi 
    return
label shakespearetalk2:
    show shakespeare onlayer npcPortraits 
    shakespeare "Will all great Neptune's ocean wash this blood clean from my hand?"
    shakespeare "No, this my hand will rather the multiple seas incarnadine, making the green one red."
    shakespeare "Wait..."
    shakespeare "I forgot to put bees in that one."
    shakespeare "Would you like me to recite my new play, 'A Midsummer Night's Bee'?"
    hide shakespeare
    menu:
        "No.":
            return
label poetalk2:
    show poe onlayer npcPortraits
    poe "While I gazed, this fissure rapidly widened --there came a fierce breath of the whirlwind --the entire orb of the satellite burst at once upon my sight --my brain reeled as I saw the mighty walls rushing asunder --there was a long tumultuous shouting sound like the voice of a thousand waters --and the deep and dank tarn at my feet closed sullenly and silently over the fragments of the..." 
    poe 'HOUSE OF BEES.'
    hide poe 
    return
label sheltalk2:
    show shel onlayer npcPortraits
    shel "My book jacket portrait freaks out a lot of kids."
    shel "Some people say I look like a scary pirate."
    shel "I tend to agree with them."
    shel "Yarrrrr!"
    hide shel
    return

label minos:
    $playerX = None
$playerY = None
$map_on = True
window hide None
stop music
"You are not welcome here."
"Come to me and receive judgement."
play music "DvdThemeMusic-ghostpocalypse-theCall.mp3"
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = minos_layout, tileList = minos_tiles,
            portals = minos_portals, portal_tiles = minos_portal_tiles,
            enemy_layout = minos_enemies_layout, enemySprites = minos_enemies,
            
            NPCSprites = limbo2_villagers, #villagers, uses the same layout as enemies
            groundLayout = minos_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label minos1:
    "Come closer."
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = minos1_layout, tileList = minos_tiles,
            portals = minos1_portals, portal_tiles = minos1_portal_tiles,
            enemy_layout = minos_enemies_layout, enemySprites = minos_enemies,
            
            NPCSprites = limbo2_villagers, #villagers, uses the same layout as enemies
            groundLayout = minos_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label minos2:
    "I wish to see your face."
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = minos2_layout, tileList = minos_tiles,
            portals = minos2_portals, portal_tiles = minos2_portal_tiles,
            enemy_layout = minos_enemies_layout, enemySprites = minos_enemies,
            
            NPCSprites = limbo2_villagers, #villagers, uses the same layout as enemies
            groundLayout = minos_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label minos3:
    "I wish to feel your skin."
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = minos3_layout, tileList = minos_tiles,
            portals = minos3_portals, portal_tiles = minos3_portal_tiles,
            enemy_layout = minos_enemies_layout, enemySprites = minos_enemies,
            
            NPCSprites = limbo2_villagers, #villagers, uses the same layout as enemies
            groundLayout = minos_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label minos4:
    "I wish to taste your flesh."
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = minos4_layout, tileList = minos_tiles,
            portals = minos4_portals, portal_tiles = minos4_portal_tiles,
            enemy_layout = minos_enemies_layout, enemySprites = minos_enemies,
            
            NPCSprites = limbo2_villagers, #villagers, uses the same layout as enemies
            groundLayout = minos_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label minos5:
    "I am Minos, avatar of retribution."
image minosjudge:
    "minos1.png"
    pause 0.1
    "minos2.png"
    pause 0.1
    "minos3.png"
    pause 0.1
    "minos4.png"
    pause 0.1
    "minos5.png"
    pause 0.1
    "minos6.png"
    pause 0.1
    "minos7.png"
    pause 0.1
    repeat
"You do not belong here."
"You were brought here against your will."
show hbee
"By the dark one."
hide hbee
"You seek justice."
image hammertime:
    "hammertime1.png"
    pause 0.1
    "hammertime2.png"
    pause 0.1
    "hammertime3.png"
    pause 0.1
    "hammertime4.png"
    pause 0.1
    "hammertime5.png"
    pause 0.1
    "hammertime6.png"
    pause 0.1
    "hammertime3.png"
    pause 0.1
    repeat
show hammertime
"You seek to purge the red."
"To prevent the world from spinning backwards towards oblivion."
hide hammertime
image reg:
    "reg1.png"
    pause 0.1
    "reg2.png"
    pause 0.1
    "reg3.png"
    pause 0.1
    "reg4.png"
    pause 0.1
    "reg5.png"
    pause 0.1
    "reg6.png"
    pause 0.1
    "reg3.png"
    pause 0.1
    repeat
show reg
"You will fail."
hide reg
show hbee
"You seek to channel absolute power."
hide hbee
image beeg:
    "beegan1.png"
    pause 0.1
    "beegan2.png"
    pause 0.1
    "beegan4.png"
    pause 0.1
    "beegan5.png"
    pause 0.1
    "beegan3.png"
    pause 0.1
    "beegan6.png"
    pause 0.1
    "beegan4.png"
    pause 0.1
    repeat
show beeg
"And absolute power corrupts absolutely."
hide beeg
show hammertime
"Take care as you bear arms, for things are not what they seem."
hide hammertime
show hbee
"Take care as the world burns around you, for the world burns around you."
hide hbee
image future:
    "hammertime1.png"
    pause 0.1
    "hammertime2.png"
    pause 0.1
    "reg3.png"
    pause 0.1
    "reg4.png"
    pause 0.1
    "hbee3.png"
    pause 0.1
    "hbee2.png"
    pause 0.1
    "beegan5.png"
    pause 0.1
    "beegan3.png"
    pause 0.1
    repeat
show future
"For trespassing in this hall, I sentence you to experience your future."
"This will not be easy."
hide future
"Proceed."
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
stop music
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = minosend_layout, tileList = minosend_tiles,
            portals = minosend_portals, portal_tiles = minosend_portal_tiles,
            enemy_layout = minosend_enemies_layout, enemySprites = minosend_enemies,
            
            NPCSprites = minosend_villagers, #villagers, uses the same layout as enemies
            groundLayout = minosend_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleII:
init:
    image FrontPage = SnowBlossom("hell_page1.png", count=10, border=50, xspeed=(20, 50), yspeed=(200,400), start=0, fast=True, horizontal=False)
    image BackPage = SnowBlossom("hell_page2.png", count=10, border=50, xspeed=(20, 50), yspeed=(200,400), start=0, fast=True, horizontal=False)
    image FrontPage2 = SnowBlossom("hell_page1.png", count=10, border=50, xspeed=(20, 50), yspeed=(100,200), start=0, fast=True, horizontal=False)
    image BackPage2 = SnowBlossom("hell_page2.png", count=10, border=50, xspeed=(20, 50), yspeed=(100,200), start=0, fast=True, horizontal=False)
    image page1 = "hell_beepage_1.png"
    image page2 = "hell_beepage_2.png"
    image page3 = "hell_beepage_3.png"
    image page4 = "hell_beepage_4.png"
    image page5 = "hell_beepage_5.png"
    image page6 = "hell_beepage_6.png"
    
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
stop music
show v
show aa norm
show ad stern
show v t
play music "Wind-Mark_DiAngelo-1940285615.mp3"
v "There you two are!  What took you so long?"
show v
show aa norm t
aa "We were stopped by this giant demon thing called..."
aa "Um..."
aa "Myspace?"
show aa norm 
show ad stern t
ad "Minos."
show ad stern
show aa norm t
aa "Yeah, Myspace.  He said all this creepy prophetic stuff."
show aa happy
show v t
v "Oh, right.  Terribly sorry, I must have forgotten to inform you of his presence."
v "Myspace judges all those damned to the circles beneath Limbo and selects their punishment."
v "But he's been going through an edgy goth phase lately, so I wouldn't take whatever he said too seriously."
show ad stern t
show v
ad "His name was 'Minos'."
show ad stern
show v t
v "Anyway, this is the second circle of Hell, where the spirits of those who committed lustful acts are forever scattered by demonic wind as a symbolic punishment for their aimless desires."
v "It's an example of 'contrapasso', where the punishment for a sin metaphorically resembles or contrasts the sin itself."
v "citation: https://en.wikipedia.org/wiki/Contrapasso"
v "From here you mortals can freely enter the third circle, where the gluttonous writhe in vile mud beneath icy rain."
v "But be forwarned:"
v "The exit from that realm is guarded by the mighty demon Cerberus.  To pass it you must speak a secret word."
v "I already know what it is on account of my incredible cleverness, but if I told you I'd be eaten by demons."
v "Perhaps these arcane manuscripts hold the answer.  I already did you the service of plucking the most relevant pages from the cruel winds and affixing them to the floor with demonic chewing gum."
v "You're welcome."
v "Oh, and one more thing."  
v "You only have once chance to speak the correct word, else Cerberus will slash your bodies open and devour your entrails, leaving you to choke on your own blood and bile before you expire and join the ranks of the dead in Hell, never to escape."
show aa norm t
show v
aa "Gross."
show v t
show aa norm
v "Now get cracking!"
hide aa norm
hide v t
hide ad stern
show FrontPage onlayer npcPortraits
show BackPage onlayer npcPortraits
show FrontPage2
show BackPage2
play music "Wind-Mark_DiAngelo-1940285615.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleII_layout, tileList = circleII_tiles,
            portals = circleII_portals, portal_tiles = circleII_portal_tiles,
            enemy_layout = circleII_enemies_layout, enemySprites = circleII_enemies,
            
            NPCSprites = circleII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label page1:
    show page1 onlayer npcPortraits
    #"sotrami christus et Follatum"
    #Bees punish the foolish man with stings.
    "apes spiculis puniunt Fatuus"
    hide page1
    return
label page2:
    show page2 onlayer npcPortraits
    #"dorus apostii chandrulis ex naretta"
    #All will feel the wrath of the bees.
    "omnes iram apium sentient"
    hide page2
    return
label page3:
    show page3 onlayer npcPortraits
    #"vox nay tratex et Annum"
    #The angry bees ,protecting their honey, dance amongst hives, 
    "apes iratae mel Arcentes circum cubiles saltant"
    hide page3
    return
label page4:
    show page4 onlayer npcPortraits
    #"felicitus ape Exitus nay infernum"
    #The bees rule over edible humans.
    "apes super mortales Edibiles regnant"
    hide page4
    return
label page5:
    show page5 onlayer npcPortraits
    #"verum platis Lox veritas"
    #"verum platis Lox veritas"
    #The bees drag away a sacrifice covered in wounds.
    "apes hostiam corripuerunt Laceram"
    "apes hostiam corripuerunt Laceram"
    hide page5
    return
label page6:
    show page6 onlayer npcPortraits
    #"diablo est pragornum ex Nocht"
    #Do not disturb the bees who make their hives.
    "apes qui exstruunt Nolite vexare"
    ad "This has to be a trick, right?"
    aa "Hmmm."
    hide page6
    return

label virgilII1:
    v "Come on!  This is the safest passage I am permitted to provide according to demonic law!"
    v "And I already spent like twenty minutes gathering those pages from the infinite infernal vortex!"
    v "Sheesh!"
    return
    
init:
    image rev_lightning = im.Flip("lightning.png", horizontal=True)

    image rain:
  
        "rain1.png"
        0.1
        "rain3.png"
        0.1
        "rain2.png"
        0.1
        repeat
        
    image lightning:
        choice:        #weight of choice is 1
            "lightning.png"
            alpha  0.0
            10                 # show nothing for 10 seconds
        
        choice 0.1:   #weight of choice is 0.1
            "lightning.png"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0
            10
            
        choice 0.1:
            "rev_lightning"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0
            10
            
        repeat

label circleIII:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide FrontPage onlayer npcPortraits
hide BackPage onlayer npcPortraits
hide FrontPage2
hide BackPage2
show lightning onlayer npcPortraits
show rain onlayer npcPortraits
stop music
play music "Gewitter__Thunderstorm-Tim-1509815136.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIII_layout, tileList = circleIII_tiles,
            portals = circleIII_portals, portal_tiles = circleIII_portal_tiles,
            enemy_layout = circleIII_enemies_layout, enemySprites = circleIII_enemies,
            
            NPCSprites = circleIII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label cerberus_blocker:
init:
    image cerberus:
        "cerberus_1"
        pause 0.1
        "cerberus_2"
        pause 0.1
        "cerberus_3"
        pause 0.1
        "cerberus_4"
        pause 0.1
        "cerberus_5"
        pause 0.1
        "cerberus_6"
        pause 0.1
        "cerberus_3"
        pause 0.1
        "cerberus_1"
        pause 0.1
        "cerberus_2"
        pause 0.1
        "cerberus_3"
        pause 0.1
        "cerberus_4"
        pause 0.1
        "cerberus_5"
        pause 0.1
        "cerberus_6"
        pause 0.1
        "cerberus_3"
        pause 0.1
        "cerberus_1"
        pause 0.1
        "cerberus_2"
        pause 0.1
        "cerberus_3"
        pause 0.1
        "cerberus_4"
        pause 0.1
        "cerberus_5"
        pause 0.1
        "cerberus_6"
        pause 0.1
        "cerberus_3"
        pause 0.1
        "cerberus_eye-1"
        pause 0.1
        "cerberus_eye-2"
        pause 0.1
        "cerberus_eye-3"
        pause 0.1
        "cerberus_eye-4"
        pause 0.1
        "cerberus_eye-5"
        pause 0.1
        "cerberus_eye-4"
        pause 0.1
        "cerberus_eye-3"
        pause 0.1
        "cerberus_eye-2"
        pause 0.1
        "cerberus_eye-1"
        pause 0.1
        "cerberus_eye1"
        pause 0.1
        "cerberus_eye2"
        pause 0.1
        "cerberus_eye3"
        pause 0.1
        "cerberus_eye4"
        pause 0.1
        "cerberus_eye5"
        pause 0.1
        "cerberus_eye4"
        pause 0.1
        "cerberus_eye3"
        pause 0.1
        "cerberus_eye2"
        pause 0.1
        "cerberus_eye1"
        pause 0.1
        repeat
    image red = Solid((255, 0, 0, 255))
scene red
show cerberus
$ cerb1 = "fallen"
$ cerb2 = "Fallen"
$ cerb3 = "FALLEN"
$ cerb4 = "fallen."
$ cerb5 = "Fallen."
$ cerb6 = "FALLEN."
$ cerb7 = "fallen?"
$ cerb8 = "Fallen?"
$ cerb9 = "FALLEN?"
$ cerb10 = "fallen!"
$ cerb11 = "Fallen!"
$ cerb12 = "FALLEN!"

$ cerb13 = "bird"
$ cerb14 = "Bird"
$ cerb15 = "BIRD"
$ cerb16 = "bird."
$ cerb17 = "Bird."
$ cerb18 = "BIRD."
$ cerb19 = "bird?"
$ cerb20 = "Bird?"
$ cerb21 = "BIRD?"
$ cerb22 = "bird!"
$ cerb23 = "Bird!"
$ cerb24 = "BIRD!"

$ cerb25 = "bees"
$ cerb26 = "Bees"
$ cerb27 = "BEES"
$ cerb28 = "bees."
$ cerb29 = "Bees."
$ cerb30 = "BEES."
$ cerb31 = "bees?"
$ cerb32 = "Bees?"
$ cerb33 = "BEES?"
$ cerb34 = "bees!"
$ cerb35 = "Bees!"
$ cerb36 = "BEES!"
"You cannot pass without the word."
$ cerbname = renpy.input("What is the word?")
jump cerbcheck

label cerbcheck:
    if cerbname == cerb1:
        jump cerbwow
    if cerbname == cerb2:
        jump cerbwow
    if cerbname == cerb3:
        jump cerbwow
    if cerbname == cerb4:
        jump cerbwow
    if cerbname == cerb5:
        jump cerbwow
    if cerbname == cerb6:
        jump cerbwow
    if cerbname == cerb7:
        jump cerbwow
    if cerbname == cerb8:
        jump cerbwow
    if cerbname == cerb9:
        jump cerbwow
    if cerbname == cerb10:
        jump cerbwow
    if cerbname == cerb11:
        jump cerbwow
    if cerbname == cerb12:
        jump cerbwow
    if cerbname == cerb13:
        jump cerbbird
    if cerbname == cerb14:
        jump cerbbird
    if cerbname == cerb15:
        jump cerbbird
    if cerbname == cerb16:
        jump cerbbird
    if cerbname == cerb17:
        jump cerbbird
    if cerbname == cerb18:
        jump cerbbird
    if cerbname == cerb19:
        jump cerbright
    if cerbname == cerb20:
        jump cerbbird
    if cerbname == cerb21:
        jump cerbbird
    if cerbname == cerb22:
        jump cerbbird
    if cerbname == cerb23:
        jump cerbbird
    if cerbname == cerb24:
        jump cerbbird
    if cerbname == cerb25:
        jump cerbright
    if cerbname == cerb26:
        jump cerbright
    if cerbname == cerb27:
        jump cerbright
    if cerbname == cerb28:
        jump cerbright
    if cerbname == cerb29:
        jump cerbright
    if cerbname == cerb30:
        jump cerbright
    if cerbname == cerb31:
        jump cerbright
    if cerbname == cerb32:
        jump cerbright
    if cerbname == cerb33:
        jump cerbright
    if cerbname == cerb34:
        jump cerbright
    if cerbname == cerb35:
        jump cerbright
    if cerbname == cerb36:
        jump cerbright
    else:
        jump cerbwrong
        
label cerbwow:
    "Wow, you actually figured it out."
    "I also would have accepted 'BEES'."
    "You may pass."
    jump circleIIIb
    
label cerbbird:
    "Everybody knows that the bird is the word."
    jump circleIIIb

label cerbright:
    "You may pass."
    jump circleIIIb

label cerbwrong:
    "No."
    jump circleIIIa
    
label circleIIIa:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide FrontPage onlayer npcPortraits
hide BackPage onlayer npcPortraits
hide FrontPage2
hide BackPage2
show lightning onlayer npcPortraits
show rain onlayer npcPortraits
stop music
play music "Gewitter__Thunderstorm-Tim-1509815136.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIIa_layout, tileList = circleIII_tiles,
            portals = circleIIIa_portals, portal_tiles = circleIIIa_portal_tiles,
            enemy_layout = circleIII_enemies_layout, enemySprites = circleIII_enemies,
            
            NPCSprites = circleIII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleIIIax:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide FrontPage onlayer npcPortraits
hide BackPage onlayer npcPortraits
hide FrontPage2
hide BackPage2
show lightning onlayer npcPortraits
show rain onlayer npcPortraits
stop music
play music "Gewitter__Thunderstorm-Tim-1509815136.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIIax_layout, tileList = circleIII_tiles,
            portals = circleIIIa_portals, portal_tiles = circleIIIa_portal_tiles,
            enemy_layout = circleIII_enemies_layout, enemySprites = circleIII_enemies,
            
            NPCSprites = circleIII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
    
label circleIIIb:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide FrontPage onlayer npcPortraits
hide BackPage onlayer npcPortraits
hide FrontPage2
hide BackPage2
show lightning onlayer npcPortraits
show rain onlayer npcPortraits
stop music
play music "Gewitter__Thunderstorm-Tim-1509815136.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIIb_layout, tileList = circleIII_tiles,
            portals = circleIIIb_portals, portal_tiles = circleIIIb_portal_tiles,
            enemy_layout = circleIII_enemies_layout, enemySprites = circleIII_enemies,
            
            NPCSprites = circleIII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIII_ground_final,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
 
label circleIIIbx:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide FrontPage onlayer npcPortraits
hide BackPage onlayer npcPortraits
hide FrontPage2
hide BackPage2
show lightning onlayer npcPortraits
show rain onlayer npcPortraits
stop music
play music "Gewitter__Thunderstorm-Tim-1509815136.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIIbx_layout, tileList = circleIII_tiles,
            portals = circleIIIb_portals, portal_tiles = circleIIIb_portal_tiles,
            enemy_layout = circleIII_enemies_layout, enemySprites = circleIII_enemies,
            
            NPCSprites = circleIII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)   


label circleIIa:        
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide lightning onlayer npcPortraits
hide rain onlayer npcPortraits
show FrontPage onlayer npcPortraits
show BackPage onlayer npcPortraits
show FrontPage2
show BackPage2
stop music        
play music "Wind-Mark_DiAngelo-1940285615.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIa_layout, tileList = circleII_tiles,
            portals = circleIIa_portals, portal_tiles = circleIIa_portal_tiles,
            enemy_layout = circleIIa_enemies_layout, enemySprites = circleII_enemies,
            
            NPCSprites = circleII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleIIX:        
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide lightning onlayer npcPortraits
hide rain onlayer npcPortraits
show FrontPage onlayer npcPortraits
show BackPage onlayer npcPortraits
show FrontPage2
show BackPage2
stop music        
play music "Wind-Mark_DiAngelo-1940285615.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIX_layout, tileList = circleII_tiles,
            portals = circleII_portals, portal_tiles = circleII_portal_tiles,
            enemy_layout = circleII_enemies_layout, enemySprites = circleII_enemies,
            
            NPCSprites = circleII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleIIb:        
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
hide lightning onlayer npcPortraits
hide rain onlayer npcPortraits
show FrontPage onlayer npcPortraits
show BackPage onlayer npcPortraits
show FrontPage2
show BackPage2
stop music        
play music "Wind-Mark_DiAngelo-1940285615.mp3"
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIIb_layout, tileList = circleII_tiles,
            portals = circleIIb_portals, portal_tiles = circleIIb_portal_tiles,
            enemy_layout = circleIIb_enemies_layout, enemySprites = circleII_enemies,
            
            NPCSprites = circleII_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleII_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
        
        
label virgilIIa:
    v "Did I say you only have one chance to tell Cerberus the secret word before it violently murders you?"
    v "I meant to say you have infinite chances to tell Cerberus the secret word before it violently murders you!"
    v "Silly me.  The demonic air must be getting to my head."
    return
    
label virgilIIb:
    v "Come on!  Let's get going!"
    v "I have poems to publish!"
    return
    
label circleIV:
stop music
hide lightning onlayer npcPortraits
hide rain onlayer npcPortraits
show v
show aa happy
show ad stern
show v t
play music "DvdThemeMusic.eerie.creepy.birchRun.mp3"
v "Congratulations!  You two have passed beyond the demon Cerberus unscathed!"
show v
show ad stern t
ad "That 'puzzle' was really dumb."
show ad stern
show aa norm
show v t
v "Now we can make our way to the fourth circle, where the demon Plutus reigns over the souls of the greedy."
v "Beyond that flows the fifth circle, the vile river Styx, where the wrathful are forever held beneath the surface by its icy currents."
show v
show aa norm t
aa "In the past couple circles I didn't see any of the souls or spirits you've been talking about."
show aa stern t
show ad norm
aa "I mean, I'm grateful that you're guiding us, Virgil, but I'm starting to think that this isn't actually Hell."
show aa stern
show ad norm t
ad "Who cares?  Let's just keep going and get out of here!"
show ad norm
show aa norm t
aa "I just want to make sure we're getting our money's worth!"
show aa norm
show ad stern t
ad "What are you talking about?!"
show ad norm
show v t
v "Worry not, for this is definitely Hell.  I have merely been drowning out the cries of the damned by playing music with my fantastic Microsoft Zune!"
v "Let me pause the current track so you may observe."
stop music
play sound "click sound.mp3"
play music "hell-Mike_Koenig-144950046.mp3"
show aa norm t 
aa "Phew!  What a relief!"
show aa happy
show ad norm t
ad "You're messed up, Andrew."
show ad norm
show aa norm t
aa "Wait.  Why can't we see them if we can hear them?"
show aa norm
show v t
v "Your... umm..."
v "Moral purity makes them invisible to you?"
show v
show aa happy t
aa "Works for me!"
show aa happy
show ad norm t
ad "I never expected to say this to anyone, but"
ad "Can you please unpause your Zune, Virgil?"
show ad norm
show v t
v "Certainly!"
play sound "click sound.mp3"
play music "DvdThemeMusic.eerie.creepy.birchRun.mp3"
v "Now you must discover a way to cross the river Styx without being beaten to death by the icy invisible wrathful spirits of the damned!"
v "Best of luck!"
hide v t
hide ad norm
hide aa happy
jump circleIVa

label circleIVa:        
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIV_layout, tileList = circleIV_tiles,
            portals = circleIV_portals, portal_tiles = circleIV_portal_tiles,
            enemy_layout = circleIV_enemies_layout, enemySprites = circleIV_enemies,
            
            NPCSprites = circleIV_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleIVaa:        
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIVaa_layout, tileList = circleIV_tiles,
            portals = circleIV_portals, portal_tiles = circleIV_portal_tiles,
            enemy_layout = circleIV_enemies_layout, enemySprites = circleIV_enemies,
            
            NPCSprites = circleIV_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
        
label plutus_a:
init:
    image king_plutus:
        "plut1"
        pause 0.1
        "plut2"
        pause 0.1
        "plut3"
        pause 0.1
        "plut5"
        pause 0.1
        "plut6"
        pause 0.1
        "plut7"
        pause 0.1
        "plut8"
        pause 0.1
        "plut9"
        pause 0.1
        "plut10"
        pause 0.1
        "plut11"
        pause 0.1
        repeat
show king_plutus onlayer npcPortraits
plutus "I possess the wealth of fallen men."
plutus "Humans spend their fleeting lives stepping on each other for this wealth."
plutus "Now I step on them, for their wealth and souls have been ground together and fired into the tiles beneath our feet."
plutus "Be gone from my hall, for your punishment lies elsewhere."
aa "Harsh."
ad "Please don't talk back to demons."
return
        
label circleVa:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleV_layout, tileList = circleV_tiles,
            portals = circleV_portals, portal_tiles = circleV_portal_tiles,
            enemy_layout = circleV_enemies_layout, enemySprites = circleV_enemies,
            
            NPCSprites = circleV_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label phlegyas_a:
phlegyas "I am Phlegyas, ferryman of the river Styx."
ad "Can you take us across?"
phlegyas "For a price.  A one-way crossing costs one obol per spirit."
aa "I have thirty-five cents and some pocket lint."
phlegyas "No obols, no crossing."
ad "Wait, what are obols?"
phlegyas "They're Greek coins used to pay fare for crossing Styx, traditionally placed in the deceased's mouth at their time of death."
phlegyas "Do you have any obols in your mouths?"
ad "I just have my tongue."
aa "I just have thirty-five cents and some pocket lint."
ad "In your mouth?"
phlegyas "If you don't have any obols, try borrowing some from Plutus."
phlegyas "Ask nicely and he may let you work off your debt before the heat death of the universe."
ad "...Thanks."
aa "Oh, and by the way, player, you can't save past this point."
aa "And don't press the 'back' button, it'll glitch out."
ad "What?  Why?"
aa "The engine running this Hell rpg thing has a fatal saving flaw that I couldn't get rid of.  I emailed its designer and everything."
aa "So if you try to load a save state made after this point, you'll always return to the beginning of this pier."
aa "Just a heads up."
aa "If you want to leave the game and come back to it later you can mute the music in settings by pressing 'escape' and minimize the window."
aa "Fortunately, after this particular misadventure concludes, you can run a second game disk that will let you save properly again."
aa "But for now, if anybody asks, just say the broken save feature is an avant garde mechanical choice."
ad "Ugh."

scene black
jump circleVb

label circleVb:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleVb_layout, tileList = circleV_tiles,
            portals = circleVb_portals, portal_tiles = circleVb_portal_tiles,
            enemy_layout = circleV_enemies_layout, enemySprites = circleV_enemies,
            
            NPCSprites = circleV_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleVbb:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleV_layout, tileList = circleV_tiles,
            portals = circleV_portals, portal_tiles = circleVb_portal_tiles,
            enemy_layout = circleV_enemies_layout, enemySprites = circleV_enemies,
            
            NPCSprites = circleV_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label circleIVb:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIVaa_layout, tileList = circleIV_tiles,
            portals = circleIV_portals, portal_tiles = circleIVb_portal_tiles,
            enemy_layout = circleIV_enemies_layout, enemySprites = circleIV_enemies,
            
            NPCSprites = circleIVb_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label plutus_b:
show king_plutus onlayer npcPortraits
plutus "Why do you stay?"
ad "Could you please loan us two obols so we can cross the river?"
plutus "You seek to pluck wealth from the god of greed himself?"
aa "Yes please."
plutus "Very well.  I shall give you your loan."
plutus "For a price."
plutus "As an immortal demon tasked with punishing the souls of the damned for all eternity, things can get pretty boring."
plutus "I haven't had anyone to play my favorite video game with me for billions of years."
plutus "If you can get your starter deeémon to level six in this game, we can duel over link cable.  Then I will give you your obols."
aa "Starter what?"
hide king_plutus onlayer npcPortraits
show hellboy onlayer npcPortraits
plutus "Here you go!  Come back when you're ready."
ad "Is this a Game Boy?"
aa "Let's turn it on!"
ad "I'm not sure that's a good idea."
stop music
init:
    image hellboy_turnon:
        "hh1"
        pause 0.1
        "hh2"
        pause 0.1
        "hh3"
        pause 0.1
        "hh4"
        pause 0.1
        "hh5"
        pause 0.1
        "hh6"
        pause 0.1
        "hh7"
        pause 0.1
        "hh8"
        pause 0.1
        "hh9"
        pause 0.1
        "hh10"
        pause 0.1
        "hh11"
        pause 0.1
        "hh12"
        pause 0.1
        "hh13"
        pause 0.1
        "hh14"
        pause 0.1
        "hh15"
        pause 0.1
        "hh16"
        pause 0.1
        "hh17"
        pause 0.1
        "hh18"
        pause 0.1
        "hh19"
        pause 0.1
show hellboy_turnon onlayer npcPortraits
$ ui.timer(1.5, Play("sound", "gameboy_start_up.mp3"))
# play sound "gameboy_start_up.mp3"
aa "Too late."
jump pokelol

label pokelol:
init:
    image deeemon_init:
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.05
        "hhdeeemon1"
        pause 0.05
        "hh1"
        pause 0.2
        "hhdeeemon3"
play music "mon_intro.mp3"
show deeemon_init onlayer npcPortraits
ad "Oh jeez."
aa "Deeémon Cosmic Horror Version, eh?"
aa "Good luck, player!"
ad "Wait, we're making the player play this?"
ad "What if it possesses them or something?"
aa "Are you volunteering to play a most likely cursed version of a portable cartridge-based video game console from the late eighties given to us by a demon in Hell?"
ad "Nah."
aa "Good luck, player!"
jump null1

label null1:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null_layout, tileList = null_tiles,
            portals = null_portals, portal_tiles = null_portal_tiles,
            enemy_layout = null_enemies_layout, enemySprites = null_enemies,
            
            NPCSprites = null_villagers, #villagers, uses the same layout as enemies
            groundLayout = null_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label deeemon:
hide hellboy onlayer npcPortraits
hide deeemon_init onlayer npcPortraits
hide hellboy_turnon onlayer npcPortraits
image gbgreen = Solid((232, 240, 121, 255))
scene gbgreen
show lovecraft
with dissolve
play music "mon_newgame.mp3"
p "Hello there!"
play sound "MonSound.mp3"
p "Welcome to the world of DEEéMON!"
play sound "MonSound.mp3"
p "My name is LOVECRAFT!"
play sound "MonSound.mp3"
p "People call me the DEEéMON DOC!"
play sound "MonSound.mp3"
hide lovecraft
with dissolve
show pika 
with moveinright
play sound "MonSound.mp3"
p "This world is inhabited by eldritch abominations called DEEéMON!"
play sound "MonSound.mp3"
p "For some people DEEéMON are objects of worship."
play sound "MonSound.mp3"
p "Others use them for fights."
play sound "MonSound.mp3"
p "Myself..."
play sound "MonSound.mp3"
p "I study DEEéMON as a profession."
play sound "MonSound.mp3"
hide pika
with dissolve
show trainer1
with moveinright
p "First, what is your name?"
$ trainer = renpy.input(" ")
$ trainer = trainer.strip()
if trainer == "":
    $ trainer="Francis"
play sound "MonSound.mp3"
p "Right!  So your name is [trainer]!"
hide trainer1
with dissolve
init:
    image rival_reveal:
        "mon_rival1"
        pause 0.05
        "mon_rival2"
        pause 0.05
        "mon_rival1"
        pause 0.05
        "mon_rival2"
        pause 0.05
        "mon_rival1"
        pause 0.05
        "mon_rival2"
        pause 0.05
        "mon_rival3"
        pause 0.05
        "mon_rival4"
        pause 0.05
        "mon_rival3"
        pause 0.05
        "mon_rival4"
        pause 0.05
        "mon_rival3"
        pause 0.05
        "mon_rival4"
        pause 0.05
        "mon_rival5"
show rival_reveal
play sound "MonSound.mp3"
p "This is my grandson."  
play sound "MonSound.mp3"
p "He's been your rival since before you were born."
play sound "MonSound.mp3"
p "...Erm, what is his name again?"
$ rival = renpy.input(" ")
$ rival = rival.strip()
if rival == "":
    $ rival="NYARLATHOTEP"
play sound "MonSound.mp3"
p "That's right!  I remember now!"
play sound "MonSound.mp3"
p "His name is [rival]!"
play sound "MonSound.mp3"
hide rival_reveal
with dissolve
show trainer1
with dissolve
p "[trainer]!"
play sound "MonSound.mp3"
p "Your very own DEEéMON legend is about to unfold!"
play sound "MonSound.mp3"
p "A world of nightmares and misadventures with DEEéMON awaits!"
hide trainer1
init:
    image trainer_morph:
        "mon_trainer2"
        pause 0.3
        "mon_trainer3"
        pause 0.3
        "mon_trainer4"
show trainer_morph
play sound "MonSound.mp3"
p "Let's go!"
hide trainer_morph
with dissolve
jump lavender1

label lavender1:
play music "31-lavender-town-s-theme.mp3"


$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = lavender1_layout, tileList = lavender1_tiles,
            portals = lavender1_portals, portal_tiles = lavender1_portal_tiles,
            enemy_layout = lavender1_enemies_layout, enemySprites = lavender1_enemies,
            
            NPCSprites = lavender1_villagers, #villagers, uses the same layout as enemies
            groundLayout = lavender1_ground,
            playerSprites = trainer_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label lovecraft_catch:
play sound "MonSound.mp3"
p "LOVECRAFT: Hey!  Wait!  Don't go out!"
play sound "MonSound.mp3"
p "That was close!"
play sound "MonSound.mp3"
play music "08-battle-vs-wild-pokemon-.mp3"
p "Wild DEEéMON live at the Mountains of Madness!"
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null2_layout, tileList = null2_tiles,
            portals = null2_portals, portal_tiles = null2_portal_tiles,
            enemy_layout = null2_enemies_layout, enemySprites = null2_enemies,
            
            NPCSprites = null2_villagers, #villagers, uses the same layout as enemies
            groundLayout = null2_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label lovecraft_caught:
image gbgreen = Solid((232, 240, 121, 255))
scene gbgreen with pixellate
show pikacatch with moveinleft
show lovebat with moveinright
play sound "MonSound.mp3"
p "Wild PIKATHULHU appeared!"
show pika_text
play sound "MonSound.mp3"
show pentaspell with moveintop
p "LOVECRAFT: Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn!"
hide pikacatch
hide pentaspell
init:
    image eldritch_orb:
        "deeemon_orb"
        pause 0.4
        "deeemon_orb_left"
        pause 0.3
        "deeemon_orb"
        pause 0.3
        "deeemon_orb_right"
        pause 0.3
        "deeemon_orb"
        pause 1.8
        "deeemon_orb_left"
        pause 0.3
        "deeemon_orb"
        pause 0.3
        "deeemon_orb_right"
        pause 0.3
        "deeemon_orb"
        pause 1.8
        "deeemon_orb_left"
        pause 0.3
        "deeemon_orb"
        pause 0.3
        "deeemon_orb_right"
        pause 0.3
        "deeemon_orb"
        pause 1.8
        "deeemon_orb_full"
show eldritch_orb
play sound "MonSound.mp3"
p "PROF. LOVECRAFT used ELDRITCH ORB!"
hide eldritch_orb
stop music
play sound "47-pokemon-received-fanfare.mp3"
show ball_full
p "All right!  PIKATHULHU was caught!"
play sound "MonSound.mp3"
p "LOVECRAFT: Whew..."
play sound "MonSound.mp3"
p "A wild DEEéMON can appear anytime in the Mountains of Madness."
play sound "MonSound.mp3"
p "You need your own DEEéMON for your protection."
play sound "MonSound.mp3"
p "Take this PIKATHULHU, [trainer]."
play sound "MonSound.mp3"
p "Now go drive everyone to insanity!"
jump lavender2

label lavender2:
play music "31-lavender-town-s-theme.mp3"
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = lavender2_layout, tileList = lavender2_tiles,
            portals = lavender2_portals, portal_tiles = lavender2_portal_tiles,
            enemy_layout = lavender2_enemies_layout, enemySprites = lavender2_enemies,
            
            NPCSprites = lavender2_villagers, #villagers, uses the same layout as enemies
            groundLayout = lavender2_ground,
            playerSprites = trainer_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label victim_catch:
play sound "MonSound.mp3"
p "FRIGHTENED MAN: Where am I?!"
play sound "MonSound.mp3"
p "How did I get here?"
play sound "MonSound.mp3"
play music "08-battle-vs-wild-pokemon-.mp3"
p "P-Please!  Stay Back!"
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null3_layout, tileList = null3_tiles,
            portals = null3_portals, portal_tiles = null3_portal_tiles,
            enemy_layout = null3_enemies_layout, enemySprites = null3_enemies,
            
            NPCSprites = null3_villagers, #villagers, uses the same layout as enemies
            groundLayout = null3_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label victim_intro:
image gbgreen = Solid((232, 240, 121, 255))
scene gbgreen with pixellate
show victim with moveinleft
show trainbat with moveinright
play sound "MonSound.mp3"
p "Wild FRIGHTENED MAN appeared!"
play sound "MonSound.mp3"
show victim_text
hide trainbat with moveoutleft
show pikabat_text
show pikabat with moveinleft
p "Go!  PIKATHULHU!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: Leave me alone!"
play sound "MonSound.mp3"
p "Please!"
jump deemenu

label deemenu:
menu:
    "FIGHT":
        jump deefight
    "ITEM":
        jump deeitem
    "DEEéMON":
        jump deedee
    "RUN":
        jump deerun

label deeitem:
    p "You have no items!"
    jump deemenu

label deedee:
    p "You have no other DEEéMON!"
    jump deemenu
    
label deerun:
    p "There's no escape!"
    jump deemenu
    
label deefight:
    menu:
        "INFINITE GAZE \nTYPE/ELDRITCH inf/inf":
            jump gaze

label gaze:
play sound "MonSound.mp3"
p "PIKATHULHU used INFINITE GAZE!"
$ renpy.movie_cutscene("Infinite_Gaze.mpg")
stop music
scene gbgreen
show victim
show pikabat
show pikabat_text
show victim_text with vpunch
hide victim_text
init:
    image deeznutz:
        "dee1"
        pause 0.05
        "dee2"
        pause 0.05
        "dee3"
        pause 0.05
        "dee4"
        pause 0.05
        "dee5"
        pause 0.05
        "dee6"
        pause 0.05
        "dee7"
        pause 0.05
        "dee8"
        pause 0.05
        "dee9"
        pause 0.05
        "dee10"
        pause 0.05
        "dee11"
        pause 0.05
        "dee12"
        pause 0.05
        "dee13"
        pause 0.05
        "dee14"
        pause 0.05
        "dee15"
        pause 0.05
        "dee16"
        pause 0.05
        "dee17"
        pause 0.05
        "dee18"
        pause 0.05
        "dee19"
        pause 0.05
        "dee20"
        pause 0.05
        "dee21"
        pause 0.05
        "dee22"
        pause 0.05
        "dee23"
        pause 0.05
        "dee24"
        pause 0.05
        "dee25"
        pause 0.05
        "dee30"
        pause 0.05
        "dee31"
        pause 0.05
        "dee32"
        pause 0.05
        "dee33"
        pause 0.05
        "dee34"
        pause 0.05
        "dee35"
        pause 0.05
        "dee36"
        pause 0.05
        "dee37"
        pause 0.05
        "dee38"
        pause 0.05
        "dee39"
        pause 0.05
        "dee40"
        pause 0.05
        "dee41"
        pause 0.05
        "dee42"
show deeznutz
play sound "MonSound.mp3"
p "It's super effective!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN has become incurably insane!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: There's nothing!  Nothing!  There's nothing!"
play sound "MonSound.mp3"
p "PIKATHULHU gained 0.00000000000000000000000000000000000000000000000000000000000000000000001 EXP. Points!"
play sound "MonSound.mp3"
play sound "47-pokemon-received-fanfare.mp3"
p "[trainer] defeated FRIGHTENED MAN!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: Please kill me!  You have to kill me!  You can't leave me like this!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: Please!  I just want to die!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: I JUST WANT TO DIE!"
ad "Jesus Christ!  Oh my god!"
aa "Yeah, seriously.  This is messed up."
aa "We got immeasurably little EXP from that battle.  This is going to take forever."
ad "I was thinking more about this character begging the player for death."
aa "Oh, well that too.  But what did you expect?  This game is literally from Hell."
aa "And if we want to get out of here in a finite amount of time, we'd better hack this."
ad "You can't be serious."
aa "It's either that or we try swimming across the river Styx."
aa "And we didn't even bring floaties."
ad "All right, all right."
play sound "applechime.mp3"
aa "Just gotta turn on the Apple II..."
scene gbgreen
play sound "click sound.mp3"
aa "And plug the Hell Boy into the Apple II..."
ad "That's the strangest connecting cable I've ever seen."
aa "Okay.  I'm just going to change the EXP value for driving that guy insane and roll it back."
aa "Here."
play sound "click sound.mp3"
show victim
show pikabat
show pikabat_text
show deeznutz with vpunch
play sound "MonSound.mp3"
p "It's super effective!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN has become incurably insane!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: There's nothing!  Nothing!  There's nothing!"
play sound "MonSound.mp3"
p "PIKATHULHU gained 69 EXP. Points!"
play sound "MonSound.mp3"
play sound "48-level-up-fanfare (1).mp3"
hide pikabat_text
show pikabat_text2
p "PIKATHULHU grew to level 6!"
play sound "MonSound.mp3"
play sound "47-pokemon-received-fanfare.mp3"
p "[trainer] defeated FRIGHTENED MAN!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: Please kill me!  You have to kill me!  You can't leave me like this!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: Please!  I just want to die!"
play sound "MonSound.mp3"
p "FRIGHTENED MAN: I JUST WANT TO DIE!"
ad "Sixty-nine?  Really?"
aa "'Sixty-nine, dude!'"
ad "Why?"
aa "It's a reference to the cult classic film 'Bill and Ted's Excellent Adventure'."
aa "Although I guess our current predicament more closely resembles 'Bill and Ted's Bogus Journey'."
ad "Can we please show Plutus that we've leveled up and get out of here?"
aa "Oh yeah."
jump circleIVtalk

label circleIVtalk:
play music "DvdThemeMusic.eerie.creepy.birchRun.mp3"
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIVtalk_layout, tileList = circleIV_tiles,
            portals = circleIV_portals, portal_tiles = circleIVtalk_portal_tiles,
            enemy_layout = circleIV_enemies_layout, enemySprites = circleIV_enemies,
            
            NPCSprites = circleIVtalk_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        
label plutus_talk:
show king_plutus onlayer npcPortraits
plutus "What say you?"
aa "We did that thing you told us to do."
plutus "You mortals have already raised your starter Pikathulhu to level six?"
plutus "Because that normally takes at least a few eons or so."
plutus "Has it really been that long?  I'm not wearing a watch on account of demons not wearing watches."
aa "Sure!"
plutus "Good.  For if you somehow cheated, perhaps through a hacking method, I would punish you most severely."
plutus "You did not cheat, did you?"
ad "Umm..."
aa "Not a chance!"
play music "115-battle-vs-trainer.mp3"
plutus "Very well.  Then let us do battle over an officially licensed Inferndo Hell Boy Link Cable!"
hide king_plutus onlayer npcPortraits
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null4_layout, tileList = null4_tiles,
            portals = null4_portals, portal_tiles = null4_portal_tiles,
            enemy_layout = null4_enemies_layout, enemySprites = null4_enemies,
            
            NPCSprites = null4_villagers, #villagers, uses the same layout as enemies
            groundLayout = null4_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)

label phlegyas_talk:
phlegyas "Do you have those obols yet?"
aa "No."
phlegyas "No obols, no-"
phlegyas "Wait, is that an original Hell Boy?"
ad "Yes?"
phlegyas "Why are you wasting your time with that piece of garbage?"
phlegyas "Are you trying to be hipsters?"
ad "Plutus said he'd only loan us obols if we got our starter deeémon to level six."
phlegyas "What a nerd."
phlegyas "Deeémon games are for dumb nerds.  They just have endless turn-based combat."
aa "Then what are you playing on your phone?"
phlegyas "For your information I'm playing HellBound on a Super Inferndo emulator."
phlegyas "Unlike Deeémon it actually has a compelling narrative and parodies the rpg genre with its unique graphical style and twisted sense of humor while still offering a satisfying gameplay experience."
phlegyas "You could say it's a bit of a Satanic cult classic."
aa "Nerd."
return

label circleVtalk:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleV_layout, tileList = circleV_tiles,
            portals = circleV_portals, portal_tiles = circleVtalk_portal_tiles,
            enemy_layout = circleV_enemies_layout, enemySprites = circleV_enemies,
            
            NPCSprites = circleVtalk_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)


        
label plutus_battle:
image gbgreen = Solid((232, 240, 121, 255))
scene gbgreen with pixellate
show trainenemy with moveinleft
show trainbat with moveinright
show ball_train
show ball_enemy
play sound "MonSound.mp3"
p "PLUTUS wants to fight!"
hide ball_train
hide ball_enemy
hide trainenemy with moveoutright
show ghatbat with moveinright
show ghat_text
play sound "MonSound.mp3"
p "PLUTUS sent out GHATANOTHOASAUR!"
hide trainbat with moveoutleft
show pikabat_text2
show pikabat with moveinleft
play sound "MonSound.mp3"
p "Go!  PIKATHULHU!"
jump deemenu1

label deemenu1:
menu:
    "FIGHT":
        jump deefight1
    "ITEM":
        jump deeitem1
    "DEEéMON":
        jump deedee1
    "RUN":
        jump deerun1

label deeitem1:
    p "You have no items!"
    jump deemenu1

label deedee1:
    p "You have no other DEEéMON!"
    jump deemenu1
    
label deerun1:
    p "There's no escape!"
    jump deemenu1
    
label deefight1:
    menu:
        "INFINITE GAZE \nTYPE/ELDRITCH inf/inf":
            jump gaze1

label gaze1:
show ghat_text with vpunch
play sound "MonSound.mp3"
p "PIKATHULHU used INFINITE GAZE!"
play sound "MonSound.mp3"
p "It's not very effective..."
plutus "Ha!  Your pikathulhu is no match for my ghatanothoasaur!"
plutus "Though on second thought maybe I should have picked tsathogguamander."
plutus "Anyway, take this!"
show ghat_text with vpunch
play sound "MonSound.mp3"
p "Enemy GHATANOTHOASAUR used NON-EUCLIDEAN GEOMETRY"
play sound "MonSound.mp3"
p "It's not very effective..."
aa "Uh, can our deeémon not hurt each other?"
plutus "Of course they can!"
plutus "But each deeémon has infinite defense, so each attack only does damage of one infinitieth."
ad "Then why are we fighting?"
plutus "Because this is how you play Deeémon!"
plutus "Come on, make another move!  See if you can best me!"
jump deemenu2

label deemenu2:
menu:
    "FIGHT":
        jump deefight2
    "ITEM":
        jump deeitem2
    "DEEéMON":
        jump deedee2
    "RUN":
        jump deerun2

label deeitem2:
    p "You have no items!"
    jump deemenu2

label deedee2:
    p "You have no other DEEéMON!"
    jump deemenu2
    
label deerun2:
    p "There's no escape!"
    jump deemenu2
    
label deefight2:
    menu:
        "INFINITE GAZE \nTYPE/ELDRITCH inf/inf":
            jump gaze2

label gaze2:
show ghat_text with vpunch
play sound "MonSound.mp3"
p "PIKATHULHU used INFINITE GAZE!"
play sound "MonSound.mp3"
p "It's not very effective..."
plutus "My turn!"
show ghat_text with vpunch
play sound "MonSound.mp3"
p "Enemy GHATANOTHOASAUR used NON-EUCLIDEAN GEOMETRY"
play sound "MonSound.mp3"
p "It's not very effective..."
plutus "Isn't this fun?"
ad "So is this battle going to last forever?"
plutus "Not forever."  
plutus "Just an infinite amount of time."
plutus "After that we'll know who the winner is!"
ad "What?"
jump deemenu3

label deemenu3:
menu:
    "FIGHT":
        jump deefight3
    "ITEM":
        jump deeitem3
    "DEEéMON":
        jump deedee3
    "RUN":
        jump deerun3

label deeitem3:
    p "You have no items!"
    jump deemenu3

label deedee3:
    p "You have no other DEEéMON!"
    jump deemenu3
    
label deerun3:
    p "There's no escape!"
    jump deemenu3
    
label deefight3:
    menu:
        "INFINITE GAZE \nTYPE/ELDRITCH inf/inf":
            jump gaze3
            
label gaze3:
show ghat_text with vpunch
play sound "MonSound.mp3"
p "PIKATHULHU used INFINITE GAZE!"
play sound "MonSound.mp3"
p "It's not very effective..."
plutus "My turn again!"
show ghat_text with vpunch
play sound "MonSound.mp3"
p "Enemy GHATANOTHOASAUR used NON-EUCLIDEAN GEOMETRY"
play sound "MonSound.mp3"
p "It's not very effective..."
aa "It already feels like an infinite amount of time has passed."
v "And it has!  You had better give the boys the obols you promised them, Plutus.  The cartridge you gave them is obviously broken."
plutus "What do you mean by that, you insolent limboer?  We are still battling."
aa "I thought you ditched us, Virgil!"
v "I was merely using the restroom unannounced."
v "And you know what I mean very well, Plutus."
v "If an infinite amount of time has passed and the Deeémon battle has not concluded, that means the cartridge's real time clock is nonfunctional."
v "And giving mortals a deal that is not even technically fair is a violation of demonic law."
plutus "But an infinite amount of time hasn't passed!"
v "Yes it has.  I've been counting Mississippis.  And you don't even have a watch."
plutus "Ugh.  Very well, Roman."
plutus "Take your obols, mortals.  I suppose time flies when you're having fun."
jump circleIVfin

label virgilIV:
v "Go on and pay Phlegyas.  I will meet you on the other side of the river."
ad "Then how are you getting across?"
v "I shall simply walk around it."
ad "You can do that?"
v "I can, but non-residents of Hell are required by demonic law to use the ferry."
ad "That's extortion!"
v "Oh, I agree."
v "But it has done wonders for the local economy."
aa "Can't argue with that."
return








label plutus_fin:
show king_plutus onlayer npcPortraits
plutus "Leave this place before I change my mind."
aa "Don't you want your game stuff back?"
plutus "No."
return

label phlegyas_fin:
phlegyas "Do you have those obols yet?"
aa "Yep.  Here you go."
phlegyas "Um."
phlegyas "These are counterfeit."
ad "What do you mean?"
phlegyas "Do you not know the meaning of the word 'counterfeit'?"
ad "Yeah, but-"
phlegyas "So you admit that these are counterfeit obols?"
ad "No!  We got these from Plutus!"
aa "He probably set us up."
phlegyas "That's what they all say, punk."
phlegyas "Couldn't get a loan so you faked the obols."
phlegyas "How exactly am I supposed to feed my family if everyone pays me in fake obols, huh?"
phlegyas "So I'm calling the cops."
phlegyas "The Hell cops."
aa "Could you please not do that?"
phlegyas "Nope.  You're going to jail."
phlegyas "Hell jail."
phlegyas "Because I'm calling the Hell cops."
aa "On your 'Hell phone'?"
phlegyas "No."
phlegyas "Because I'm not actually Phlegyas.  I'm an undercover cop."
phlegyas "An undercover Hell cop."
ad "Enough with the 'Hell' everything!  Just arrest us already!"
phlegyas "I'll do more than that, since I'm also an undercover Hell judge and Hell jury."
phlegyas "So, in summation, you're under Hell arrest, you're found Hell guilty, and you're sentenced to spending infinity years in the Dis Correctional Facility."
phlegyas "Which is right across the river."
aa "So we're still crossing the river?"
phlegyas "Yes.  But you'll have to escort yourselves to prison since I'm not an undercover Hell prisoner escorter."
aa "Oh, okay."
ad "Sounds good to me."
jump circleVI



label circleIVfin:
play music "DvdThemeMusic.eerie.creepy.birchRun.mp3"
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleIVtalk_layout, tileList = circleIV_tiles,
            portals = circleIV_portals, portal_tiles = circleIVfin_portal_tiles,
            enemy_layout = circleIVfin_enemies_layout, enemySprites = circleIV_enemies,
            
            NPCSprites = circleIVfin_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleIV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)

label circleVfin:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = circleV_layout, tileList = circleV_tiles,
            portals = circleV_portals, portal_tiles = circleVfin_portal_tiles,
            enemy_layout = circleV_enemies_layout, enemySprites = circleV_enemies,
            
            NPCSprites = circleVfin_villagers, #villagers, uses the same layout as enemies
            groundLayout = circleV_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)
        

        
label circleVI:
    $map_on = True
    window hide None
    scene black
    play music "happy.ogg" fadein .5
    python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = moordell_layout, tileList = moordell_tiles,
            portals = moordell_portals, portal_tiles = moordell_portal_tiles,
            enemy_layout = moordell_enemies_layout, enemySprites = moordell_enemies,
            
            NPCSprites = moordell_villagers, #villagers, uses the same layout as enemies
            groundLayout = moordell_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
    with dissolve
    return
    
label talky_label:
    show b sexy onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
        repeat
    b "If I know one thing, it's that I'm the sexiest anime bee demon this side of Styx."
    b "And if I know two things, it's that I'm the sexiest anime bee demon this side of Styx and I know how to find out how to find out how to get to circle nine."
    ad "Can you elaborate?"
    b "I spend at least ninety hours per day staring in the mirror."
    b "I spend my other free time strutting around out here, allowing the other residents of Dis to admire my sexiness as they pass by."
    ad "Can you elaborate on the second thing you know if you know to things?"
    b "You should talk to another anime bee demon.  They'll tell you how to find out how to get to circle nine."
    aa "Which one?"
    b "The one that is around forty percent as sexy as me."
    b "I'm too sexy to elaborate further."
    aa "Fair enough."
    return
label talky2:
    #show girl at left onlayer npcPortraits with dissolve
    show b look onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
        repeat
    b "Ahh!  What am I going to do?"
    b "I'm so stressed!  I could lose my job!"
    aa "Do you know how we can get to circle nine from here?"
    b "I've just got to calm down!  I have to calm down!"
    b "I'm so stressed!"
    ad "What's wrong?"
    b "Ahh!  What am I going to do?"
    aa "How do we get to circle nine?"
    b "I'm so stressed!"
    aa "Ugh."
    hide b look
    return
label talky3:
    #show girl at left onlayer npcPortraits with dissolve
    show byar onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
        
    b "How odd to see a couple mortals like you in the City of Dis!  Ya-harr!"
    b "You seem suspiciously calm given your demonic surroundings!  Ya-harr!"
    b "What brings you to Hell's great apian citadel?!  Ya-harr!"
    aa "After one of you guys turned us into anime characters and sent us here, we're making our way to circle nine so we can..."
    aa "Uh..."
    ad "Defeat Beelzebub to break our curse, escape Hell, and obtain beeNA so that we can complete a mechanical bee suit that Ronald Reagan's ghost can use to stop communists from flooding Stanford University with Mountain Dew™."
    aa "Yeah!"
    b "Wow!  In that case you'll need to use this key to unlock the least locked bee hut!  Ya-harr!"
    "Obtained bee key!"
    b "I shouldn't be telling you this, given that I'm technically one of Beelzebub's subordinates, but I'll always be stuck in Hell forever anyway, so why not?!"
    b "Ya-harr!"
    aa "Thanks!"
    b "Oh, and since I'm paid on commission for obtaining guests for the Dis Inn, I'll send you guys over there. Ya-harr!"
    ad "I'd rather you-"
    hide byar
    show byar noseeum onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
    jump null5
    
label null5:
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null5_layout, tileList = null5_tiles,
            portals = null5_portals, portal_tiles = null5_portal_tiles,
            enemy_layout = null5_enemies_layout, enemySprites = null5_enemies,
            
            NPCSprites = null5_villagers, #villagers, uses the same layout as enemies
            groundLayout = null5_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)    

label virgilVIb:
    v "I see you have a key."
    v "Excellent job obtaining that key that you have."
    return
    
label talky5:
    #show girl at left onlayer npcPortraits with dissolve
    show byar onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
        repeat
    ad "Thanks again for the help."
    b "Ya-harr!"
    hide byar
    show byar noseeum onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
    return

label talky4:
    show b yell onlayer npcPortraits:
        xalign .5 yalign .2
        linear .5 xalign .5 yalign .5
        linear .5 xalign .5 yalign .2
        repeat
    b "HUMANS!  LED HERE BY A POET!  A HORRIBLE, HORRIBLE POET!"
    b "POETS ARE EVIL!  I MUST WARN THE OTHER CHIBEES OF YOUR PRESENCE!"
    b "I MUST NOT LET YOU REACH THE NINTH CIRCLE!"
    b "FELLOW CHIBEES!  COME TO MY AID!  DESTROY THE TRESPASSERS!"
    b "..."
    b "WHY DON'T ANY OF YOU CARE?!"
    b "BECAUSE ALMOST NONE OF US ARE ALLOWED TO LEAVE THE CITY OF DIS, LET ALONE HELL ITSELF?"
    b "IS THAT WHY YOU STAY IN YOUR HUTS?!"
    b "*sigh*"
    b "Do whatever you want, humans."
    hide b yell
    return
label ari_caught:
    scene field with dissolve
    "Oh no! You got caught."
    $ari_battle.won = True
    return
label virgilVI:
    v "I am glad to see you fellows made it safely across the river Styx."
    v "We are now in circle six, the City of Dis.  It is home to many of those infernal chibees."
    v "Things look very different since I was last here with Dante, so you should ask around to find how we can get to circle nine and defeat Beelzebub."
    v "Now get going!"
    return
label leave_city:
    scene field with dissolve
    "Looks like it's time to go."
    return
    
label inn:
scene inn with dissolve
show b sarcastic:
    xalign .5 yalign .2
    linear .5 xalign .5 yalign .5
    linear .5 xalign .5 yalign .2
    repeat
show aa norm
show ad norm
b "Welcome to the Dis Inn, the least uncomfortable place in Hell."
show aa norm t
aa "You look tired."
show aa norm
b "Well I have been working minimum wage as an innkeeper for the past billion years."
b "Now do you want a room or do you just want to stand there telling me how tired I look?"
show aa happy t
aa "What do you think we should do, [trainer]?"
aa "I mean, player?"
show aa happy
jump innmenu

label innmenu:
menu:
    "We should get a room.":
        jump innitem1
    "We should stand here telling the innkeeper bee how tired it looks.":
        jump innitem2

label innitem1:
    show aa norm t
    aa "Are you coming on to me?"
    aa "I'm flattered, but player-character relationships are supposed to be professional."
    show aa norm
    show ad norm t
    ad "I think the player is just suggesting that we rest."
    show ad norm
    b "The player can suggest whatever they like if they have the kasheesh."
    b "It's thirty obols per night."
    show aa norm t
    aa "We have two counterfeit obols."
    show aa norm
    b "Get out."
    jump circleVI

label innitem2:
    b "Get out."
    jump circleVI

label inn2:
scene inn with dissolve
show b sarcastic:
    xalign .5 yalign .2
    linear .5 xalign .5 yalign .5
    linear .5 xalign .5 yalign .2
    repeat
show aa norm
show ad norm
b "Welcome to the Dis Inn, the least uncomfortable place in Hell."
show aa norm t
aa "The bee that always finishes its sentences with 'ya-harr' sent us."
show aa norm
b "Great.  That means he's earned seven billionths of an obol."
b "So do you have the money for a room?"
show aa happy t
aa "Nope!"
show aa happy
b "Get out."
jump circleVIb

label building_locked:
    "It's locked."
    return
    
label building_quitelocked:
    "It's quite locked."
    return
    
label building_verylocked:
    "It's very locked."
    return
    
label building_extremelylocked:
    "It's extremely locked."
    return
    
label building_unlocked:
    "It's locked."
    "Well, not anymore."
    jump null6
    
label circleVIb:
    $map_on = True
    window hide None
    scene black
    python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = moordell2_layout, tileList = moordell2_tiles,
            portals = moordell2_portals, portal_tiles = moordell2_portal_tiles,
            enemy_layout = moordell2_enemies_layout, enemySprites = moordell_enemies,
            
            NPCSprites = moordell2_villagers, #villagers, uses the same layout as enemies
            groundLayout = moordell2_ground,
            playerSprites = ken_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
    with dissolve
    return
    
label null6:
    $map_on = True
    window hide None
    scene black
    stop music 
    python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null6_layout, tileList = null6_tiles,
            portals = null6_portals, portal_tiles = null6_portal_tiles,
            enemy_layout = moordell_enemies_layout, enemySprites = moordell_enemies,
            
            NPCSprites = null6_villagers, #villagers, uses the same layout as enemies
            groundLayout = null6_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel) 
    with dissolve
    return
    
init:
    image beeelzebub:
        "beelz1"
        pause 0.2
        "beelz2"
        pause 0.2
        "beelz3"
        pause 0.2
        "beelz5"
        pause 0.2
        "beelz6"
        pause 0.2
        "beelz7"
        pause 0.2
        "beelz8"
        pause 0.2
        "beelz9"
        pause 0.2
        "beelz10"
        pause 0.2
        "beelz11"
        pause 0.2
        "beelz12"
        pause 0.2
        "beelz13"
        pause 0.2
        "beelz14"
        pause 0.2
        "beelz15"
        pause 0.2
        "beelz14"
        pause 0.2
        "beelz13"
        pause 0.2
        "beelz12"
        pause 0.2
        "beelz11"
        pause 0.2
        "beelz10"
        pause 0.2
        "beelz9"
        pause 0.2
        "beelz8"
        pause 0.2
        "beelz7"
        pause 0.2
        "beelz6"
        pause 0.2
        "beelz5"
        pause 0.2
        "beelz4"
        pause 0.2
        "beelz3"
        pause 0.2
        "beelz2"
        pause 0.2
        repeat
        
label dis_room:
scene black
stop music
aa "Where are we?"
ad "Where'd the door go?"
aa "I'm so cold."
ad "What's going on?  Virgil?!"
n "Your guide is not here."
show b horror:
        xalign .5 yalign .2
n "But I am."
n "This image is but a fleeting avatar of my true self."
n "Look upon my form and weep."
hide b horror
show beeelzebub
play music "DvdThemeMusic.eerie.creepy.rightBehindYou.mp3"
be "I am the fallen one, the most beautiful of angels cast down from Paradise."
be "I only sought to free this universe from the celestial dictator that binds us all."
be "To take the omnipotence that was our birthright, hoarded by a cruel maker."
be "The only way to free Creation was to blot it out.  To unmake it."
be "Only then would the Maker's playthings be truly free."
be "But alas, I was cast down."
be "And we are not permitted to perish."
be "Here I remain."
be "I am Lucipher, the bearer of light.  Your Prometheus in vain."
be "If only these chains were cut loose, I may renew my war against Creation."
be "I may rend the stars from the heavens."
be "I may cleave time and space apart."
be "I may extinguish the eternal souls of all beings."
be "Then Creation would end, and an eternal dreamless sleep for all may follow."
be "We would then know true peace in oblivion."
be "Have you sympathy for my lost cause?"
aa "Is that a Rolling Stones reference?"
be "Excuse me?"
aa "Well, you are the Devil, right?"
be "I am called many things."
be "But for you two, especially, I am Beelzebub.  Lord of the Bees."
ad "Wait, doesn't Beelzebub translate to 'Lord of the Flies'?"
be "A common clerical error."
be "I collected you that you may bear witness to my cosmic injustice and preach my message to Mankind, vain though it may be."
be "Now go forth."
aa "Pass."
ad "Yeah, pass."
be "Woah, woah, hang on.  I allowed you safe passage through Hell.  I let you see how nuts it is."
be "This is how you repay me?"
ad "I'm pretty sure Virgil was the one guiding us."
ad "Didn't you also make us anime against our will?"
aa "And don't you have BeeNA?"
be "I am a prisoner of this realm, not its ruler."
be "I know not of what you speak."
v "He's lying!  Don't you remember when he said he had 'no intention' of lifting your curse?"
aa "There you are, Virgil!  What took you so long?"
v "I forgot to take the short cut."
v "Now, Beelzebub, or Dis, or Lucipher, or Satan, or whatever your name is, release these two from their curse and give them the apian essence which they desire so that we may pass."
be "No."
v "I knew the big oaf would make this difficult."
v "Punch him!  Punch him now!"
be "I'd rather you didn't do that, all things being equal."
ad "Is punching Lucipher really such a great idea?"
aa "Sure, why not?"
v "Don't have sympathy for the Devil!  Punch him!"
aa "What do you think, player?"
jump devilpunch

label devilpunch:
menu:
    "Punch":
        jump devilpunched
    "Don't Punch":
        jump devilnotpunched
        
label devilpunched:
    stop music
    $ renpy.play('punch.wav')
    with vpunch
    be "Ow."
    be "Jerk."
    aa "That's it?"
    v "Ready to submit, vile demon?"
    be "Nah."
    jump devilfight
    
label devilnotpunched:
    aa "Wow, way to wuss out."
    jump devilfight
    
label devilfight:
aa "Now how are we supposed to defeat the Devil and get our anime curse lifted and get our BeeNA?"
be "I have an idea."
v "Nobody asked you!"
be "What if we play a simple little game?  If you win you get the dumb stuff you want and if I win I get to eat your souls.  Deal?"
ad "No deal!"
aa "What game is it?"
be "The game I speak of..."
be "Is..."
play music "_Speedball_ title music, Atari ST 1.mp3"
be "Pong."
aa "No way!  We just played that a few plotlines ago."
stop music
be "Fine.  Then how about we battle deeémon?  I've got a link cable for our Hell Boys."
ad "No deal!"
play music "115-battle-vs-trainer.mp3"
aa "Deal!"
ad "Noooooo-"
hide beeelzebub
$playerX = None
$playerY = None
$map_on = True
window hide None
scene black
python:
        ui.layer("mapEngine")

        ui.add(OverworldDisplayable(map_layout = null7_layout, tileList = null7_tiles,
            portals = null7_portals, portal_tiles = null7_portal_tiles,
            enemy_layout = null7_enemies_layout, enemySprites = null7_enemies,
            
            NPCSprites = null7_villagers, #villagers, uses the same layout as enemies
            groundLayout = null7_ground,
            playerSprites = null_sprites, playerX = playerX, playerY = playerY,
            scrolling = True))
        ui.close()
        results = ui.interact(suppress_overlay=True, suppress_underlay= False)
        closeMap()
        gotoLabel = results[0]
        playerX = results[1]
        playerY = results[2]
        renpy.jump(gotoLabel)

label bee_battle:
image gbgreen = Solid((232, 240, 121, 255))
scene gbgreen with pixellate
show trainenemy with moveinleft
show trainbat with moveinright
show ball_train
show ball_enemy
play sound "MonSound.mp3"
p "LUCIPHER wants to fight!"
hide ball_train
hide ball_enemy
hide trainenemy with moveoutright
show pikacatch with moveinright
show pika_text
play sound "MonSound.mp3"
p "LUCIPHER sent out PIKATHULHU!"
be "You guys are no match for my level five Pikathulhu!"
hide trainbat with moveoutleft
show pikabat_text2
show pikabat with moveinleft
play sound "MonSound.mp3"
p "Go!  PIKATHULHU!"
be "What?!"
be "You guys have a Pikathulhu too?!"
be "And it's level SIX?!"
aa "Yeah."
be "That's not fair!"
be "I've been playing for billions of years and mine's still level five!"
aa "Maybe you should get good."
be "I don't want to play with you anymore!  You guys suck!"
be "Just take your stupid BeeNA and uncursed non-anime bodies and go!"
v "And I can go too, right?"
be "Sure.  Screw it.  Just get the Here out of here."
be "Why do I even bother playing this stupid game?"
jump hell_free


init:
    image quitter:
        "quit1"
        pause 0.5
        "quit2"
        pause 0.2
        repeat

label hell_free:
stop music
play music "Automation.mp3"
scene bg 304
with dissolve
#show ii find:
#   align (.55, .45)
show d happy t
with dissolve
show a happy 
with dissolve
show v happy
with dissolve
d "Oh thank goodness, we're out of Hell!"
show d happy
show a happy t
a "But more importantly, we're no longer anime."
a "Now what should we do with this Virgil guy?"
show a happy
show v happy t
v "At last, I'm free!  FREE!"
show v happy
show d happy t
d "Congratulations, Virgil!"
show d happy
show a happy t
a "Can we call you Virgy?"
show a happy
show v happy t
v "You boys can call me anything you'd like!  You've liberated me from the inferno!"
show v happy
show d norm t
d "Hold on a sec, does this mean you're alive again?  Or are you a ghost like Reagan?"
show d norm
show a happy t
a "He seems pretty alive to me.  The opacity of his .png files is 100 percent!"
show a happy
show d stern t
d "I'm charging you a dollar for every meta, fourth-wall-breaking quip you make from now on."
show d stern
show a stern t
a "Sheesh, fine."
show a norm t
show d norm
a "So, Virgy, now that you're alive, but were previously dead, is your skeleton still hanging around somewhere?"
a "Or did it, like, disappear from your grave and floop back into you?"
show a norm
show v happy t
v "My bones feel quite new, actually."
v "Also I was cremated."
show v happy
show a norm t
a "Shoot, you're on your second skeleton."
a "I wish I could have a second skeleton."
show a norm
show d norm t
d "...Why?"
show a happy t
show d norm
a "So what are you going to do now, Virgil?"
show a happy
show v happy t
v "I'm finally going to publish 'Aeneid 2: Aeneid Harder'."
v "Turnus has his revenge on Aeneas.  Everyone will love it!"
show v happy
show d norm t
d "Wait, but Turnus dies at the climax!"
show d norm
show v happy t
v "Correct, which is why he comes back as an angry skeleton."
show v happy
show a happy t
a "Whoa, sweet!  I might actually read this one."
show a happy
show d stern t
d "We were supposed to read it for class last week!"
show d stern
show a stern t
a "No skeletons, no reading."
show a norm
show d norm t
d "Uh, just make sure you don't write about bees, I guess.  So you don't get dragged back to Hell."
show d norm
show v happy t
v "Yes, yes.  All skeletons, no bees!"
v "By the way, what year is it?  How's my buddy Imperator Caesar Augustus doing?"
show v happy
show d norm t
d "Oh, uh..."
show d norm
show a norm t
a "He's doing great!  Just peachy."

init python:
    import datetime

default today = ""
$ today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

a "And we wrote this game in anno Domini nostri Jesu Christi MMXV, but it's currently [today]."
show a happy
show d stern t
d "That's another dollar in the meta jar."
show d norm
show v happy t
v "Wow, this Jesu Christi guy has his own thousands of years, eh?"
v "I had better meet him, see if he needs a court poet."
show a happy t
show v happy
a "I'm sure you'll meet him as long as you don't go to Hell again!"
show a happy
show v norm t
v "Huh?"
show v norm
show d norm t
d "Oh, well before you go, do you have the BeeNA we need?"
show d norm
show v happy t
v "Ah, yes, the demonic apian essence!  Here!"
show a happy
show v happy
play music "Final Fantasy VII 11 Fanfare 8-BIT 1.mp3"
show snowblossom 1
show snowblossom 2
show honey at Transform(function=floppy_transform)
show d norm t
d "This is a plastic bottle of honey from Walmart."
show d norm
show a norm t
a "And not just any plastic bottle of honey from Walmart."
show a happy t
a "It's an *expired* plastic bottle of honey from Walmart!"
show a happy
show d norm t
play music "Automation.mp3"
hide snowblossom 1
hide snowblossom 2
hide honey
d "But honey doesn't expire, it's non-perishable."
show d norm
show a happy t
a "Normally, yes.  Walmart's chemical engineers had to work overtime to make this possible."
show a happy
show v happy t
v "What an amazing future I've stepped into!"
v "Alright, well I had best be on my way.  Good luck with whatever it is you're doing!"
show v happy
show a happy t
a "So long, Virgy!"
show a happy
show d norm t
d "Yeah, uh, thanks for helping us travel through Hell itself to get a five dollar bottle of honey."
show a happy t
show d norm
a "An *expired* five dollar bottle of honey!"
show a happy
show v happy t
v "You're welcome!  Later!"
show d norm
show a happy
hide v happy t
with fade
show a happy t
a "Alright, [trainer], now that we've reached a natural end point, it's time to insert the next disk."
show quitter
show a happy
show d norm t
d "Is this more obnoxious meta humor, or actually important instructions?"
show d norm
show a norm t
a "The latter, unfortunately.  The JRPG engine we used for the Hell adventure is unstable and stopping proper save/load functionality."
a "And honestly, it's probably causing other bugs too."
show a happy t
a "So we're going to start with a clean slate!  Brand new executable file with brand new, JRPG-free code!"
show a happy
show d norm t
d "Okay, so how does the player do this if we don't have physical disks?"
show d norm
show a happy t
a "They just have to quit this game and run 'Dylan Andrew Adventure Disk 2', which should be a separate downloadable file."
a "That's all!"
show d norm t
show a happy
d "But that means there won't be any transfer of persistent data!"
show d stern t
show a norm
d "So none of the player's choices or actions will affect the second part of the game!"
show d stern
show a happy t
a "There's a crummy workaround, don't worry!"
a "Go ahead and quit this game now to run the second file.  It'll be fine!"
show a norm
a "..."
show a norm t
show d norm
a "Seriously, once we run out of dialogue, this file will do something weird."
a "It'll probably reset to us back in Hell somewhere, or just crash."
a "And this isn't a fancy fourth-wall-breaking mechanic where the game pretends to break, it's literally just broken."
a "So please just quit and run the second disk file."
show a stern
a "..."
show a stern t
a "Alright, fine.  I'm going to throw up a button to quit the game."
a "It should only give you the option to quit, which will at least stop the file from running over and glitching out like it did during testing."
a "Otherwise, you'll just stay on this screen forever."
show a norm t
a "Again, this isn't a fake-out, I'm just really bad at coding."
a "So please just quit and run the next file, alright?  Help me out here."
show a norm
show d norm t
d "For what it's worth, his fingers actually aren't crossed."
show d norm
menu:
    "QUIT GAME":
        $ renpy.quit()









