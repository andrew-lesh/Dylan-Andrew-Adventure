# You can place the script of your game in this file.
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Declare characters used by this game.


# Custom Mouse Cursors
define config.mouse = {
    "default" : [("default_cursor.png", 0, 0)],
    "magnify_blue" : [("magnifier_blue_cursor.png", 0, 0)],
    "magnify_gold" : [("magnifier_gold_cursor_blue.png", 0, 0)]
    }

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
    def j_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voice_sans.wav", channel="blips")
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
            
init python:
    def attorney_voice_m(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-blipmale.ogg", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
            
init python:
    def attorney_voice_f(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-blipfemale.ogg", channel="blips")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blips")
                        
            
             
# Character Definitions
define d = Character('Dylan', color="#00f9ff", callback=d_voice)
define ad = Character('Dylan-senpai', color="#00f9ff", callback=d_voice)
define aj = Character('Ace Jenkins', color="#00f9ff", callback=d_voice)
define a = Character('Andrew', color="#51e130", callback=a_voice)
define aa = Character('Andrew-san', color="#51e130", callback=a_voice)
define fm = Character('Flint McSteel', color="#51e130", callback=a_voice)
define cp = Character('Comrade Pichael', color ="#ff0000", callback=cp_voice)
define j = Character('Javarcia', color ="#d783ff", callback=j_voice)
define da = Character('Adam', color ="#adadad", callback=navy_voice)
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
define dd = Character('Dylan', color="#00f9ff", what_font="Igiari.ttf", callback=attorney_voice_m)
define jj = Character('Judge', color="#00f9ff", what_font="Igiari.ttf", callback=attorney_voice_m)
define pp = Character('Prosecutor', color="#00f9ff", what_font="Igiari.ttf", callback=attorney_voice_m)

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
image a cuff norm = "a_cuff_norm.png"
image a cuff norm t = "a_cuff_norm_t.png"
image a cuff stern = "a_cuff_stern.png"
image a cuff stern t = "a_cuff_stern_t.png"

# Javarcia Images
image j happy = "javarcia_hap.png"
image j happy t = "javarcia_hap_t.png"
image j norm = "javarcia_norm.png"
image j norm t = "javarcia_norm_t.png"
image j stern = "javarcia_stern.png"
image j stern t = "javarcia_stern_t.png"

# Adam Images
image da happy = "adam_hap.png"
image da happy t = "adam_hap_t.png"
image da norm = "adam_norm.png"
image da norm t = "adam_norm_t.png"
image da evil = "adam_evil.png"
image da evil t = "adam_evil_t.png"

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

# Ace Jenkins Images
image aj norm = "ace_norm.png"
image aj norm t = "ace_norm_t.png"
image aj happy = "ace_hap.png"
image aj happy t = "ace_hap_t.png" 

# Flint McSteel Images
image fm norm = "flint_norm.png"
image fm norm t = "flint_norm_t.png"
image fm happy = "flint_hap.png"
image fm happy t = "flint_hap_t.png"

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

# Cop Images
image cop norm = "cop_norm.png"
image cop norm t = "cop_norm_t.png"

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

# Prosecutor Images
image pros norm t = "prosecutor_norm_t.webm"

# Misc. Images
image floppy = "floppy.png"
image honey = "honey.png"
image beeprints = "blueprints.png"
image scary anime girl = "scary_anime_girl.png"
image hellboy = "heendadeen.png"
image quit = "quit.png"
image oats = "oats.png"
image dino_bowl = "dino_bowl.png"
image walrus = "chocolate_walrus.png"

# Don't worry Bill Murray
image 1bill = "billbill.png"
image 6bill = "billmageddon.png"

# Court Evidence
image ev_id = "ev_id_andrew.png"
image ev_book = "ev_jane_book.png"
image ev_photo = "ev_photo_dylan_andrew.png"
image ev_chicken = "ev_rubber_chicken.png"
image ev_flag = "ev_sovereignty_materials304.png"

# Room 304 Door Posters
image poster_adam = "poster_adam.png"
image poster_dino = "poster_dino.png"
image poster_octocat = "poster_octocat.png"
image poster_star = "poster_star.png"
image poster_doge = "poster_doge.png"
image poster_304 = "poster_304.png"


# --- BACKGROUNDS ---
image bg 304 = "bg_room_304_dingus.png"
image bg 304 dingus = "bg_room_304.png"
image bg 304 door = "bg_304_door.png"
image bg 304 door2 = "bg_304_doo2r.png"
image bg hoover = "hootow.jpeg"
image bg hooverinside = "hootervower.jpeg"
image bg beeprints = "blueprints_screen.jpeg"
image bg 304 beeprints = "bg_room_304_beeprints.png"
image bg cherry = "bg_blossoms_1.png"
image bg jrpg-start = "jrpg-start.png"
image bg daatalescreen = "daatale-screen.png"
image bg eternity = "LDN_622.jpg"
image bg javarcia open = "bg_javarcia_open.png"
image bg javarcia closed = "bg_javarcia_closed.png"
image bg adam open = "bg_adam_open.png"
image bg adam closed = "bg_adam_closed.png"
image bg adam room = "bg_adam_room.png"
image bg ace dylan = "ace_dylan.png"
image bg ace dylan 2 = "ace_dylan_ground.png"
image bg court j = "court_judge.png"
image bg court d = "court_defense.png"
image bg court p = "court_prosecution.png"
image bg court w = "court_witness.png"


init:
    $ call_bhutan = False
    $ cerberus_answer = "bees"
    $ name = "Francis"
    $ woodchuck = False
    $ magcursor = False


# The game starts here.
$ default_mouse = None
label start:
    # $ save_name = "Twas brillig, and the slithy toves"
    play music "Automation.mp3"
    scene bg 304
    with dissolve
    show d happy 
    with dissolve
    show a happy
    with dissolve
    

    
show a happy t
a "Great!  Disk 2 is running fine!"
show a happy
show d norm t
#$ default_mouse = "default"
d "Dang, I was kind of hoping we'd be free to go."
show d norm
show a happy t
a "To restore persistent data from disk 1, we have a couple of questions."
a "First, did you call the King of Bhutan?"
show a happy
show d norm t
d "Wait, that was actually important?"
show d norm
show a happy
menu:
    "Yes, I called his majesty, the Dragon King of Bhutan.":
        $ call_bhutan = True
        jump question2
    "No, I did not.":
        jump question2

init:
    $ stepahead = False
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

label question2:
show a happy t
a "Next, what word did you use to get past Cerberus?"

label cerbquestion:
$ cerbname = renpy.input("What is the word?")
jump cerbcheck

label cerbcheck:
    if cerbname == cerb1:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb2:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb3:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb4:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb5:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb6:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb7:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb8:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb9:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb10:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb11:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb12:
        $ cerberus_answer = "fallen"
        jump cerb
    if cerbname == cerb13:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb14:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb15:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb16:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb17:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb18:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb19:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb20:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb21:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb22:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb23:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb24:
        $ cerberus_answer = "bird"
        jump nice
    if cerbname == cerb25:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb26:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb27:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb28:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb29:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb30:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb31:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb32:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb33:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb34:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb35:
        $ cerberus_answer = "bees"
        jump cerb
    if cerbname == cerb36:
        $ cerberus_answer = "bees"
        jump cerb
    else:
        jump cerbwrong
        

label nice:
show a happy t
a "Ha!  Nice."
show a happy
jump question3

label cerb:
show a norm t
a "Bummer, there's another answer I like more."
show a happy
jump question3

label cerbwrong:
show a stern t
a "You didn't say that, liar!"
show a stern
show d norm t
show a 
d "Hey, if you don't remember, you probably said 'bees'."
d "(Without the quotation marks)"
show d norm
show a happy
jump cerbquestion

label question3:
show a happy t
a "Thanks.  Now what did you name your deeémon trainer?"
show a happy
$ name = renpy.input("What is your trainer name?")
show a happy t
a "Great!  I hope you like your choice, because we're exclusively referring to you as [name] now."
show a norm t
a "Time for our final question."
a "You should take this seriously, because this will directly affect the ending of the game."
a "Are you ready for the ultimate question?"
show a norm

menu:
    "Yes.":
        jump chuck
    "No.":
        jump chuck


label chuck:
show a happy t
a "Great, thanks for your answer!"
scene bg 304 beeprints
show a happy t
show d norm
a "Alright, now it's time to pick the next item you want to find!"
show a happy
show d norm t
d "Wait, what's the question you were going to ask?"
show d norm
show a happy t
a "What question?"
show a happy
show d stern t
d "The 'ultimate' question?!"
show d stern
show a happy t
a "Yeah, I asked it."
show a happy
show d stern t
d "So the ultimate question was asking them if they were ready for the ultimate question?"
show d stern
show a happy t
a "Yeah!  It's funny."
show a happy
show d stern t
d "No, it's obnoxious.  Can you ask them a real question please?"
scene bg 304
show d stern
show a stern t
a "Fine."
show a happy t
a "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
show a happy
show d norm

menu:
    "Yes.":
        $ woodchuck = True
        jump chucked
    "No.":
        $ woodchuck = False
        jump chucked

label chucked:
show d stern t
d "Gosh dang it!  That's not what I-"
scene bg 304 beeprints
show a happy t
show d stern
a "Alright, now it's time to pick the next item you want to find!"
jump beeprint_map

# ---Beeprints Legit
screen beeprints_imagemap:
    imagemap:
        auto "blueprints_screen_%s.jpeg"
        hotspot (552, 77, 90, 48) action Return("code") alt "Code" # mouse "magnify_gold"
        hotspot (44, 244, 292, 46) action Return("quantum computer") alt "Quantum Computer" # mouse "magnify_gold"
        #hotspot (165, 407, 93, 54) action Return("beena") alt "Beena"
        hotspot (551, 414, 174, 136) action Return("industrial grade oatmeal") alt "Industrial Grade Oatmeal" mouse # "magnify_gold"
label beeprint_map:        
window hide None
call screen beeprints_imagemap
window show None
if _return == "code":
    jump code
if _return == "quantum computer":
    jump quantum
#if _return == "beena":
#    jump beeprint_map
if _return == "industrial grade oatmeal":
    jump oatmeal

label code:
jump beeprint_map

label quantum:
jump beeprint_map












