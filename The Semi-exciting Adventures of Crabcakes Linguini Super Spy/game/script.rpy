
# ---Start Screen
screen start_imagemap:
    imagemap:
        auto "tartjame_%s.png"
        hotspot (297, 539, 207, 45) action Return("start") alt "Start"  
label start:
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
    jump control1
    
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
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"

# ---Tart 3 (unrolled)
screen spaceship_unrolled_imagemap:
    imagemap:
        auto "spaceship_unrolled_%s.png"
        hotspot (214, 0, 371, 274) action Return("space") alt "space"
        hotspot (250, 297, 22, 20) action Return("phant") alt "Phant"
        hotspot (30, 54, 155, 230) action Return("elements") alt "Elements"
        
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
    jump victory
    
# ---Victory
screen victory_imagemap:
    imagemap:
        auto "victoire_%s.png"
        hotspot (0, 0, 800, 600) action Return("click") alt "click"
    
label victory:
window hide None
call screen victory_imagemap
window show None
if _return == "click":
    jump begin 
    
    
d "LOL What?"

